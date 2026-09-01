# FinFET 自熱效應文獻庫 — TCAD 校準用

87 篇矽 FinFET 自熱效應（self-heating effect, SHE）文獻的逐篇深度卡，用途是校準飽和區自熱的 TCAD deck。

## 這是什麼

從一份既有的 121 篇 SHE 文獻目錄（`FinFET_SHE_saturation_Ion_121papers (3).pdf`）出發，對第二、三、四、五、七章共 **87 篇逐篇上網重新查證**，每篇產出固定八欄的深度卡。第六章（可靠度／其他指標，34 篇）依需求完全排除，未解析、未查證、未產出。

兩個用途：

- **TCAD 校準** — 從文獻取得 Rth／ΔT／thermode 邊界條件的合理量級，校準矽 FinFET 飽和區自熱模擬
- **領域掌握** — 知道哪幾篇必讀、哪些是離群值、哪些不能引用

| 章 | 分類 | 篇數 |
|---|---|---|
| 二 | 電熱 vs 等溫（ET-vs-ISO）｜矽 FinFET | 16 |
| 三 | 電熱 vs 等溫｜nanosheet / GAA | 14 |
| 四 | 量測 pulsed-vs-DC / TRE | 8 |
| 五 | 熱阻 Rth / ΔT | 45 |
| 七 | ta_sweep（環境溫度掃描，**不是** SHE） | 4 |
| | **合計** | **87** |

## 資料紀律

這是本專案的核心設計，決定卡片可不可信：

- 每個數字都標**來源 URL 與取得層級**（全文／摘要／僅 metadata／未取得）
- **讀不到就寫「未取得」** —— 這是可接受的答案，編造不是
- 與原目錄數值衝突時**兩說並列標 CONFLICT**，不覆蓋原記載
- 確認原目錄有誤時標 **CORRECTION** 並附證據 URL
- 不新增原目錄以外的論文

程式化稽核結果（全數通過）：

| 檢查 | 結果 |
|---|---|
| 宣稱取得內容但 sources 為空 | 0 筆 |
| 標「未取得」卻出現百分比數字 | 0 筆 |
| sources 含非 URL 字串 | 0 筆 |
| 八欄有空欄位 | 0 筆 |
| 批判少於 3 點 | 0 筆 |

共 273 個查證來源 URL，年份跨度 2008–2026。

## 取得層級實況

| 層級 | 篇數 | 說明 |
|---|---|---|
| 全文 | 16 | MDPI / IOP / Sci. Rep. / arXiv / KoreaScience |
| 摘要 | 65 | 多為 IEEE（TED / IEDM / IRPS），付費牆內僅得摘要 |
| 僅 metadata | 6 | 多為 Elsevier；引用前必須自行取得全文 |
| 完全未取得 | 0 | — |

IEEE 61 篇／非 IEEE 26 篇。**摘要層級佔多數是付費牆的資料現實，不是查證失敗** —— 卡片會照實標明，不會拿推測填補。

可引用性分級：**A** 可直接引用數字 23 篇｜**B** 只能引用定性結論 37 篇｜**C** 僅可當背景引用 26 篇｜**D** 不建議引用 1 篇。

## 判準帶

沿用原目錄第一章，逐字不動。每張卡的批判第 1 點都據此判定落在帶內或帶外。

| 項目 | 值 | 備註 |
|---|---|---|
| 標準矽 FinFET 飽和 Ion 下降 | ~7–11 % | VDD≈0.7 V、TA=300 K、電熱 vs 等溫；bulk 3–12 %、SOI 8–17 % |
| 交叉檢核比值 | ΔIon% ÷ ΔT ≈ 0.10–0.20 %/K | 兩端都對得上才算自洽 |
| 過強訊號 | 飽和 Ion 差 > 20 % | 排除 DMG／junctionless 特例後 → 查 thermode 是否過絕熱 |
| 過弱訊號 | 飽和 Ion 差 < 1 % | SHE 被邊界條件抹掉 → 查 thermode 是否貼太近通道 |
| single-fin 熱阻 | Rth ≈ 1–4 MK/W | 單鰭元件級 |
| 多鰭多指 RF 結構熱阻 | Rth ≈ 34 kK/W | 與單鰭相差近百倍，最常搞錯的量級 |
| 核心錨點 · 14 nm | n 7.26 % / p 8.91 % @VDS=0.7 V | 卡片 二09（全文可取得） |
| 核心錨點 · 3 nm | n 10.6 % / p 21.6 % @VG=VD=0.7 V | 卡片 二08；p 值含機械應力糾纏，非硬上限 |

## 本次查證翻出的 10 筆修正與衝突

完整清單見 [PROGRESS.md](PROGRESS.md)，最值得注意的幾筆：

- **二16** — 原目錄記「無任何 %」；自 KoreaScience 取得免費全文後，Figure 3 標註 SOI 19% / bulk 14%，且有 Id 絕對值（SOI 1.28→1.04、bulk 1.21→1.05 mA/μm @Vd=Vg=1.0 V、TA=300 K）
- **五44** — 原文 Rth 的功率單位 mW 與元件物理不自洽（會推得單鰭 45 mA），依內部一致性應為 μW；重建後 Rth=1.05 MK/W 正好落進 1–4 MK/W 判準帶
- **五14** — GAAFET 溫升摘要作 17 K、正文 Sec. V 作 18 K，原目錄「摘要與全文一致」的判定不成立
- **五35** — 該文**沒有註冊 DOI**（Crossref 題名檢索無命中、OpenAlex doi 欄為 null），bib 應改以「2013 Symposium on VLSI Technology, IEEE Xplore doc. 6576663」定位
- **五40**（唯一 CONFLICT）— 原目錄記 Fig.5 中「HfO2 BOX 最高」；全文只印出「SiO₂+Si₃N₄ 最低」，且該文 Table 2 熱導率 SiO2 1.4 < HfO2 2.3，依其自述機制應為 SiO2 BOX 最熱，方向相反。兩說並列，需自行重讀原圖判定

