import pandas as pd

def csv_download(df: pd.DataFrame, filename: str) -> None:
    """
    df (pd.DataFrame)：要儲存的 DataFrame。
    filename (str)：CSV 檔案的名稱
    """
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"已儲存為 {filename}")

    