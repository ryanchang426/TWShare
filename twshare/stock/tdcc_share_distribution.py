import os
import pandas as pd
from datetime import datetime

def tdcc_share_distribution():
    url = "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5"

    # 產生儲存路徑
    base_dir = os.path.dirname(__file__)
    save_dir = os.path.join(base_dir, "..", "data")
    os.makedirs(save_dir, exist_ok=True)

    today_str = datetime.today().strftime("%Y%m%d")
    file_name = f"tdcc_share_distribution_{today_str}.csv"
    file_path = os.path.join(save_dir, file_name)

    # 讀取 CSV
    df = pd.read_csv(url)

    # 存成 UTF-8-sig (兼容 Excel)
    df.to_csv(file_path, index=False, encoding="utf-8-sig")

    print(f"下載並轉存完成：{file_path}")