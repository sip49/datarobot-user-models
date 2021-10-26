"""
Copyright 2021 DataRobot, Inc. and its affiliates.
All rights reserved.
This is proprietary source code of DataRobot, Inc. and its affiliates.
Released under the terms of DataRobot Tool and Utility Agreement.
"""
import numpy as np
import pandas as pd


def score(data, model, **kwargs):
    assert list(data.columns) == [
        "abatjours",
        "abaton",
        "abator",
        "abators",
        "ABATS",
        "abattage",
        "abattis",
        "abattised",
        "abattises",
        "abattoir",
        "abattoirs",
        "abattu",
        "abattue",
        "Abatua",
        "abature",
        "abaue",
        "abave",
        "abaxial",
        "abaxile",
        "abaze",
        "abb",
        "Abba",
        "abbacy",
        "abbacies",
        "abbacomes",
        "Abbadide",
        "Abbai",
        "abbaye",
        "abbandono",
        "abbas",
        "abbasi",
        "Abbasid",
        "abbassi",
        "Abbassid",
        "Abbasside",
        "Abbate",
        "abbatial",
        "abbatical",
        "abbatie",
        "Abbe",
        "Abbey",
        "abbeys",
        "abbey's",
        "abbeystead",
        "abbeystede",
        "abbes",
        "abbess",
        "abbesses",
        "abbest",
        "Abbevilean",
        "Abbeville",
        "Abbevillian",
        "Abbi",
        "Abby",
        "Abbie",
        "Abbye",
        "Abbyville",
        "abboccato",
        "abbogada",
        "Abbot",
        "abbotcy",
        "abbotcies",
        "abbotnullius",
        "abbotric",
        "abbots",
        "abbot's",
        "Abbotsen",
        "Abbotsford",
        "abbotship",
        "abbotships",
        "Abbotson",
        "Abbotsun",
        "Abbott",
        "Abbottson",
        "Abbottstown",
        "Abboud",
        "abbozzo",
        "ABBR",
        "abbrev",
        "abbreviatable",
        "abbreviate",
        "abbreviated",
        "abbreviately",
        "abbreviates",
        "abbreviating",
        "abbreviation",
        "abbreviations",
        "abbreviator",
        "abbreviatory",
        "abbreviators",
        "abbreviature",
        "abbroachment",
        "ABC",
        "abcess",
        "abcissa",
        "abcoulomb",
        "ABCs",
        "abd",
        "abdal",
        "abdali",
        "abdaria",
        "abdat",
        "Abdel",
        "Abd-el-Kadir",
        "Abd-el-Krim",
        "Abdella",
        "Abderhalden",
        "Abderian",
        "Abderite",
        "Abderus",
        "abdest",
        "Abdias",
        "abdicable",
        "abdicant",
        "abdicate",
        "abdicated",
        "abdicates",
        "abdicating",
        "abdication",
        "abdications",
        "abdicative",
        "abdicator",
        "Abdiel",
        "abditive",
        "abditory",
        "abdom",
        "abdomen",
        "abdomens",
        "abdomen's",
        "abdomina",
        "abdominal",
        "Abdominales",
        "abdominalia",
        "abdominalian",
        "abdominally",
        "abdominals",
        "abdominoanterior",
        "abdominocardiac",
        "abdominocentesis",
        "abdominocystic",
        "abdominogenital",
        "abdominohysterectomy",
        "abdominohysterotomy",
        "abdominoposterior",
        "abdominoscope",
        "abdominoscopy",
        "abdominothoracic",
        "abdominous",
        "abdomino-uterotomy",
        "abdominovaginal",
        "abdominovesical",
        "Abdon",
        "Abdu",
        "abduce",
        "abduced",
        "abducens",
        "abducent",
        "abducentes",
        "abduces",
        "abducing",
        "abduct",
        "abducted",
    ]
    expected_dtype = pd.SparseDtype(np.float64, 0)
    for col in data:
        assert data[col].dtype == expected_dtype, f"Column {col} is not sparse."
    predictions = pd.DataFrame(model.predict(data), columns=["Predictions"])
    return predictions
