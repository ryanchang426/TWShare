import pandas as pd
import requests

def stock_tpex_company_info(category: str = "tpex") -> pd.DataFrame:
    """
    抓取 TPEx 的上櫃（tpex）或興櫃（otc）公司基本資料，
    返回格式：DataFrame。
    """
    url_map = {
        "tpex": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O",
        "otc": "https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_R"
    }

    if category not in url_map:
        raise ValueError("category 只支持 'tpex' 或 'otc'")

    url = url_map[category]
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "If-Modified-Since": "Mon, 26 Jul 1997 05:00:00 GMT"
    }

    resp = requests.get(url, headers=headers, verify=False)
    resp.raise_for_status()

    data = resp.json()  # 直接解析 JSON
    df = pd.DataFrame(data)

    # 中文欄位名稱對應
    df.columns = [
        "日期", "股票代碼", "公司名稱", "公司簡稱", "公司登記地",
        "產業別代碼", "地址", "統一編號", "董事長", "總經理",
        "發言人", "發言人職稱", "代理發言人", "電話", "設立日期",
        "上櫃日期", "每股面額", "實收資本額(元)", "私募股數", "特別股股數",
        "財報編製類型", "股務代理機構", "股務代理電話", "股務代理地址", "會計師事務所",
        "簽證會計師一", "簽證會計師二","英文簡稱","傳真機號碼","電子郵件信箱","網址","已發行股數"
    ]

    return df
 