import pandas as pd

def get_area_borough(area_series) -> pd.Series:
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

    borough = area_series.str[0]
    borough = borough.map(borough_mapping)

    return borough