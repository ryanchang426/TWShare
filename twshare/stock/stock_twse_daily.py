import requests
import pandas as pd

def stock_twse_daily() -> pd.DataFrame:
    url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
    
    # 绕过 SSL 验证
    response = requests.get(url, verify=False)
    data = response.json()
    df = pd.DataFrame(data)

    column_map = {
        "Date": "交易日期",
        "Code": "證券代號",
        "Name": "公司名稱",
        "TradeVolume": "成交股數",
        "TradeValue": "成交金額",
        "OpeningPrice": "開盤價",
        "HighestPrice": "最高價",
        "LowestPrice": "最低價",
        "ClosingPrice": "收盤價",
        "Change": "漲跌價差",
        "Transaction": "成交筆數"
    }

    df.rename(columns=column_map, inplace=True)
    return df
