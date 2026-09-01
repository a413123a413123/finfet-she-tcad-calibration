# PROGRESS — 87 篇逐篇深度介紹　✅ 完成

任務來源：[PROMPT_87篇逐篇深度介紹.md](PROMPT_87篇逐篇深度介紹.md)　·　工作清單：[WORKLIST.md](WORKLIST.md)
**網頁 artifact**：https://claude.ai/code/artifact/5a4735e7-c20a-4bc2-a0e8-0b6c2c896bd4

## 完成定義（DoD）逐項核對

| # | 項目 | 結果 |
|---|---|---|
| 1 | WORKLIST 87 筆，與 PDF 五章逐一比對無缺漏 | ✅ 16+14+8+45+4 = 87，DOI 全唯一 |
| 2 | `cards/` 卡片總數 = 87 | ✅ 87（缺漏 0、多出 0、重複 0） |
| 3 | 每張卡八欄齊全，每個數字有來源標註 | ✅ 空欄位 0；批判 <3 點者 0；273 個來源 URL |
| 4 | PROGRESS 顯示 87/87 並列出未取得篇目 | ✅ 見下 |
| 5 | artifact 已發布 | ✅ |

### 反幻覺稽核（程式化，全數通過）
- 宣稱取得但 sources 為空：**0 筆**
- access_level=未取得 卻出現百分比數字：**0 筆**
- sources 含非 URL 字串：**0 筆**

## 產出

| 檔案 | 內容 |
|---|---|
| [cards/02_ET_vs_ISO_FinFET.md](cards/02_ET_vs_ISO_FinFET.md) | 第二章 16 篇（102 KB） |
| [cards/03_ET_vs_ISO_NS_GAA.md](cards/03_ET_vs_ISO_NS_GAA.md) | 第三章 14 篇（99 KB） |
| [cards/04_measurement.md](cards/04_measurement.md) | 第四章 8 篇（58 KB） |
| [cards/05_Rth_dT.md](cards/05_Rth_dT.md) | 第五章 45 篇（289 KB） |
| [cards/07_ta_sweep.md](cards/07_ta_sweep.md) | 第七章 4 篇（32 KB） |
| [87papers_review.html](87papers_review.html) | 網頁版（595 KB，已發布為 artifact） |
| [make_review.py](make_review.py) | 從 `_cards.json` 重建上述全部產出 |
| `_worklist.json` / `_items.json` / `_cards.json` | 中間資料，可重跑 |

第六章（可靠度／其他指標，34 篇）依指示完全排除：未解析、未查證、未產出。

## 取得層級實況

| 層級 | 篇數 | 說明 |
|---|---|---|
| 全文 | 16 | 主要為 MDPI / IOP / Sci. Rep. / arXiv / KoreaScience |
| 摘要 | 65 | 主要為 IEEE（TED / IEDM / IRPS），付費牆內僅得摘要 |
| 僅 metadata | 6 | 見下清單 |
| **完全未取得** | **0** | — |

IEEE 61 篇 / 非 IEEE 26 篇。查證來源 URL 共 273 個，年份跨度 2008–2026。

### 僅 metadata 的 6 篇（引用前必須自行取得全文）
- 二11 `10.1007/s12633-023-02835-3` — Springer 與 colab.ws 鏡像的摘要數字皆被截斷
- 二13 `10.1016/j.mejo.2024.106152` — Elsevier
- 二14 `10.1016/j.mejo.2023.105765` — Elsevier
- 三09 `10.1016/j.microrel.2025.115588` — ScienceDirect 403
- 三13 `10.1016/j.mejo.2023.105904` — Elsevier
- 五42 `10.1016/j.microrel.2017.12.034` — Elsevier；唯一 D 級（不建議引用，取得全文後極可能升 A/B）

## 可引用性分級

