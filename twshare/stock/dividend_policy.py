import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def dividend_policy(stock_id: str) -> pd.DataFrame:
    # 設定 Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        url = f"https://goodinfo.tw/tw/StockDividendPolicy.asp?STOCK_ID={stock_id}"
        driver.get(url)
        time.sleep(3)
        
        # 取得股利政策表格 HTML
        div = driver.find_element(By.ID, "divDetail")
        html = div.get_attribute("outerHTML")
        
        # 轉成 DataFrame
        df = pd.read_html(html)[0]

        return df

    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

    finally:
        driver.quit()