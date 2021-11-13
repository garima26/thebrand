import pandas as pd

def get_nrf_color_group(x):
    '''
    Returns NRF color groups based on NRF color codes of an article.

            Parameters:
                    x (Dataframe): An input dataframe that has `NRF_COLOR_CODE` column
    '''
    
    if x["NRF_COLOR_CODE"] == 0:
        return "no color"
    elif x["NRF_COLOR_CODE"] == 1:
        return "black"
    elif x["NRF_COLOR_CODE"] >= 2 and x["NRF_COLOR_CODE"] <= 9:
        return "oxford"
    elif x["NRF_COLOR_CODE"] >= 10 and x["NRF_COLOR_CODE"] <= 19:
        return "charcoal"
    elif x["NRF_COLOR_CODE"] >= 20 and x["NRF_COLOR_CODE"] <= 99:
        return "gray"
    elif x["NRF_COLOR_CODE"] >= 100 and x["NRF_COLOR_CODE"] <= 199:
        return "white"
    elif x["NRF_COLOR_CODE"] >= 200 and x["NRF_COLOR_CODE"] <= 249:
        return "brown"
    elif x["NRF_COLOR_CODE"] >= 250 and x["NRF_COLOR_CODE"] <= 299:
        return "beige"
    elif x["NRF_COLOR_CODE"] >= 300 and x["NRF_COLOR_CODE"] <= 399:
        return "green"
    elif x["NRF_COLOR_CODE"] >= 400 and x["NRF_COLOR_CODE"] <= 499:
        return "blue"
    elif x["NRF_COLOR_CODE"] >= 500 and x["NRF_COLOR_CODE"] <= 599:
        return "purple"
    elif x["NRF_COLOR_CODE"] >= 600 and x["NRF_COLOR_CODE"] <= 649:
        return "red"
    elif x["NRF_COLOR_CODE"] >= 650 and x["NRF_COLOR_CODE"] <= 699:
        return "pink"
    elif x["NRF_COLOR_CODE"] >= 700 and x["NRF_COLOR_CODE"] <= 799:
        return "yellow"
    elif x["NRF_COLOR_CODE"] >= 800 and x["NRF_COLOR_CODE"] <= 899:
        return "orange"
    elif x["NRF_COLOR_CODE"] >= 900 and x["NRF_COLOR_CODE"] <= 929:
        return "neutral overflow"
    elif x["NRF_COLOR_CODE"] >= 930 and x["NRF_COLOR_CODE"] <= 949:
        return "red overflow"
    elif x["NRF_COLOR_CODE"] >= 950 and x["NRF_COLOR_CODE"] <= 959:
        return "pink overflow"
    elif x["NRF_COLOR_CODE"] >= 960 and x["NRF_COLOR_CODE"] <= 998:
        return "multi"
    elif x["NRF_COLOR_CODE"] == 999:
        return "assorted"
    else:
        return "unknown"