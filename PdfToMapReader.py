from MapEngine import pdf_to_map
from HighlighterEngine import pdf_highlighter
import MapGuides

import os
import json

# ----------------- VARIABLES ----------------- #

dir_path = "01_Pdf_original"

# FILES
All_map_guides = MapGuides.Map_guides
paths = MapGuides.paths
map_guides_to_import = []
MAP_GUIDES = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        map_guides_to_import.append(path)
for every_map in All_map_guides:
    if f"{every_map['file_name']}.pdf" in map_guides_to_import:
        MAP_GUIDES.append(every_map)

# ----------------- PDF TO MAP ----------------- #
for guide in MAP_GUIDES:
    print(f"Working on {guide['file_name']}")

    this_map = pdf_to_map(guide)

    # save
    with open(
        f"{paths['map_save_path']}/{guide['file_name']}_map.json",
        "w",
        encoding="utf-8",
    ) as outfile:
        json.dump(this_map, outfile, ensure_ascii=False)
