import pandas as pd

def stock_twse_company_info() -> pd.DataFrame:
    """
    台灣上市公司基本資料查詢
    資料來源：https://openapi.twse.com.tw/v1/opendata/t187ap03_L
    備註：回傳欄位包括公司代號、公司名稱、產業類別、地址等
    """
    url = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"
    df = pd.read_json(url)
    return df
