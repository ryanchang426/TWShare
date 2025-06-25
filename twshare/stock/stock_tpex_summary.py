import pandas as pd
import requests

def stock_tpex_summary() -> pd.DataFrame:
    """
    擷取櫃買中心每日市況
    """
    url = "https://www.tpex.org.tw/openapi/v1/tpex_mainborad_highlight"
    resp = requests.get(url, verify=False)
    resp.raise_for_status()
    df = pd.DataFrame(resp.json())

    column_map = {
        "Date": "交易日期",
        "ListedCompanyNumbers": "上櫃公司數",
        "AuthorizedCapital": "發行股本（百萬）",
        "MarketCapitalization": "市值（百萬）",
        "DailyTradingValue": "當日成交金額（百萬）",
        "DailyTradingVolume": "當日成交股數（千股）",
        "CloseIndex": "收盤指數",
        "IndexChange": "指數漲跌點數",
        "PriceRiseCompanyNumbers": "上漲公司數",
        "LimitUpCompanyNumbers": "漲停公司數",
        "PriceDeclineCompanyNumbers": "下跌公司數",
        "LimitDownCompanyNumbers": "跌停公司數",
        "PriceFlatCompanyNumbers": "平盤公司數",
        "UnmatchedCompanyNumbersSuspensionStocksIncluded": "未成交公司數(含暫停交易)"
    }

    df.rename(columns=column_map, inplace=True)
    return df