**分類警訊**：`method_type` 判為 `ta_sweep` 的有 5 篇，但第七章只有 4 篇 —— 三12 與五03 是環境溫度掃描性質卻不在第七章。引用它們的百分比前務必確認是自熱造成還是環境溫度造成，這正是原目錄自己點名的「最常見分類陷阱」。

## 八欄卡片規格

| # | 欄位 | 內容 |
|---|---|---|
| 1 | 識別 | 補全的完整標題、第一作者與單位、期刊或會議全名、年、DOI |
| 2 | 元件 | 節點、bulk/SOI/GAA/nanosheet/CFET、Lg、fin 或 sheet 幾何、n/p、鰭數 |
| 3 | 方法與 SHE 定義 | `ET-vs-ISO`／`pulsed-vs-DC`／`Rth-extraction`／`ta_sweep`／`model`，加求解器、熱邊界、thermode 位置與 SurfaceResistance |
| 4 | 關鍵定量結果 | Ion 下降 %、Rth、ΔT、峰值晶格溫度 + 對應偏壓；含逐字英文引用；標明「原文印出數字」或「僅圖層級」 |
| 5 | TCAD 校準用途 | 這篇能餵給 deck 什麼；不可用時寫明理由 |
| 6 | 批判 | 至少 3 點，第 1 點固定為判準帶內／外判定 |
| 7 | 可引用性 | A／B／C／D + 理由 |
| 8 | 取得狀態 | 取得層級、來源 URL、與原目錄的差異 |

## 重建

```bash
pip install pymupdf
```

```bash
python parse_pdf.py
```

階段 1：PDF → `WORKLIST.md`（87 筆，內建 16/14/8/45/4 對數驗證，不通過會中止）

```bash
python make_review.py
```

階段 3：`_cards.json` → `cards/*.md` + `87papers_review.html`

**階段 2（87 篇上網查證 → `_cards.json`）無法純腳本化**：需要對每個 DOI 走一次取得鏈（Semantic Scholar API → OpenAlex → openAccessPdf／arXiv → doi.org 出版者頁 → 網頁搜尋）並撰寫八欄卡片。本次以 13 批平行 AI subagent 完成（每批 7 篇，501 次工具呼叫，約 17 分鐘），使用的完整 prompt 見 [PROMPT_87篇逐篇深度介紹.md](PROMPT_87篇逐篇深度介紹.md)。

`_cards.json` 已納入 repo，因此階段 1 與 3 可獨立重跑驗證 —— 實測重建出的 HTML 與 `cards/*.md` 與 repo 內版本**位元組完全一致**。

## 檔案

```
FinFET_SHE_saturation_Ion_121papers (3).pdf   來源目錄（121 篇）
parse_pdf.py          階段 1：PDF → WORKLIST（含對數驗證）
make_review.py        階段 3：_cards.json → Markdown + HTML
_style.css / _app.js  網頁版樣式與互動（由 make_review.py 內嵌）

WORKLIST.md           87 筆工作清單（DOI 為唯一識別鍵）
PROGRESS.md           完成核對表、稽核結果、修正清單
PROMPT_87篇逐篇深度介紹.md   階段 2 使用的完整 prompt

cards/                八欄深度卡（Markdown，依章分檔）
  02_ET_vs_ISO_FinFET.md    第二章 16 篇
  03_ET_vs_ISO_NS_GAA.md    第三章 14 篇
  04_measurement.md         第四章 8 篇
  05_Rth_dT.md              第五章 45 篇
  07_ta_sweep.md            第七章 4 篇
87papers_review.html  網頁版（可多維篩選、卡片可展開）

_121papers_fulltext.txt   PDF 抽取全文（UTF-8）
_sections.json            分章原始文字
_worklist.json            87 筆結構化條目
_items.json               餵給查證 agent 的精簡版
_cards.json               87 張卡的原始資料
_top10.json               必讀 Top 10 與挑選理由
```

### PDF 解析的三個陷阱

重跑 `parse_pdf.py` 時請勿移除這些處理：

1. 硬換行會切斷 DOI，例如 `10.1109/ted.2020.29978` + 換行 + `48`
2. 五35 的識別碼是 IEEE Xplore URL 而非 DOI（該文確實沒有註冊 DOI）
3. 查證狀態欄也會被換行切開，例如 `value_corr` + 換行 + `ected`

另有一個下游陷阱：判斷卡片是否標了 CONFLICT／CORRECTION 時，必須先剔除「無 CONFLICT」「非 CORRECTION」這類否定語境 —— 粗略字串比對會把 10 筆誤判成 28 筆。

## 使用聲明

- 卡片內的英文逐字引用出自各論文原文，著作權屬原作者與出版者；本庫為研究筆記用途
- 標「僅圖層級」者表示原文有曲線但未印出單一百分比，**引用前務必自讀原圖**
- 標 CONFLICT 者兩說並列，需自行讀原文判定
- 「僅 metadata」的 6 篇沒有任何內容層級的佐證，引用前必須自行取得全文
