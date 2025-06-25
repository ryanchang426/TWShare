import numpy as np
import pandas as pd
import os
import json
from IPython.display import display, HTML

def stock_check1(df: pd.DataFrame, source_name: str, schema_dir: str = "./schemas") -> None:
    os.makedirs(schema_dir, exist_ok=True)
    schema_path = os.path.join(schema_dir, f"schema_{source_name}.json")

    # 1. 若本地已有前一天 schema，則讀入作為檢查標準
    if os.path.exists(schema_path):
        with open(schema_path, "r", encoding="utf-8") as f:
            expected_cols = set(json.load(f))
        print(f" 使用昨日儲存的 schema 進行欄位檢查：{source_name}")
    else:
        # 第一次使用時直接建立標準
        expected_cols = set(df.columns)
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(list(expected_cols), f, ensure_ascii=False, indent=2)
        print(f" 初次建立 schema: {source_name}")
    
    actual_cols = set(df.columns)

    # 2. 檢查欄位異動
    if expected_cols == actual_cols:
        print("✅ 欄位結構與昨日一致")
    else:
        print("⚠️ 欄位結構發生變動！")
        print(f"- 缺少欄位：{expected_cols - actual_cols}")
        print(f"- 多出欄位：{actual_cols - expected_cols}")

    # 3. 自動更新 schema 為今日版本
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(list(actual_cols), f, ensure_ascii=False, indent=2)
        print("--已更新 schema 為今日版本--")

    # 4. 資料列數
    print(f" 資料維度：{df.shape[0]} rows × {df.shape[1]} columns")

    # 5. 判斷 NaN
    null_mask = df.isnull()
    null_counts = null_mask.sum()
    total_null = null_counts.sum()

    # 6. 判斷空字串
    empty_mask = df.astype(str).apply(lambda col: col.str.strip() == "")
    empty_string_counts = empty_mask.sum()
    total_empty = empty_string_counts.sum()

    if total_null + total_empty > 0:
        print(f" 發現 {total_null} 個 NaN 及 {total_empty} 個空字串欄位")
    
    if total_null > 0:
        print("-- NaN 欄位統計：")
        print(null_counts[null_counts > 0])
        print("-- 對應資料預覽(NaN): ")
        display(HTML(df[null_mask.any(axis=1)].to_html(max_cols=1000)))
    
    if total_empty > 0:
        print("-- 空字串欄位統計：")
        print(empty_string_counts[empty_string_counts > 0])
        print("-- 對應資料預覽(空字串): ")
        display(HTML(df[empty_mask.any(axis=1)].to_html(max_cols=1000)))
    else:
        print("✅ 無缺失值")
