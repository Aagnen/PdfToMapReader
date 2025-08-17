depth_patterns_Art_1 = [r"\s*(Art[.]\s*\d{1,3}[a-z]{0,3}[.])\s*",
                        r"\s*(\d{1,3}[a-z]{,3}[.]).*",
                        r"\s*(\d{1,3}[a-z]{0,3}[)]).*",
                    ]
#  without Art. dots etc: 
#  [
#     r"\s*Art[.]\s*(\d{1,3}[a-z]{0,3})[.]\s*",
#     r"\s*(\d{1,3}[a-z]{0,3})[.].*",
#     r"\s*(\d{1,3}[a-z]{0,3})[)].*",
# ]


depth_patterns_Par_1 = [r"(§\s*\d{1,3}[a-z]{0,3}[.])",
                        r"\s*(\d{1,3}[a-z]{0,3}[.]).*",
                        r"\s*(\d{1,3}[a-z]{0,3}[)]).*",
                    ]

# ------------------------------------------------------------------- #

paths = {
    "file_open_path": "01_Pdf_original",
    "txt_save_path": "02_Txt",
    "map_save_path": "03_Maps",
    "highlight_pdf_save_path": "04_Pdf_highlighted",
}

# ------------------------------------------------------------------- #

Map_guides = [
    {
        "paths": paths,
        "file_name": "2023_05_16-2023_05_16",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 10,
    },
    {
        "paths": paths,
        "file_name": "2023_05_31-2023_05_31",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9,
    },
    {
        "paths": paths,
        "file_name": "2024_07_12-2024_07_12-doZmiany",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "paths": paths,
        "file_name": "1998_09_10_1998_09_10",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "paths": paths,
        "file_name": "1989_05_17-2021_11_03",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "paths": paths,
        "file_name": "1994_07_07-2023_12_04",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
        {
        "paths": paths,
        "file_name": "1994_07_07-2025_04_02",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9,
    },
    {
        "paths": paths,
        "file_name": "1995_04_21-1995_04_21",
        "depth_patterns": [
            r"\s*($\s(\d{1,3})\.).*",
            r"\s*(\d{1,3}[a-z]{0,3}\)).*",
            r"\s*(Załącznik do rozporządzenia).*",
        ],
        "main_text_font_size": 6,
    },
    {
        "paths": paths,
        "file_name": "1996_08_02-2017_03_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 11,
    },
    {
        "paths": paths,
        "file_name": "2002_04_12-2022_04_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 10,
    }
]
