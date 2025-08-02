## 必要套件說明

| 套件名稱             | 用途說明                                                                 |
|----------------------|--------------------------------------------------------------------------|
| `pandas`             | 數據處理與分析，主要處理 `DataFrame` 結構                                 |
| `requests`           | 發送 HTTP API 請求，抓取 TWSE、TPEx 等公開資料                            |
| `selenium`           | 自動化瀏覽器操作，爬取無 API 提供的資料（如：XBRL 財報、Goodinfo 股利）    |
| `webdriver-manager`  | 自動下載與管理 ChromeDriver，搭配 Selenium 使用                           |
| `lxml`               | 加速 HTML/XML 解析，通常與 `pandas.read_html()` 配合使用                   |
| `openpyxl`           | 處理 Excel 格式檔案（`.xlsx`），可用於資料匯入與儲存                        |
