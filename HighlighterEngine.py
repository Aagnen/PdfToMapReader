import fitz  # library of PyMuPDF
import json


def pdf_highlighter(guide, section_path, pages_around=(2, 2)):
    pdf_file_path = f"{guide['paths']['file_open_path']}/{guide['file_name']}.pdf"
    map_file_path = f"{guide['paths']['map_save_path']}/{guide['file_name']}_map.json"

    pdf_file = fitz.open(pdf_file_path)
    with open(map_file_path, "r", encoding="utf8") as map_path:
        map_file = json.load(map_path)

    section_keys = section_path.split("->")
    print(f"Keys: {section_keys}")

    nested_map = map_file
    for sec_key in section_keys:
        try:
            nested_map = nested_map[sec_key]
        except:
            print(f"Wrong file path: {sec_key} in {section_path}.")

    section_pages = []
    pages_to_see = []

    highlight(nested_map, pdf_file, section_pages)

    for page in section_pages:
        true_page = page - 1
        if true_page not in pages_to_see:
            pages_to_see.append(true_page)
    # print(f"Pages to see: {pages_to_see}")

    pages_to_see_first = pages_to_see[0]
    pages_to_see_last = pages_to_see[-1]

    for i in range(1, pages_around[0] + 1):
        if pages_to_see_first - i >= 0:
            pages_to_see.append(pages_to_see_first - i)
    for i in range(1, pages_around[1] + 1):
        if pages_to_see_last + i < pdf_file.page_count:
            pages_to_see.append(pages_to_see_last + i)
    pages_to_see.sort()
    # print(f"Pages to see after sort and around: {pages_to_see}")
    pdf_file.select(pages_to_see)

    return pdf_file, pages_to_see_first


def highlight(nested_map, pdf_file, section_pages):
    for key, value in nested_map.items():
        if key == "spans":
            for span in value:
                rect = fitz.Rect(
                    span["bbox"][0],
                    span["bbox"][1],
                    span["bbox"][2],
                    span["bbox"][3],
                )
                pdf_file[int(span["page"]) - 1].draw_rect(
                    rect, fill=(0, 1, 1), fill_opacity=0.2, stroke_opacity=0
                )
                section_pages.append(span["page"])
            # print(f"Section on pages: {set(section_pages)}")
        else:
            highlight(value, pdf_file, section_pages)
    print(f"Section on pages: {set(section_pages)}")
