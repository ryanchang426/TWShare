import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def xbrl(stock_id: str, year_quarter: str = None) -> None:
    """
    stock_id      - 股票代号
    year_quarter  - 例如 '113Q1' 指定期别（可选），不传就下载第一笔最新
    """
    # 创建存储目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "xbrl_data")
    os.makedirs(output_dir, exist_ok=True)

    # Selenium 设定
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    prefs = {
        "download.default_directory": output_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # 开启 driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print(f"✅ 開啟 MOPS 觀測站...")
        url = "https://mopsov.twse.com.tw/mops/web/t203sb01"
        driver.get(url)
        time.sleep(2)

        # 填入股票代號
        print(f"✅ 輸入股票代號 {stock_id}")
        input_box = driver.find_element(By.ID, "co_id")
        input_box.clear()
        input_box.send_keys(stock_id)
        time.sleep(0.5)

        # 按查詢
        search_btn = driver.find_element(By.XPATH, '//button[contains(text(),"查詢")]')
        search_btn.click()
        time.sleep(3)

        # 等表格出現
        print("✅ 等待結果表格載入")
        table = driver.find_element(By.ID, "table01")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # 解析表格
        target_row = None
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            if not cells:
                continue
            period = cells[0].text.strip()
            if year_quarter is None or period == year_quarter:
                target_row = row
                print(f"✅ 選定期別：{period}")
                break

        if not target_row:
            print("❌ 找不到符合的年季別")
            return

        # 點擊下載按鈕
        download_link = target_row.find_element(By.LINK_TEXT, "下載")
        print(f"✅ 觸發下載...")
        download_link.click()

        # 等待下載
        time.sleep(10)
        print(f"✅ 檔案已下載到資料夾：{output_dir}")

    except Exception as e:
        print(f"❌ 發生錯誤：{e}")
    finally:
        driver.quit()