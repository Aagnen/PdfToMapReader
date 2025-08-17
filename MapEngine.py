import fitz  # library of PyMuPDF
import re

def get_bounding_box_spans(dictSpans, pad=0):
    bboxSelf = {}
    for span in dictSpans:
        page = span["page"]
        bbox = span["bbox"]
        if not isinstance(page, int): continue
        if page not in bboxSelf:
            bboxSelf[page] = bbox
        else:
            current_bbox = bboxSelf[page]
            bboxSelf[page] = [
                min(current_bbox[0], bbox[0]),
                min(current_bbox[1], bbox[1]),
                max(current_bbox[2], bbox[2]),
                max(current_bbox[3], bbox[3])
            ]
    for key, bbox in bboxSelf.items():
        bboxSelf[key] = [
                round(bbox[0]-pad, 2),
                round(bbox[1]-pad, 2),
                round(bbox[2]+pad, 2),
                round(bbox[3]+pad, 2)
            ]
    return bboxSelf

def update_dict_box(original_dict, new_dict, pad=0):
    for key, new_bbox in new_dict.items():
        if not isinstance(key, int): continue
        elif not original_dict:
           # Add the new key-value pair from new_dict to original_dict
            original_dict[key] = new_bbox
        elif key in original_dict:
            # Compare and choose the bigger values for each coordinate
            original_bbox = original_dict[key]
            updated_bbox = [
                min(original_bbox[0], new_bbox[0]),
                min(original_bbox[1], new_bbox[1]),
                max(original_bbox[2], new_bbox[2]),
                max(original_bbox[3], new_bbox[3])
            ]
            original_dict[key] = updated_bbox
        else:
            # Add the new key-value pair from new_dict to original_dict
            original_dict[key] = new_bbox
    for key, bbox in original_dict.items():
        original_dict[key] = [
                round(bbox[0]-pad, 2),
                round(bbox[1]-pad, 2),
                round(bbox[2]+pad, 2),
                round(bbox[3]+pad, 2)
            ]
    return original_dict



def pdf_to_map(map_guide):
    # ----------------- VARIABLES ----------------- #
    res = {}
    current_path = []
    page_num = 0
    txt_text = ""

    # ----------------- OPEN FILE ----------------- #
    pdf_fitz = fitz.open(
        f"{map_guide['paths']['file_open_path']}/{map_guide['file_name']}.pdf"
    )

    # ----------------- READ FILE ----------------- #
    for page in pdf_fitz:
        page_num += 1

        dict_pdf = page.get_text("dict")

        # ----------------- TXT FILE ----------------- #
        for block in dict_pdf["blocks"]:
            try:
                for line in block["lines"]:
                    for span in line["spans"]:
                        txt_text += span["text"]
                        txt_text += "\n"
            except KeyError:
                print(block)

        # ----------------- MAP FILE ----------------- #
        # loop over all text fragments
        for block in dict_pdf["blocks"]:
            if "lines" not in block: 
                print("Block without lines:")
                continue  # skip blocks without lines
            for line in block["lines"]:
                for span in line["spans"]:
                    # If the text is too small, leave it out
                    if int(span["size"]) < map_guide["main_text_font_size"]:
                        # print("Text too small:", span["size"])
                        continue

                    # ----------------- FIND DELIMITER ----------------- #
                    # check if any of the delimiter patterns match and adjust the currentPath based on found matches
                    for depth in range(len(map_guide["depth_patterns"])):
                        match = re.match(
                            map_guide["depth_patterns"][depth], span["text"]
                        )
                        if match: # if found any appropriate delimiter
                            # if there are missing levels replace them with zeros
                            if len(current_path) < depth:
                                current_path = current_path + [
                                    "0" for _ in range(depth - len(current_path))
                                ]
                            current_path = current_path[:depth] + [match.group(1)] #  updates current_path to include the new level identified by the regex match
                            break # when found, break looking for delimiter pattern
                    
                    if not len(current_path):
                        continue

                    # ----------------- MAP FILE ----------------- #
                    nested_dict = res
                    for key in current_path[:-1]:
                        if key not in nested_dict:
                            nested_dict[key] = {}
                        nested_dict = nested_dict[key]

                    new_span = {
                        "text": span["text"],
                        "page": page_num,
                        "bbox": span["bbox"],
                    }

                    if current_path[-1] in nested_dict:
                        nested_dict[current_path[-1]]["spans"].append(new_span)
                    else:
                        nested_dict[current_path[-1]] = {"spans": [new_span]}
    # ----------------- ADD BBoxSelf and BBoxSelfAndChildren ----------------- #
    for level1 in res:
        if not isinstance(res[level1], dict): continue
        if "spans" in res[level1]: res[level1]["bboxSelf"] = get_bounding_box_spans(res[level1]["spans"], 5)
        bboxSelfWithChildren1 = {}

        for level2 in res[level1]:
            if level2 == "bboxSelf": continue
            if not isinstance(res[level1][level2], dict): continue
            if "spans" in res[level1][level2]: res[level1][level2]["bboxSelf"] = get_bounding_box_spans(res[level1][level2]["spans"], 5)
            bboxSelfWithChildren2 = {}

            for level3 in res[level1][level2]:
                if level3 == "bboxSelf": continue
                if not isinstance(res[level1][level2][level3], dict): continue
                if "spans" in res[level1][level2][level3]:
                    res[level1][level2][level3]["bboxSelf"] = get_bounding_box_spans(res[level1][level2][level3]["spans"], 5)
                    bboxSelfWithChildren2 = update_dict_box(bboxSelfWithChildren2, res[level1][level2][level3]["bboxSelf"])
                    #print(f"{level1}:{level2}:{level3}: {bboxSelfWithChildren2}")
            
            if "spans" in res[level1][level2]: bboxSelfWithChildren2 = update_dict_box(bboxSelfWithChildren2, res[level1][level2]["bboxSelf"])
            res[level1][level2]["bboxSelfWithChildren"] = bboxSelfWithChildren2
            
            bboxSelfWithChildren1 = update_dict_box(bboxSelfWithChildren1, res[level1][level2]["bboxSelfWithChildren"])
        
        if "spans" in res[level1]: bboxSelfWithChildren1 = update_dict_box(bboxSelfWithChildren1, res[level1]["bboxSelf"])
        res[level1]["bboxSelfWithChildren"] = bboxSelfWithChildren1
        

    with open(f"{map_guide['paths']['txt_save_path']}/{map_guide['file_name']}_text.txt", "w", encoding='utf-8') \
            as outfile:
        outfile.write(txt_text)
    print("Saved txt file")
    print("Created Map file")

    return res
