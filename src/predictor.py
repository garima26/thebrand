import pandas as pd


def convert_dtypes(df) -> pd.DataFrame:
    """Returns a dataframe with all numeric fields converted to float32

    Args:
        df (DataFrame): DataFrame with all features

    Returns:
        df (DataFrame): DataFrame with numeric fields converted to float32

    """
    for col in df.columns:
        if col != "area":
            df[col] = df[col].astype("float32")
    return df

def fill_na_values(df) -> pd.DataFrame:
    """Returns a dataframe with all null values filled with 0

    Args:
        df (DataFrame): DataFrame with all features

    Returns:
        df (DataFrame): DataFrame with all null values filled with 0

    """
    df = df.fillna(0)
    return df

def check_if_area_is_empty(df):
    """Checks if the area filed in the dataframe is empty. Raises ValueError if empty.

    """
    if df.area.isnull().sum() > 0:
        raise ValueError
    else:
        return df
        
def get_area_borough(df) -> pd.DataFrame:
    """Returns a series with borough names corresponding to the area names in the input series.

    Args:
        area_series (Series): Series with names of areas

    Returns:
        borough (Series): Series with names of corresponsing boroughs

    """

    borough_mapping = {
        "A": "Centrum",
        "E": "West",
        "F": "Neiuw-West",
        "K": "Zuid",
        "M": "Oost",
        "N": "Noord",
        "T": "Zuidoost",
        "B": "Port-area",
    }

    borough = df['area'].str[0]
    df['borough'] = borough.map(borough_mapping)

    return df


def get_perc_row_totals(df) -> pd.DataFrame:
    """Returns a DataFrame with percentage of row totals added as features

    Args:
        df (DataFrame): DataFrame with family composition features

    Returns:
        df (DataFrame): DataFrame with percentage of row totals added as features

    """
    abs_cols = [
    "single",
    "married_no_kids",
    "not_married_no_kids",
    "married_with_kids",
    "not_married_with_kids",
    "single_parent",
    "other",
    ]

    num_test = df[abs_cols]
    row_totals = num_test.div(df["total"], axis=0) * 100
    row_totals = row_totals.add_prefix("perc_area_")
    df = df.merge(row_totals, how="inner", left_index=True, right_index=True)
    return df


def add_area_name_features(df) -> pd.DataFrame:
    """Returns a DataFrame with features indicating if a string is present in the area name

    Args:
        df (DataFrame): DataFrame with area description

    Returns:
        df (DataFrame): DataFrame with boolean features indicating the presence of a string

    """

    df["area_lower"] = df["area"].str.lower()
    df["area_has_buurt"] = df["area_lower"].str.contains("buurt")
    return df


def add_borough_details(df) -> pd.DataFrame:
    """Returns a DataFrame with borough related features added to the original dataframe

    Args:
        df (DataFrame): DataFrame with original features

    Returns:
        df (DataFrame): DataFrame with borough related features added to the original dataframe

    """
    borough_details = pd.DataFrame(
        {
            "borough": {
                0: "Centrum",
                1: "Noord",
                2: "Neiuw-West",
                3: "Oost",
                4: "West",
                5: "Westpoort",
                6: "Zuid",
                7: "Zuidoost",
            },
            "Highest_income_hhs": {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0},
            "Touristy": {0: 1, 1: 9, 2: 9, 3: 4, 4: 2, 5: 4, 6: 1, 7: 4},
            "Diversity": {0: 4, 1: 9, 2: 9, 3: 1, 4: 2, 5: 9, 6: 4, 7: 9},
            "HasHomeStadium": {0: 9, 1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 1},
            "IsPosh": {0: 3, 1: 9, 2: 9, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9},
        }
    )

    borough_details["borough"] = borough_details["borough"].replace(
        "Nieuw-West", "Neiuw-West"
    )

    df = df.merge(borough_details, how="left", on="borough")
    return df


def rename_column_names(df) -> pd.DataFrame:
    """Removes commas and replaces spaces with underscore from column names

    """
    new_column_names = {col: col.replace(" ", "_").replace(",", "") for col in df.columns}

    df.rename(mapper=new_column_names, inplace=True, axis=1)
    return df
