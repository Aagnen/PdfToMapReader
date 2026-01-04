depth_patterns_Art_1 = [
    r"\s*(Art[.]\s*\d{1,3}[a-z]{0,3}[.])\s*",  # Art. 3.
    r"\s*(\d{1,3}[a-z]{,3}[.]).*",  # 3.
    r"\s*(\d{1,3}[a-z]{0,3}[)]).*",  # 3)
]
#  without Art. dots etc:
#  [
#     r"\s*Art[.]\s*(\d{1,3}[a-z]{0,3})[.]\s*",
#     r"\s*(\d{1,3}[a-z]{0,3})[.].*",
#     r"\s*(\d{1,3}[a-z]{0,3})[)].*",
# ]


depth_patterns_Par_1 = [
    r"(§\s*\d{1,3}[a-z]{0,3}[.])",  # § 1.
    r"\s*(\d{1,3}[a-z]{0,3}[.]).*",  # 2.
    r"\s*(\d{1,3}[a-z]{0,3}[)]).*",  # 1)
]

depth_patterns_Art_par = [
    r"\s*(Art[.]\s*\d{1,3}[a-z]{0,3}[.])\s*",  # Art. 3.
    r"\s*(§\s*\d{1,3}[a-z]{,3}[.]).*",  # § 1.
    r"\s*(\d{1,3}[a-z]{0,3}[)]).*",  # 1)
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
        "file_name": "2022_06_24",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1960_06_14",
        "depth_patterns": depth_patterns_Art_par,
        "main_text_font_size": 12,
    },
    {
        "file_name": "1999_08_16",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2013_04_26",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2000_03_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9,
    },
    {
        "file_name": "2015_10_20",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_07_23",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2019_08_28",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1985_03_21",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2001_04_27",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2000_12_15",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2023_05_16",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_01_13",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1985_03_14",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2005_07_18",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_05_26_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_03_22",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1997_04_10",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "1989_05_17",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1997_08_21",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2004_04_16_1",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1964_04_23",
        "depth_patterns": depth_patterns_Art_par,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2011_08_19",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2022_12_22",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2017_07_20",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2019_09_11",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2010_06_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2008_10_03",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2001_08_11",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2023_03_08",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2010_05_07",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2023_07_24",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_09_12",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2012_04_25",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2007_04_13_1",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2003_03_28",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2019_04_29",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_12_16",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2001_06_07",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_04_10",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2009_12_28",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_08_30",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2008_11_21",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2016_11_09",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_08_05",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_05_26_2",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_06_01",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1994_02_04",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2022_07_01",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_06_21",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1974_06_26",
        "depth_patterns": depth_patterns_Art_par,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2003_02_06",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2018_10_30",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2012_11_13",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_07_16",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_06_19",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2010_11_25",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2015_10_09",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2020_10_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2010_12_13",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2016_11_18",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_04_02",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2007_12_19",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2015_12_23_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_04_16_2",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "1995_04_21",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_06_06",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1995_02_03",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2020_01_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2016_11_17_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2000_04_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2006_07_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1998_09_10",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1997_06_19",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2002_10_31",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2001_03_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2020_09_11",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_12_11",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2011_02_18",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1998_08_31",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_11_25",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2022_12_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2007_01_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1996_05_28",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_06_25",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2016_06_02",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2016_11_17_2",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_10_26",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2007_04_20",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2008_10_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2019_12_17",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1998_06_01",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2009_07_01",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2011_03_09",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1997_09_26",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_09_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2019_05_21",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2016_06_17",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_12_17",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_08_31",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_07_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2019_07_12",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2015_04_21",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2008_08_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2011_12_22",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2013_04_30",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2010_07_02",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_03_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1998_12_01",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2012_09_12",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2011_06_09",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2015_02_20",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "1991_08_24",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2006_10_23",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1994_10_27",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2007_04_13_2",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2002_10_30_2",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2005_07_04",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1994_07_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_11_29",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2011_12_20",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1994_01_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2017_12_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2015_12_23_2",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_06_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1977_02_10",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_12_20_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_12_23",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2005_10_14",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_08_26",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_07_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1991_07_20",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_04_12",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2015_02_27",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_07_03",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2012_12_14",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2023_03_28",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2001_09_20",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2017_04_03",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2017_12_22",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2021_12_20_2",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2012_12_07",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_07_09",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2024_07_15",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2004_08_30",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2022_08_26",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2018_08_02",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1997_09_02",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_06_23",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2020_05_30",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1993_10_01_2",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2001_11_19",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2002_10_30_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2007_06_20",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2000_12_21",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2003_12_23",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2022_12_09",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "2014_08_29",
        "depth_patterns": depth_patterns_Art_1,
        "main_text_font_size": 12,
    },
    {
        "file_name": "2009_07_24",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
    {
        "file_name": "1993_10_01_1",
        "depth_patterns": depth_patterns_Par_1,
        "main_text_font_size": 9.5,
    },
]

# Map_guides = [
#     {
#         "file_name": "2023_05_16-2023_05_16",
#         "depth_patterns": depth_patterns_Par_1,
#         "main_text_font_size": 9.5,
#     },
#     {
#         "file_name": "2023_05_31-2023_05_31",
#         "depth_patterns": depth_patterns_Par_1,
#         "main_text_font_size": 9,
#     },
#     {
#         "file_name": "2024_07_12-2024_07_12-doZmiany",
#         "depth_patterns": depth_patterns_Art_1,
#         "main_text_font_size": 12,
#     },
#     {
#         "file_name": "1998_09_10_1998_09_10",
#         "depth_patterns": depth_patterns_Art_1,
#         "main_text_font_size": 12,
#     },
#     {
#         "file_name": "1989_05_17-2021_11_03",
#         "depth_patterns": depth_patterns_Art_1,
#         "main_text_font_size": 12,
#     },
#     {
#         "file_name": "1994_07_07-2023_12_04",
#         "depth_patterns": depth_patterns_Art_1,
#         "main_text_font_size": 12,
#     },
#     {
#         "file_name": "1994_07_07-2025_04_02",
#         "depth_patterns": depth_patterns_Art_1,
#         "main_text_font_size": 9,
#     },
#     {
#         "file_name": "1995_04_21-1995_04_21",
#         "depth_patterns": [
#             r"\s*($\s(\d{1,3})\.).*",
#             r"\s*(\d{1,3}[a-z]{0,3}\)).*",
#             r"\s*(Załącznik do rozporządzenia).*",
#         ],
#         "main_text_font_size": 6,
#     },
#     {
#         "file_name": "1996_08_02-2017_03_14",
#         "depth_patterns": depth_patterns_Par_1,
#         "main_text_font_size": 11,
#     },
#     {
#         "file_name": "2002_04_12-2022_04_15",
#         "depth_patterns": depth_patterns_Par_1,
#         "main_text_font_size": 9.5,
#     },
# ]
