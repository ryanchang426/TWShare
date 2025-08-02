# TWShare

**TWShare** 是一個以 Python 為基礎、仿照 AKShare 開發的台灣股市數據擷取工具包，支援自台灣證券交易所（TWSE）與櫃買中心（TPEx）等官方 API 擷取各類公開資料。  
旨在為金融研究者、資料分析師及投資人提供乾淨、結構化且可程式化取得的台股財經資料。

## 功能涵蓋：

1. 每日股價行情  
　　‣ TWSE 上市公司：`stock_twse_daily.py`  
　　‣ TPEx 上櫃公司：`stock_tpex_daily.py`

2. 公司基本資料查詢  
　　‣ TWSE 上市公司：`stock_twse_company.py`  
　　‣ TPEx 上櫃公司（支援 tpex/otc 分類）：`stock_tpex_company.py`

3. 市場整體/指數資料  
　　‣ TWSE 指數日行情：`stock_twse_index_daily.py`
    ‣ TPEx 行情汇总：`stock_tpex_summary.py`

4. 股利政策爬蟲（Selenium）  
　　‣ Goodinfo 股利決策：`dividend_policy.py`

5. XBRL 財報壓縮包下載  
　　‣ 自 TWSE 官網抓取並儲存完整壓縮檔：`xbrl_report.py`

6. TDCC 股東結構資料爬蟲  
　　‣ 集保戶股權結構分布：`tdcc_share_distribution.py`

7. 資料結構檢查工具  
　　‣ Schema 自動建立與比對：`stock_check.py`

8. CSV 儲存模組  
　　‣ 直接儲存 DataFrame 至 CSV：`csv_download.py`
