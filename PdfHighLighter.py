from HighlighterEngine import pdf_highlighter
import fitz  # library of PyMuPDF
import MapGuides
import json
import os
import subprocess
import time

# ----------------- VARIABLES ----------------- #

dir_path = r'01_Pdf_original'

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


# SECTION_TO_HIGHLIGHT = "2->2.->1)"
PAGES_AROUND = (0, 1)


# ----------------- GET BRANCHES ----------------- #


def get_branches(json_obj, prefix="", branches=None):
    if branches is None:
        branches = []

    for key, value in json_obj.items():
        branch = f"{prefix}{key}"
        branches.append(branch)

        if isinstance(value, dict):
            get_branches(value, f"{branch}->", branches)

    return branches


def open_pdf(pdf_path):
    command = ["start", pdf_path]
    subprocess.run(command, shell=True)
    # time.sleep(1)


# Function to save the branches_list to a txt file
def save_branches_to_txt(file_path, branches_list):
    with open(file_path, "w") as txt_file:
        for branch in branches_list:
            txt_file.write(branch + "\n")


# Function to read branches from a txt file
def read_branches_from_txt(file_path):
    with open(file_path, "r") as txt_file:
        return [line.strip() for line in txt_file]


# -----------------  ----------------- #


# for guide in MAP_GUIDES:
#     print(f"Working on {guide['file_name']}")
#
#     map_file_path = f"{guide['paths']['map_save_path']}/{guide['file_name']}_map.json"
#     with open(map_file_path, "r", encoding="utf8") as map_path:
#         map_file = json.load(map_path)
#         branches_list = get_branches(map_file)
#         branches_list = [item for item in branches_list if "spans" not in item]
#         print(branches_list)
#         print(f"Length of a list:{len(branches_list)}")
#
#     # Save the branches_list to a txt file
#     txt_file_path = f"{guide['file_name']}_branches_to_check.txt"
#     save_branches_to_txt(txt_file_path, branches_list)

page = 0

for guide in MAP_GUIDES:
    # Read the branches_list from the txt file
    txt_file_path = f"{guide['file_name']}_branches_to_check.txt"
    branches_list = read_branches_from_txt(txt_file_path)

    for i in range(900, len(branches_list)):
        print("\n\n\n\n")
        # ----------------- HIGHLIGHT PDF ----------------- #
        print(f"Working on the branch: {branches_list[i]}")
        highlighted_pdf, new_page = pdf_highlighter(guide, branches_list[i], PAGES_AROUND)
        if page-new_page > 2:
            print(f"CAREFULLY! {page} - {new_page}")
        page = new_page

        # save
        pdf_highlighted_path = f"{guide['paths']['highlight_pdf_save_path']}/{guide['file_name']}_highlighted.pdf"
        highlighted_pdf.save(pdf_highlighted_path)
        open_pdf(pdf_highlighted_path)

        # Adjust the duration (in seconds) as needed before closing the PDF file
        time.sleep(2)

        # Prompt the user for input
        while True:
            user_input = input(
                "Choose an option: enter - Close the PDF file and continue with the loop. n -  Exit the code.\n")

            if user_input == "":
                # Close the PDF file
                subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], shell=True)  # Update the process name if needed
                # Remove the processed branch from the list
                branches_list.pop(i)
                txt_file_path = f"{guide['file_name']}_branches_to_check.txt"
                save_branches_to_txt(txt_file_path, branches_list)
                break
            elif user_input == "n":
                # Exit the code
                exit()
            else:
                print("Invalid option. Please choose 1 or 2.")



