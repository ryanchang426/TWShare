import pandas as pd
from datetime import datetime

def tdcc_share_distribution():
    url = "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5"
    df = pd.read_csv(url)
    today_str = datetime.today().strftime("%Y%m%d")
    df.attrs['download_date'] = today_str
    return df