| 級 | 篇數 | 定義 |
|---|---|---|
| A | 23 | 可直接引用數字 |
| B | 37 | 只能引用定性結論 |
| C | 26 | 僅可當背景引用 |
| D | 1 | 不建議引用（五42） |

方法類型：Rth-extraction 24｜ET-vs-ISO 23｜model 23｜pulsed-vs-DC 7｜ta_sweep 5｜未取得 5

⚠ **ta_sweep 有 5 篇，但第七章只有 4 篇** — 三12（`10.3390/nano13222971`）與五03（`10.1109/EDTM58488.2024.10511833`）經本次查證判為 ta_sweep 性質，而七01 的分類另有討論。引用這兩篇的百分比前務必確認是自熱還是環境溫度造成。

## 本次查證的修正與衝突（10 筆）

### CONFLICT（1 筆，兩說並列未覆蓋原表）
- **五40** `10.26565/2312-4334-2025-3-35` — 原表記 Fig.5 中「HfO2 BOX 最高」；全文只印出「SiO₂+Si₃N₄ 最低」，且該文 Table 2 熱導率 SiO2 1.4 < HfO2 2.3，依其自述機制應為 SiO2 BOX 最熱，與原表方向相反。需自行重讀 Fig.5 三條曲線判定。

### CORRECTION（9 筆）
- **二16** `10.5573/ieie.2015.52.10.064` — 原表記「無任何 %」；自 KoreaScience 取得免費全文後，Figure 3 標註 SOI 19% / bulk 14%，且有 Id 絕對值（SOI 1.28→1.04、bulk 1.21→1.05 mA/μm @Vd=Vg=1.0V、TA=300K）
- **五03** `10.1109/EDTM58488.2024.10511833` — 原表記「摘要未載」；摘要實際印出四個百分比（JL 改善 5.1%/11.5%，IM 退化 7.4%/21.51%）
- **五14** `10.1109/ISQED.2019.8697786` — GAAFET 溫升摘要作 17 K、正文 Sec. V 作 18 K，原表「摘要與全文一致」不成立
- **五44** `10.5573/jsts.2016.16.2.204` — 原文 Rth 功率單位 mW 與元件物理不自洽（會推得單鰭 45 mA），依內部一致性應為 μW；重建後 Rth=1.05 MK/W 正落 1–4 MK/W 判準帶
- **五35** — 該文無註冊 DOI（Crossref 題名檢索無命中、OpenAlex doi 欄為 null），bib 應改以「2013 Symposium on VLSI Technology, IEEE Xplore doc. 6576663」定位
- **二07** `10.1109/ULIS.2008.4527143` — 取得層級由「未取得」上修為「摘要」（OpenAlex abstract_inverted_index 重建成功）
- **二06** `10.1109/SISPAD.2014.6931615` — 應為「SOI 與 bulk 各一範例並比較」而非「SOI（含 bulk 範例）」；另原表提到的姊妹作數值 341→433 K(bulk) / 351→457 K(SOI) 屬另一篇
- **三03** `10.1109/icee56203.2022.10117683` — Semantic Scholar 將 venue 誤植為 E-Business and E-Government 會議，正確為 2022 IEEE ICEE
- **三12** `10.3390/nano13222971` — 圖號修正

## 執行紀錄

- 階段 1 解析：修掉三個 PDF 陷阱 —— 硬換行切斷 DOI、五35 的識別是 IEEE Xplore URL 非 DOI、查證狀態欄被換行切開（`value_corr` + `ected`）
- 階段 2 查證：13 批平行 subagent（每批 7 篇），13/13 成功、0 錯誤、501 次工具呼叫、約 17 分鐘
- 差異標記偵測需剔除否定語境 —— agent 常寫「無 CONFLICT」「非 CORRECTION」，粗略字串比對會誤判成 28 筆，實際 10 筆
- 階段 5 視覺檢查：全頁 595 KB / 14885 px 超過截圖工具負荷，改切片段（`_frag_*.html`）逐區檢視，明暗兩色皆驗
