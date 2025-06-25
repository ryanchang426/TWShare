import pandas as pd

def stock_twse_index_daily() -> pd.DataFrame:
    """
    台灣上市公司指數行情
    資料來源：https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX
    """
    url = "https://openapi.twse.com.tw/v1/exchangeReport/MI_INDEX"
    df = pd.read_json(url)
    return df
