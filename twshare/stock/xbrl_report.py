import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def xbrl(stock_id: str, year_quarter: str = None) -> None:
    output_dir = os.path.join(os.getcwd(), "xbrl_data")
    os.makedirs(output_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": output_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print("✅ 開啟 MOPS 觀測站...")
        driver.get("https://mopsov.twse.com.tw/mops/web/t203sb01")
        time.sleep(7)

        print(f"✅ 輸入股票代號 {stock_id}")
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "co_id"))
        )
        input_box.clear()
        input_box.send_keys(stock_id)
        time.sleep(0.5)

        print("✅ 點擊查詢")
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @onclick="javascript:doAction();ajax1(document.form1,\'table01\');"]'))
        )
        search_button.click()
        time.sleep(3)

        print("✅ 等待結果表格載入")
        table = driver.find_element(By.ID, "table01")
        rows = table.find_elements(By.TAG_NAME, "tr")

        target_row = None
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            if not cols:
                continue
            period = cols[0].text.strip()
            if year_quarter is None or period == year_quarter:
                target_row = row
                print(f"✅ 選定期別：{period}")
                break

        if not target_row:
            print("❌ 找不到符合的年季別")
            return

        # 紀錄下載前文件清單
        before_files = set(os.listdir(output_dir))

        # 點下載按鈕
        download_button = target_row.find_element(By.XPATH, ".//input[@type='button' and contains(@onclick, 'FileDownLoad')]")
        download_button.click()
        print("✅ 已透過 Selenium 點擊下載按鈕，等待檔案下載中...")

        # 等待新文件出现在文件夾中
        new_file = None
        for _ in range(20):  # 最多等 10 秒
            time.sleep(0.5)
            after_files = set(os.listdir(output_dir))
            new_files = after_files - before_files
            if new_files:
                new_file = new_files.pop()
                break

        if new_file:
            old_path = os.path.join(output_dir, new_file)
            new_filename = f"{stock_id}_{year_quarter or 'latest'}.html"
            new_path = os.path.join(output_dir, new_filename)
            os.rename(old_path, new_path)
            print(f"✅ 成功下載並重新命名為：{new_filename}")
        else:
            print("❌ 等待下載失敗，未偵測到新檔案")

    except Exception as e:
        import traceback
        print(f"❌ 錯誤：{e}")
        traceback.print_exc()

    finally:
        driver.quit()