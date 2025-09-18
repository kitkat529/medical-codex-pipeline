import pandas as pd

file_path = "input\icd10who_2019.txt"

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

icd10who = pd.read_csv(file_path, sep=';', header=None, names=columns)
icd10who_small = icd10who[['icd10_code', 'detailed_title']].copy()
icd10who_small = icd10who_small.rename(columns={'icd10_code': 'code', 'detailed_title': 'description'})
icd10who_small["last_updated"] = "09-18-2025"
output_path = 'output/icd10who_small.csv'
icd10who_small.to_csv(output_path, index=False)



print(f"Successfully parsed {len(icd10who)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(icd10who.head())
