import fitz  # library of PyMuPDF
import re


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
            for line in block["lines"]:
                for span in line["spans"]:
                    if int(span["size"]) != map_guide["main_text_font_size"]:
                        continue

                    # check if any of the delimiter patterns match and adjust the currentPath based on found matches
                    for depth in range(len(map_guide["depth_patterns"])):
                        match = re.match(
                            map_guide["depth_patterns"][depth], span["text"]
                        )
                        if match:
                            # if there are missing levels replace them with zeros
                            if len(current_path) < depth:
                                current_path = current_path + [
                                    "0" for _ in range(depth - len(current_path))
                                ]
                            # new_path = ''.join(e for e in match.group(1) if e.isalnum())
                            # new_path_list = [new_path]
                            # current_path = current_path[:depth] + new_path_list
                            current_path = current_path[:depth] + [match.group(1)]
                            break

                    if not len(current_path):
                        continue

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

    with open(f"{map_guide['paths']['txt_save_path']}/{map_guide['file_name']}_text.txt", "w", encoding='utf-8') \
            as outfile:
        outfile.write(txt_text)
    print("Saved txt file")
    print("Created Map file")

    return res
