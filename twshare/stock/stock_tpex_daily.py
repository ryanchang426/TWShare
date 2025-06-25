import pandas as pd
import requests

def stock_tpex_daily() -> pd.DataFrame:
    """
    擷取櫃買中心每日市況
    """
    url = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes"
    resp = requests.get(url, verify=False)
    resp.raise_for_status()
    df = pd.DataFrame(resp.json())

    column_map = {
    "Date": "交易日期",
    "SecuritiesCompanyCode": "證券代號",
    "CompanyName": "公司名稱",
    "Close": "收盤價",
    "Change": "漲跌價差",
    "Open": "開盤價",
    "High": "最高價",
    "Low": "最低價",
    "Average": "均價",
    "TradingShares": "成交股數",
    "TransactionAmount": "成交金額",
    "TransactionNumber": "成交筆數",
    "LatestBidPrice": "買進價格",
    "LatesAskPrice": "賣出價格",
    "Capitals": "股本",
    "NextReferencePrice": "次日參考價",
    "NextLimitUp": "次日漲停價",
    "NextLimitDown": "次日跌停價"
}

    df.rename(columns=column_map, inplace=True)
    return df


