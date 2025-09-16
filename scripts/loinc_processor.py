import pandas as pd
loinc = pd.read_csv("input/loinc.csv")
loinc.describe()
loinc.info()
loinc.STATUS.value_counts()
loinc.LOINC_NUM 
loinc.DefinitionDescription
loinc.iloc[0]
loinc.DefinitionDescription.describe()
loinc.LONG_COMMON_NAME.describe()

keep_columns = ["LOINC_NUM", "LONG_COMMON_NAME"]
loinc_small = loinc[["LOINC_NUM", "LONG_COMMON_NAME"]]

loinc_small = loinc[keep_columns]

loinc_small["last_updated"] = "9-16-2025"

loinc_small = loinc_small.rename(columns={"LOINC_NUM": "Code", "LONG_COMMON_NAME": "Description"})

file_output_path = "output/loinc_small.csv"
loinc_small.to_csv(file_output_path)