
from MapEngine import pdf_to_map
from HighlighterEngine import pdf_highlighter
import MapGuides

import os
import json

# ----------------- VARIABLES ----------------- #

dir_path = "01_Pdf_original"

# FILES
All_map_guides = MapGuides.Map_guides
map_guides_to_import = []
MAP_GUIDES = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        map_guides_to_import.append(path)
for every_map in All_map_guides:
    if f"{every_map['file_name']}.pdf" in map_guides_to_import:
        MAP_GUIDES.append(every_map)


IF_TO_MAP = True

IF_TO_HIGHLIGHT = False
SECTION_TO_HIGHLIGHT = "2->2.->1)"
PAGES_AROUND = 0


# ----------------- PDF TO MAP ----------------- #
if IF_TO_MAP:
    for guide in MAP_GUIDES:
        print(f"Working on {guide['file_name']}")

        this_map = pdf_to_map(guide)

        # save
        with open(
            f"{guide['paths']['map_save_path']}/{guide['file_name']}_map.json",
            "w",
            encoding="utf-8",
        ) as outfile:
            json.dump(this_map, outfile)


# ----------------- HIGHLIGHT PDF ----------------- #
if IF_TO_HIGHLIGHT:
    for guide in MAP_GUIDES:

        print(f"Working on {guide['file_name']}")

        highlighted_pdf = pdf_highlighter(guide, SECTION_TO_HIGHLIGHT, PAGES_AROUND)

        # save
        pdf_highlighted_path = f"{guide['paths']['highlight_pdf_save_path']}/{guide['file_name']}_highlighted.pdf"
        highlighted_pdf.save(pdf_highlighted_path)
