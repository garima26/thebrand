from pathlib import Path

BASE_DIR = Path("/")
DATA_PATH = BASE_DIR / "data"
ARTIFACT_PATH = BASE_DIR / "artifacts"

MODEL_FEATURES = ['single',
                 'married_no_kids',
                 'not_married_no_kids',
                 'married_with_kids',
                 'not_married_with_kids',
                 'single_parent',
                 'other',
                 'perc_area_single',
                 'perc_area_married_no_kids',
                 'perc_area_not_married_no_kids',
                 'perc_area_married_with_kids',
                 'perc_area_not_married_with_kids',
                 'perc_area_single_parent',
                 'perc_area_other',
                 'Highest_income_hhs',
                 'Touristy',
                 'Diversity',
                 'HasHomeStadium',
                 'IsPosh',
                 'total',
                 'area_has_buurt',
                 'borough']

TARGET = 'Units_sold'
