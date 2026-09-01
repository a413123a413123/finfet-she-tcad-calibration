# 第五章 · 熱阻 Rth / ΔT

_thermode SurfaceResistance 的校準標的_

原表 45 篇｜本檔 45 篇｜取得層級：摘要 40、全文 4、僅metadata 1

## 五01 — Multiscale Thermal Simulation for GAAFET With First-Principles-Based Boltzmann Transport Equation

- **DOI／識別**：`10.1109/TED.2025.3592887`　**來源**：IEEE　**年**：2025
- **作者／單位**：Yufei Sheng（第一作者），Shanghai Jiao Tong University, China；共同作者含 Yonglin Xia、Jiaxuan Xu、Shuying Wang（皆 SJTU）、Pengpeng Ren、Zhigang Ji、Hua Bao。
- **出處**：IEEE Transactions on Electron Devices

**1 元件**　摘要層級：gate-all-around field-effect transistors (GAAFETs)，特徵尺寸達 10 nm 等級；全文分析對象為 stacked nanosheet GAAFET。具體 Lg、TNS（nanosheet 厚度）、WNS（nanosheet 寬度）、堆疊層數、n 或 p 通道、鰭/指數：摘要未載，全文未取得（IEEE 付費牆，OpenAlex 確認 oa_status = closed、無任何機構庫全文）。

**2 方法與 SHE 定義**　`model`　多尺度純熱模擬：以 first-principles-based nongray phonon Boltzmann transport equation (BTE) 與 heat diffusion equation (HDE) 耦合；金屬區改以 electron–phonon BTE 納入尺寸相依熱導率；對照組為 gray BTE 與 HDE。摘要明言目的在於擺脫「以擬合的有效熱導率直接餵進 HDE 或熱阻網路」的傳統做法（"previous studies predominantly relied on simplified or fitting models to directly adjust the effective thermal conductivities of various device components within the heat diffusion equation (HDE) or thermal resistance networks"）。求解器名稱、網格、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無電性求解器耦合：摘要未載，未取得。

**3 關鍵定量結果**　無任何數值（無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度、無 VGS/VDS/TA）。摘要層級逐字引用（原文印出但為定性）："By comparing the temperature distributions calculated using the gray BTE and HDE, we demonstrate the necessity of employing the nongray phonon BTE for accurate simulation of the active region."；"We further discover that the size-dependent thermal conductivity of metal regions should be incorporated using the electron–phonon BTE."；"we identify that the amorphous passive layer, interfacial thermal resistance between different layers, along with the thermal resistance of the STI/BDI layers and interconnections, are key factors limiting heat dissipation." 溫度分布差異僅圖層級，且圖未取得。

**4 TCAD 校準用途**　不可直接校準，理由：可及文本無任何溫度、熱阻或電流數值，也無幾何尺寸，無法對應到 SurfaceResistance 量級或 ΔT 判準。但方法論上有兩點可直接影響使用者的 deck 設定：（a）本文的核心論點是 HDE / gray BTE 會低估主動區溫度，因此使用者若在 Sentaurus 中僅用傅立葉熱傳導（標準 thermodynamic/hydrodynamic 模型），解出的通道 ΔT 應視為下界，SHE 造成的 Ion 退化亦為下界；（b）本文指認主要熱阻項為 amorphous passive layer、層間界面熱阻、STI/BDI 與 interconnect——這對應到 deck 中 thermode 應該擺在哪裡：若把 thermode 直接貼在矽基板底部而不模擬 STI/BDI 與界面熱阻，等於把這些主導熱阻整段短路，SHE 會被邊界條件抹掉（落入判準帶「ΔIon% < 1%」的失效模式）。

**5 批判**
   1. 無數值可判定，原因：本次僅取得 Semantic Scholar 提供的摘要，摘要未印出任何溫度、熱阻或電流數字；IEEE 全文付費且 OpenAlex 確認無任何開放版本或機構庫全文，故無法與判準帶（7–11%、0.10–0.20 %/K、1–4 MK/W）比較。
   2. 元件類型不匹配：本篇是 stacked nanosheet GAAFET，使用者的目標是矽 FinFET；GAA 的熱是四面被閘極介電/金屬包住、散熱幾乎只能走源汲極與底部，與 fin 的散熱幾何不同，即使有數值也不能直接平移到 FinFET deck。
   3. 缺乏實驗錨點：摘要通篇為模擬對模擬的比較（nongray BTE vs gray BTE vs HDE），未提及任何實驗校驗；nongray BTE 的絕對溫度優勢在沒有量測對照時屬於方法論主張，不是被驗證的事實。
   4. 與使用者做法方向相反，正是其價值所在：本文明確反對用「擬合的有效熱導率＋熱阻網路」，而使用者的 thermode + SurfaceResistance 正是集總熱阻網路的做法。這篇不能拿來校準參數，但可以拿來論證該做法的系統性偏差方向（低估主動區峰值溫度），適合寫在論文的 limitation 段。
   5. 無誤差棒/重複性概念：純數值模擬，摘要未提網格收斂性、聲子譜取樣密度或第一原理計算的收斂判準，數值可信度無從評估。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景或方法論引用：可支持「傅立葉/灰體近似會低估奈米尺度元件主動區溫度」與「STI/BDI、界面熱阻、內連線是散熱瓶頸」這類定性陳述，並用於 limitation 討論；但無任何可引用的數字，元件類型亦非矽 FinFET。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2025.3592887?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/TED.2025.3592887

**8 與原表差異**　與原表一致：原表記「堆疊奈米片 GAAFET（約 10 nm 特徵尺寸）；摘要未給數值；僅定性指出 gray BTE/HDE 低估主動區溫度、需 nongray BTE；無（摘要未載）」，本次逐字複驗全部成立，無衝突。補充本次新增之書目與可及性事實：第一作者 Yufei Sheng 隸屬上海交通大學，OpenAlex 確認 oa_status = closed 且無任何機構庫全文版本，故「未取得全文」為資料現實而非查證不足。

---

## 五02 — Transient Thermal Model of Advanced Nanotransistors: A Case Study of CFET

- **DOI／識別**：`10.1109/TED.2025.3574124`　**來源**：IEEE　**年**：2025
- **作者／單位**：Kunlong An（第一作者），Institute of Microelectronics, Chinese Academy of Sciences, China；共同作者含 Qinzhi Xu、Hao He、Xiaoning Ma（皆 IMECAS / 中國科學院）、Zhiqiang Li。
- **出處**：IEEE Transactions on Electron Devices

**1 元件**　摘要層級：complementary field-effect transistor (CFET) 作為案例研究元件（"the thermal behavior of a complementary field-effect transistor (CFET) was investigated in detail as an illustration"）。技術節點、堆疊順序（n-on-p 或 p-on-n）、nanosheet 厚度/寬度、堆疊層數、Lg、鰭/指數：摘要皆未載明，全文未取得（IEEE 付費牆，OpenAlex 確認 oa_status = closed、無機構庫全文）。

**2 方法與 SHE 定義**　`model`　純數值熱模型：以 hydrodynamic regime 的 dual-phase lag (DPL) 方程建立 3-D 非傅立葉暫態熱模型；引入中間變數並以有限體積法 (finite volume method, FVM) 建構迭代數值演算法求解 3-D DPL 方程；對照組為傳統 Fourier 模型。額外討論 metal interconnect 對散熱的影響並提出熱優化策略。求解器名稱、網格、熱邊界條件、thermode 位置與 SurfaceResistance、是否耦合電性求解器（drift-diffusion / hydrodynamic 載子輸運）：摘要未載，未取得；DPL 的兩個弛豫時間 τq、τT 取值亦未載。

**3 關鍵定量結果**　無任何數值（無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度、無 VGS/VDS/TA）。摘要層級逐字引用（原文印出但為定性）："the simulation results between the Fourier model and the DPL model were compared to emphasize the importance of constructing the non-Fourier thermal mechanism."；"The impact of the metal interconnect on its thermal performance has been discussed and a feasible thermal optimization strategy was proposed." Fourier 與 DPL 的暫態溫度差異僅圖層級，圖未取得。

**4 TCAD 校準用途**　不可直接校準，理由：可及文本無任何溫度、熱阻、電流數值，亦無幾何尺寸與偏壓。方法論上可轉用兩點：（a）若使用者只做穩態 SHE（本任務主軸即為飽和區穩態 Ion），本文的非傅立葉修正基本不影響結論——DPL 與 Fourier 的差異集中在 ps–ns 級暫態，穩態解相同；這反而可以拿來論證「穩態 deck 用 Fourier 熱模型是合理的」。（b）本文指認 metal interconnect 是 CFET 的關鍵散熱路徑，呼應 deck 中 BEOL 熱阻是否被納入的問題。

**5 批判**
   1. 無數值可判定，原因：僅取得摘要，摘要未印出任何溫度或電流數字；IEEE 全文付費且 OpenAlex 確認無任何開放版本，無法與判準帶比較。
   2. 元件幾何與使用者目標差距最大：CFET 為垂直堆疊互補元件，上層元件的散熱必須穿過下層元件與內連線，熱路徑拓樸與單層矽 FinFET 完全不同，本批七篇中對使用者 deck 的幾何可對齊度最低。
   3. 模型自由參數未受檢驗：DPL 方程的關鍵在於熱通量弛豫時間 τq 與溫度梯度弛豫時間 τT，非傅立葉修正的量級完全由這組參數決定，而摘要未說明其取值來源（第一原理？實驗擬合？文獻沿用？）。在沒有實驗校驗的情況下，Fourier 與 DPL 的差異大小不具可信度。
   4. 是否為電熱耦合不明：摘要通篇只談熱模型與熱行為，未提任何電性求解器或 Ion；若本篇是給定發熱源的純熱模擬，則根本無法產出 ΔIon%，不能被歸類為 SHE 對電流影響的研究——引用時務必避免把它寫成「CFET 的 SHE 使電流下降 X%」。
   5. 無誤差棒/收斂性資訊：純數值工作，摘要未提網格獨立性驗證或與解析解的對照，數值演算法的正確性無從評估。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可支持「奈米尺度元件的 ps–ns 級暫態需要非傅立葉熱模型」與「CFET 的內連線是散熱瓶頸」這類定性陳述；無任何可引用數字，元件類型亦與矽 FinFET 相去甚遠。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2025.3574124?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/TED.2025.3574124

**8 與原表差異**　與原表一致：原表記「no values in abstract; Fourier-vs-DPL transient temperature differences shown figure-level only; not applicable / not accessible」，本次逐字複驗成立，無衝突。惟需標明一項無法複驗的記載：原表 orig 稱「monolithic CFET (stacked nFET-on-pFET)」，本次可及摘要僅稱 "a complementary field-effect transistor (CFET)"，未載明 monolithic 或堆疊順序（nFET-on-pFET）；該細節應標為未複驗。本次補充書目：第一作者 Kunlong An 隸屬中國科學院微電子研究所。

---

## 五03 — Impact of Back End of Line (BEOL) and Ambient Temperature on Self-Heating in Twin Nanowire Gate-All-Around FETs: Junctionless Mode Versus Inversion Mode

- **DOI／識別**：`10.1109/EDTM58488.2024.10511833`　**來源**：IEEE　**年**：2024
- **作者／單位**：Nitish Kumar（第一作者），Indian Institute of Technology Delhi, New Delhi, India（OpenAlex 原始單位字串為 "Indian Institute of Technology Delhi, New Delhi, India"）；共同作者 Karan Gupta、Ayush Gupta、Ankur Gupta、Pushpapraj Singh，單位同。
- **出處**：2024 IEEE Electron Devices Technology and Manufacturing Conference (EDTM)

**1 元件**　摘要層級：twin nanowire gate-all-around FET（雙奈米線 GAA FET），比較 junctionless (JL) mode 與 inversion mode (IM) 兩種操作模式。奈米線直徑、Lg、線間距、堆疊/並列數、n 或 p 通道、鰭數/指數：摘要皆未載，全文未取得（IEEE 付費牆，OpenAlex 確認 oa_status = closed、無開放版本）。

**2 方法與 SHE 定義**　`ta_sweep`　摘要層級：分析 BEOL effective thermal resistance (RTH) 與 isothermal ambient temperature (TA) 兩個掃描變數對 SHE 的影響。注意 RTH 與 TA 在此皆為「被掃描的邊界條件參數」，而非被抽出的結果量。求解器（Sentaurus / GARAND / 其他）、網格、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic/BTE/聲子模型：摘要全未載明，全文未取得；摘要甚至未明說是 TCAD 模擬或實驗（依「isothermal ambient temperature 為可掃描變數」與「BEOL effective RTH 為可掃描變數」判斷應為模擬，但此為推論而非可及文本所述）。

**3 關鍵定量結果**　四個百分比皆為摘要原文印出數字："The JL device performance is drastically improved by 5.1 % and 11.5 %, respectively, at higher $\\mathrm{R}_{\\mathrm{T}\\mathrm{H}}$ and $\\mathrm{T}_{\\mathrm{A}}$."；"However, the IM device performance is traditionally degraded by ~7.4 % and 21.51 %, respectively, at higher $\\mathrm{R}_{\\mathrm{T}\\mathrm{H}}$ and $\\mathrm{T}_{\\mathrm{A}}$." 即：JL 在較高 RTH 下改善 5.1%、在較高 TA 下改善 11.5%；IM 在較高 RTH 下退化約 7.4%、在較高 TA 下退化 21.51%。摘要未印出：RTH 的絕對值與掃描範圍、TA 的絕對值與掃描範圍、ΔT、峰值晶格溫度、VGS、VDS，以及「performance」究竟指 Ion、gm、SS 還是其他指標（此為關鍵語意缺口）。

**4 TCAD 校準用途**　不可直接校準，理由有三：（a）元件為 twin nanowire GAA 且其中一半是 junctionless，屬判準帶明文排除的特例，幾何與載子輸運機制皆無法對齊使用者的矽 FinFET；（b）21.51% 與 11.5% 是環境溫度 TA 掃描的結果，語意上是「改變 TA」而非「電熱 vs 等溫」的 SHE 對照，與判準帶定義的 ΔIon% 不是同一個量；（c）摘要無 RTH 絕對值（僅稱 higher/lower）、無 ΔT、無偏壓，無法反推 SurfaceResistance 量級或做 ΔIon%/ΔT 交叉檢核。唯一可用處是負面校準：它示範了「RTH 掃描」與「TA 掃描」兩種參數研究必須與 SHE 的 ET-vs-ISO 對照分開報告，使用者在自己的 deck 中做參數掃描時應比照切割，避免把 TA 效應報成 SHE 效應。

**5 批判**
   1. 判準帶判定：本篇的數字不應被放進判準帶比較，因為量的定義不對等。IM 隨 BEOL RTH 升高退化約 7.4%，數值上看似落在 bulk 3–12% 帶內，但它是「熱阻邊界條件變大 vs 變小」的差值，不是「電熱 vs 等溫」的差值；而 IM 隨 TA 升高退化 21.51%，若被誤當成 SHE 的 ΔIon% 就會落進判準帶「>20% 即 SHE 過強、thermode 可能過絕熱」的誤判區——實際上它只是環境溫度上升造成的移動度退化，與 thermode 設定無關。原表已將本篇 reclassified，判斷正確。
   2. 分類陷阱的教科書案例：本篇正是「ta_sweep 被誤當 SHE」的典型。TA 是等溫環境溫度（摘要明寫 "isothermal ambient temperature"），改 TA 是改邊界溫度，不會產生任何自熱資訊；引用時必須明確標註為 ta_sweep。
   3. 糾纏因子（junctionless）：JL 元件在較高 TA / 較高 RTH 下效能反而「改善」5.1% / 11.5%，這是 junctionless 通道特有的補償效應（體導通、摻雜濃度高，溫度上升時載子活化與移動度退化互相抵銷甚至淨為正），屬判準帶明文排除的 junctionless 特例，完全不可外推到 inversion-mode 矽 FinFET。同一篇內 JL 與 IM 走相反方向，本身就證明結論高度依賴通道工程。
   4. 關鍵語意缺口：摘要通篇用 "device performance" 而未定義是 Ion、drive current、gm 還是延遲；在不知道被量的是什麼的情況下，5.1 / 11.5 / 7.4 / 21.51 這四個百分比無法對應到任何 TCAD 可比對的量。
   5. 精度宣稱與資訊量不匹配：21.51% 給到小數點後兩位、5.1% 給到一位、7.4% 前面還加 "~"，同一段內精度標示不一致；摘要無誤差棒、無元件數、無網格收斂或重複性資訊，這種位數的宣稱缺乏支撐。

**6 可引用性**　B（只能引用定性結論）— 可引用定性結論（junctionless mode 與 inversion mode 在高 BEOL 熱阻與高環境溫度下呈相反趨勢；BEOL 熱阻是 GAA 元件 SHE 的重要邊界條件），四個百分比雖為原文印出、可如實轉述，但因基準量（"performance" 指什麼）與掃描範圍未定義、且屬 ta_sweep 而非 SHE 對照，不建議當作 SHE 數值引用或寫進判準帶比較。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edtm58488.2024.10511833?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/EDTM58488.2024.10511833

**8 與原表差異**　CORRECTION：原表 orig 記「摘要未載」「摘要未列 VGS/VDS；RTH 與 TA 為掃描變數」，但本次自 Semantic Scholar 取得的摘要全文確實印出四個百分比——JL 在較高 RTH / TA 下分別改善 5.1% 與 11.5%，IM 在較高 RTH / TA 下分別退化約 7.4% 與 21.51%。證據 URL：https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edtm58488.2024.10511833?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf 。原表「摘要未列 VGS/VDS」與「RTH 與 TA 為掃描變數」兩點本次複驗成立，維持不變；原表 verdict「reclassified」（歸類為 ta_sweep 而非 SHE）本次確認正確。另補正單位：本文作者群依 OpenAlex 原始單位字串為 Indian Institute of Technology Delhi。

---

## 五04 — Understanding the Self-Heating Effects Measured With the AC Output Conductance Method in Advanced FinFET Nodes

- **DOI／識別**：`10.1109/TED.2024.3469187`　**來源**：IEEE　**年**：2024
- **作者／單位**：L. Tondelli（第一作者），Università degli Studi di Modena e Reggio Emilia（University of Modena and Reggio Emilia）, Italy —— 依 UniMoRe 機構典藏庫 IRIS 之 OAI-PMH 紀錄（oai:iris.unimore.it:11380/1364190）認定；共同作者 R. Asanovski、A. J. Scholten、T. V. Dinh、S.-W. Tam、R. M. T. Pijper、L. Selmi（Scholten 與 Pijper 為業界合作者，個別單位字串本次未取得）。
- **出處**：IEEE Transactions on Electron Devices

**1 元件**　摘要層級：bulk FinFET（IRIS 關鍵字第一項即 "Bulk FinFET"），涵蓋 short-channel 與 long-channel 兩類元件，並對 scaled technology nodes 做投影。具體技術節點、Lg、Hfin、Wfin、鰭數/指數、n 或 p 通道：摘要與 metadata 皆未載，全文未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　電熱模擬為主、以實驗校準："we use extensive electrothermal simulations, calibrated against experiments, to validate a popular method to monitor SHEs based on the measured AC output conductance." 研究內容為比較 AC output conductance 法抽出的過溫與鰭內最高溫，並掃描元件偏壓與尺寸。求解器名稱、網格、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic/BTE/聲子模型：摘要與 IRIS metadata 皆未載明。唯一明確的材料模型資訊為：奈米尺度矽鰭的熱導率相對塊材矽退化（"The results confirm that nanoscale silicon fins exhibit degraded thermal conductivity compared with the bulk silicon case."）。IRIS 索引關鍵字為 Bulk FinFET、device reliability、self-heating、thermal conductivity、thermal resistance。

**3 關鍵定量結果**　無任何數值（無 Ion 下降 %、無 Rth 數值、無 ΔT 數值、無峰值晶格溫度數值、無 VGS/VDS/TA）。摘要層級逐字引用（原文印出但為定性）："1) the overtemperature extracted with the AC output conductance method represents an average overtemperature across the device active area and 2) the AC conductance method largely underestimates the peak temperature of long-channel devices; less so for short-channel ones. In this latter case, however, the difference between the above temperatures changes appreciably as a function of gate voltage." 具體的 ΔT_avg 與 ΔT_peak 數值、偏壓相依曲線、縮放節點投影值皆為圖層級，全文未取得（IEEE 付費牆；Unpaywall/OpenAlex 標示 GREEN OA 指向 UniMoRe IRIS，但該站以 Cloudflare 質詢阻擋，PDF 未取得）。

**4 TCAD 校準用途**　方法論上高價值，數值上不可直接校準。可用之處：（a）語意校準——凡是文獻用 AC output conductance 法量到的 Rth 與 ΔT（本批的四08 即屬此類），代表的是主動區的「面積平均過溫」，不是鰭內峰值溫度；使用者若拿這類文獻 ΔT 去對 deck 解出的 peak lattice temperature，會系統性低估峰值，進而把 thermode 調得過度絕熱以「補」出差額，落入判準帶所述的失效模式。（b）長短通道差異——長通道元件的低估幅度大、短通道小，使用者若模擬短通道 FinFET，AC-gout 型文獻值與 peak 的落差相對可接受；模擬長通道對照組時則不可混用。（c）偏壓相依——ΔT_peak 與 ΔT_avg 的差值隨 VGS 明顯變化，因此單一偏壓點的校準不可外推到整條 ID-VG 曲線；deck 校準應至少取兩個 VGS 點交叉檢核。（d）材料模型——明確支持在 deck 中把奈米尺度矽鰭的熱導率設得低於塊材矽，這是直接影響 Rth 與 ΔT 的設定項。（e）不可用於設定 SurfaceResistance 具體數值，理由：可及文本無任何 Rth 或 ΔT 的數字。

**5 批判**
   1. 無數值可判定，原因：IEEE 全文付費，Unpaywall 標示的 GREEN OA 位置（UniMoRe IRIS, hdl 11380/1364190）以 Cloudflare 質詢阻擋、DSpace REST 與網頁皆回 403，本次僅能自 IRIS 的 OAI-PMH 介面與 Semantic Scholar 取得完整摘要；摘要未印出任何 Rth/ΔT/Ion 數字，故無法與判準帶（7–11%、0.10–0.20 %/K、single-fin 1–4 MK/W）比較。
   2. 本批對使用者 deck 最關鍵的一篇：它直接指出「量測到的過溫」與「模擬解出的峰值溫度」是兩個不同的量。使用者若把兩者混為一談，校準方向會系統性偏誤——為了讓 deck 的 peak 溫度對上文獻的 avg 過溫，會不自覺把 thermode 拉遠或加大 SurfaceResistance，造成過絕熱。這是本篇最該被引用的一點。
   3. 校準資料不透明：摘要稱電熱模擬 "calibrated against experiments"，但未載明校準用的節點、元件尺寸、元件數量、量測頻率範圍與擬合殘差；可重複性無從評估，且有業界合作者參與（Scholten、Pijper），製程細節通常不公開。
   4. 外推層級需標明："providing a few projections toward scaled technology nodes" 屬模型投影而非量測或校準過的模擬結果；引用時必須標為 projection，否則會把外推值當成已驗證數據。
   5. 無誤差棒與重複性資訊：摘要層級未提元件數、批次、量測不確定度；且結論 2) 的「largely underestimates」缺乏量化幅度，需自讀原圖才有數字。
   6. 分類正確：本篇是 Rth-extraction 方法本身的效度研究（驗證 AC-gout 法量到的是什麼），而非 ta_sweep，也不是 ET-vs-ISO 的 Ion 退化量化，分類無誤。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論——(i) AC output conductance 法抽出的過溫是主動區面積平均過溫；(ii) 該法大幅低估長通道元件的峰值溫度、短通道低估較少；(iii) 兩者差值隨閘極電壓明顯變化；(iv) 奈米尺度矽鰭熱導率低於塊材矽。這四點都是原文印出的明確主張且對使用者的校準方法論直接有用，但全篇無任何可引用的數值。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2024.3469187?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://iris.unimore.it/oai/request?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:iris.unimore.it:11380/1364190
   - https://api.openalex.org/works/doi:10.1109/TED.2024.3469187

**8 與原表差異**　與原表一致：原表記「advanced-node bulk silicon FinFETs, short- and long-channel…；abstract confirms: AC-gout overtemperature = area-averaged overtemperature across active area; largely underestimates pe…；gate-voltage dependence discussed; specific VGS/VDS values figure-level, not accessed」，本次以 Semantic Scholar 與 IRIS OAI-PMH 兩個獨立來源逐字複驗全部成立，無衝突。本次補充之新事實：(1) 完整作者列表與第一作者單位（L. Tondelli, University of Modena and Reggio Emilia，依 IRIS 機構典藏認定）；(2) IRIS 索引關鍵字含 "Bulk FinFET"，佐證元件為 bulk 而非 SOI；(3) 可及性細節——Unpaywall 記錄本文為 GREEN OA（CC-BY, submittedVersion）指向 hdl.handle.net/11380/1364190，但該站台以 Cloudflare 質詢阻擋自動存取，實際 PDF 本次未取得，故存取層級維持「摘要」。

---

## 五05 — Influence of the Gate Oxide and Back Oxide Material Types on Self-heating Effect in Junctionless FinFET

- **DOI／識別**：`10.1109/EDM61683.2024.10615156`　**來源**：IEEE　**年**：2024
- **作者／單位**：Atabek Atamuratov（第一作者），Urgench State University, Physics Department, Urgench, Uzbekistan；合著者分屬 Tashkent University of Information Technologies（Uzbekistan）與 Vellore Institute of Technology, Dept. of Micro and Nanoelectronics（India）
- **出處**：2024 IEEE 25th International Conference of Young Professionals in Electron Devices and Materials (EDM), pp. 2630–2633

**1 元件**　Junctionless FinFET，具 back oxide（即含 BOX 的 SOI 型結構；摘要出現 back oxide 一詞可支持此推論，但未逐字寫 SOI）。閘極氧化層與背氧化層材料變因為 SiO₂、HfO₂、Si₃N₄ 及其組合。技術節點、Lg、Hfin/Wfin、n or p、鰭數：摘要未印出，未取得。

**2 方法與 SHE 定義**　`model`　3D 電熱 TCAD 模擬，逐字："3D simulation is performed using Sentaurus TCAD"。觀測量為通道中心（channel center）的 lattice temperature 對 gate oxide 厚度與 back oxide 厚度的相依性，並比較不同氧化層材料組合。求解器＝Sentaurus TCAD（3D）。熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型：摘要完全未述，未取得。

**3 關鍵定量結果**　無 Ion 下降 %、無 Rth、無 ΔT 絕對值、無峰值晶格溫度數字——摘要未印出任何數字，僅趨勢陳述。逐字引用："It is shown, that the lattice temperature mainly monotonically decreased with the increasing gate oxide thickness." 與 "the lattice temperature is monotonically increased with increasing the thickness of the back oxide."，機制解釋逐字為 "explained by a difference in the heat conductivity of the oxide materials" 及 "the increase of the contact area between gate oxide and the gate with increasing the gate oxide thickness"。以上全部屬「僅圖層級（需自讀原圖）」；對應偏壓（VGS / VDS / TA）未取得。

**4 TCAD 校準用途**　不可直接校準，理由：可取得文字零數值（無溫度、無 Rth、無 Ion），且元件為 junctionless（通道全摻雜、無接面），其自熱功率密度分布與使用者的 inversion-mode 標準矽 FinFET 不可直接對應。唯一可轉用的是定性設計規則：BOX 越厚 → 通道晶格溫度越高（垂直熱阻主導）。此規則可拿來 sanity-check 使用者 deck 的 BOX / 埋層厚度掃描方向：若 deck 掃厚 BOX 反而降溫，代表底部 thermode 很可能直接貼在 BOX 下方甚至 BOX 內，使 BOX 熱阻被短路，屬「thermode 貼太近通道、SHE 被邊界抹掉」的典型症狀。

**5 批判**
   1. 無數值可判定，原因：摘要未印出任何 Ion 下降 %、ΔT、Rth 或峰值晶格溫度，僅有「單調上升 / 單調下降」的趨勢敘述，無法與判準帶（電熱 vs 等溫飽和 Ion 下降 bulk 3–12%、SOI 8–17%，交叉檢核比值 0.10–0.20 %/K）做任何比對。
   2. 熱邊界條件與 thermode 設定完全未在可取得文字中揭露。對一篇結論明確建立在「熱產生率與熱散逸率之比」上的論文，這是致命的可重現性缺口：同一組 BOX 厚度掃描，底部 thermode 的 SurfaceResistance 取 0（理想熱沉）或取有限值，趨勢斜率可以差數倍，甚至改變「單調」與否的判定。
   3. 糾纏因子明顯且作者自承：gate oxide 厚度同時改變（a）閘極電容與汲極電流因而改變 Joule 產熱率、（b）氧化層本身的熱阻、（c）作者自陳的 gate/gate-oxide 接觸面積。摘要逐字寫 "the Joule heat generation rate depends on drain current, which also depends on oxide materials"，等於自承電性與熱性未解耦，因此「晶格溫度隨 tox 增加而下降」不能單獨歸因於熱傳路徑。
   4. 分類正確（非 ta_sweep）：自變數是幾何厚度與氧化層材料，不是環境溫度。但元件屬 junctionless，是判準帶明示要排除的特例族群之一，任何結論外推到 inversion-mode 矽 FinFET 都需另行驗證。
   5. 無誤差棒、無網格收斂性說明、無重複性資訊；4 頁會議短文，方法細節密度先天偏低，且發表於以 young professionals 為對象的區域性會議，同儕審查強度低於 TED / IEDM 級別。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可支撐「BOX 厚度增加會加劇自熱、閘極/背氧化層材料熱導率會影響通道晶格溫度」這類定性敘述，但全篇無任何可引用的數字，且元件為 junctionless 特例、會議層級偏低，不宜作為主要證據。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edm61683.2024.10615156?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/edm61683.2024.10615156

**8 與原表差異**　與原表一致。原表記載的「SOI junctionless FinFET（Sentaurus 3D TCAD）、晶格溫度隨閘極氧化層厚度增加大致單調下降、隨背氧化層厚度增加單調上升、歸因於材料熱導率差異與接觸面積變化、數值為圖級、全文未讀」全部由摘要逐字證實。補充三點：(1) Crossref 確認會議全名為 2024 IEEE 25th International Conference of Young Professionals in Electron Devices and Materials (EDM), pp. 2630–2633；(2) Semantic Scholar 的 venue 欄誤植為 "Educational Data Mining"，此為 S2 metadata 錯誤（DOI 前綴 edm 被錯誤匹配），非原表錯誤，抄寫時勿採信；(3) 摘要明示氧化層材料變因為 SiO₂ / HfO₂ / Si₃N₄ 及其組合，此為原表未載。Unpaywall 與 OpenAlex 均回報 closed、無 OA 版本。

---

## 五06 — Theoretical Study of Self-Heating-Induced Thermal Stress Effects on Quantum Transport in p-Type Ultrathin Body-FinFET by Multiphysics Simulation

- **DOI／識別**：`10.1109/TED.2023.3280865`　**來源**：IEEE　**年**：2023
- **作者／單位**：Huali Duan（第一作者），Zhejiang University/University of Illinois Urbana-Champaign Institute (ZJU-UIUC Institute), International Campus, Zhejiang University, Haining, China；兼 College of Information Science and Electronic Engineering, Key Laboratory of Advanced Micro/Nano Electronic Devices and Smart Systems of Zhejiang Province, Zhejiang University, Hangzhou, China。資深作者 Er-Ping Li、Wenchao Chen 同單位。
- **出處**：IEEE Transactions on Electron Devices, vol. 70, no. 8, pp. 4001–4007

**1 元件**　p-type ultrathin body (UTB) FinFET；自變數包含不同 crystal orientation configurations 與不同 channel lengths。技術節點、Lg 具體數值、Hfin / Wfin、鰭數：摘要未印出，未取得。無 GAA / nanosheet / CFET 成分。

**2 方法與 SHE 定義**　`model`　自洽耦合多物理場模擬（非量測、非 ET-vs-ISO 對比實驗）。逐字："The quantum transport equation with consideration of thermal stress effects by the strain term in k·p Hamiltonian, heat conduction equation, and equilibrium equations of solid mechanics are solved self-consistently." 即 k·p Hamiltonian（含應變項）量子輸運 ＋ 熱傳導方程 ＋ 固體力學平衡方程三者自洽求解。輸出量為 hole effective mass、hole average velocity、current density。商用求解器名稱（Sentaurus / COMSOL / 自研）、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic / BTE / 聲子模型：摘要完全未述，未取得。

**3 關鍵定量結果**　無任何數字。逐字引用："The simulation results show that thermal stress can decrease or increase the ON-state current depending on the crystal orientation configuration." 以及 "thermal stress can change the material properties such as the hole effective mass of the top subband, thus leading to the variations of device characteristics."。ON-state current 的變化百分比、ΔT、峰值晶格溫度、Rth 全部未在可取得文字中印出 → 僅圖層級（需自讀原圖）。對應偏壓（VGS / VDS / TA）未取得。

**4 TCAD 校準用途**　不可直接校準（無任何數值），但方法學上對使用者 deck 有一項重要警示：本文顯示 SHE 對電流的影響不只是「遷移率隨晶格溫度上升而下降」這一條路徑，還包含自熱誘發的 thermal stress 經由 k·p 改變 top subband 的 hole effective mass，且該效應在不同晶向配置下可正可負。實務意涵有二：(1) 若使用者做 p-type FinFET 且 deck 僅用 drift-diffusion＋溫度相依遷移率，等於完全略去此項；(2) 反向而言，若使用者量到 p 型 Ion 下降超出判準帶（例如遠高於 8.91% 的 14nm p 型錨點），晶向與熱應力可能是糾纏因子，不應立刻歸因於 thermode 過絕熱。本篇適合寫進論文的 limitation / discussion 段落，不可用於數值校準。

**5 批判**
   1. 無數值可判定，原因：摘要僅陳述 ON-state current「可增可減」，未印出任何百分比、ΔT 或峰值晶格溫度，無法對照判準帶的 7–11%（bulk 3–12% / SOI 8–17%）或 0.10–0.20 %/K 交叉檢核比值。
   2. 本篇是判準帶明示的「糾纏因子」典型案例：thermal stress 效應與純熱效應（遷移率退化）在同一模擬中疊加，且作者刻意讓晶向成為自變數。因此本文的 ΔIon 即使取得全文後有數字，也不可當作「純 SHE 造成的飽和 Ion 下降」拿去校準 thermode——它是熱＋應力的合成量。
   3. 熱邊界條件完全未揭露，而 thermal stress 的量級直接正比於溫升場的空間分布。缺了 thermode 位置與 SurfaceResistance，本文的應力量級無法被外部檢驗；搜尋到同組後續在 J. Appl. Phys. 的相關工作標題即強調熱環境相依性（僅見標題與檢索摘要，未讀全文，此點僅作旁證不作結論）。
   4. 元件為 p-type ultrathin body FinFET 單一幾何族。使用者若做 n-type 或 bulk FinFET，電子谷（Δ valley）與電洞子帶對應變的響應方向與量級本就不同，本文結論不可跨載子型別外推。
   5. 未取得誤差棒、網格收斂性、或跨晶向配置的統計重複性資訊；「theoretical study」性質，全篇無實驗驗證的跡象出現在可取得文字中。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：「自熱誘發的熱應力可依晶向配置增加或減少 ON-state current，並經由改變 top subband 的 hole effective mass 產生作用」有摘要逐字支撐。任何數字都必須先取得全文（IEEE TED, vol. 70, no. 8, pp. 4001–4007）才可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2023.3280865?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2023.3280865

**8 與原表差異**　與原表一致。原表「p-type ultrathin-body silicon FinFET；multiple crystal orientations；數值未印在摘要；未取得全文」全部證實。補充：完整標題（原表被刪節號截斷）、卷期頁碼 IEEE Transactions on Electron Devices, vol. 70, no. 8, pp. 4001–4007 (2023)、第一作者 Huali Duan 與單位（浙江大學 ZJU-UIUC Institute / 資訊與電子工程學院）。另補充原表未載的方法學核心：三場（量子輸運 k·p＋熱傳導＋固體力學）自洽耦合，以及結論機制為 top subband hole effective mass 的改變。OpenAlex 與 Semantic Scholar 均回報 closed、無 OA 版本。

---

## 五07 — Localized thermal effects in Gate-all-around devices

- **DOI／識別**：`10.1109/IRPS48203.2023.10117903`　**來源**：IEEE　**年**：2023
- **作者／單位**：Colin Landon（第一作者），Intel Corporation, Logic Technology Development, Hillsboro, USA；合著者含 Lei Jiang、Daniel Pantuso（同 LTD）與 Inanc Meric、K. Komeyli、J. Hicks、Daniel Schroeder（Intel Corporate Quality Network, Hillsboro）
- **出處**：2023 IEEE International Reliability Physics Symposium (IRPS)

**1 元件**　Gate-all-around (GAA) 電晶體，與 FinFET 對照；比較口徑明確為 cell 級（"GAA cell thermal resistance to Fin-FET cells"），非單元件級。技術節點、Lg、nanosheet 幾何（TNS / WNS / 堆疊數）、n or p、鰭數或指數：摘要未印出，未取得。原表所寫「RibbonFET-class」屬合理推論（Intel LTD 的 GAA 即 RibbonFET），但可取得文字僅寫 "Gate-all-around (GAA) devices"。

**2 方法與 SHE 定義**　`Rth-extraction`　逐字："We describe the methodology used for localized thermal analysis and data collection of temperature rise on the transistor scale and compare GAA cell thermal resistance to Fin-FET cells." 即：電晶體尺度的局部熱分析方法學 ＋ 溫升資料收集 ＋ GAA/FinFET cell 熱阻對比，故歸為 Rth-extraction。但具體萃取技術（gate resistance thermometry、pulsed I-V、AC conductance、熱反射顯微等）、量測偏壓、模擬工具、熱邊界條件、thermode 位置與 SurfaceResistance：摘要完全未述，未取得。方法學本身是本文自陳的主要貢獻，卻不在可取得文字內。

**3 關鍵定量結果**　無任何數字。可取得文字僅有定性陳述，逐字："Gate-all-around (GAA) devices continue the technology trends of increased localized thermal confinement and higher performance." 與 "We demonstrate that the implications of GAA on device temperature are not a constraint to realizing the full technology benefits with proper thermal management."。溫升絕對值、GAA vs FinFET 熱阻比值、Ion 下降 %、峰值晶格溫度、對應偏壓：全部屬「僅圖層級（需自讀原圖）」。另已額外檢索一篇引用本文的 GAA nanosheet 可靠度回顧（ouci 索引頁），確認其內文未轉引本文任何數值，僅在參考文獻中列出——即二手來源亦無數字可用。

**4 TCAD 校準用途**　不可直接校準，理由：可取得文字零數值。但有兩個非數值用途：(1) 這是少數來自量產廠（Intel）的 transistor-scale 溫升量測方法學文獻，可在論文中支撐「GAA 相較 FinFET 熱侷限加劇」的研究動機敘述，權威性高於純學術模擬；(2) 其比較口徑為 cell thermal resistance 而非 single-device Rth，正好提醒使用者：引用文獻 Rth 前必須先確認參考邊界在哪（device / cell / cell boundary / 封裝），否則會把 single-fin 的 1–4 MK/W 與 cell 級或 RF 多鰭多指的 kK/W 量級錯誤混用，導致 thermode SurfaceResistance 設定差好幾個數量級。

**5 批判**
   1. 無數值可判定，原因：摘要與所有可索引的二手來源（含一篇引用本文的 GAA 可靠度回顧）皆未印出任何溫升或熱阻數字，無法判定是否落在 single-fin 1–4 MK/W 或多鰭多指 RF 結構約 34 kK/W 的判準帶內。
   2. 結論句 "not a constraint to realizing the full technology benefits with proper thermal management" 帶有明顯的廠商立場：Intel 正在推 RibbonFET 量產，本文實質是一篇宣示自家 GAA 熱問題可控的文章。此類結論不宜當作中立的第三方文獻證據，引用時須標明利益相關。
   3. 方法學是本文自陳的主要貢獻，卻完全不在可取得文字中，等於本文對外只剩一句定性結論。對 TCAD 校準而言價值幾近於零，除非取得全文。
   4. 口徑風險：本文比較的是 cell thermal resistance，不是 single-device Rth。若日後取得全文並把其數字直接對回 single-fin thermode，會系統性低估元件級溫升——cell 級 Rth 把 cell 內部的多鰭並聯與 cell 邊界熱沉都算了進去。
   5. 無誤差棒、無樣本數、無量測不確定度資訊；商業機密性質使得外部完全無法重製。
   6. 原表寫的「RibbonFET-class」是推論性描述，摘要原文只寫 "Gate-all-around (GAA) devices"，建議抄寫時退回原文用語並另行加註推論來源。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可用來支撐「GAA 架構的局部熱侷限較 FinFET 加劇、業界已在 transistor scale 建立溫升量測方法」的動機句，並須註明來源為 Intel 且結論具廠商立場。全篇無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps48203.2023.10117903?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps48203.2023.10117903
   - https://ouci.dntb.gov.ua/en/works/4wBKQeJ7/

**8 與原表差異**　與原表一致。原表「Intel gate-all-around 元件、thermal resistance、transistor scale 溫升資料收集、數值為圖級不在摘要、未取得全文」皆逐字證實。補充：第一作者 C. Landon，Intel Corporation Logic Technology Development, Hillsboro；會議全名 2023 IEEE International Reliability Physics Symposium (IRPS)。註記（非 CORRECTION，原表已用「-class」保留語氣）：摘要原文用語為 "Gate-all-around (GAA) devices"，未出現 RibbonFET；且比較對象明確是 "GAA cell thermal resistance" vs "Fin-FET cells"（cell 級口徑），建議原表補上此口徑註記以免日後誤用為單元件 Rth。OpenAlex 回報 closed、無 OA 版本。

---

## 五08 — Self-Heating in iN8–iN2 CMOS Logic Cells: Thermal Impact of Architecture (FinFET, Nanosheet, Forksheet and CFET) and Scaling Boosters

- **DOI／識別**：`10.1109/VLSITechnologyandCir46769.2022.9830228`　**來源**：IEEE　**年**：2022
- **作者／單位**：B. Vermeersch（Bjorn Vermeersch，第一作者），imec, Leuven, Belgium；合著者 E. Bury、Y. Xiang、P. Schuddinck、G. Hellings、J. Ryckaert 同屬 imec，K. K. Bhuwalka 另掛 Huawei Technologies R&D Belgium N.V., Leuven
- **出處**：2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)

**1 元件**　imec 想定節點 iN8–iN2 的標準 CMOS 邏輯 cell，四種架構：finFET (iN8–iN5)、nanosheet (iN5/iN3)、forksheet (iN3)、monolithic CFET (iN2)。另含 scaling boosters 變因（摘要明示 buried power rails）。Lg、Hfin / Wfin、TNS / WNS、堆疊數、鰭數或指數：摘要未印出，未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　逐字："using an in-house Monte Carlo framework with first-principles heat carrier properties"，且 "Experimental validations highlight the impact of non-diffusive thermal transport inside logic cells."。即 imec 自研的聲子 Monte Carlo 求解器（熱載子性質取自第一原理），明確處理 non-diffusive（準彈道）熱輸運，並有實驗驗證——不是 Sentaurus 的 Fourier 電熱求解器。熱參考面明確為 cell boundary（超額通道升溫定義為 relative to the cell boundary），此即等效的 thermode 參考位置。SurfaceResistance 具體設定值、網格與統計取樣參數：未取得。

**3 關鍵定量結果**　有原文印出數字（摘要層級）。逐字："Excess channel heating (relative to the cell boundary) of 0.8–1.6 and 10–19 degrees is observed for baseline (0.7VDD at 2GHz clock) and turbo (1.4VDD at 6GHz clock) operation scenarios respectively." → 超額通道升溫 ΔT = 0.8–1.6 K @ baseline（0.7 VDD、2 GHz clock）；ΔT = 10–19 K @ turbo（1.4 VDD、6 GHz clock）。另逐字："Thermal resistance oscillates node by node but grows near linearly with power density." 與 "Channel fragmentation (finFET to nanosheet) raises temperatures, while buried power rails help reduce self-heating."。Rth 絕對值（K/W）、Ion 下降 %、峰值晶格溫度：僅圖層級（需自讀原圖）。

**4 TCAD 校準用途**　本批對使用者最有校準價值的一篇，但用法必須正確。(1) ΔT 下界的合理性檢查：cell 級、含時脈開關稀釋的操作情境下，0.7 VDD 的超額通道升溫僅 0.8–1.6 K；使用者的 DC 飽和區偏壓（連續導通、無 duty cycle）ΔT 理應顯著高於此值。若使用者 deck 在 VDD ≈ 0.7 V 的 DC 條件下算出 ΔT 只有 1 K 等級，幾乎可斷定 thermode 貼太近通道、SHE 被邊界條件抹掉（對應判準帶的「ΔIon% < 1%」異常）。(2) 參考面口徑：本文明確定義為 relative to the cell boundary；使用者 deck 若把 thermode 放在基板底部或 BEOL 頂端，量到的是相對環境的總 ΔT，數值不可與本文直接相減或對齊。(3) 幾何/架構趨勢可對齊：finFET→nanosheet 因 channel fragmentation 升溫上升、buried power rails 降低自熱，可用來 sanity-check deck 的幾何掃描方向是否正確。(4) 物理模型提醒：本文的實驗驗證強調 non-diffusive 熱輸運的影響，意味著純 Fourier 熱傳導在 sub-10 nm 尺度會低估局部升溫；這正是實務上以 thermode SurfaceResistance 或壓低有效 κ 做唯象補償的依據。

**5 批判**
   1. 數字落在判準帶外，但屬「口徑不同」而非數據有誤：baseline 的 0.8–1.6 K 若套用 0.10–0.20 %/K 交叉檢核比值，只對應 0.08–0.32% 的 ΔIon，遠低於判準帶的 7–11%。原因有三：(a) 這是相對 cell boundary 的「超額」升溫，不是相對環境的總 ΔT；(b) 這是 2 GHz 時脈下的 cell 級操作情境，含開關 duty cycle 稀釋，不是 DC 飽和偏壓；(c) 判準帶針對的是單一元件 DC 電熱 vs 等溫對比。因此本文數字不可直接代入判準帶；反倒是 turbo 的 10–19 K 才接近 DC 級熱應力的量級。
   2. 參考面選在 cell boundary 本身就是一個隱含的「過導熱」邊界：把 cell 邊界視為固定溫度，等於把 cell 以外的 BEOL、封裝、散熱器熱阻全部排除在這個數字之外。真實晶片上通道相對環境的絕對溫升會遠高於 0.8–1.6 K。若有人拿這個數字當「FinFET 自熱其實很小」的證據，會嚴重誤判。
   3. 跨架構比較含多重糾纏因子：iN8→iN2 同時改變了架構（finFET / nanosheet / forksheet / CFET）、節點尺寸、功率密度、以及是否採用 buried power rails。摘要自陳 "Thermal resistance oscillates node by node"，這個「逐節點振盪」正是多變因同時變動的症狀，無法把溫升歸因到單一架構因素。
   4. 使用 in-house Monte Carlo 框架，非公開工具，外部無法重製；摘要僅寫 "Experimental validations" 而未給量測對象、樣本數、誤差棒或吻合度指標，驗證強度無法評估。
   5. iN8–iN2 是 imec 的想定（projected）節點路線圖，iN3 的 forksheet 與 iN2 的 monolithic CFET 並非量產元件，其幾何與材料假設具預測性質，外推到使用者的真實矽 FinFET 需明確保留。
   6. 分類正確：非 ta_sweep（環境溫度非自變數，掃的是架構與功率密度 / 操作情境），亦非單純 ET-vs-ISO 對比。

**6 可引用性**　A（可直接引用數字）— 可直接引用數字：excess channel heating 0.8–1.6 K（baseline, 0.7 VDD @ 2 GHz clock）與 10–19 K（turbo, 1.4 VDD @ 6 GHz clock）在摘要中逐字印出，偏壓與時脈條件明確標示，屬可查證的一手數字。唯引用時務必連同「relative to the cell boundary」的參考面與操作情境一併寫出，否則會被誤讀為元件絕對溫升。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/vlsitechnologyandcir46769.2022.9830228?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/vlsitechnologyandcir46769.2022.9830228

**8 與原表差異**　與原表一致。原表已自摘要查證的 excess channel heating 0.8–1.6 K（baseline）與 10–19 K（turbo）、以及 baseline = 0.7VDD @ 2 GHz clock、turbo = 1.4VDD @ 6 GHz clock，本次逐字複核完全吻合，無 CONFLICT。補充原表未載的四項：(1) 完整標題結尾為 "…and Scaling Boosters"；(2) 第一作者 B. Vermeersch, imec Leuven（合著者 K. K. Bhuwalka 兼 Huawei R&D Belgium）；(3) 方法為 in-house 聲子 Monte Carlo（first-principles heat carrier properties）＋實驗驗證＋明確處理 non-diffusive 熱輸運，此為判斷其數字可否套用到 Fourier-based Sentaurus deck 的關鍵；(4) 兩項額外結論——"Thermal resistance oscillates node by node but grows near linearly with power density" 與 buried power rails 可降低自熱。Unpaywall 與 OpenAlex 均回報 is_oa = false / closed、無 OA 版本。

---

## 五09 — Self-Heating and Thermal Network Model for Complementary FET

- **DOI／識別**：`10.1109/TED.2021.3130010`　**來源**：IEEE　**年**：2022（IEEE 線上首發 2021 年 12 月，正式收錄於 vol. 69, no. 1, Jan. 2022）
- **作者／單位**：Songhan Zhao（第一作者），Institute of Microelectronics, Peking University, Beijing, China；合著者 Linlin Cai、Wangyong Chen、Yandong He、Gang Du 同單位
- **出處**：IEEE Transactions on Electron Devices, vol. 69, no. 1, pp. 11–16

**1 元件**　Complementary FET (CFET)，垂直堆疊的互補 n/p 元件，並與 standard CMOS 對照；所提熱網路模型可擴展至 array level。技術節點、Lg、nanosheet 幾何（TNS / WNS / 堆疊數）、鰭數或指數：摘要未印出，未取得。

**2 方法與 SHE 定義**　`model`　SHE 模擬 ＋ 提出 cross-coupled thermal network model（集總熱阻/熱容網路）。逐字："we investigate the self-heating effect (SHE) of the Complementary FET (CFET) device and propose a cross-coupled thermal network model"；串擾評估逐字為 "the intra- and inter-device crosstalk of CFET is evaluated qualitatively through the defined crosstalk coefficient"。分析變因含 load capacitance 與 operating frequency；模型輸出的 lattice temperature 再驅動 BTI 壽命預測。底層 TCAD 求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic / BTE：摘要完全未述，未取得。

**3 關鍵定量結果**　有兩個原文印出的數字，但都不是 Ion / Rth / ΔT。逐字："The results indicate that CFETs have more severe intra-device thermal crosstalk, almost twice that of CMOS."（intra-device 熱串擾約為 CMOS 的兩倍）與 "the bias temperature instability (BTI) lifetime of CFET degrades by 84% compared with standard CMOS."（BTI 壽命較標準 CMOS 退化 84%）。另有定性結論逐字："the vertical structure makes the heat dissipation path of CFET devices significantly different in the two transition states (inputs \"1\" and \"0\")"。Ion 下降 %、Rth 絕對值、ΔT、峰值晶格溫度、對應偏壓（VGS / VDS / TA）：全部僅圖層級（需自讀原圖）。

**4 TCAD 校準用途**　不可直接校準 thermode，理由：無 Rth、無 ΔT、無 Ion 數字，且 CFET 的垂直堆疊熱路徑拓樸與使用者的平面基板 FinFET 根本不同（上層元件的熱必須先穿過下層元件）。可轉用的有三點：(1) 熱網路（集總 RC）作為 TCAD 之外的快速降階模型範式——若使用者要把 TCAD 萃出的單元件 Rth 外推到 cell / array 級，本文是方法學參考；(2)「intra-device crosstalk 幾乎是 CMOS 兩倍」提醒使用者，多鰭 / 多指結構中相鄰通道的熱耦合不可忽略，若 deck 只模一根 fin 再乘以鰭數，會系統性低估溫升；(3) 本文明示 SHE 溫升與 load capacitance、operating frequency 相關，即 DC 飽和區模擬給出的是熱應力上界，不是電路實際工作溫度——這是使用者在論述其 DC 結果的適用範圍時該引用的界線。

**5 批判**
   1. 就 Ion 判準帶而言無數值可判定，原因：摘要印出的兩個數字（crosstalk 約 2 倍、BTI 壽命退化 84%）都不是飽和 Ion 下降百分比，也沒有 ΔT 或 Rth，無法與 bulk 3–12% / SOI 8–17% 或 0.10–0.20 %/K 判準帶做任何對照。
   2. crosstalk coefficient 是作者自定義的量，且摘要自陳評估方式為 "evaluated qualitatively"。一個自定義、自承定性的係數，其「幾乎兩倍」的說法在不知道定義式的情況下不可被引用為定量證據，只能當方向性描述。
   3. 84% 的 BTI 壽命退化是多層外推的末端結果：SHE 模擬 → 熱網路降階模型 → lattice temperature → BTI 壽命模型。每一層都有自己的參數與不確定度，摘要未提供任何誤差棒或敏感度分析，該數字的實際不確定度可能遠大於其兩位有效數字所暗示的精度。
   4. 熱邊界條件未揭露，而 CFET 的核心爭點正是上層元件散熱路徑受阻。缺了 thermode 位置與 SurfaceResistance，「CFET 比 CMOS 熱」這個結論的量級無法被外部檢驗——它有相當可能主要由邊界設定（底部熱沉距離、上方是否絕熱）決定，而非架構本身。
   5. 元件為 CFET，與使用者的矽 FinFET 在熱路徑拓樸上根本不同，任何數值皆不可外推，只能作為架構趨勢的背景文獻。
   6. 分類正確：非 ta_sweep；自變數為 load capacitance 與 operating frequency（電路操作情境），環境溫度未作為掃描變數。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論與帶保留的比值：「CFET 的 intra-device 熱串擾約為 CMOS 的兩倍」與「CFET 的 BTI 壽命較標準 CMOS 退化 84%」均有摘要逐字支撐，但前者依賴作者自定義且自承定性的 crosstalk coefficient，後者是多層模型外推的末端結果。引用時必須註明為模擬結果並說明模型鏈，不可當作量測值。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2021.3130010?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2021.3130010

**8 與原表差異**　與原表一致。原表「CFET 垂直堆疊互補 n/p 元件、array 級、數值為圖級、熱網路模型的 lattice T 驅動壽命預測、未取得全文」皆證實。補充原表未載的兩個摘要層級數字（屬新增，非衝突）：intra-device thermal crosstalk 約為 CMOS 的兩倍、BTI lifetime 較標準 CMOS 退化 84%；另補充 CFET 在輸入 "1" / "0" 兩種轉態下散熱路徑顯著不同的結論。年份說明：OpenAlex 顯示 publication_year = 2021（線上首發年），Semantic Scholar 與 IEEE 正式引用為 vol. 69, no. 1, pp. 11–16, Jan. 2022，原表填 2022 正確，勿依 OpenAlex 改動。OpenAlex 回報 closed、無 OA 版本。

---

## 五10 — Thermal Conductivity Model to Analyze the Thermal Implications in Nanowire FETs

- **DOI／識別**：`10.1109/TED.2022.3208848`　**來源**：IEEE　**年**：2022
- **作者／單位**：Nitish Kumar（第一作者），Centre for Applied Research in Electronics, Indian Institute of Technology Delhi, New Delhi, India；合著者 Pragyey Kumar Kaushik、Sushil Kumar、Ankur Gupta、Pushpapraj Singh 同單位
- **出處**：IEEE Transactions on Electron Devices, vol. 69, no. 11, pp. 6388–6393（2022 年 11 月號）

**1 元件**　應用示範元件為 SOI 基礎的 junctionless nanowire (JL-NW) FET，採 sub-5-nm technology node 的物理參數；κ 模型本身針對 SOI 矽薄膜（相依於 temperature、thickness、doping concentration）。Lg、奈米線直徑或截面尺寸、堆疊數、n or p、指數：摘要未印出，未取得。

**2 方法與 SHE 定義**　`model`　提出並驗證一個熱導率 κ 模型，非電性量測、非 ET-vs-ISO 對比。逐字："a thermal conductivity (κ) model is proposed (i.e., dependent on the temperature, thickness, and doping concentration) for investigating the thermal behavior of silicon-on-insulator (SOI)-based devices."；並自陳 "The proposed model is also easier to implement in the TCAD simulator than the existing model, which is currently being used in the Sentaurus TCAD electrothermal module"。驗證方式為與 reported experimental data 及既有複雜解析模型比對。求解器脈絡明確指向 Sentaurus TCAD electrothermal module（作為對照的現行模型所在）。熱邊界條件、thermode 位置與 SurfaceResistance、有無 BTE / 聲子模型：摘要未述，未取得。

**3 關鍵定量結果**　無任何數字。逐字："The thermal conductivity (κ) predictions are analyzed using the proposed model, which agrees with the reported experimental data and existing complex analytical models." 與 "It is observed that the thermal behavior depends on the temperature, thickness, and doping concentrations of the SOI devices."。κ 的具體數值（W/m·K）、擬合誤差 %、ΔT、Rth、Ion 下降 %、峰值晶格溫度：全部僅圖層級（需自讀原圖），對應偏壓（VGS / VDS / TA）未取得。

**4 TCAD 校準用途**　本篇的價值不在數值而在 deck 的物理模型層，且直接對應使用者的 Sentaurus 工作流。要點：在 sub-10 nm 尺度做電熱模擬時，矽的熱導率必須同時是 thickness-dependent（薄膜與奈米線的聲子邊界散射會把 κ 從 bulk 的量級大幅壓低）與 doping-dependent（雜質散射），本文正是提供這樣一個可寫進 Sentaurus 的 κ(T, t, N) 模型，且作者自陳比 Sentaurus electrothermal module 現行採用的模型更易實作。實務意涵：若使用者 deck 沿用預設的 bulk 或過度簡化的 κ，會系統性低估 ΔT，進而低估 Ion 下降——這與「thermode 貼太近通道」並列為「ΔIon% < 1%、SHE 被抹掉」的兩大成因。取得全文後應優先抄出 κ 模型方程式與係數，這是本篇對使用者 deck 最實質的貢獻；但其在 JL-NW 上的示範數值不可直接套用。

**5 批判**
   1. 無數值可判定，原因：摘要未印出任何 κ 值、ΔT、Rth 或 Ion 下降百分比，全部是「與實驗資料及既有模型吻合」的定性宣稱，無法對照判準帶。
   2. "agrees with the reported experimental data" 沒有給任何量化吻合度（RMSE、最大偏差 %、R²），也未指名比對的是哪一組實驗資料。對一篇以模型精度為賣點的論文，這是核心證據缺口——「吻合」在缺乏量化指標時是不可檢驗的宣稱。
   3. 作者主打的優勢之一是「比既有模型不複雜、更容易在 TCAD 中實作」，這是工程便利性論證而非物理精度論證，兩者不應混為一談。更簡化的模型在極端薄厚度或高摻雜區間可能反而偏差更大，而摘要未見任何適用範圍（validity range）界定。
   4. 應用示範元件是 junctionless nanowire FET（判準帶明示要排除的特例族群），且採 sub-5-nm 想定節點參數，非量產矽 FinFET。κ 模型本身（SOI 矽薄膜）具可外推性，但其在 JL-NW 上的示範結果不可外推到使用者的元件。
   5. 分類陷阱提醒：本文的溫度相依性是 κ(T) 材料模型的參數相依，不是改變環境溫度的 ta_sweep，也不是 ET-vs-ISO 對比實驗，切勿因摘要出現 temperature 一詞而誤分類。
   6. 無誤差棒、無網格收斂性、無參數敏感度分析的可見證據。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：「SOI / 奈米線尺度元件的矽熱導率須同時考慮溫度、厚度與摻雜濃度相依性，且存在比 Sentaurus electrothermal module 現行模型更易實作的替代式」有摘要逐字支撐。若要在 deck 中真正採用其 κ 模型，必須取得全文（IEEE TED, vol. 69, no. 11, pp. 6388–6393）抄出方程式與係數，否則無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2022.3208848?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2022.3208848
   - https://api.crossref.org/works/10.1109/ted.2022.3208848

**8 與原表差異**　與原表一致。原表「SOI-based junctionless nanowire (JL-NW) FET、sub-5-nm 技術節點、數值不在摘要、無法取得全文」皆證實。補充：完整標題結尾為 "…in Nanowire FETs"（原表被刪節號截斷於 "Nano…"）、卷期頁碼 IEEE TED, vol. 69, no. 11, pp. 6388–6393, Nov. 2022（Crossref 與 OpenAlex 雙源一致）、第一作者 Nitish Kumar 與單位（IIT Delhi, Centre for Applied Research in Electronics）。另補充原表未載的關鍵資訊：所提 κ 模型同時相依於 temperature / thickness / doping concentration，且作者自陳比 Sentaurus TCAD electrothermal module 現行使用的模型更易實作——這是本篇對使用者 TCAD deck 唯一的實質接口。OpenAlex 回報 closed、無 OA 版本。

---

## 五11 — FEOL Self-heating and BEOL Joule-heating Effects of FinFET Technology and Its Implications for Reliability Prediction

- **DOI／識別**：`10.1109/IIRW49815.2020.9312859`　**來源**：IEEE　**年**：2020
- **作者／單位**：Hai Jiang（第一作者），Foundry Business, Samsung Electronics, 1 Samsung-ro, Giheung-gu, Korea；合著者 Tae-Young Jeong、Hyun Chul Sagong、Kihyun Choi、Minjung Jin、Myungsoo Yeo、Hwasung Rhee、Eun-Cheol Lee 全部同屬三星晶圓代工
- **出處**：2020 IEEE International Integrated Reliability Workshop (IIRW)

**1 元件**　先進 FinFET 技術（含技術節點微縮世代比較）。摘要未逐字寫明 bulk 或 SOI——原表記為 bulk，就三星量產 FinFET 而言為合理推論，但可取得文字未證實，抄寫時應加註。幾何變因為 fin 更高更窄（taller and narrower fin）與 CPP（contacted poly pitch）縮短，另含 BEOL 金屬層。具體節點名稱、Lg、Hfin / Wfin 數值、n or p、鰭數或指數：摘要未印出，未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　逐字："we characterize and model the FinFET SHE with technology scaling down as well as BEOL Joule-heating effect (JHE, ΔT_jh)"。即實測特徵化與建模並行，目標量為 ΔT_sh（FEOL 自熱升溫）與 ΔT_jh（BEOL 焦耳升溫），並探討 BEOL 金屬層之間以及 FEOL 與 BEOL 之間的熱耦合，故歸為 Rth-extraction。但具體萃取技術（gate resistance thermometry、DC-vs-pulsed I-V、AC conductance 等）、量測偏壓、模擬工具、熱邊界條件與 thermode 設定：摘要完全未述，未取得——method_type 的歸類是依「characterize ΔT_sh」推得，原文未指名萃取法，此點須保留。

**3 關鍵定量結果**　無任何數字。逐字："Self-heating effect (SHE, ΔT_sh) has been aggravated due to compact layout footprint in advanced FinFET technology, which needs a significant concern for device performance, variability and reliability co-optimization."、"demonstrating the device with taller and narrower fin, shorter CPP presents higher ΔT_sh, and there is a strong thermal coupling between BEOL metal layers, FEOL and BEOL."、"accurate FEOL SHE and BEOL JHE should be considered for HCI, ON-state TDDB and EM reliability lifetime prediction."。ΔT_sh 與 ΔT_jh 的絕對值、Rth、Ion 下降 %、峰值晶格溫度、對應偏壓（VGS / VDS / TA）：全部屬「僅圖層級（需自讀原圖）」。

**4 TCAD 校準用途**　不可直接校準（零數值），但這是本批唯一來自量產晶圓廠、以實測特徵化為基礎的 FinFET SHE 文獻，對使用者 deck 的設計有三項直接指導意義：(1) 幾何趨勢的 sanity-check——deck 若把 fin 拉高、拉窄、CPP 縮短而 ΔT 沒有上升，代表側向散熱路徑（source/drain epi、contact、STI）在 deck 中被過度導熱化，或 thermode 被放在離通道太近的位置；(2) 熱路徑完整性——本文強調 FEOL 與 BEOL 之間存在強熱耦合，提醒使用者若 thermode 只放在基板底部而把 BEOL 簡化掉，會漏掉元件相當比例經 contact / M0 / M1 向上散出的熱：把 BEOL 面設為絕熱會高估 ΔT，設為理想熱沉則會低估，兩者都會讓 ΔIon% 偏離判準帶；(3) 可支撐「SHE 必須進入 HCI / ON-state TDDB / EM 壽命預測」的論述，用於論文動機或 implication 段落。

**5 批判**
   1. 無數值可判定，原因：摘要僅給趨勢（taller / narrower fin、shorter CPP → 較高 ΔT_sh）與定性的強熱耦合陳述，未印出任何 ΔT_sh、ΔT_jh、Rth 或 Ion 下降數字，無法對照 single-fin 1–4 MK/W、多鰭多指 RF 約 34 kK/W，或 0.10–0.20 %/K 的判準帶。
   2. 來源權威性是本篇最大優點也是最大限制：三星量產技術的實測資料，趨勢可信度高；但量測方法、節點名稱、樣本數、誤差棒全部因商業機密未揭露，外部完全無法重製或驗證量級。這類論文只能用來定方向，不能用來定數值。
   3. 三個幾何變因（fin 更高、fin 更窄、CPP 更短）在摘要中被綁在同一句敘述裡，而它們在真實節點微縮中本來就同時發生。因此無法從本文分離出各自對 ΔT_sh 的貢獻——對想單獨掃 Hfin 或單獨掃 CPP 的使用者而言，這是無法解耦的糾纏因子。
   4. 本文核心貢獻之一是 FEOL/BEOL 熱耦合，這反過來意味著任何只模到 FEOL 就結案的 TCAD deck 都缺了一整段熱路徑。既是對使用者的提醒，也代表本文的數字（若日後取得）不可直接對回 FEOL-only 的 deck 做校準。
   5. 分類正確：非 ta_sweep，環境溫度不是自變數；自變數為版圖幾何（fin 形貌、CPP）與 BEOL 電流。
   6. IIRW 為工作坊短文（非全長期刊論文），方法細節密度先天偏低，且無同儕可檢驗的原始資料。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論，但定性引用價值高：「先進 FinFET 因版圖 footprint 壓縮而自熱加劇」「fin 更高更窄、CPP 更短的元件呈現更高的 ΔT_sh」「BEOL 金屬層之間以及 FEOL 與 BEOL 之間存在強熱耦合，故 HCI、ON-state TDDB 與 EM 壽命預測須同時納入 FEOL SHE 與 BEOL JHE」——全部有摘要逐字支撐，且來源為三星量產技術，適合作為研究動機與 implication 的權威引用。無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iirw49815.2020.9312859?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/iirw49815.2020.9312859

**8 與原表差異**　與原表一致。原表「taller/narrower fin 與 shorter CPP 給出更高 ΔT_sh、SHE 因 compact layout footprint 而加劇、未取得全文」皆逐字證實。補充：第一作者 Hai Jiang，Samsung Electronics Foundry Business（八位作者全部同屬三星），會議全名 2020 IEEE International Integrated Reliability Workshop (IIRW)。並補齊原表被截斷處的完整結論：強熱耦合同時存在於 BEOL metal layers 之間以及 FEOL 與 BEOL 之間，且該耦合須納入 HCI、ON-state TDDB 與 EM 三類可靠度壽命預測。註記（非 CORRECTION）：原表寫「Advanced bulk FinFET」，摘要原文僅寫 "advanced FinFET technology"，未逐字指明 bulk，建議原表加註此為推論。OpenAlex 回報 closed、無 OA 版本。

---

## 五12 — Impact of Geometry, Doping, Temperature, and Boundary Conductivity on Thermal Characteristics of 14-nm Bulk and SOI FinFETs

- **DOI／識別**：`10.1109/TDMR.2020.2964734`　**來源**：IEEE　**年**：2020（March）
- **作者／單位**：Junya Sun（第一作者），School of Communication and Electronic Engineering, East China Normal University (ECNU), 上海；通訊作者 Xiaojin Li（同單位）；共同作者 Yabin Sun、Yanling Shi（同單位）
- **出處**：IEEE Transactions on Device and Materials Reliability (TDMR), vol. 20, no. 1, pp. 119–127, Art. no. 8951282

**1 元件**　14-nm bulk FinFET 與 14-nm SOI FinFET，TCAD 結構以實驗 ID-VG 曲線擬合校準。掃描參數涵蓋 fin width、fin height、source extension (SE) 與 drain extension (DE) 長度、STI 厚度、BOX 厚度、extension 摻雜濃度、gate voltage。Lg、Hfin/Wfin 具體數值未取得；n/p 型別未載明；鰭數未載明（摘要無，全文未取得）。

**2 方法與 SHE 定義**　`Rth-extraction`　TCAD 電熱模擬（摘要僅寫 “through the TCAD simulation”，未指名 Sentaurus / GARAND 或其他求解器）；以實驗 ID-VG 曲線擬合完成校準。分析內容：沿通道的 heat generation 與溫度梯度分佈、最高晶格溫度（maximum lattice temperature）與熱阻對元件幾何與參數的依存性、不同環境溫度下 SHE 對電性的影響、bulk 與 SOI 的關鍵散熱路徑。熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型皆未取得（全文未取得）。標題明列 “Boundary Conductivity” 為自變數之一，顯示有做熱邊界導熱率掃描，但設定與數值未取得。

**3 關鍵定量結果**　未取得數值——摘要完全無印出數字，Ion 下降 %、Rth、ΔT、峰值晶格溫度全部屬全文圖表層級且未取得。可逐字引用的定性結果：“Two peeks of heat generation are observed in source extension (SE) and drain extension (DE), respectively”（原文即拼作 “peeks”）；“The dependence of maximum lattice temperature and thermal resistance on device geometry and parameters including fin width, fin height, length of SE and DE, the thickness of STI and BOX, doping concentration of extension, and gate voltage, are thoroughly analyzed”；“For the former, most of heat vertically diffuses to the substrate, and then to heat sink, whereas in SOI FinFET it firstly dissipates to source, drain, and gate, and then to heat sink.” 標示：以上均為原文摘要逐字，但無任何數值；所有量化結果僅圖層級（需取得全文自讀原圖）。

**4 TCAD 校準用途**　不可直接校準（無任何數值）。但提供三項可立即寫進 deck 的定性錨點：(1) 熱源分佈應在 SE 與 DE 呈雙峰，而非只有 drain 端單峰——可用來檢查 deck 中 Joule heating（J·E）分佈是否合理；(2) thermode 擺放策略應依基板型態分流：bulk 熱主要垂直往 substrate，故 thermode 放基板底面；SOI 熱先往 source/drain/gate，故 thermode 應放在 S/D/gate 接觸面，若 SOI deck 只在基板底面設 thermode 會嚴重高估 ΔT；(3) 標題把 boundary conductivity 列為一階變數，支持把 SurfaceResistance 當敏感度掃描參數而非固定值。無法提供 SurfaceResistance 量級、可比對的 ΔT 或 ΔIon%。

**5 批判**
   1. 數字落在判準帶外或內：無數值可判定，原因：僅取得摘要，Ion 下降 %、Rth、ΔT、峰值晶格溫度全部為全文圖表層級且未取得，無法與 bulk 3–12% / SOI 8–17% 判準帶或 0.10–0.20 %/K 的交叉檢核比值比對。
   2. 分類陷阱警示：本文把兩種性質完全不同的實驗混在同一篇——(a) Rth 與 Tmax 對幾何/摻雜的掃描（真 SHE），(b) “under different ambient temperatures”（ta_sweep，改的是環境溫度而非自熱）。使用者引用時必須拆開，否則會落入把 ta_sweep 誤當 SHE 的常見陷阱。
   3. 方法學過度宣稱：摘要以 “To achieve high authoritative evidences, the calibration is performed by ID-VG curve fitting based on the experimental data” 為可信度背書，但 ID-VG（以線性區/次臨界區為主）校準的是電性參數（Vth、mobility、SCE），對熱模型參數（薄膜矽熱導率、界面熱阻、boundary conductivity）幾乎無約束力。電性校準不等於熱校準，這是 TCAD 自熱論文最常見的推論跳躍。
   4. 外推風險：單一 14-nm 幾何，且鰭數與 n/p 型別未載明，能否外推到 3 nm 或多鰭結構無證據。摘要亦無誤差棒、無重複性或網格收斂性敘述。
   5. 與使用者主題高度相關（14 nm 矽 FinFET、bulk 與 SOI 對照、TCAD 電熱），是本批中主題最貼近的一篇，若能取得全文（TDMR vol.20 no.1 pp.119–127）價值會遠高於其他篇，建議優先透過學校圖書館 IEEE Xplore 取得。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可引用其定性結論（SE/DE 雙熱源峰、bulk 與 SOI 散熱路徑差異、boundary conductivity 為一階變數），任何數值一律不可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/tdmr.2020.2964734?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://pure.ecnu.edu.cn/en/publications/impact-of-geometry-doping-temperature-and-boundary-conductivity-o/

**8 與原表差異**　與原表一致。原表記「14-nm bulk 與 SOI FinFET（實驗 ID-VG 校準之 TCAD）／not accessed（摘要無數值）／not accessed」，本次獨立驗證結果相同：摘要確實無任何數值，全文（IEEE Xplore）不可取得（回傳 HTTP 418）。補充原表未載之完整書目：第一作者 Junya Sun、華東師範大學通信與電子工程學院，通訊作者 Xiaojin Li；TDMR vol. 20, no. 1, pp. 119–127（2020年3月）。

---

## 五13 — Advanced Self-heating Model and Methodology for Layout Proximity Effect in FinFET Technology

- **DOI／識別**：`10.1109/IRPS45951.2020.9128322`　**來源**：IEEE　**年**：2020
- **作者／單位**：Hai Jiang（第一作者），Samsung Electronics, Foundry Business, Giheung-gu, Gyeonggi-do, Korea；全體 13 位作者（含 Hyun Chul Sagong、Taiki Uemura、Hwasung Rhee、Sangwoo Pae、Brandon Lee）均隸屬同一單位
- **出處**：2020 IEEE International Reliability Physics Symposium (IRPS), pp. 1–5

**1 元件**　三星晶圓代工（Samsung Foundry）之先進 FinFET 技術。技術節點名稱、bulk/SOI 型態、Lg、Hfin/Wfin、n/p 型別、鰭數與指數全部未載明（摘要無，全文未取得）。摘要僅以 “more confined layout geometry and lower-thermal-conductivity materials adopted in advanced technology” 定性描述。

**2 方法與 SHE 定義**　`model`　提出以散熱路徑為基礎（heat-dissipation-path based）的 SHE 模型，用 interactive thermal resistance Rth(i,j) 描述熱往鄰近佈局的擴散；再以 Rth-matrix 方法論搭配線性疊加演算法（linear superposition algorithm）計算佈局鄰近效應下的 ΔTsh 分佈。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型皆未取得。無法判斷 Rth(i,j) 是由量測擷取、TCAD 模擬擷取，或兩者混合。

**3 關鍵定量結果**　未取得數值。摘要逐字：“Self-heating effect (SHE, ΔTsh) has become a significant concern for device performance, variability and reliability co-optimization due to more confined layout geometry and lower-thermal-conductivity materials adopted in advanced technology”；“a new heat-dissipation-path based SHE model is proposed to describe the heat spreading to layout proximity by interactive thermal resistance (Rth(i,j))”；“Therefore, ΔTsh profile can be more accurately reckoned with account for thermal interaction effect.” 標示：摘要以 ΔTsh 為核心量但完全未印出任何 Rth、ΔTsh、峰值晶格溫度或 Ion 下降 % 之數值；全部為全文圖表層級且未取得。

**4 TCAD 校準用途**　不可直接校準，理由：全篇未取得任何數值，無 Rth 量級、無 ΔT、無幾何。方法論層級可用：若使用者的 deck 日後要從單鰭/單元件擴展到多鰭多指或鄰近元件陣列，本文的 Rth-matrix + 線性疊加是把單一 thermode 校準結果外推到陣列的正規做法；但前提是熱問題可視為線性（即熱導率的溫度相依性可忽略），而該前提在本批的五18 已被量測否證（Rth 隨溫度變化達 70%），使用時須自行檢驗適用範圍。

**5 批判**
   1. 數字落在判準帶外或內：無數值可判定，原因：僅取得摘要，ΔTsh 與 Rth(i,j) 全為全文圖表層級且未取得，無法與 single-fin Rth 1–4 MK/W 或多鰭多指 RF ~34 kK/W 的判準帶比對。
   2. 核心方法假設有系統性風險：線性疊加要求熱傳導問題線性，但 Si 熱導率隨溫度顯著下降（本批五18 量到 20-fin nFET 的 Rth 從 -40 °C 到 175 °C 上升 70%）。在高 ΔTsh 下用疊加會系統性低估溫度，而摘要未交代模型的適用溫度範圍或誤差上界。
   3. 層次不匹配：本文處理的是 layout proximity / thermal crosstalk（元件之間的熱交互作用），與使用者關心的「單一 FinFET 飽和區 Ion 因自熱下降多少」是不同層次的問題，引用時不可混用，否則會把陣列熱串擾誤讀成單元件自熱強度。
   4. 工業界揭露限制：三星晶圓代工論文慣例不揭露節點、fin 幾何與絕對熱阻，只給正規化曲線與相對趨勢；對想校準絕對 SurfaceResistance 的 TCAD 使用者價值有限。摘要亦無誤差棒、無與量測的驗證誤差百分比。
   5. 與本批五17（VLSI Technology 2018，同為三星晶圓代工）為同一團隊延續工作，作者群高度重疊（Sagong、Shim、Jeong、Park、Pae 同時出現在兩篇）；若同時引用兩篇，應說明其為同一團隊的方法演進而非獨立驗證。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可引用其定性/方法論結論（先進 FinFET 的 SHE 評估須納入佈局鄰近熱交互作用，且可用 interactive Rth 矩陣搭配線性疊加建模），任何數值一律不可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps45951.2020.9128322?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps45951.2020.9128322

**8 與原表差異**　與原表一致。原表記「先進 FinFET 技術（Samsung foundry）／ΔTsh 隨佈局鄰近之分佈（摘要以 ΔTsh 為核心量，無具體數值）／摘要未給；全文未讀」，本次獨立驗證結果相同。補充原表未載：第一作者 Hai Jiang，全體 13 位作者均隸屬 Samsung Electronics, Foundry Business (Giheung-gu, Gyeonggi-do, Korea)；IRPS 2020 pp. 1–5。另註記 Semantic Scholar 與 OpenAlex 兩版摘要用字有極小差異（S2 版為 “heat spreading to layout proximity … to account for SHE layout proximity effect”，OpenAlex 版為 “heat spreading to proximity … to account for layout SHE”），逐字引用建議以 S2 版為準並標明來源。

---

## 五14 — Impact of Self-heating on Performance and Reliability in FinFET and GAAFET Designs

- **DOI／識別**：`10.1109/ISQED.2019.8697786`　**來源**：IEEE　**年**：2019
- **作者／單位**：Vidya A. Chhabria（第一作者），Department of Electrical and Computer Engineering, University of Minnesota, Minneapolis, MN 55455, USA；共同作者 Sachin S. Sapatnekar（同單位）
- **出處**：20th International Symposium on Quality Electronic Design (ISQED 2019), pp. 235–240（頁碼取自 Experts@Minnesota 檢索摘要，未於原 PDF 上逐字驗證）

**1 元件**　三種架構並列。(a) 7 nm bulk FinFET 與 (b) 7 nm SOI FinFET，幾何取自 ASAP7 PDK（Table III 原文印出）：fin width 7 nm、fin height 32 nm、fin pitch 27 nm、gate length 20 nm、gate pitch 55 nm、oxide thickness 1.8 nm、SOI BOX thickness 140 nm、substrate thickness 1 µm、gate to contact 8 nm、contact width/length 標為「18mm」（明顯排版錯誤，依上下文應為 18 nm）。(c) 5 nm lateral GAAFET：NW diameter 6 nm、NW horizontal spacing 14 nm、NW vertical spacing 10.6 nm、gate length 12 nm、gate pitch 33 nm、oxide thickness 1 nm、BOX 140 nm、substrate 1 µm、gate to contact 4 nm。陣列掃描範圍：1–17 fins、2–4 gate terminals（inputs）、1–7 層垂直堆疊 NW。以邏輯閘 PUN/PDN 處理，未分別報 n/p 元件級數據。

**2 方法與 SHE 定義**　`model`　自建 finite difference method (FDM) 穩態三維熱傳導求解器（非 Sentaurus / GARAND），解 GT = P 線性系統，G 為熱導矩陣。熱源分佈用 Joule heating H = J·E，沿通道靠 drain 端出現峰值（profile 取自 Pop 等人）。不含 hydrodynamic 或 BTE 求解；聲子/邊界散射效應以「降低的薄膜熱導率」等效代入——原文：“boundary scattering is exacerbated which has reduced the thermal conductivity of silicon by 10× in a fin and by 25× in a NW”。Table IV 熱導率（原文印出，單位 W/mK）：Si fins 13、Si nanowires 5、Si substrate 148、SiO2 (SOI BOX) 0.8、HfO2 (gate dielectric) 0.27、metal gate 48、Cu interconnect 42.4。熱接地路徑有兩條：“(a) along the fin and then through the metal contacts and interconnects, and (b) downwards through the BOX (if any) and the substrate”。以 N×N×F 三維查找表（LUT）對 series/parallel 電晶體陣列做一次性預特徵化，再以線性疊加 Temperature(j) = Σ Pi·T_ij^(k) 求各電晶體溫度；含 leakage-temperature feedback 迭代。電路級：ASAP7 標準元件庫、頻率 1 GHz、供應電壓 0.7 V、HSPICE 特徵化的 NLDM 延遲模型、activity-factor 加權功率分配。全文未給任何 thermode SurfaceResistance 數值，基板底面等效為理想熱接地。

**3 關鍵定量結果**　多數為原文印出數字。【元件/陣列級，原文印出】Table V（NAND4X1，3 fins/4 inputs，探討供應接點位置）——PUN 2 contacts：GAAFET 18.1 K、SOI FinFET 8.8 K；PUN 3 contacts：GAAFET 13.8 K、SOI 6.5 K；PDN contact adjacent to I1：GAAFET 31.4 K、SOI 21.1 K；PDN contact adjacent to I4：GAAFET 23.3 K、SOI 18.4 K。Fig. 4 溫度分佈對應條件為 “a power dissipation of 0.1µW”（3 fins / 2 gates 串聯）。【電路級平均升溫，原文印出，但摘要與正文不一致】摘要：“On average, logic gates in a circuit heat up by 12K for 7nm SOI FinFET and by 17K for 5nm GAAFET designs.”；正文 Sec. V：“On an average, each gate in the benchmark heats up by 5K for bulk FinFET, 12K for SOI FinFET, and 18K for GAAFET technology.” → GAAFET 值 17 K（摘要）vs 18 K（正文）互相矛盾。【延遲與可靠度，原文印出】“an average delay degradation of 10.3% for 7nm bulk FinFET technology, 12.4% for SOI FinFET technology, and 9.9% for 5nm GAAFET technology is observed due to SH”；“On average, the percentage change EM-induced TTF is 14% for bulk FinFET, 38% for SOI FinFET and 45% for GAAFET.”；b20 benchmark：“the acceleration in aging in bulk FinFETs (28%) due to SH is lower than that for SOI FinFETs (37%)”；“SH in GAAFETs accelerate aging by an average of 62% over 10 years”。【僅圖層級，需自讀原圖】Fig. 5(a) 平均升溫 vs. 鰭數 1–17（縱軸約 10–40 K）、Fig. 5(b) 平均升溫 vs. 垂直堆疊 NW 數 1–7（縱軸約 0–60 K）、Fig. 7 各 benchmark 平均與最高升溫（縱軸 0–45 °C）、Fig. 10 t=0 虛線（純溫度、無老化的延遲差）。【重要缺項】全文完全不報飽和區 Ion 或 Ion 下降 %，亦不報任何熱阻絕對值（K/W）。偏壓條件：VDD = 0.7 V、1 GHz、activity-factor 加權，非單一 VGS/VDS DC 偏壓點；環境溫度未明示。

**4 TCAD 校準用途**　高價值，但可用的是「材料熱導率表」而非 thermode 電阻。(1) 可直接寫進 deck 的薄膜矽熱導率：Si fin 13 W/mK、Si NW 5 W/mK、Si substrate 148 W/mK、SiO2 0.8、HfO2 0.27、metal gate 48、Cu 42.4 W/mK，以及「fin 內 Si 熱導率較 bulk 降 10×」的原則——這是使用者在 Sentaurus 中設定 thin-layer 矽熱導率最直接的文獻依據。(2) 幾何可完整對齊 7 nm ASAP7：Wfin 7 nm、Hfin 32 nm、fin pitch 27 nm、Lg 20 nm、gate pitch 55 nm、EOT 1.8 nm、BOX 140 nm、substrate 1 µm。(3) 可比對的 ΔT：單一 NAND4X1 的 SOI FinFET 升溫 6.5–21.1 K、GAAFET 13.8–31.4 K（依供應接點位置），電路平均 bulk 5 K / SOI 12 K（VDD 0.7 V）。(4) Sanity-check：使用者的 bulk FinFET deck 在 0.7 V 下若單元件 ΔT 遠高於此量級，thermode 可能過絕熱；反之若 bulk 與 SOI 的 ΔT 比值不接近 1:2.4，BOX 熱阻可能設錯。(5) 明確不可用之處：本文不給 Rth 絕對值、不給 SurfaceResistance、不報 Ion 下降 %，故無法用來校準 ΔIon%/ΔT 比值，也無法直接反推 thermode 熱阻量級。

**5 批判**
   1. 數字落在判準帶外：本文完全不報飽和區 Ion 下降 %，無法直接判定。以 ΔT 側面檢核——bulk 5 K、SOI 12 K（VDD 0.7 V、電路平均）套上 0.10–0.20 %/K 的交叉檢核比值，等效 Ion 影響僅約 bulk 0.5–1.0%、SOI 1.2–2.4%，遠低於 bulk 3–12% / SOI 8–17% 判準帶。原因不是 SHE 被邊界條件抹掉，而是量測對象不同：這是「電路中邏輯閘在 activity-factor 加權下的平均升溫」，工作週期遠低於 100%，本質上是時間平均功率，不是單元件 100% duty 的 DC 飽和偏壓峰值溫度。使用者切勿把這組 ΔT 直接拿去驗證元件級 deck，改用 Table V 的 6.5–21.1 K（SOI 單一 NAND4）才是較接近的對照。
   2. 論文內部自相矛盾：摘要寫 GAAFET 平均升溫 “17K”，正文 Sec. V 寫 “18K”。引用時必須指明採用哪一處；且原表記載的「摘要與全文 Fig. 7 一致」無法成立——Fig. 7 是長條圖，只能圖層級讀取，無法逐字核對到 17 K。
   3. 熱邊界偏導熱：Si substrate 熱導率取 148 W/mK 且厚度僅 1 µm，底面等效為理想熱接地；SOI BOX 僅 140 nm。對 bulk FinFET 而言這條垂直路徑幾乎是熱短路，正是 bulk 只有 5 K 的主因。使用者若在 deck 中把基板設得更厚、或在 thermode 加上有限的 SurfaceResistance，ΔT 會顯著高於本文——兩者不可直接比大小，必須先對齊邊界條件。
   4. 常數熱導率 + 純線性疊加：Table IV 的熱導率不隨溫度變化，且全篇以 LUT 疊加求解。在 ΔT 達數十 K 時會系統性低估溫度（對照本批五18 的量測：Rth 從 -40 °C 到 175 °C 上升 70%）。論文做了 leakage-temperature feedback 迭代，卻沒做 k(T) 迭代，這是模型的不對稱處理。
   5. 糾纏因子嚴重：報出的 25%/39% 延遲退化與 38%/45% EM 退化都疊加了 BTI/HCI/EM 老化模型（Table II 全部引用他人模型：Mishra、Yu、Messaris、Lee）與 10 年外推，不是純 SHE 效應。純溫度（無老化）造成的延遲差只能從 Fig. 10 的 t=0 虛線讀取，屬圖層級。全篇無誤差棒、無重複性統計、無網格收斂性驗證。
   6. 可查證的排版錯誤：Table III 中 7 nm FinFET 的 “Contact width/length” 標為 18 mm，依上下文（其餘尺寸皆為 nm 級）顯然應為 18 nm。這類錯誤提醒使用者引用此表數值時需逐項合理性檢查。

**6 可引用性**　A（可直接引用數字）— 已取得完整全文 PDF，Table III/IV/V 與正文的數字均為原文印出（5K/12K/18K、6.5–31.4 K、熱導率表、10.3%/12.4%/9.9%、14%/38%/45%），可直接引用。引用時必須同時註明兩項限制：摘要 17 K 與正文 18 K 的內部矛盾，以及「電路級 activity-factor 加權平均升溫」不等於「元件級 DC 峰值溫度」。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/isqed.2019.8697786?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - http://www.ece.umn.edu/~sachin/conf/isqed19vac.pdf

**8 與原表差異**　CORRECTION 加大量補充。原表記「7nm SOI FinFET +12K、bulk FinFET +5K、5nm GAAFET +17K（摘要與全文 Fig. 7 一致）」——本次取得全文並實讀：bulk +5 K 與 SOI +12 K 與原表一致；但 GAAFET 值在正文 Sec. V 為 “18K for GAAFET technology”，與摘要的 17 K 不一致，原表「摘要與全文 Fig. 7 一致」的判定無法成立（Fig. 7 為長條圖，僅圖層級）。原表 verdict 為 reclassified、註明「電路級 workload（activity factor 加權），非單一 VGS/VDS 偏壓點」——此判斷正確且經全文確認（1 GHz、VDD 0.7 V、ASAP7、activity-factor 加權）。重要補充（原表未載，且對使用者 TCAD deck 價值高於原表所記的電路級數字）：Table III 完整幾何表（7 nm：Wfin 7 nm / Hfin 32 nm / fin pitch 27 nm / Lg 20 nm / BOX 140 nm / substrate 1 µm；5 nm GAAFET：NW 直徑 6 nm / 垂直間距 10.6 nm / Lg 12 nm）、Table IV 完整熱導率表（Si fin 13、Si NW 5、substrate 148、SiO2 0.8、HfO2 0.27、metal gate 48、Cu 42.4 W/mK）、Table V 元件級 ΔT（SOI 6.5–21.1 K、GAAFET 13.8–31.4 K）。另發現原表未提及的原文排版錯誤：Table III 之 “Contact width/length 18mm” 應為 18 nm。

---

## 五15 — Investigation of self-heating effect on stacked nanosheet GAA transistors

- **DOI／識別**：`10.1109/VLSI-TSA.2018.8403821`　**來源**：IEEE　**年**：2018
- **作者／單位**：Linlin Cai（第一作者），Institute of Microelectronics, Peking University, Beijing, China（北京大學微電子學研究院）；共同作者 Wangyong Chen、Gang Du、Jinfeng Kang、Xing Zhang（另掛 National Center for Nanoscience and Technology）、Xiaoyan Liu
- **出處**：2018 International Symposium on VLSI Technology, Systems and Application (VLSI-TSA)

**1 元件**　水平堆疊 gate-all-around (GAA) nanosheet 電晶體（stacked nanosheet GAA / NSHFET），摘要明示模擬含 back-end-of-line (BEOL)。堆疊層數、TNS/WNS、Lg、技術節點、n/p 型別、指數/陣列尺寸全部未載明（OpenAlex 重建摘要無，全文未取得）。註：原表記「三層」——該資訊在本文摘要中並未出現，僅在同組五16（TED 2018）摘要中明確為 “horizontally stacked three-layer”，屬跨文推得，使用時須註明。

**2 方法與 SHE 定義**　`model`　摘要僅稱：評估水平堆疊 GAA nanosheet 電晶體的自熱行為，研究空間溫度分佈（spatial temperature profile）與熱通量分佈（heat flux distribution），並考慮 BEOL；同時給出元件幾何與材料熱導率的影響以作為抑制自熱的設計指引。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型皆未取得。特別聲明：網路搜尋彙整結果曾稱本文使用 COMSOL FEM，但該敘述出自搜尋引擎的二手摘要，非本次實際取得之原文頁面，故不採信、不列為事實。

**3 關鍵定量結果**　未取得數值。可逐字引用者僅 OpenAlex 重建摘要：“The self-heating behavior of horizontally stacked gate-all-around nanosheet transistors is evaluated to investigate the spatial temperature profile and heat flux distribution considering the back-end-of-line.”；“The impacts of device geometry and material thermal conductivity are given to provide guidelines for mitigating self-heating effect in device design.”；“The results indicate that self-heating in nanoscale devices should be attached great importance in achieving robust thermal management and precise reliability prediction.” 無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度，全部屬全文圖表層級且未取得。附加警示：Semantic Scholar 的 abstract 欄為 null，上述摘要由 OpenAlex 的 abstract_inverted_index 重建，字序與原刊可能有極小差異，逐字引用前應以出版者頁面複核。

**4 TCAD 校準用途**　不可直接校準，理由：無任何數值，連基本幾何（層數、TNS、WNS、Lg）都未取得，且元件類別為 GAA nanosheet 而非矽 FinFET。唯一可用的設計原則是「熱模擬邊界必須含 BEOL」——這對使用者的 deck 有直接影響：若模擬區域只到 contact 就設 thermode，會漏掉經金屬層向上散熱的路徑，導致 ΔT 高估；本批五14 的全文（“a significant amount of heat flows through the metal interconnects”）亦獨立支持此點。

**5 批判**
   1. 數字落在判準帶外或內：無數值可判定，原因：僅取得 OpenAlex 重建摘要，Ion 下降 %、Rth、ΔT 全部未取得，無法與任何判準帶比對。
   2. 元件類別不符使用者主題：本文為 GAA nanosheet，不是矽 FinFET。可作為「節點外推方向」的背景引用，絕不可拿來校準 FinFET deck 的 thermode 或 SurfaceResistance。
   3. 重複引用風險：這是 4 頁會議短文，與同組五16（IEEE TED 2018 期刊版，同第一作者、同結構、同研究團隊）高度重疊，實質上是同一批工作的會議/期刊配對。若要引用細節，應優先引期刊版五16；同時引兩篇會造成重複計數，須說明其關係。
   4. 來源品質分層問題：本文的 metadata 在 Semantic Scholar 完全無摘要，僅能靠 OpenAlex 重建，且無任何開放全文管道。原表記「未能取得」是正確且誠實的判定，本次亦未能突破。
   5. 原表的「三層」與「簡化 BEOL 圖級數據」在本文摘要中無法驗證，很可能是從同組五16 推得；使用時務必註明出處，避免把五16 的幾何冠到本文編號下。

**6 可引用性**　C（僅可當背景引用）— 僅取得 OpenAlex 重建摘要（非出版者原文），只能引用「堆疊 nanosheet GAA 的自熱評估須納入 BEOL 才能正確描述溫度與熱通量分佈」這類定性主張，且元件類別與使用者的矽 FinFET 主題不符，數值一律不可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/vlsi-tsa.2018.8403821?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/vlsi-tsa.2018.8403821

**8 與原表差異**　與原表大致一致，並有補充與一處無法驗證。原表記「水平堆疊三層 GAA nanosheet 電晶體（北京大學組），含簡化 BEOL 圖級數據，未能取得／摘要未載明」——本次透過 OpenAlex 取得重建摘要（Semantic Scholar 的 abstract 欄為 null），確認摘要確實無任何數值，此點與原表一致；「北京大學組」經 OpenAlex 機構欄位確認正確（Institute of Microelectronics, Peking University）。補充原表未載：第一作者為 Linlin Cai；摘要明示模擬考慮 BEOL。無法驗證項：原表所記的「三層」堆疊在本文摘要中並未出現，該幾何僅見於同組五16（TED 2018）之摘要（“horizontally stacked three-layer”），屬跨文推論，非本文自證。

---

## 五16 — Layout Design Correlated With Self-Heating Effect in Stacked Nanosheet Transistors

- **DOI／識別**：`10.1109/TED.2018.2825498`　**來源**：IEEE　**年**：2018
- **作者／單位**：Linlin Cai（第一作者），Institute of Microelectronics, Peking University, Beijing, China（北京大學微電子學研究院）；共同作者 Wangyong Chen、Gang Du、Xing Zhang、Xiaoyan Liu
- **出處**：IEEE Transactions on Electron Devices（ADS bibcode 2018ITED...65.2647C 指向 vol. 65, p. 2647，惟 ADS 頁面回傳 HTTP 405 未成功取得，卷期頁未逐字驗證）

**1 元件**　5 nm 技術節點；水平堆疊三層 GAA nanosheet 電晶體（“horizontally stacked three-layer GAA nanosheet transistors”，原文逐字）。研究範圍從單一元件（single device）到元件陣列（device arrays）。nanosheet 寬度（WNS）被摘要明指為關鍵參數。TNS、Lg、堆疊垂直間距、n/p 型別、陣列尺寸與指數均未載明（摘要無，全文未取得）。

**2 方法與 SHE 定義**　`model`　三維有限元素法（3-D finite-element modeling, FEM）熱模擬（摘要未指名商用工具名稱）。關鍵方法特徵：在 FEM 求解器中實作 nanosheet 的各向異性熱導率，且該熱導率同時相依於矽厚度與溫度——原文逐字：“The anisotropic thermal conductivity of nanosheets with the dependence of silicon thickness and temperature is implemented in the FEM simulator to evaluate thermal behavior accurately.” 無 hydrodynamic 或 BTE 求解敘述（以等效熱導率模型取代聲子輸運）。熱邊界條件、thermode 位置與 SurfaceResistance 設定未取得。分析對象涵蓋 self-heating、溫度不均勻性（nonuniformity of temperature）與元件層級的熱串擾（thermal crosstalk at device level）。

**3 關鍵定量結果**　未取得數值。可逐字引用者：“With technology node scaling down to 5 nm, the narrow device geometry confines the material thermal conductivity and further aggravates the self-heating effect in gate-all-around (GAA) transistors.”；“The results indicate that the width of nanosheet is the key parameter to make the tradeoffs between self-heating and electrical characteristic.”；“the optimizations of layout design are given to suppress the thermal effects, including self-heating, nonuniformity of temperature, and thermal crosstalk at device level.” 摘要未印出任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度；全部屬全文圖表層級且未取得。

**4 TCAD 校準用途**　方法論層級部分可用，數值完全不可用。可直接搬進 deck 的建模原則：nanosheet 或任何薄膜矽區域應採用「厚度相依且溫度相依的各向異性熱導率」，而非等向常數值——這比本批五14 所用的常數 13 / 5 W/mK 更嚴謹，可作為使用者 deck 熱導率模型的升級依據，並直接呼應五18 量測到的 k(T) 效應。另可對齊的是「單元件 → 元件陣列」的分層驗證流程與熱串擾檢查程序。不可用於校準 SurfaceResistance、不可用於比對 ΔIon%（無數值，且元件為 5 nm GAA nanosheet 而非矽 FinFET）。

**5 批判**
   1. 數字落在判準帶外或內：無數值可判定，原因：僅取得摘要，Ion 下降 %、Rth、ΔT 全為全文圖表層級且未取得，無法與判準帶比對。
   2. 元件不匹配：5 nm GAA nanosheet ≠ 矽 FinFET。使用者引用時只能當作「更先進節點自熱更嚴重」的趨勢背景，不可拿其幾何、熱阻或溫度值校準 FinFET deck。
   3. 方法嚴謹度高但無法只憑摘要背書：各向異性 + 厚度相依 + 溫度相依的熱導率處理，在本批七篇中最為講究，值得作為方法論標竿；但摘要未交代熱邊界如何截斷（基板底面?BEOL 頂面?接觸面熱阻?），而在 GAA 結構中該邊界正是決定 ΔT 絕對值的主因，因此「準確」的宣稱在只有摘要的情況下無法查證。
   4. 純模擬、無實驗校準：摘要未提及任何硬體量測或校準來源，亦無誤差棒、無網格收斂性、無重複性敘述；所謂 “guidelines for layout design” 屬設計建議而非量測結論。
   5. 與同組五15（VLSI-TSA 2018）為同一批工作的期刊/會議配對（同第一作者、同結構、同機構），引用時擇一即可，若兩篇並列須說明其非獨立驗證。
   6. 書目未完全驗證：卷期頁僅能從 ADS bibcode 推得（vol. 65, p. 2647），ADS 頁面本身取得失敗，寫入 bib 檔前應以 Crossref 或 IEEE Xplore 複核。

**6 可引用性**　C（僅可當背景引用）— 僅取得摘要，可引用其方法論特徵（各向異性、厚度與溫度相依熱導率）與定性結論（WNS 為自熱與電性 tradeoff 的關鍵參數），但元件類別與使用者主題不符，數值一律不可引用；卷期頁尚未逐字驗證。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2018.2825498?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf

**8 與原表差異**　與原表一致。原表記「5 nm 節點水平堆疊三層 GAA nanosheet 電晶體，單元件至元件陣列／圖級，未取得／摘要未載明」——本次獨立驗證：摘要確實無任何數值，「5 nm 節點」「horizontally stacked three-layer」「單元件到元件陣列」三項均由摘要逐字證實，原表記載正確。補充原表未載：第一作者 Linlin Cai（北京大學微電子學研究院）；摘要明載的方法特徵（3-D FEM，各向異性且相依於矽厚度與溫度的熱導率）與核心結論（nanosheet 寬度為自熱/電性 tradeoff 的關鍵參數；優化目標含 self-heating、溫度不均勻性與熱串擾三項）。卷期頁未能逐字驗證（ADS 頁面回傳 HTTP 405）。

---

## 五17 — Modeling of FinFET Self-Heating Effects in multiple FinFET Technology Generations with implication for Transistor and Product Reliability

- **DOI／識別**：`10.1109/VLSIT.2018.8510657`　**來源**：IEEE　**年**：2018
- **作者／單位**：Hyun Chul Sagong（第一作者），Samsung Electronics, Foundry Business, Giheung, Korea；全體 10 位作者（含 Kiho Choi、Tae-Young Jeong、Hyewon Shim、Jung O. Park、Sangwoo Pae）均隸屬同一單位
- **出處**：2018 IEEE Symposium on VLSI Technology（VLSI Technology 2018）

**1 元件**　量產（production）bulk FinFET，跨多個 FinFET 製程世代（“multiple FinFET process technology generations”）。具體節點名稱、Lg、Hfin/Wfin 數值、n/p 型別、鰭數與指數全部未載明（摘要無，全文未取得）。摘要僅定性指出隨節點微縮 fin 變得更高更窄：“taller and narrower Fin shape allows higher performance”。

**2 方法與 SHE 定義**　`Rth-extraction`　摘要僅稱進行 FinFET 自熱（FSH）的特徵化（characterization）與建模（modeling），並將建模成果用於設計。屬產線元件量測 + 建模，而非 TCAD 電熱模擬。量測方法（何種 thermometry：VT / gate resistance / pn junction）、pulsed 或 DC、環境溫度、熱邊界條件、thermode 與 SurfaceResistance、模擬工具全部未取得。

**3 關鍵定量結果**　未取得數值。摘要逐字：“We report the characterization and modeling of FinFET self-heating (FSH) and its reliability impact across multiple FinFET process technology generations.”；“With technology node scaling, taller and narrower Fin shape allows higher performance. However, increased FSH and potential reliability issues must be well understood and mitigated.”；“The results on transistor and product level demonstrate excellent reliability performance beyond 10yrs”。摘要完全未印出任何 ΔT、Rth、峰值晶格溫度、Ion 下降 % 或逐世代數值；全部屬全文圖表層級且未取得。

**4 TCAD 校準用途**　不可直接校準，理由：無任何數值、無幾何、無節點名稱、無量測條件。唯一可用的是趨勢命題「fin 更高更窄 → FSH 增加」，可作為使用者做 Hfin / Wfin 敏感度掃描時的方向性 sanity-check——deck 若掃出相反趨勢（例如增高 fin 反而 ΔT 下降），即代表熱邊界或熱導率模型設定有誤。無法提供任何 SurfaceResistance 量級或可比對的 ΔT。

**5 批判**
   1. 數字落在判準帶外或內：無數值可判定，原因：僅取得摘要，逐世代的 ΔT 與 Rth 為全文圖表層級且未取得，無法與 single-fin Rth 1–4 MK/W 或 Ion 下降 % 判準帶比對。
   2. 物理因子未拆分：「fin 更高更窄使 FSH 增加」把兩個機制綁在一起——Hfin 增加提高單鰭驅動電流與功率（熱源變強），Wfin 縮小則降低薄膜矽熱導率並增加熱阻（散熱變差）。摘要未拆分兩者的相對貢獻，使用者若要用本文驗證 deck，必須分別單獨掃 Hfin 與 Wfin，否則無法判定 deck 的哪一項物理設定有誤。
   3. 結論指標高度糾纏：“beyond 10yrs” 是產品層級可靠度結論，內含 BTI/HCI/EM 老化模型、加速因子與外推假設，與元件級 SHE 的因果距離很遠，絕不可反推自熱強度或 Ion 下降幅度。
   4. 工業界揭露限制：三星量產製程論文慣例不揭露節點名稱、fin 幾何與絕對熱阻，只給正規化趨勢曲線；對想校準絕對 SurfaceResistance 的 TCAD 使用者價值有限。摘要亦無誤差棒、無樣本數、無重複性敘述。
   5. 搜尋引擎污染警示：本次網路搜尋的彙整結果曾把本批五13（IRPS 2020）的貢獻（“heat-dissipation-path based SHE model”、“interactive thermal resistance / Rth-matrix”）誤植到本文名下。本文摘要並無該敘述，兩篇雖為同一團隊延續工作（Sagong、Shim、Jeong、Park、Pae 五人重疊），但貢獻必須分清，切勿把 Rth-matrix 方法歸給 2018 這篇。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可引用其定性趨勢結論（隨節點微縮 fin 更高更窄，FSH 隨之加劇，且已在量產世代完成特徵化與建模），任何數值與逐世代比較一律不可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/vlsit.2018.8510657?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/vlsit.2018.8510657

**8 與原表差異**　與原表一致。原表記「Production bulk FinFETs across multiple technology generat…／Abstract confirms taller/narrower fins in newer generations increase FSH; per-generation dT values are figure-level only…／not accessed」——本次獨立驗證完全相符：摘要逐字證實 “taller and narrower Fin shape” 與 FSH 增加的因果敘述，且摘要確無任何逐世代 ΔT 數值，全文不可取得。補充原表未載：第一作者 Hyun Chul Sagong，全體 10 位作者均隸屬 Samsung Electronics, Foundry Business (Giheung, Korea)；與本批五13（IRPS 2020）為同團隊延續工作，作者群重疊五人。另記錄一項需防範的外部錯誤：網路搜尋彙整曾把五13 的 Rth-matrix 貢獻誤植到本文，非原表問題，但引用時須注意。

---

## 五18 — Ambient temperature and layout impact on self-heating characterization in FinFET devices

- **DOI／識別**：`10.1109/IRPS.2018.8353640`　**來源**：IEEE　**年**：2018
- **作者／單位**：P. Paliwoda（Peter Christopher Paliwoda，第一作者），GlobalFoundries Inc., Malta, NY, USA；共同作者 Z. Chbili、A. Kerber、D. Singh（同屬 GlobalFoundries）；D. Misra（New Jersey Institute of Technology / Newark College of Engineering, Newark, NJ, USA）
- **出處**：2018 IEEE International Reliability Physics Symposium (IRPS), pp. 6E.2-1–6E.2-5

**1 元件**　14 nm bulk FinFET 與 14 nm SOI FinFET（GLOBALFOUNDRIES 提供之量產晶圓樣品）；logic 與 IO 元件皆測。每個 active region (RX) 的鰭數為 2 / 5 / 20 fins（範圍 2–20），n 型與 p 型 FinFET 皆測，屬多鰭/多指佈局；另設計側向熱傳導測試結構（8 個 heater gate 逐一開啟）。Lg、Hfin、Wfin 未揭露（產線製程保密）。以上鰭數與 bulk/SOI 對照的細節取自同一第一作者的 NJIT 博士論文（Fall 2018）Chapter 4，IRPS 論文本體僅取得摘要。

**2 方法與 SHE 定義**　`Rth-extraction`　晶圓級電性熱量測（wafer-level characterization），並以 TCAD 熱模擬佐證側向散熱。設備（取自 NJIT 博士論文）：Cascade Microtech Elite 300 wafer prober、Keysight B1500A 半導體參數分析儀、Keysight B2201A 切換矩陣、prober thermal chuck 控溫（-40 °C 至 175 °C）。三種溫度感測器：Type I 用 FET 的線性區臨界電壓 VTlin、Type II 用 pn junction（source-to-substrate diffusion）順偏電壓 VD、Type III 用 gate resistance RG（4-terminal Kelvin contact）；三者先在多個 chuck 溫度下校準取得溫度係數。加熱元件為鄰近的飽和區 FET（Vgs = Vds），另做「倍功率」實驗以擴大溫度範圍。無 thermode / SurfaceResistance 數值揭露（本文非以 TCAD 為主）。重要來源分層：除摘要外，本欄所有設定細節均出自 NJIT 博士論文，非 IRPS 論文本體逐字。

**3 關鍵定量結果**　【IRPS 論文本體，摘要逐字，原文印出數字】“Self-Heating effects are going to be of increasing significance in future nodes. Understanding self-heating measurement results and its accuracy is of vital importance. In this paper we show for the first time through measurement that the ambient temperature can affect self-heating measurement by up to 70%. Through a series of measurements at different temperatures and dissipated power, we show that the Si fin has a more dominant effect in heat transport and its varying thermal conductivity should be taken into account.”【以下數值出自同一第一作者 NJIT 博士論文 Chapter 4（同一資料集、不同文件），非 IRPS 論文本體，引用時須標明出處】熱阻的環境溫度相依性：“The thermal resistance of the 20-fin n-type and p-type devices show 70% and 45% increase respectively as chuck temperature increases from -40 to 175°C.”；佈局密度效應：“Temperature rise of 2x is observed as density of fins increases from 2 to 5 and 1.25x moving from 5 to 20 fins per active region. Saturation of heat is observed at 20 fins for bulk Fin FET technology.”；側向散熱範圍：“The radial distance affected by self-heating is within radial distance of ~1µm”，SOI 對照 “the heat needs to travel ~500nm further compared to bulk FinFET to be totally dissipated”；感測器系統偏差：“VTlin and PN junction sensors underestimate the actual peak channel temperature by ~3.7x”；bulk 與 SOI 對照：“self-heating response (RTH) of the same sensor in a 2 fin SOI FinFET (with similar gate/fin pitch) technology is ~5x higher”；倍功率實驗：“the slope starts changing (~8% increase) at higher temperatures”。【未取得】Rth 絕對值（K/W 或 MK/W）、ΔT 絕對值、峰值晶格溫度、Ion 下降 % 一律未揭露；論文以正規化與相對值呈現，屬圖層級。對應條件：heater 為 Vgs = Vds 之飽和區操作（具體電壓值未印出），Ta 為 -40 至 175 °C。

**4 TCAD 校準用途**　對使用者 deck 有三項高價值輸入。(1) 量測與模擬之間的橋接係數：VT 與 pn-junction 感測器低估真實峰值通道溫度約 3.7×——使用者若拿文獻中的量測 ΔT 去校準 deck 的峰值晶格溫度，必須先乘上此係數，否則會系統性把 thermode 調得過度導熱，導致 SHE 被抹掉（落入判準帶「ΔIon 小於 1%」的失敗區）。(2) k(T) 必須開啟：20-fin nFET 的 Rth 從 -40 °C 到 175 °C 上升 70%，代表在 TA = 300 K 附近 Si 熱導率的溫度相依性已不可忽略；deck 若用常數熱導率會低估 ΔT，這同時是本批五13、五14 之線性疊加模型的直接反證。(3) 幾何與 thermode 擺放的邊界：2→5 fins 升溫 2×、5→20 fins 僅 1.25× 且在 20 fins 飽和，說明多鰭熱阻不是簡單並聯，使用者不可用單鰭 Rth 除以鰭數推多鰭 Rth；側向影響半徑 bulk 約 1 µm、SOI 再多約 500 nm，可直接用來決定模擬區域的橫向尺寸與 thermode 的橫向擺放距離——thermode 若設在距通道 1 µm 以內，會人為抽走熱量。另可 sanity-check：同一感測器下 2-fin SOI 的 Rth 約為 bulk 的 5 倍。除 70% 外，上述數值均須以博士論文而非 IRPS 論文編號引用。

**5 批判**
   1. 數字落在判準帶外或內：本文不報飽和區 Ion 下降 %，無法直接落入 bulk 3–12% 判準帶；但它直接衝擊「single-fin Rth 約 1–4 MK/W」這條判準本身——本文量到 Rth 隨環境溫度變動達 70%（n 型 20-fin，-40→175 °C），代表任何單一 Rth 數字（含 1–4 MK/W 判準帶）若未附註量測/模擬溫度即不可比較。這是本批對使用者判準帶最重要的修正。
   2. 分類要小心但本文不是 ta_sweep 陷阱：本文大量使用 ta_sweep（-40 至 175 °C），但目的不是把環境溫度當成自熱，而是量「自熱量測結果本身對環境溫度的敏感度」，屬方法學研究。反過來，若把 70% 讀成「自熱使 Ion 掉 70%」則是嚴重誤讀——70% 是熱阻的相對變化量，不是電流變化量。
   3. 熱邊界不是問題但絕對值不可得：這是量測而非模擬，沒有 thermode 過絕熱或過導熱的疑慮；但相對地，產線資料保密使其完全不提供絕對 Rth 值，使用者無法用它設定 SurfaceResistance，只能用它校正趨勢與量測偏差係數。
   4. 3.7× 低估係數存在循環論證風險：該係數由硬體校準的熱 TCAD 模型反推得出（用 TCAD 校正量測，再用量測校準 TCAD）。使用者引用此係數時應標明其模型相依性，並視為量級估計而非精確常數。
   5. 糾纏因子少、可信度相對高：本文為純熱量測，未疊加老化模型或通道工程；且使用三種獨立感測器（VT / pn junction / gate RG）互相驗證並建立誤差棒（依博士論文 Chapter 3，含常態分佈、機率圖與 heater 前後的遲滯檢查），這在自熱文獻中相對罕見，是本批可信度最高的實驗來源。但 14 nm 產線元件的 fin 幾何未揭露，單一技術世代能否外推到 3 nm 或 GAA 無證據。
   6. 資料來源必須分層：只有 “up to 70%” 這一個數字出自 IRPS 論文本體（摘要逐字）；其餘所有數值（45%、2×/1.25×、~1 µm、~500 nm、3.7×、~5×、~8%）均出自同一第一作者的 NJIT 博士論文（2018, Dissertations 1389）Chapter 4。兩者為同一資料集但屬不同文件，引用時不可全掛在 IRPS 論文編號下。

**6 可引用性**　A（可直接引用數字）— “up to 70%” 出自 IRPS 論文摘要逐字（原文印出數字），可直接引用並註明其定義為「環境溫度對自熱量測結果的影響幅度」。其餘所有數值均取自同作者的 NJIT 博士論文全文，同樣可直接引用，但必須改用博士論文（Paliwoda, NJIT Dissertations 1389, 2018）作為引用來源，不可掛在 IRPS 編號下。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps.2018.8353640?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps.2018.8353640
   - https://digitalcommons.njit.edu/fac_pubs/8659/
   - https://digitalcommons.njit.edu/dissertations/1389/
   - https://digitalcommons.njit.edu/cgi/viewcontent.cgi?article=2444&context=dissertations

**8 與原表差異**　與原表一致，並大幅補充。原表 verdict 為 value_corrected，記「Bulk FinFET (14nm-class), multi-fin/multi-finger layouts／Abstract-verified new number: ambient temperature can affect the self-heating MEASUREMENT by up to 70%（first such demon…）／not accessed」——本次從 NJIT DigitalCommons 取得逐字摘要，確認原文為 “we show for the first time through measurement that the ambient temperature can affect self-heating measurement by up to 70%”，原表記載（特別是強調 MEASUREMENT）完全正確。重要警示：OpenAlex 的重建摘要漏掉 “measurement” 一字，作 “can affect self-heating by up to 70%”，該版本會誤導讀者以為自熱本身變化 70%，逐字引用務必以 NJIT fac_pubs 版為準。補充原表未載（來源為同作者 NJIT 博士論文，非 IRPS 本體）：70% 的精確定義是 20-fin n 型元件熱阻在 -40 °C→175 °C 間的增幅（p 型對應為 45%）；元件為 GLOBALFOUNDRIES 14 nm bulk 與 SOI FinFET，鰭數 2–20 per RX；另有密度效應（2→5 fins 升溫 2×、5→20 fins 1.25×、20 fins 飽和）、側向影響半徑 ~1 µm（SOI 再多 ~500 nm）、感測器低估峰值通道溫度 ~3.7×、2-fin SOI 之 RTH 約為 bulk 的 5 倍等原表未收錄但對 TCAD 校準價值極高的數值。原表「multi-fin/multi-finger layouts」與「14nm-class」均獲證實；唯一可再精確處是本文同時涵蓋 bulk 與 SOI（原表只寫 Bulk FinFET）。

---

## 五19 — Bottom-up methodology for predictive simulations of self-heating in aggressively scaled process technologies

- **DOI／識別**：`10.1109/IRPS.2018.8353650`　**來源**：IEEE　**年**：2018
- **作者／單位**：D. Singh（GlobalFoundries, United States）；共 19 位作者，多數為 GlobalFoundries（含 P. Paliwoda，與 五24 為同一人）
- **出處**：2018 IEEE International Reliability Physics Symposium (IRPS)，Burlingame, CA, USA，pp. 6F.6-1–6F.6-7

**1 元件**　摘要與可讀章節僅泛指 FinFET technologies，並同時涵蓋 interconnects 與 integrated precision resistors。技術節點、bulk/SOI、Lg、Hfin/Wfin、n/p、鰭數 全部未取得（全文付費牆）。

**2 方法與 SHE 定義**　`model`　階層式（bottom-up）三層流程：ab-initio 聲子散射 + 電子傳輸計算 → 製程專屬材料/介面熱性質 → multi-scale finite element（FEM）模擬。IEEE 章節結構為 I. Introduction / II. FEOL Thermal Properties / III. MOL and BEOL Thermal Properties / IV. Application to Thermal Measurements / V. Conclusions。摘要宣稱與 Rth 量測相符且無擬合參數。求解器名稱（Sentaurus/GARAND 或自建 FEM）、熱邊界條件、thermode 位置與 SurfaceResistance 設定、是否含 hydrodynamic/BTE 全數未取得。

**3 關鍵定量結果**　未取得數值。摘要僅有定性宣稱：跨多種元件型態與製程技術，模擬與熱阻量測「excellent agreement」且無任何擬合。無 Ion 下降 %、無 Rth 絕對值、無 ΔT、無峰值晶格溫度，也無任何偏壓條件（VGS/VDS/TA）。層級為「僅摘要 + Introduction 首段」，連圖說都未取得（IEEE figures 頁同樣被付費牆擋下）。

**4 TCAD 校準用途**　不可直接校準，理由：本次未取得任何 Rth/ΔT 數值、幾何或熱邊界設定。唯一可轉化的是方法論立場——它主張介面熱阻（TBR）與合金熱導應由第一原理決定而非事後擬合。對照使用者的 deck：若 thermode 的 SurfaceResistance 是「調到 I-V 對得上」的擬合值，本篇正是反例文獻。要真正拿來校準，必須取得全文第 II、III 節的 FEOL/MOL/BEOL 熱性質數值表。

**5 批判**
   1. 無數值可判定，原因：IRPS 全文付費牆，本次僅取得摘要與 Introduction 首段，未見任何 Ion 下降 %、Rth、ΔT 數字，既無法判斷是否落在 3-12%（bulk）判準帶，也無法做 ΔIon%/ΔT 的 0.10-0.20 %/K 交叉檢核。
   2. 「without any fitting」是強宣稱，但驗證標的是集總 Rth。集總量對上游多個材料參數的組合並不敏感，存在「多組參數互相補償仍能對上量測」的等效性問題；摘要層級未見誤差棒、不確定度或參數敏感度分析。
   3. 作者幾乎全屬 GlobalFoundries，量測與模型皆為內部資料，元件幾何未公開，外部無法重現，外推到使用者的矽 FinFET deck 須自行假設節點與 fin 幾何。
   4. 涵蓋 FinFET + interconnect + precision resistor 三類熱源，摘要層級無法區分哪些結論屬元件層級 SHE、哪些屬 BEOL 焦耳熱；引用時若不加限定，容易把 BEOL 結論誤植為通道自熱結論。
   5. 分類確認：本篇為模擬方法學（model），不是 ET-vs-ISO 的 Ion 退化研究，也不是 ta_sweep；不要期待從它拿到飽和區 Ion 下降百分比。

**6 可引用性**　C（僅可當背景引用）— 只讀到摘要與引言，僅能引用「bottom-up ab-initio + 多尺度 FEM 可預測 FinFET 自熱並與 Rth 量測相符」這類方法論背景陳述，無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps.2018.8353650?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps.2018.8353650
   - https://ieeexplore.ieee.org/document/8353650/

**8 與原表差異**　與原表大致一致並補強。原表 orig 記「aggressively scaled bulk FinFET process technologies (GF 1… not accessed not accessed」；本次補齊完整摘要、GlobalFoundries 作者單位、頁碼 6F.6-1–6F.6-7、會議地點 Burlingame 與五節章節結構。注意：原表推測的「bulk FinFET / GF 14nm 節點」在本次可讀內容中並未出現（摘要只說 FinFET technologies），標記為待查，非 CONFLICT。原表「not accessed」的取得狀態維持成立。

---

## 五20 — Self-Heating Effects Investigation on Nanoscale FinFET and Its Thermal Resistance Modeling

- **DOI／識別**：`10.1109/ICSICT.2018.8564853`　**來源**：IEEE　**年**：2018
- **作者／單位**：Jun-Ya Sun（Shanghai Key Laboratory of Multidimensional Information Processing, East China Normal University, Shanghai, China）；後段共同作者 Shou-Mian Chen、Shao-Jian Hu、Ao Guo 來自 Shanghai Integrated Circuit Research & Development Center Ltd. (SICC)
- **出處**：2018 14th IEEE International Conference on Solid-State and Integrated Circuit Technology (ICSICT)，Qingdao, China，pp. 1-3

**1 元件**　sub-14-nm FinFET；Introduction 自述為「14-nm FinFET」的 3-D 電熱模擬。bulk/SOI 未言明。掃描變數明列 S/D extension 尺寸、摻雜濃度、fin width、fin height，但各自的實際數值未取得。Lg、n/p、鰭數 未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　3-D electrothermal device simulation（TCAD）。摘要明確採用 hydrodynamic 與 thermodynamic 傳輸模型（載子溫度與晶格溫度分離），並宣稱參數已用實驗資料校準。輸出包含 hotspot 位置與 lumped thermal resistance。章節為 1. Introduction / 2. Device Simulation Setup and Calibration / 3. Results and Discussions / 4. Summary。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance 設定、是否含 BTE 或聲子模型 全數未取得。

**3 關鍵定量結果**　未取得數值。摘要三項結論皆為定性：(1) 散熱對 S/D extension 尺寸敏感；(2) 溫度變化由摻雜濃度改變造成，且可藉縮短 extension 長度進一步抑制；(3) 不同 fin 寬與 fin 高顯著影響電特性，進而影響 hotspot 位置與 lumped thermal resistance。無 Ion 下降 %、無 Rth 絕對值、無 ΔT、無峰值晶格溫度，也無任何偏壓條件。層級為「僅摘要 + Introduction 首段」，非圖層級（圖說亦未取得）。

**4 TCAD 校準用途**　僅結構性指引，無數值可校準。可轉化的是變數優先序：S/D extension 長度與 extension 摻雜是熱逸散的主控變數。對映到使用者 deck——若 thermode 設在 S/D 接觸上，extension 幾何會直接改變萃取到的 Rth，因此 extension 長度應列入 deck 的敏感度掃描清單，不能當固定值。另外它同時掃 fin 寬/高並觀察 hotspot 位移，可提醒使用者在改 fin 幾何時要重新確認 hotspot 是否仍落在 thermode 影響範圍內。

**5 批判**
   1. 無數值可判定，原因：僅取得摘要與 Introduction 首段，未見任何 Ion 下降 %、Rth、ΔT 數字，無法比對 3-12%（bulk）判準帶，也無法做 ΔIon%/ΔT 交叉檢核。
   2. hydrodynamic + thermodynamic 並用是合理且必要的設定（避免用 drift-diffusion 低估載子加熱），但 3 頁會議短文通常不揭露熱邊界條件；在 thermode 位置與接觸熱阻未知的情況下，其 lumped Rth 的絕對值不可直接搬進使用者的 deck。
   3. 「參數已用實驗資料校準」未說明校準對象是電性 I-V 還是熱量測。若只校準 I-V，熱模型（熱導率、介面熱阻）仍是完全未受約束的自由度，這是 TCAD 自熱模擬最常見的隱性弱點。
   4. fin 寬/高掃描屬單一幾何族群的局部外推；且合作方 SICC 的製程細節不公開，跨技術節點外推的風險高，無誤差棒與重複性資訊。
   5. 分類注意：標題宣稱 thermal resistance modeling，但摘要未給模型形式或係數，本篇實質介於 Rth-extraction 與 model 之間；本次依「從 TCAD 萃取集總 Rth」歸為 Rth-extraction，需全文才能定案。

**6 可引用性**　C（僅可當背景引用）— 僅取得摘要層級的三條定性結論，無任何數字、無模型形式，只能當「sub-14nm FinFET 自熱對 S/D extension 與 fin 幾何敏感」的背景引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/icsict.2018.8564853?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/icsict.2018.8564853
   - https://ieeexplore.ieee.org/document/8564853/

**8 與原表差異**　與原表一致。原表 orig 所記三項結論（散熱對 S/D extension 尺寸敏感、摻雜濃度相關之溫度變化可藉縮短 extension 降低、fin 寬/高影響電特性與 hotspot 及集總 Rth）與本次讀到的摘要逐點吻合，無衝突。本次補齊：第一作者單位 East China Normal University（上海多維信息處理重點實驗室）+ SICC、會議全名與地點 Qingdao、頁碼 1-3、四節章節結構，以及 Introduction 自述為「14-nm FinFET 的 3-D 電熱模擬」。原表「未取得（全文未讀）」狀態維持成立。

---

## 五21 — A Novel Approach to Localize the Channel Temperature Induced by the Self-heating Effect in 14nm High-k Metal-gate FinFET

- **DOI／識別**：`10.1109/EDTM.2018.8421479`　**來源**：IEEE　**年**：2018
- **作者／單位**：E. R. Hsieh（Department of Electronics Engineering, National Chiao Tung University, Taiwan，今國立陽明交通大學）；學界端另有 M.-R. Jiang、H. W. Chen、J.-Y. Lin、Steve S. Chung（同系）；業界端 T. P. Chen、Y. H. Yeah、T. J. Chen、Osbert Cheng 皆為 United Microelectronics Corporation (UMC)
- **出處**：2018 IEEE 2nd Electron Devices Technology and Manufacturing Conference (EDTM)，Kobe, Japan，pp. 148-150

**1 元件**　14 nm high-k/metal-gate FinFET，n 型與 p 型兩種；pFinFET 具 embedded SiGe (eSiGe) S/D。bulk/SOI 未明說，但 Introduction 強調 fin 之間交錯的 STI 阻擋寬度方向散熱、熱只能沿通道方向傳導，語意偏 bulk FinFET。Lg、Hfin、Wfin、鰭數 未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗量測法：以 RTN（random telegraph noise）量測沿通道方向的溫度分佈，論文宣稱為首次；再以 SPICE 內建模型萃取參數，分離通道電阻 Rc 與 S/D 串聯電阻 Rsd 的溫度相依行為；最後以 SRAM 訊噪比（SNM）縮減作為 benchmark。純量測 + 緊湊模型，無 TCAD 求解器、無 thermode、無熱邊界設定。Introduction 明列既有量測法作為對照：IBM 以改良 AFM 探針感測、Takahashi 以 4-terminal gate poly liner 偵測閘下溫度、imec 以旁置 diode 或 MOSFET 感測 DUT 熱輻射；本文批評這些方法只能取得遠距的平均溫度。

**3 關鍵定量結果**　原文印出數字（出自摘要）：14nm pFinFET 的通道溫度比 nFinFET 高 170 K，歸因於 pFinFET 的 eSiGe S/D 散熱困難。原文短語：pFinFET 通道溫度 "170K higher than that of nFinFET"（Hsieh et al., EDTM 2018 摘要）。其餘為定性：nFinFET 在室溫下 Rsd 主導、高溫下 Rc 因飽和速度退化而超過 Rsd；pFinFET 則 Rc 在高低溫皆主導、Rsd 於高溫因 eSiGe 高熱阻而變顯著；並以聲子散射增強造成的遷移率下降解釋。無絕對 ΔT（對地溫升）、無 Rth 數值、無 Ion 下降 %；量測偏壓 VGS/VDS 與 TA 未取得。

**4 TCAD 校準用途**　可用於 sanity-check 與模型設定，不可用於數值校準。(a) 若使用者 deck 含 p 型矽 FinFET 且 S/D 為 SiGe，本篇提供 n/p 熱不對稱的實驗錨點：deck 中若把 S/D 熱導一律設為 Si 值，將系統性低估 p 型 SHE。(b) 它指出高溫下 Rc 因飽和速度退化而反超 Rsd，這對應 deck 中「飽和速度的溫度相依」是否有開啟——若使用者只開遷移率的溫度相依而未開 vsat 溫度相依，飽和區 Ion 退化會被低估。(c) 170 K 是 n/p 差值而非對地 ΔT，無法換算成 thermode SurfaceResistance。

**5 批判**
   1. 落在判準帶外（方向為 SHE 過強）。以交叉檢核比值 0.10-0.20 %/K 換算，170 K 的通道溫差等效約 17-34% 的額外 ΔIon，超過「飽和 Ion 差 >20% 即 SHE 過強」的警戒線。最合理的解釋是：RTN 探測到的是 trap 附近的局部溫度而非通道平均溫度，且量測偏壓很可能遠高於 VDD=0.7 V 的常用工作點——但這兩點都無法從已取得的摘要與引言證實，因此 170 K 不可當成 deck 的 ΔT 目標值。
   2. RTN 溫度計是間接量測：從 trap 的捕捉/釋放時間常數反推活化能再反推溫度，強烈依賴 trap 能階、位置與弛豫模型的假設。單顆 trap 的空間定位精度與統計代表性在可讀內容中完全未說明，也未見誤差棒或多顆 trap 的重複性。
   3. 糾纏因子明顯：pFinFET 的 eSiGe 同時改變通道應力（提升遷移率）與熱導（阻礙散熱），量到的 Rc/Rsd 溫度行為是應力效應與熱效應的疊加。摘要把 n/p 差異幾乎全數歸因於 SiGe 熱導，屬單因子歸因，未見拆解設計（例如同 layout 不同 SiGe 濃度的對照組）。
   4. 分類注意：本篇不是 ET-vs-ISO，也不是 ta_sweep，而是通道溫度（ΔT）的量測方法學；把 170 K 當成 Rth 或 Ion 退化的直接來源是分類誤用。本次歸為 Rth-extraction 是「熱特性萃取」的最近似歸類，嚴格說是 ΔT-extraction。
   5. 以 SRAM SNM 作為 benchmark 屬電路層級外推，元件層級 ΔT 與 SNM 縮減之間的定量橋接在摘要層級無法檢驗，引用時不應把 SNM 結論當作元件層級證據。

**6 可引用性**　B（只能引用定性結論）— 170 K 雖是原文印出的數字，但缺偏壓、缺誤差棒、缺「局部溫度 vs 通道平均溫度」的定義說明，單獨引用會誤導讀者；宜引用「14nm pFinFET 因 eSiGe S/D 散熱不良而顯著較 nFinFET 熱」這個定性結論。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edtm.2018.8421479?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/edtm.2018.8421479
   - https://ieeexplore.ieee.org/document/8421479/

**8 與原表差異**　與原表一致並補強。原表 orig 記「14 nm high-k/metal-gate bulk FinFETs (UMC), n and p；pFinFET channel ~170 K hotter than nFinFET（abstract-confirmed；歸因 eSiGe S/D 散熱）；exact VGS/VDS not in accessed material」——本次以 IEEE Xplore 摘要頁與 Semantic Scholar 摘要逐字複核，170 K 與 eSiGe 歸因無誤，VGS/VDS 仍未取得。原表標註的「(UMC)」經 OpenAlex 作者單位證實（T. P. Chen、Y. H. Yeah、T. J. Chen、Osbert Cheng 四人為 UMC；學界端為 National Chiao Tung University）。補齊：頁碼 148-150、地點 Kobe、Introduction 中對 IBM/Takahashi/imec 三種既有量測法的對照敘述。原表所稱「bulk」在本次可讀內容中未明說，僅有 STI 阻擋橫向散熱的間接語意，標為待查。

---

## 五22 — Analysis of DC Self Heating Effect in Stacked Nanosheet Gate-All-Around Transistor

- **DOI／識別**：`10.1109/EDTM.2018.8421495`　**來源**：IEEE　**年**：2018
- **作者／單位**：Min-Jae Kang（Korea National University of Transportation；OpenAlex 另掛 Imperial College London，研判為機構比對錯誤）；共同作者 Ilho Myeong 與 Hyungcheol Shin 為 Seoul National University，Myounggon Kang 為 Korea National University of Transportation
- **出處**：2018 IEEE 2nd Electron Devices Technology and Manufacturing Conference (EDTM)，Kobe, Japan，pp. 343-345

**1 元件**　Vertically stacked nanosheet gate-all-around (GAA) transistor。摘要明列的架構掃描參數為：metal gate thickness、number of channels（堆疊數）、thermal conductivity of ILD、channel thickness（TNS）。WNS、Lg、技術節點、n/p、通道長度 未取得。Introduction 指出 nanosheet 的 SHE 可能比其他架構更嚴重，因低熱導的 gate dielectric 完全包覆通道。

**2 方法與 SHE 定義**　`Rth-extraction`　DC 條件下的元件模擬（摘要用語為 simulations），輸出 lattice temperature 與 thermal resistance 對架構參數的變化趨勢。章節為 Introduction / Device Structure and Simulation Experiment / Results and Discussion / Conclusion。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、是否含 hydrodynamic/BTE/聲子模型 全數未取得。摘要與引言均未提 pulsed 量測，可確定為純 DC 電熱模擬。

**3 關鍵定量結果**　摘要層級為定性：nanosheet FET 因架構參數改變而呈現顯著的 lattice temperature 變化與 thermal resistance 波動，可藉提高 ILD 熱導與加厚 metal gate 緩解。摘要中無 Rth、ΔT、峰值晶格溫度的絕對數字，也無偏壓條件。【待查數字，不可引用】：多次 WebSearch 索引摘要一致將「drive current 因 SHE 退化 5.85%（VDD = 0.65 V）」歸屬本篇，但該敘述只出現在 ResearchGate 落地頁的搜尋索引片段中，該頁直接抓取回傳 HTTP 403，本次未能親自讀到原始頁面，故不列入 sources、不作為可引用結果，需取得全文確認。

**4 TCAD 校準用途**　價值有限且方向性大於數值性。可轉化的是散熱路徑排序：ILD 熱導與 metal gate 厚度是 GAA 架構的兩條主要散熱路徑——對映到使用者 deck，代表 gate stack 材料與 ILD 的熱導設定會顯著改變萃取到的 Rth，不可沿用工具預設值。但使用者做的是矽 FinFET，本篇僅能當跨架構對照（GAA 因介電質全包覆而比 FinFET 更難散熱）。未經驗證的 5.85% @ 0.65 V 在取得全文前不得寫入 deck 的比對基準。

**5 批判**
   1. 無可引用數值可判定，原因：摘要無任何數字，唯一候選（5.85% @ VDD=0.65 V）未經一手驗證。即使該數字為真，也不能直接套用使用者的 7-11% 錨點：本篇是 nanosheet GAA 而非矽 FinFET，且 VDD=0.65 V 低於判準帶假設的 0.7 V；若強行比對，5.85% 落在 bulk 判準帶 3-12% 的偏低端，但兩項前提條件都不同。
   2. 只有 DC 條件（標題即明示 DC）。DC 是 SHE 的最壞情況，本篇未做 pulsed-vs-DC 對照，因此其退化量無法代表實際開關工作下的效應——同批的 五24 作者在其博士論文中即指出真實切換條件下 SHE 明顯低於定電壓應力。
   3. 架構參數掃描彼此耦合且摘要未說明控制變因：增加 channel 數同時改變總消耗功率與散熱面積，若不固定功率密度就比 Rth，結論會被驅動電流差異污染。這是 Rth 比較最常見的混淆點，摘要層級完全無法檢驗。
   4. 3 頁會議短文，無誤差棒、無網格收斂說明、無熱邊界條件（基板底部溫度、接觸熱阻）揭露；其 Rth 絕對值即使取得全文也不可直接搬用，只能看趨勢。
   5. 分類確認：本篇為 DC 電熱模擬下的 Rth 與晶格溫度萃取，不是 ta_sweep（未掃環境溫度），摘要也未提等溫基準對照，因此不歸為 ET-vs-ISO。原表 verdict 標為 reclassified，本次結果支持將其定位為 Rth-extraction。

**6 可引用性**　C（僅可當背景引用）— 僅取得摘要層級的定性結論；唯一數字來自搜尋索引片段且原始頁面 403 無法一手驗證，在取得全文前不建議引用任何數值，只能當「GAA nanosheet 自熱受 ILD 熱導與 metal gate 厚度支配」的背景引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edtm.2018.8421495?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/edtm.2018.8421495
   - https://ieeexplore.ieee.org/document/8421495/
   - https://www.semanticscholar.org/paper/ac0fbd89c6b9d84e6797403594e02323dc8561d6

**8 與原表差異**　與原表大致一致。原表 orig 記「Vertically stacked nanosheet GAA transistor (SNU/KNUT TCAD…)；figure-level per abstract ('great lattice temperature variations')；values not in abstract；DC bias」——本次複核摘要，確認確實無任何數值，原表判斷正確；SNU/KNUT 的單位歸屬亦經 OpenAlex 證實（Seoul National University + Korea National University of Transportation）。補齊：頁碼 343-345、地點 Kobe、四節章節結構、摘要明列的四個掃描參數。新增待查線索（非 CORRECTION、非 CONFLICT）：搜尋索引反覆將「drive current degraded 5.85% (VDD = 0.65 V)」歸屬本篇，但 ResearchGate 落地頁 403 無法一手驗證，故未寫入原表既有欄位，僅列為待查。另註：OpenAlex 將第一作者額外掛上 Imperial College London，研判為機構比對錯誤，勿沿用。

---

## 五23 — Modeling of Effective Thermal Resistance in Sub-14-nm Stacked Nanowire and FinFETs

- **DOI／識別**：`10.1109/TED.2018.2863730`　**來源**：IEEE　**年**：2018
- **作者／單位**：Ishita Jain（Indian Institute of Technology Delhi, India）；共同作者 Anshul Gupta（IIT Delhi）、Terence B. Hook（IBM, United States）、Abhisek Dixit（IIT Delhi）
- **出處**：IEEE Transactions on Electron Devices，vol. 65，pp. 4238-4244，出版日 2018-08-23

**1 元件**　sub-14-nm 節點的 FinFET 與 stacked-nanowire FET (NWFET)。模型自變數明列為：鰭數（number of fins）、gate finger 數、堆疊奈米線的數量與尺寸。Lg、Hfin/Wfin、奈米線直徑、n/p、bulk/SOI 未取得（僅讀到摘要與 Section I）。

**2 方法與 SHE 定義**　`model`　以 3-D device simulation（摘要與引言用語為 calibrated 3-D TCAD simulations）為基礎，再用經驗式（empirically extracted equations）建立 effective thermal resistance 的解析模型，並在一系列元件設計變數範圍內把模型對 TCAD 做萃取比對。Section I 明確指出散熱有兩條競爭路徑——往基板背接觸（substrate back contact），以及往 gate 與 source/drain 接觸再進入 interconnect stack——並指出熱是產生在 channel-drain junction，因 SiO2 與薄矽層的低熱導而外流受阻。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance 數值 未取得（全文付費牆）。

**3 關鍵定量結果**　未取得數值。摘要僅宣稱該模型首次同時涵蓋鰭數、gate finger 數、堆疊奈米線數量與尺寸的整體影響，且適用於大型 layout 的 Rth 估算。無 Rth 絕對值、無 ΔT、無 Ion 下降 %、無偏壓條件。層級為「僅摘要 + Section I 引言」，非圖層級（圖說與模型係數皆未取得）。

**4 TCAD 校準用途**　本批對使用者潛在價值最高、但必須取得全文的一篇。它是唯一直接處理「多鰭 × 多 gate finger × 堆疊數」對 effective Rth 之集總影響的文獻，正好橋接判準帶中 single-fin Rth 約 1-4 MK/W 與多鰭多指 RF 結構約 34 kK/W 之間的落差——若取得模型係數，可直接檢查使用者 deck 從單鰭外推到多鰭 layout 時 Rth 是否落在合理量級。目前僅能取得一項結構性提示：散熱同時走基板與 gate/S-D 接觸兩路，因此 deck 若把 thermode 只設在基板底部、而 gate 與 S/D 接觸端設為絕熱，會系統性高估 Rth（即 thermode 過絕熱）。建議優先向館際或機構授權取得 IEEE TED 65(11) pp. 4238-4244 全文。

**5 批判**
   1. 無數值可判定，原因：IEEE TED 全文付費牆，僅取得摘要與 Section I，未見任何 Rth、ΔT、Ion% 數字，無法對判準帶（尤其無法驗證 single-fin 1-4 MK/W 的量級是否吻合）。
   2. 模型是 empirically extracted 的經驗擬合式而非物理推導，其外推能力受限於摘要中所稱「a range of device design variables of interest」這個未公開的取樣範圍；超出該範圍使用會失準，而範圍本身在摘要層級不可見。
   3. 驗證對象是 calibrated 3-D TCAD 模擬，不是實測 Rth。也就是說模型的準確度只保證「對得上 TCAD」；若 TCAD 自身的熱邊界（thermode 位置、接觸熱阻）過絕熱或過導熱，誤差會整包繼承進模型。摘要未提任何實驗 Rth 比對，這是引用此模型時最大的風險。
   4. FinFET 與 stacked NWFET 兩種幾何截然不同的架構共用一組經驗式，其形式一致性在摘要層級無法檢驗；且有 IBM 共同作者，幾何可能取自未公開的內部製程，重現性受限。
   5. 分類確認：本篇是 Rth 的建模研究（model），不是 ET-vs-ISO 的 Ion 退化研究；不要期待從它取得飽和區 Ion 下降百分比，也不要把它的 Rth 直接乘上功率當成 ΔT 而不檢查功率定義（是否含閘極漏電、是否為通道區域功率）。

**6 可引用性**　C（僅可當背景引用）— 以目前取得層級，摘要與引言只支撐「已提出一個涵蓋鰭數/finger 數/堆疊數的 effective Rth 模型」這句陳述；任何 Rth 數字或模型係數都必須取得全文才可引用。取得全文後有機會升為 A。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2018.2863730?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2018.2863730
   - https://ieeexplore.ieee.org/document/8444736/
   - https://www.semanticscholar.org/paper/5293c6e116c7f985c2ee1edc4368e6bcc9f679e0

**8 與原表差異**　與原表一致。原表 orig 記「sub-14nm FinFET 與堆疊奈米線 FET（含大型 layout：多鰭、多 gate finger）；Rth vs 幾何設計變數（鰭數、finger 數、奈米線堆疊數/尺寸）；適用於大 layout 之 Rth 估算」——與本次讀到的摘要逐項吻合。本次補齊：卷別 vol. 65、頁碼 4238-4244、出版日 2018-08-23、作者單位（IIT Delhi + IBM），以及 Section I 中「散熱兩條路徑：基板背接觸 vs gate/S-D 接觸進 interconnect stack」與「熱源在 channel-drain junction」的敘述。差異說明（判斷層面，非事實錯誤，故不標 CORRECTION）：原表 tcad_use 記「不適用(Rth 模型)」，本次評估認為應改為「潛在高價值但需取得全文」——因為使用者的 deck 正需要 single-fin 到多鰭 layout 的 Rth 外推依據，本篇是本批唯一直接處理該問題的文獻。

---

## 五24 — Self-heating measurement methodologies and their assessment on bulk FinFET devices

- **DOI／識別**：`10.1109/IIRW.2017.8361226`　**來源**：IEEE　**年**：2017
- **作者／單位**：P. Paliwoda（Department of Electrical and Computer Engineering, New Jersey Institute of Technology, USA）；共同作者 Z. Chbili 與 A. Kerber（GlobalFoundries, United States）、A. Gondal、D. Misra（NJIT）
- **出處**：2017 IEEE International Integrated Reliability Workshop (IIRW)，South Lake Tahoe, CA, USA，pp. 1-4

**1 元件**　bulk FinFET（標題明示 bulk；GlobalFoundries 技術）。Introduction 用語為 thin body silicon FET devices such as bulk/SOI FinFET。測試結構包含 DUT、相鄰感測 FET、相鄰 pn junction，以及 DUT 自身的 4-terminal Kelvin gate 接點。技術節點、Lg、Hfin/Wfin、n/p、鰭數、元件間距 全數未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　純 wafer-level 電性量測（無 TCAD、無 thermode 設定）。三種感測方式：(1) 以相鄰 FET 的臨界電壓 VT 作溫度計；(2) 以相鄰 pn junction 的順偏電壓 VD 作溫度計；(3) 以 DUT 自身 gate 電阻 RG 作溫度計，用 4-terminal Kelvin 接點量測 gate 的電阻溫度係數。Fig. 1 圖說明確區分 a) surround heat sensing（用鄰近 FET 的電性）與 b) local heat sensing（用 gate 的熱電阻係數）。章節為 I. Introduction / II. Experimental Setup / III. Results and Discussions / IV. Conclusion。

**3 關鍵定量結果**　原文印出數字（摘要層級）：以鄰近元件感測時，自熱被低估 35%；並確認來自本地熱源與周圍熱源的貢獻是可加成的（additive）。原文短語：self-heating is "underestimated by 35%" when sensed at a neighboring device（Paliwoda et al., IIRW 2017 摘要）。Introduction 另轉引其參考文獻 [5]，稱高遷移率材料（如 Ge）的自熱可增加超過 100%——此為轉引，非本篇量測結果。本篇無絕對 ΔT、無 Rth 數值、無偏壓條件（VGS/VDS/TA）。【不同文獻，須分開標註】同作者 P. C. Paliwoda 的 NJIT 博士論文（2018，Characterization of self-heating effects and assessment of its impact on reliability in FinFET technology）落地頁摘要記載三項可量化資訊：bulk FinFET 的橫向熱傳可及約 1 µm、SOI FinFET 約 1.5 µm；fin 熱阻在 −40 °C 至 175 °C 區間變化可達 70%；且在實際元件切換條件下 SHE 明顯低於定電壓應力條件。

**4 TCAD 校準用途**　本批對 thermode 設定最有直接指導價值的一篇。(a) 35% 低估這個數字量化了「感測點離熱源越遠、量到的溫升越低」——直接對映到 deck：thermode 若貼在離通道太遠的位置、或 SurfaceResistance 設得太小，萃取到的 ΔT 會系統性偏低，正是判準帶中「飽和 Ion 差 <1% 表示 thermode 貼太近通道、SHE 被邊界抹掉」的實驗對照面。(b) 本地與周圍熱源可加成，支持在多鰭/多指 deck 中以疊加方式估算總溫升。(c) 博論的 1 µm（bulk）/1.5 µm（SOI）橫向熱擴散距離，可直接當成 deck 模擬域側向邊界至少要留多寬的依據——若側向等溫邊界設在 1 µm 以內，等於人為導熱、抹掉 SHE。(d) 博論指出切換條件下 SHE 遠低於 DC 定壓，提醒使用者的 DC 飽和區模擬是最壞情況上界。

**5 批判**
   1. 唯一數字（35%）不是 Ion 下降 %，因此不能直接對判準帶；它屬於判準帶「熱邊界是否過導熱」那一軸的實驗證據——以此推論，任何把感測點或等溫邊界放在鄰近元件位置的設定，都會低估自熱約三分之一。若使用者的 deck 出現飽和 Ion 差 <1%，本篇正是可引用的機制性解釋。
   2. 35% 是在特定元件間距、特定 layout、特定偏壓下量到的單一數字，摘要未給間距、未給偏壓、未給誤差棒與樣本數；換一個間距這個比例就會改變，不可當成普適的修正係數使用。
   3. 三種感測法的糾纏因子各不相同且摘要未說明如何互校：VT 法會混入 BTI/trap 造成的 VT 漂移，VD 法會混入 junction leakage 的溫度相依，RG 法量到的是 gate 金屬的平均溫度而非通道峰值溫度。三者所稱的「溫度」定義並不相同，直接互比會有系統偏差。
   4. 純量測、無模擬對照，因此 35% 無法轉換成 thermode 的 SurfaceResistance 數值；只能作為方向性的 sanity-check，不能作為 deck 參數的來源。
   5. 分類確認：本篇是 Rth/ΔT 的量測方法學評估（Rth-extraction），不是 pulsed-vs-DC，也不是 ta_sweep。若使用者需要 pulsed-vs-DC 或環境溫度掃描的證據，應改引同作者的 NJIT 博士論文而非本篇——並注意兩者是不同文獻，不可混用引用。

**6 可引用性**　B（只能引用定性結論）— 35% 是摘要原文印出且語意明確的數字，但缺元件間距、偏壓與誤差資訊，作為定量錨點過於單薄；安全的用法是引用「以鄰近元件感測會低估自熱約 35%」這個半定量結論，以及「本地與周圍熱源可加成」的定性結論。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iirw.2017.8361226?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/iirw.2017.8361226
   - https://ieeexplore.ieee.org/document/8361226/
   - https://researchwith.njit.edu/en/publications/self-heating-measurement-methodologies-and-their-assessment-on-bu/
   - https://digitalcommons.njit.edu/dissertations/1389/

**8 與原表差異**　與原表一致並大幅補強。原表 orig 記「bulk FinFET (GlobalFoundries technology), wafer-level test…；no absolute dT/Rth printed in abstract；key quantified result: self-heating underestimated by 35% when sensed at a neighbo…；not verified (full text not accessed)」——本次以 IEEE Xplore 摘要頁與 NJIT researchwith 頁雙源逐字複核，35% 與「熱源可加成」皆無誤。補齊：完整作者名單與單位（NJIT + GlobalFoundries）、會議全名/地點/頁碼 1-4、四節章節結構、Fig. 1 圖說（surround vs local heat sensing 的區分）、Introduction 中轉引的「Ge 自熱可增加 >100% [5]」。新增（屬不同文獻，已分開標註）：同作者 NJIT 2018 博士論文落地頁摘要提供 bulk 1 µm / SOI 1.5 µm 橫向熱傳距離、fin 熱阻在 −40~175 °C 變化達 70%、切換條件下 SHE 遠低於定壓應力等可用於 deck 邊界設定的資訊；博論 PDF 本身被 Cloudflare 擋下（HTTP 403），僅取得落地頁摘要。原表「not verified (full text not accessed)」維持成立。

---

## 五25 — Self-heating in FinFET and GAA-NW using Si, Ge and III/V channels

- **DOI／識別**：`10.1109/IEDM.2016.7838425`　**來源**：IEEE　**年**：2016
- **作者／單位**：E. Bury（imec, Leuven, Belgium；亦掛 KU Leuven）；共同作者 B. Kaczer、D. Linten、L. Witters、H. Mertens、N. Waldron、X. Zhou、N. Collaert、N. Horiguchi、A. Spessot（imec）、G. Groeseneken（imec / KU Leuven）
- **出處**：2016 IEEE International Electron Devices Meeting (IEDM)，San Francisco, CA, USA，pp. 15.6.1-15.6.4

**1 元件**　FinFET (FF) 與 GAA nanowire (GAA-NW)，通道材料涵蓋 Si、Ge/SiGe 與 III/V 半導體。Section I 具體提到 strained Ge (s-Ge) p-FinFET 建在 SiGe Strain Relaxed Buffer (SRB) 上，並比較 STI-last 與 replacement channel 兩種整合路線（後者的優點是易於與 III/V 通道共整合）。技術節點、Lg、Hfin/Wfin、奈米線直徑、n/p、鰭數 全數未取得。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗量測與模擬並行（摘要用語為 studied experimentally and through simulations），對象是一整組 industry-relevant 的元件與多種製程分裂選項。章節為 I. Introduction / II. Thermal Properties of Alloys and Compounds / III. Experimental Setup / IV. Results / V. Conclusions——第 II 節顯示本篇有整理合金與化合物的熱性質（合金散射會大幅壓低熱導）。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、是否含 BTE/聲子模型 全數未取得。旁註：imec 團隊慣用旁置 diode/MOSFET 感測器的量測法，此點由 五21 的 Introduction 側面佐證，非本篇自述。

**3 關鍵定量結果**　未取得數值。IEDM 摘要極短（兩句），僅定性宣稱研究了 SH 並提供未來技術的管理建議。無 Rth、無 ΔT、無峰值晶格溫度、無 Ion 下降 %、無偏壓條件。層級為「僅摘要 + Section I 引言首段」；原表所述的「圖層級 dT/Rth 跨架構比較」本次連圖說都未能取得。相關待查線索：五24（Paliwoda, IIRW 2017）的 Introduction 寫道高遷移率材料如 Ge 的自熱可增加超過 100%，並標註為其參考文獻 [5]；[5] 是否即為本篇，本次未能確認，僅列為線索。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何數值、幾何或熱邊界設定。潛在價值在材料熱導的排序與絕對值：SiGe/Ge/III-V 的熱導遠低於 Si，且合金散射會進一步壓低。對使用者而言——若 deck 只做純矽 FinFET，本篇不是必要輸入；若 deck 含 SiGe S/D（p 型 FinFET 的標準做法，正對應 五21 的 n/p 熱不對稱），則本篇第 II 節 Thermal Properties of Alloys and Compounds 是取得合金熱導參數的目標來源，值得取得全文。

**5 批判**
   1. 無數值可判定，原因：IEDM 全文付費牆，摘要僅兩句且無任何數字，Section I 引言只談材料與整合選項，無法對判準帶，也無法做 ΔIon%/ΔT 交叉檢核。
   2. 橫跨 Si / Ge / III-V 與 FinFET / GAA-NW 兩個維度的比較，糾纏因子極強：通道材料同時改變熱導、遷移率、驅動電流與功率密度。若不固定功率密度做比較，Rth 或 ΔT 的差異會被驅動電流差異污染，摘要層級完全無法檢驗其比較是否公平。
   3. 「industry-relevant solutions with multiple processing options」意味元件來自 imec 內部製程分裂，元件幾何與製程細節未公開，外部無法重現；跨技術外推風險高，且無誤差棒或重複性資訊可見。
   4. IEDM 四頁格式（15.6.1-15.6.4）以圖為主，即使日後取得全文，多數 Rth/ΔT 很可能只存在於圖中而無印出數字（屬圖層級），使用者若要數字須自行讀圖，會引入判讀誤差——引用時務必標明是圖層級估讀。
   5. 分類注意：本篇不是矽 FinFET 的 ET-vs-ISO 研究，不可拿來當使用者 7-11% 飽和 Ion 下降錨點的來源；它的定位是跨通道材料與跨架構的自熱比較。

**6 可引用性**　C（僅可當背景引用）— 僅取得兩句摘要與 Section I 引言首段，只能引用「imec 於 IEDM 2016 系統性比較 Si/Ge/III-V 通道之 FinFET 與 GAA-NW 自熱」這類背景陳述；任何 Rth/ΔT 數值都不可引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iedm.2016.7838425?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/iedm.2016.7838425
   - https://ieeexplore.ieee.org/document/7838425/
   - https://ieeexplore.ieee.org/document/7838425/figures
   - https://www.semanticscholar.org/paper/3eb79fbc404f770b108cf1ef17ff8e8b1dc64b5b

**8 與原表差異**　與原表大致一致。原表 verdict 為 value_corrected、orig 記「Si (and Ge, III-V) FinFET and GAA nanowire, industry-relevant…；Figure-level dT/Rth comparisons across architectures and processing options；not accessed；not accessed (closed access)」——本次確認仍為 closed access（Semantic Scholar 與 OpenAlex 皆回報 oa_status: closed），摘要中確實無任何數值，原表判斷成立。本次補齊：完整 11 位作者名單與 imec / KU Leuven 單位、會議全名與地點 San Francisco、頁碼 15.6.1-15.6.4、五節章節結構（其中第 II 節專講合金與化合物熱性質），以及 Section I 中 strained Ge on SiGe SRB 與 STI-last / replacement channel 兩種整合選項的敘述。新增待查線索：五24 引言的「Ge 自熱可增加 >100% [5]」可能指向本篇，本次未能確認參考文獻對應關係。

---

## 五26 — Self-Heating Measurement of 14-nm FinFET SOI Transistors Using 2-D Time-Resolved Emission

- **DOI／識別**：`10.1109/TED.2016.2537054`　**來源**：IEEE　**年**：2016
- **作者／單位**：Franco Stellari（IBM Research – Thomas J. Watson Research Center；共同作者 K. A. Jenkins、A. J. Weger、B. P. Linder、Peilin Song，全部同屬 IBM Watson）
- **出處**：IEEE Transactions on Electron Devices, Vol. 63, No. 5, pp. 2016–2022

**1 元件**　14-nm 節點 FinFET，SOI 基板（摘要明示 Silicon On Insulator）。摘要指出關注對象為「large devices with dense arrays of fins」，即大面積、高鰭密度元件。Lg、Hfin、Wfin、n/p 型別、鰭數與指數：未取得（摘要僅稱評估比較多種 device geometries，具體幾何在全文與圖中，屬付費牆內）。

**2 方法與 SHE 定義**　`Rth-extraction`　純實驗光學測溫，非 TCAD 模擬。手法為 2-D time-resolved emission（TRE，時間解析光發射）自基板背面量測，以元件本身 OFF-state leakage current 的溫度相依調變當作內建溫度計，達成非侵入式、高時間解析度的 device-level 測溫。求解器／熱邊界條件／thermode 位置／SurfaceResistance／hydrodynamic 或 BTE 聲子模型：皆不適用（本文無 TCAD deck）。摘要僅稱評估比較不同 device geometries 與 operating conditions，未列偏壓表。分類說明：五選一中最接近者為 Rth-extraction，但嚴格說本文是熱量測（thermometry）而非 Rth 數值萃取，此點見 critique。

**3 關鍵定量結果**　未取得任何數值。摘要通篇無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度，亦無對應偏壓（VGS/VDS/TA）。摘要逐字片段（原文英文）：monitor the「temperature-dependent modulation of OFF-state leakage current of individual transistors」。此為方法陳述，不含數字。判定：所有溫升數值屬「僅圖層級（需自讀原圖）」，且原圖在 IEEE 付費牆內，本次未取得。Unpaywall 查證 is_oa=false、oa_status="closed"、best_oa_location=null。

**4 TCAD 校準用途**　不可直接校準，理由：本次僅取得摘要，未拿到任何 Rth、ΔT 或峰值溫度數字，無法提供 thermode SurfaceResistance 的量級，也無可比對的 ΔT 錨點。間接價值有二：(1) 若使用者日後取得全文，這是 14-nm SOI FinFET 的實測溫度基準，正好對應判準帶中「SOI 8-17%」與「single-fin Rth 約 1-4 MK/W」的實驗側錨點，是校準 SOI deck 最對口的一篇；(2) 方法學上提醒：dense fin array 的大元件熱耦合最嚴重，若使用者 deck 只模擬 single-fin 再線性外推到多鰭，會低估溫升——這是定性但可用的建模警訊。

**5 批判**
   1. 無數值可判定，原因：本次僅取得摘要層級內容，摘要未印出任何 ΔIon%、ΔT 或 Rth，無法與判準帶（bulk 3-12%／SOI 8-17%、ΔIon%÷ΔT 約 0.10-0.20 %/K、single-fin Rth 1-4 MK/W）作比對。全文與圖在 IEEE 付費牆內，Unpaywall 確認 closed，不做任何推測。
   2. 方法屬性與使用者需求錯位：本文是光學實測測溫，完全沒有電熱 vs 等溫（ET-vs-ISO）的 Ion 對照，因此即使拿到全文，也給不出使用者最需要的「飽和 Ion 下降 %」。它能校準的是溫度側（ΔT），不是電流側，使用者需自行用 ΔIon%÷ΔT≈0.10-0.20 %/K 這條交叉檢核比值把兩者接起來。
   3. 量測本身含糾纏因子：以 OFF-state leakage 當溫度計，讀到的是次臨界電流的溫度相依，而該電流同時受 DIBL、閘極漏電與 trap-assisted 成分影響；若元件在應力下有 interface trap 生成，溫度讀值會被污染。摘要未提及誤差棒、校正曲線或重複性統計，可信度無法從摘要判斷。
   4. 分類需標註：本卡 method_type 填 Rth-extraction 是五選一下的最近似歸類，實際上本文並未宣稱萃取 Rth，而是做 2-D 時間解析測溫。使用者若把本文當成 Rth 數值來源會誤用；正確定位是「溫度量測方法論 + SOI 多鰭熱耦合的定性證據」。
   5. 單一技術世代、單一基板：僅 14-nm SOI，無 bulk 對照組，無法外推到使用者若在做的 bulk FinFET deck——bulk 有基板散熱路徑，SOI 被 BOX 擋住，兩者 Rth 可差數倍，不可混用。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可引用「14-nm SOI FinFET 存在自熱可靠度疑慮、可用 2-D TRE 非侵入量測 device-level 溫度」這類定性結論與方法學，但無任何數字可引；要引數字必須先取得全文原圖。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/ted.2016.2537054
   - https://api.openalex.org/works/doi:10.1109/ted.2016.2537054?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/ted.2016.2537054
   - https://api.unpaywall.org/v2/10.1109/TED.2016.2537054

**8 與原表差異**　與原表一致。原表記載「14-nm-node SOI FinFET (IBM), silicon; multiple geometries/… figure-level only; not printed in abstract」，本次獨立查證完全吻合：摘要確實無數值、確為 IBM Watson、確為 SOI、確實稱評估多種 geometries。本次補充原表未載之書目細節：TED Vol. 63, No. 5, pp. 2016–2022, May 2016，第一作者 Franco Stellari（IBM Research – T. J. Watson）。無衝突、無錯誤。

---

## 五27 — Characterization of self-heating leads to universal scaling of HCI degradation of multi-fin SOI FinFETs

- **DOI／識別**：`10.1109/IRPS.2016.7574506`　**來源**：IEEE　**年**：2016
- **作者／單位**：Hai Jiang（Purdue University, West Lafayette；共同作者 SangHoon Shin（Purdue）、Xiaoyan Liu（Peking University, Institute of Microelectronics）、Xing Zhang（Peking University）、Muhammad Ashraful Alam（Purdue，通訊作者角色））
- **出處**：2016 IEEE International Reliability Physics Symposium (IRPS), pp. 2A-3-1–2A-3-7

**1 元件**　Multi-fin SOI FinFET，並在論述上涵蓋 gate-all-around (GAA) 拓樸；摘要明示技術定位為 sub-14 nm 節點的候選選項。鰭數 Nfin 為明確的實驗分裂變數（fin-count series）。節點實際值、Lg、Hfin、Wfin、堆疊數、n 或 p 型別：未取得（摘要未列，元件表在全文內，付費牆）。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗 + 緊湊模型併行，非 TCAD 數值元件模擬。(1) 熱阻萃取：以 AC conductance method（交流電導法）萃取 self-heating 特性並驗證模型。(2) 建模：提出 physics-based thermal circuit compact model（物理基礎熱電路緊湊模型）描述 multi-fin SOI FinFET 的熱耦合。(3) 可靠度分析：掃 fin 數（Nfin）、chuck 溫度（Tsub）、AC 應力頻率（f）三個變數看 HCI 劣化。摘要給出的結構式關係為 TL = g(NFIN, Tsub, f) 與 ΔVth(TL) = f(S(TL) × t)，並以 Si-O bond-dispersion model 解釋通用曲線。求解器（Sentaurus/GARAND）、熱邊界條件、thermode 位置與 SurfaceResistance、hydrodynamic/BTE：皆未取得，且本文性質為熱電路模型而非 FEM/drift-diffusion deck，預期原文亦無 thermode 設定。

**3 關鍵定量結果**　未取得數值。摘要無 Rth 數值、無 ΔT 數值、無 Ion 下降 %、無峰值晶格溫度，亦無對應偏壓。摘要逐字片段（原文英文）指出成因為「narrow gate geometry and reduced gate pitch suppress heat dissipation and increase thermal cross-talk」。可取得的是結構性結論而非數字：晶格溫度 TL 為 (Nfin, Tsub, f) 的函數，且 HCI 劣化對這三個變數的相依性可摺疊到單一 universal degradation curve。判定：所有 Rth 與 TL 數值屬「僅圖層級（需自讀原圖）」，本次未取得。Unpaywall 確認 is_oa=false、oa_status="closed"。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何 Rth 或 ΔT 數字，給不出 thermode SurfaceResistance 量級。但有三項結構性可用價值：(1) 熱電路拓樸——本文主張 multi-fin 的熱耦合可用集總熱電路描述，使用者若要把 single-fin TCAD 結果外推到多鰭，應採「單鰭自熱阻 + 鰭間耦合熱阻」的網路而非簡單除以鰭數；(2) 交叉檢核靶——Rth 應隨 Nfin 次線性下降（熱串音使每鰭散熱效率降低），使用者可拿自家 deck 掃 fin 數驗證是否重現此趨勢，這是不需要原文數字就能做的 sanity-check；(3) 邊界條件警訊——摘要明言 sub-14 nm 的 narrow gate 與 reduced gate pitch 抑制散熱，若使用者 deck 掃出 Rth 隨節點微縮反而下降，代表熱邊界設得過導熱。

**5 批判**
   1. 無數值可判定，原因：僅取得摘要，摘要未印出任何 Rth（MK/W）、ΔT 或 ΔIon% 數字，無法對照判準帶的 single-fin Rth 1-4 MK/W 或 SOI 8-17% Ion 下降區間。全文閉鎖（Unpaywall closed），不從標題或期刊推測數值。
   2. 本文的 SHE 指標是 ΔVth／HCI 劣化，不是飽和 Ion 下降，與使用者的 TCAD 目標量不同軸：即使取得全文，拿到的是 Rth 與 TL，仍需經由 ΔIon%÷ΔT≈0.10-0.20 %/K 才能接回使用者的 Ion 判準帶，中間隔了一層轉換假設。
   3. 含明顯糾纏因子：HCI 劣化同時受熱（TL 上升）與載子能量（Vd 相依的 hot-carrier 能譜）驅動，而掃 Nfin 會同時改變 Rth 與元件總功率。摘要宣稱三變數可摺疊成 universal curve，這個「摺疊成功」本身即是把糾纏因子歸因到單一 TL 的強假設；Si-O bond-dispersion model 是機制詮釋而非獨立驗證，需在全文檢視其擬合自由度。
   4. AC conductance 法的固有偏誤未在摘要交代：該法量到的是特定頻率窗內的熱時間常數，對 BOX 以下的慢速熱路徑（基板擴散）可能系統性漏計，導致 Rth 被低估；摘要無誤差棒、無重複性統計、無與獨立測溫法（如五26 的光學法）交叉驗證的說明。
   5. SOI 專屬，不可外推 bulk：BOX 阻斷向下散熱是本文熱串音敘事的前提；使用者若做 bulk FinFET，鰭底直通基板的散熱路徑會使 Rth 與 Nfin 相依性顯著減弱，本文趨勢不可直接移植。

**6 可引用性**　B（只能引用定性結論）— 僅摘要層級，可引用其定性與結構性結論（multi-fin SOI 熱串音嚴重、TL 為 Nfin/Tsub/f 的函數、HCI 劣化可摺疊為 universal curve、提出熱電路緊湊模型），但 Rth 與溫升數值一律不可引，需取得全文原圖後才可升為 A。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/irps.2016.7574506
   - https://api.openalex.org/works/doi:10.1109/irps.2016.7574506?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/irps.2016.7574506
   - https://api.unpaywall.org/v2/10.1109/IRPS.2016.7574506

**8 與原表差異**　與原表一致。原表記載「Multi-fin SOI FinFETs (sub-14 nm class), fin-count series；fin-count-dependent lattice temperature rise (values figure-level, not in accessed text)；HCI stress bias; Tsub and AC frequency swept; exact values not in accessed material」，本次獨立查證逐項吻合：摘要確實提及 sub-14 nm、確實掃 Nfin/Tsub/f、確實無數值。本次補充原表未載之細節：第一作者 Hai Jiang 單位為 Purdue University（非 Peking University，通訊者 M. A. Alam 亦在 Purdue，Xiaoyan Liu 與 Xing Zhang 才是北大），頁碼 2A-3-1–2A-3-7，並補上摘要中的結構式 TL = g(NFIN, Tsub, f) 與 Si-O bond-dispersion model。無衝突、無錯誤。

---

## 五28 — Self-heating on bulk FinFET from 14nm down to 7nm node

- **DOI／識別**：`10.1109/IEDM.2015.7409678`　**來源**：IEEE　**年**：2015
- **作者／單位**：Doyoung Jang（imec；共同作者 E. Bury（imec / KU Leuven）、R. Ritzenthaler、M. Garcia Bardon、T. Chiarella、K. Miyaguchi、P. Raghavan、A. Mocuta、G. Groeseneken（imec / KU Leuven）、A. Mercha、D. Verkest、A. Thean，主體皆為 imec）
- **出處**：2015 IEEE International Electron Devices Meeting (IEDM), pp. 11.6.1–11.6.4

**1 元件**　Bulk FinFET（摘要標題與內文皆明示 bulk），涵蓋 14nm → 10nm → 7nm 三個節點，依 typical 0.7x scaling 逐代微縮。通道材料含 Si-channel 與 strained Ge-channel 兩種分裂。摘要明示微縮伴隨 increased number of fins（鰭數隨節點增加）。Lg、Hfin、Wfin、確切鰭數、n 或 p 型別：未取得（元件表在全文內，付費牆）。

**2 方法與 SHE 定義**　`model`　3D FEM（三維有限元素）電熱模擬為主，並有 experimental measurements 作驗證（摘要明示 based on 3D FEM simulations and experimental measurements）。分析鏈延伸至 AC circuit benchmark，把元件層熱行為傳遞到電路層效能評估。緩解手段評估兩項：reducing capacitances（降低達成目標效能所需驅動電流）與 fin depopulation（減鰭）。具體求解器名稱（Sentaurus/GARAND/自研）、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic/BTE/聲子模型：全部未取得，摘要僅稱 3D FEM。註：本文為 FEM 熱模擬，其熱邊界設定正是使用者最需要的資訊，但恰在付費牆內。

**3 關鍵定量結果**　本批唯一在摘要即印出數字者，以下三個數值為「原文（摘要）印出數字」，非圖層級推讀：(1) 熱侷限隨節點微縮的增幅——摘要逐字片段（原文英文）：「heat confinement is expected increase by 20% Si-channel FinFETs and another 57%」（後接 by strained Ge-channel），即每代 0.7x 微縮，Si 通道熱侷限增約 20%，strained Ge 通道再額外增約 57%；(2) 電路層衝擊——摘要載明 AC circuit benchmark 上約 5%（≈5%）performance variation，適用對象為 high performance devices，成因歸為 device scaling 與鰭數增加。重要界定：上述 20% / 57% 是 heat confinement（熱侷限，即熱阻／溫升側）的增幅，不是 ΔIon%；≈5% 是 AC 電路效能變異，不是 DC 飽和 Ion 下降。本文未在摘要給出 Rth 絕對值（MK/W）、ΔT（K）、峰值晶格溫度或對應偏壓（VGS/VDS/TA），這些一律屬「僅圖層級（需自讀原圖）」且本次未取得。Unpaywall 確認 is_oa=false、oa_status="closed"。

**4 TCAD 校準用途**　本批對使用者 deck 最有價值的一篇，但只能提供「相對趨勢靶」而非絕對值。可用之處：(1) 節點微縮的熱阻標定——若使用者要從 14nm deck 外推到 10nm/7nm，本文給出可直接套用的量化錨點：每代 0.7x 微縮，Si 通道熱侷限約 +20%。使用者可掃自家 deck 的節點序列，檢查 Rth 增幅是否落在此量級；明顯低於 20% 代表 thermode 貼太近或熱邊界過導熱，明顯高出則可能過絕熱。(2) 幾何對齊——bulk FinFET、14/10/7nm、鰭數隨節點增加，與使用者的矽 FinFET 設定同軸，是本批中幾何最對得上的一篇。(3) 電路層 sanity-check——元件層自熱最終在 AC benchmark 只造成約 5% 效能變異，可用來檢查使用者是否把元件層 SHE 誇大到不合理的電路衝擊。不可用之處：無法提供 thermode SurfaceResistance 的絕對量級（無 MK/W 數值），也無 ET-vs-ISO 的 Ion 對照，故無法直接驗證 7-11% 的 Ion 下降錨點。

**5 批判**
   1. 數字無法用判準帶直接判定（既非帶內亦非帶外），原因：本文摘要印出的 20% / 57% 是 heat confinement 增幅（熱側相對量），≈5% 是 AC circuit performance variation（電路層），三者都不是判準帶所定義的「電熱 vs 等溫的飽和 Ion 下降 %」。判準帶（bulk 3-12%）與交叉比值（ΔIon%÷ΔT 0.10-0.20 %/K）需要 ΔIon% 與 ΔT 的絕對值，而本文摘要兩者皆未給，故僅能判定「與判準帶不同量綱，不可混用」。
   2. ≈5% 的電路層變異與元件層自熱不可畫等號，是本文最易被誤引之處：AC 操作下工作週期低、熱時間常數平均化，電路層看到的溫升遠低於 DC 飽和態。若使用者拿 5% 去對照自己 DC 電熱模擬的 Ion 下降（判準帶 7-11%），會誤判自家 deck 過熱——兩者物理情境不同，不構成矛盾。
   3. strained Ge 通道是明確的糾纏因子：額外 57% 的熱侷限增幅同時混入了 Ge 本身遠低於 Si 的熱導率、以及應變層／異質界面的熱邊界阻抗，並非單純幾何微縮效應。使用者做純矽 FinFET，只能取 Si-channel 的 20%，Ge 的 57% 必須剔除，不可相加使用。
   4. 關鍵的 FEM 熱邊界設定未取得，而這正是自熱模擬結論的最大敏感源：3D FEM 的基板底部溫度固定面位置、接觸熱阻、STI 與 BEOL 是否納入，會直接決定 20% 這個增幅。摘要未交代任何邊界條件，也未給誤差棒或網格收斂性說明，因此 20% 應視為「該團隊特定邊界設定下的結果」，而非普適常數。
   5. 分類提醒：本文是 model（FEM 模擬 + 實驗驗證）而非 ET-vs-ISO 對照，也不是 ta_sweep。其「節點掃描」是改幾何不是改環境溫度，這點分類正確；但使用者若把「熱侷限 +20%」誤讀成「Ion 再降 20%」則是量綱錯誤，屬本卡最需要防範的誤用。
   6. imec 單一平台、單一模擬流程：三個節點皆為同團隊同一套 FEM 假設下的外推投影（7nm 在 2015 年尚屬預測性節點），缺乏跨機構獨立複現，外推可信度受限於該假設鏈的一致性。

**6 可引用性**　A（可直接引用數字）— 摘要本身即印出可直接引用的數字（每代 0.7x 微縮 Si 通道熱侷限 +20%、strained Ge 額外 +57%、AC circuit benchmark 約 5% 效能變異），本次已逐字讀到且經 OpenAlex 逐字重建與 Crossref 書目雙重確認，可直接引用。惟引用時務必標明量綱為「heat confinement 增幅」與「AC 電路效能變異」，不得改述為 Ion 下降 %；Rth/ΔT 絕對值仍不可引（未取得）。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/iedm.2015.7409678
   - https://api.openalex.org/works/doi:10.1109/iedm.2015.7409678?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/iedm.2015.7409678
   - https://api.unpaywall.org/v2/10.1109/IEDM.2015.7409678

**8 與原表差異**　與原表一致。原表記載「Bulk Si (and strained-Ge) FinFET, 14nm/10nm/7nm nodes；Heat confinement increases ~20% per 0.7x node scaling for Si channel, and an additional ~57% for strained-Ge channel (ab…)；not accessed (closed access)」，本次獨立查證完全吻合：20% / 57% 確為摘要印出、確為 bulk、確涵蓋 14/10/7nm、確認 closed access（Unpaywall is_oa=false）。本次補充原表未載之項目：摘要另有 AC circuit benchmark ≈5% performance variation 一項數值（原表被刪節號截斷未載），以及書目細節 IEDM 2015, pp. 11.6.1–11.6.4，第一作者 Doyoung Jang（imec）。此為補充非衝突，無 CONFLICT、無 CORRECTION。

---

## 五29 — Investigation of Self-Heating Effect on Hot Carrier Degradation in Multiple-Fin SOI FinFETs

- **DOI／識別**：`10.1109/LED.2015.2487045`　**來源**：IEEE　**年**：2015
- **作者／單位**：Hai Jiang（Peking University, Institute of Microelectronics；共同作者 Xiaoyan Liu（北大）、Nuo Xu（UC Berkeley / Samsung, United States）、Yandong He（北大）、Gang Du（北大）、Xing Zhang（北大））
- **出處**：IEEE Electron Device Letters, Vol. 36, No. 12, pp. 1258–1260

**1 元件**　Multiple-fin SOI FinFET，鰭數（fin number）為明確分裂變數，含不同 fin number 的元件序列。技術節點、Lg、Hfin、Wfin、n 或 p 型別、指數：未取得（LED 為短篇 letter，元件表在全文內，付費牆）。註：摘要僅稱 silicon-on-insulator (SOI) FinFETs，未指明通道型別。

**2 方法與 SHE 定義**　`Rth-extraction`　純實驗，非 TCAD 模擬。(1) 熱阻萃取：以 ac conductance method（交流電導法）萃取不同鰭數 SOI FinFET 的熱阻 Rth——此為本文與使用者最相關的一環。(2) 可靠度應力：對閘極與汲極同時施加 DC 與 AC 應力、源極接地，量測 HCD（hot carrier degradation）；掃 AC 應力頻率。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、hydrodynamic/BTE 聲子模型：皆不適用（本文無模擬 deck）。

**3 關鍵定量結果**　僅取得一個明確數值，且為「原文（摘要）印出數字」：AC 應力頻率高於 10 MHz 時自熱影響被抑制（摘要明載 above 10 MHz）。Rth 絕對值、ΔT、峰值晶格溫度、Ion 下降 % 與對應偏壓（VGS/VDS/TA）：全部未取得，屬「僅圖層級（需自讀原圖）」。定性結論部分，摘要逐字片段（原文英文）：「the device with large fin number demonstrates high-temperature rise caused by SHE」，並指出此溫升導致 oxide bulk trapped charges 生成增加、使 HCD 顯著惡化。Unpaywall 未針對本 DOI 單獨查詢，但 Semantic Scholar 回報 openAccessPdf 不可得、abstract 遭出版者 elided，判定為付費牆內。

**4 TCAD 校準用途**　不可直接校準，理由：未取得 Rth 絕對值（MK/W）與 ΔT 數字，無法設定 thermode SurfaceResistance 量級。可用的間接價值：(1) 趨勢靶——Rth 隨鰭數變化的實測曲線是本文核心產出，使用者可用自家 deck 掃 fin 數並檢查是否重現「鰭數越多、溫升越高」的方向性；注意此結論的物理前提是多鰭共用受限散熱路徑，SOI 的 BOX 是關鍵。(2) 熱時間常數錨點——10 MHz 這個自熱抑制門檻可反推熱時間常數量級約次微秒級，使用者若在 deck 中做暫態自熱或 pulsed-IV 比對，可用此門檻檢查暫態熱容設定是否合理；這是本文少數可跨用到 TCAD 的定量資訊。(3) 反面警示——若使用者 deck 掃鰭數時 Rth 幾乎不變，代表 thermode 貼太近通道或鰭間熱耦合未被建模。

**5 批判**
   1. 無數值可判定（就 Ion 判準帶而言），原因：摘要唯一印出的數字是 10 MHz 頻率門檻，未給 ΔIon%、ΔT 或 Rth 絕對值，因此無法對照 bulk 3-12%／SOI 8-17% 的 Ion 下降帶，也無法計算 ΔIon%÷ΔT≈0.10-0.20 %/K 的交叉檢核比值，更無法與 single-fin Rth 1-4 MK/W 比對。全文付費牆內，不作推測。
   2. 目標量與使用者不同軸：本文的觀測量是 HCD 引起的 ΔVth／trapped charge，不是飽和 Ion 下降。自熱在此是 HCD 的加速因子，不是被量測的對象本身；即使取得全文，也拿不到 ET-vs-ISO 的 Ion 對照，仍需經溫度轉換才能接回使用者的 deck。
   3. 含糾纏因子且方向相反：溫度上升同時會加速 trap 生成（惡化 HCD）但降低載子平均自由程與碰撞游離率（減緩 hot-carrier 注入），兩者相消。摘要僅報告淨惡化，未交代如何拆分熱效應與載子能量效應；掃鰭數又同時改變總功率與 Rth，單一實驗分裂難以去耦。
   4. ac conductance 法對慢速熱路徑可能系統性低估 Rth：該法量到的熱阻對應特定頻率窗內的熱響應，透過 BOX 向基板的慢速擴散分量易被漏計。摘要無誤差棒、無重複性統計、亦無與獨立測溫法交叉驗證的敘述，Rth 的絕對準確度無從從摘要判斷。
   5. SOI 專屬結論，不可外推 bulk：鰭數相依的溫升敘事以 BOX 阻斷向下散熱為前提。使用者若做 bulk FinFET，鰭底直通基板，Rth 對鰭數的敏感度會明顯減弱，本文趨勢的斜率不可直接移植。
   6. 與五27 高度重疊且為同一作者群（Hai Jiang、Xiaoyan Liu、Xing Zhang）：五29（LED 2015）與五27（IRPS 2016）在元件、方法（ac conductance 萃 Rth）、結論（多鰭高溫升惡化 HCI）上構成同一研究線的前後作，兩篇不可當作獨立證據互相佐證，引用時應併述以免造成證據重複計數。

**6 可引用性**　B（只能引用定性結論）— 僅摘要層級。可引用其定性結論（多鰭 SOI FinFET 鰭數越多自熱溫升越高、SHE 顯著惡化 HCD、以 ac conductance 法萃取 Rth）以及唯一印出的 10 MHz 自熱抑制門檻；Rth 與 ΔT 的具體數值一律不可引，需取得全文原圖後才可升為 A。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/led.2015.2487045
   - https://api.openalex.org/works/doi:10.1109/led.2015.2487045?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/led.2015.2487045

**8 與原表差異**　與原表一致。原表記載「Multiple-fin SOI FinFETs (fin-number split)；higher T rise at larger fin number (numeric values figure-level, not in accessed text)；HCD stress bias; exact values not in accessed material」，本次獨立查證逐項吻合。本次補充原表未載之項目：摘要印出 AC 應力頻率高於 10 MHz 時自熱影響被抑制（此為可引用的數值，原表未載），以及書目細節 IEEE Electron Device Letters, Vol. 36, No. 12, pp. 1258–1260, Dec 2015，第一作者 Hai Jiang（北京大學微電子研究院）。此為補充非衝突，無 CONFLICT、無 CORRECTION。

---

## 五30 — Thermal behavior of self-heating effect in FinFET devices acting on back-end interconnects

- **DOI／識別**：`10.1109/IRPS.2015.7112696`　**來源**：IEEE　**年**：2015
- **作者／單位**：C. W. Chang（台積電 TSMC, Taiwan；共同作者 S. E. Liu、B. L. Lin、C. C. Chiu、Y.-H. Lee、K. Wu，全部同屬 TSMC）
- **出處**：2015 IEEE International Reliability Physics Symposium (IRPS), pp. 2F.6.1–2F.6.5

**1 元件**　FinFET 元件（摘要僅稱 FinFET devices 並與 planar devices 對比，未明示 bulk 或 SOI，亦未指明技術節點）。核心受測體其實是後段（back-end）互連結構：含不同金屬層的 metal sensors 測試結構，以及可調整的 powered devices 數量。Lg、Hfin、Wfin、堆疊數、n 或 p 型別、鰭數：未取得。註：原表記為「先進 bulk FinFET 技術（TSMC）」，其中 bulk 一項本次無法從摘要獨立驗證，見 diff_note。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗 + FEM 併行。(1) 實驗：設計、製造並量測含不同金屬層 metal sensors 的測試結構——以金屬電阻的溫度係數當作各層溫度計，量測 back-end 各金屬層的溫升。(2) 模擬：建立 computer-aided finite element model（有限元素模型）配合分析。評估項目三類：溫度隨 powered devices 數量的飽和行為、不同金屬層的溫升差異、以及 SHE 與 joule heating 併存時的耦合效應（coupling effect）。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、hydrodynamic/BTE 聲子模型：皆未取得。分類說明：五選一中最接近者為 Rth-extraction，但本文實為 back-end 溫度場量測，並未宣稱萃取元件級 Rth，見 critique。

**3 關鍵定量結果**　未取得任何數值。摘要通篇無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度，亦無對應偏壓（VGS/VDS/TA）或功率條件。可取得者僅定性結論，摘要逐字片段（原文英文）：「the contribution of SH effect would change with joule heating」，即 SHE 的貢獻度會隨 joule heating 程度而改變（兩者非簡單相加，存在耦合）。另摘要定性指出 fin 結構較 planar 產生更多熱、並影響互連可靠度。判定：溫度飽和曲線、各金屬層溫升等所有數值均屬「僅圖層級（需自讀原圖）」，本次未取得。

**4 TCAD 校準用途**　不可直接校準，理由：本文的觀測平面在 BEOL 金屬層而非通道，未取得任何元件級 Rth、ΔT 或 Ion 數值，無法提供 thermode SurfaceResistance 量級，也無可對齊的鰭幾何。唯一具建模啟示的一點是邊界條件的方向性：本文顯示熱會沿 back-end 金屬層向上傳導並在各層產生可量測溫升，代表 BEOL 是實際存在的散熱路徑之一。使用者若在 deck 中把元件上方直接設為絕熱（不建 BEOL、不給上方熱阻），會系統性高估通道溫升與 Ion 下降；反之若在閘極正上方貼一個低熱阻 thermode 取代 BEOL，則會抹掉自熱。本文可作為「上方熱路徑必須存在但不可過導熱」的定性依據，屬 sanity-check 等級，非數值校準。

**5 批判**
   1. 無數值可判定，原因：僅取得摘要，摘要未印出任何 ΔIon%、ΔT、Rth 或功率數值，無法對照判準帶（bulk 3-12%／SOI 8-17%）、交叉比值（0.10-0.20 %/K）或 Rth 區間（single-fin 1-4 MK/W；多鰭多指 RF 約 34 kK/W）。全文在 IEEE 付費牆內，不作推測。
   2. 研究平面與使用者需求錯位，是本卡最重要的判斷：本文關心的是 back-end interconnect 的可靠度風險（電遷移等），觀測量是金屬層溫度，不是通道飽和電流。它回答不了「SHE 讓飽和 Ion 掉多少」，對使用者的 TCAD 目標量只有間接的邊界條件啟示。
   3. 含明確糾纏因子且作者本人承認：SHE 與 joule heating（互連本身通電產生的焦耳熱）在測試結構中同時存在且相互耦合，摘要明言 SHE 貢獻度會隨 joule heating 改變。這代表 metal sensor 讀到的溫升無法乾淨歸因於元件自熱，任何從本文取出的溫度數字都是兩種熱源的混合值，不可當作純 SHE 錨點。
   4. 分類需標註：本卡 method_type 填 Rth-extraction 是五選一下的最近似歸類，實際上本文並未萃取元件級熱阻，而是量測 BEOL 溫度場並觀察其隨 powered device 數量的飽和。使用者若把本文當成 Rth 數值來源會誤用。另需注意「溫度隨 powered devices 數量飽和」是熱源密度掃描，不是 ta_sweep（改環境溫度），此處分類無誤但兩者易混。
   5. 元件資訊缺失使外推能力受限：摘要未指明節點、未指明 bulk 或 SOI、未給鰭幾何，僅有 FinFET vs planar 的定性對比。缺乏這些前提，本文的溫升結論無法對應到使用者的特定幾何，也無法判斷其熱邊界是否與使用者 deck 可比。
   6. 無誤差棒與重複性資訊：metal sensor 測溫需仰賴各金屬層電阻溫度係數的獨立校正，而不同層線寬、厚度與周圍介電環境不同，校正誤差可能隨層數放大。摘要未交代校正程序、量測不確定度或多晶圓重複性。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用。本次僅取得摘要且無任何數值，加上研究平面在 BEOL 互連而非通道電流，與使用者「SHE 對飽和 Ion 影響」的主題只有間接關聯。適合在論文引言中作為「FinFET 自熱會外溢影響後段互連可靠度、且與 joule heating 耦合」的背景引證，不宜作為元件層論據或數值來源。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/irps.2015.7112696
   - https://api.openalex.org/works/doi:10.1109/irps.2015.7112696?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/irps.2015.7112696

**8 與原表差異**　與原表大致一致，但有一項無法獨立驗證需標註。一致部分：原表記載「摘要無數值；內容涵蓋隨供電元件數的溫度飽和、各金屬層溫升、SHE 與 Joule heating 耦合效應；摘要未給；全文未讀」，本次逐項吻合——摘要確實無數值，且確實明載 temperature saturation with number of powered devices、rising in different metal layer、以及 SHE 與 joule heating 的 coupling effect。需標註部分：原表記為「先進 bulk FinFET 技術（TSMC）」，但本次讀到的摘要只稱 FinFET devices 並與 planar 對比，未明示 bulk 亦未給節點；TSMC 單位已由 OpenAlex 作者機構欄獨立確認無誤，惟 bulk 一項本次無法驗證，列為未驗證項而非 CONFLICT（原表可能來自全文或其他佐證）。本次補充書目細節：IRPS 2015, pp. 2F.6.1–2F.6.5, April 2015，第一作者 C. W. Chang（TSMC）。

---

## 五31 — Self-heating effect in FinFETs and its impact on devices reliability characterization

- **DOI／識別**：`10.1109/IRPS.2014.6860642`　**來源**：IEEE　**年**：2014
- **作者／單位**：S. E. Liu（台積電 TSMC, Taiwan；共同作者 J. S. Wang、Y. R. Lu、D. S. Huang、C. F. Huang、W. H. Hsieh、J. H. Lee、Y. S. Tsai、J. R. Shih、Y.-H. Lee、K. Wu，全部同屬 TSMC）
- **出處**：2014 IEEE International Reliability Physics Symposium (IRPS), pp. 4A.4.1–4A.4.4

**1 元件**　FinFET（摘要未明示節點，亦未明示 bulk 或 SOI；作者群為 TSMC 量產技術團隊）。摘要明確涉及 layout dependence——建立了 layout dependent SHE 的經驗模型，代表元件分裂含不同佈局／鰭數／指數配置。Lg、Hfin、Wfin、n 或 p 型別、鰭數、平面對照組：未取得。註：原表記為「Production FinFET (16nm-class, bulk) vs planar reference」，其中 16nm-class、bulk、planar 對照三項本次無法從摘要獨立驗證，見 diff_note。

**2 方法與 SHE 定義**　`model`　實驗量測 + 經驗建模，非 TCAD 元件模擬。核心產出為 an empirical model for layout dependent SHE（佈局相依自熱的經驗模型）。應用面涵蓋三種可靠度量測：BTI（含 NBTI 回復效應）、HCI、TDDB。方法學建議兩項去除 SHE 干擾的手段：改用 VTshift 作為指標，或採用 μs-delay measurement system（微秒延遲量測系統）以避開自熱造成的回復假象。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、hydrodynamic/BTE 聲子模型：皆不適用／未取得（本文為經驗模型而非數值 deck）。

**3 關鍵定量結果**　僅取得一組明確的偏壓建議數值，為「原文（摘要）印出數字」：HCI 應力條件建議 Vg = 0.6~0.8 Vd。摘要逐字片段（原文英文）：「Vg= 0.6~0.8Vd is suggested」，用意是在合理功率與貼近實際操作邊際之間取得平衡，避免高汲極應力偏壓造成高功率而顯著低估元件壽命。Ion 下降 %、Rth、ΔT、峰值晶格溫度：全部未取得，屬「僅圖層級或全文限定」，本次未取得。另兩項定性結論：NBTI 特性中的 recovery effect 對自熱敏感；TDDB 的汲極偏壓相依特性同樣會因 SHE 存在而低估壽命，需仔細校正才能外推到常用操作偏壓。誠實標註：本篇摘要經 OpenAlex inverted-index 逐字重建後，中段句子有明顯的詞序破碎（如 high power 一句語法不完整），故除上述 Vg = 0.6~0.8Vd 外，不從破碎段落提取任何額外主張。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何 Rth、ΔT 或 Ion 數值，無法提供 thermode SurfaceResistance 量級，也無可對齊的鰭幾何或 ET-vs-ISO 對照。可用的間接價值有二：(1) 偏壓條件設定——Vg = 0.6~0.8 Vd 這個建議，對使用者規劃 TCAD 掃描點有實務意義：在飽和區研究 SHE 時，若把 VGS 設得遠低於此範圍（接近臨界），功率過低導致自熱被稀釋、Ion 差可能掉到 1% 以下而誤判為 thermode 貼太近；反之過高則進入非典型高功率區。此範圍可作為「自熱效應可觀測且不失真」的偏壓窗參考。(2) 佈局相依性——本文主張 SHE 具 layout dependence 並可經驗建模，提醒使用者 single-fin deck 的 Rth 不可線性外推到多鰭多指佈局，需另建佈局修正。

**5 批判**
   1. 無數值可判定，原因：摘要唯一印出的數字是應力偏壓建議 Vg = 0.6~0.8 Vd，屬量測條件而非結果量。摘要未給 ΔIon%、ΔT 或 Rth，無法對照判準帶（bulk 3-12%）、交叉比值（0.10-0.20 %/K）或 Rth 區間（single-fin 1-4 MK/W）。全文在 IEEE 付費牆內，不作推測。
   2. 目標量與使用者不同軸：本文研究的是「SHE 如何污染可靠度量測（BTI/HCI/TDDB）」，即把自熱當成量測誤差源來排除，而非把自熱對飽和 Ion 的影響當成研究對象。對使用者的 TCAD deck 而言，本文提供的是量測方法學與偏壓窗，不是可校準的物理數值。
   3. 本篇摘要的 inverted-index 重建品質不佳，是本卡的方法論風險：中段出現語法破碎（詞序遺失），代表 OpenAlex 的索引還原不完全。因此僅採信結構完整且與原表既有記載相互印證的 Vg = 0.6~0.8Vd 一項；其餘破碎段落不引用、不推論。若要引用本文任何細節，強烈建議取得 IEEE 原文核對。
   4. 經驗模型的外推性受限且含糾纏因子：layout dependent SHE 的經驗模型繫於 TSMC 該特定製程的 BEOL 堆疊、STI 深度與熱導率，換製程即需重新擬合。且 BTI 的 recovery、HCI 的載子能量效應、TDDB 的電場加速本身都與溫度耦合，摘要未交代如何把純熱貢獻與這些機制拆開。
   5. 元件資訊全缺：摘要未指明節點、未指明 bulk 或 SOI、未給鰭幾何或對照組配置，使本文的結論無法對應到使用者的特定幾何，也無法判斷可比性。原表所載的 16nm-class／bulk／planar reference 三項本次均無法獨立驗證。
   6. 無誤差棒與重複性資訊：摘要未提及量測不確定度、樣本數或跨晶圓重複性；對一篇主張「壽命可能被顯著低估」的可靠度論文而言，缺乏統計描述會削弱其量化主張的強度（惟此判斷限於摘要層級，全文可能有交代）。

**6 可引用性**　B（只能引用定性結論）— 僅摘要層級。可引用其定性結論（SHE 會干擾 BTI/HCI/TDDB 可靠度量測並可能顯著低估壽命、NBTI recovery 對自熱敏感、SHE 具佈局相依性可經驗建模、建議以 μs-delay 量測或改用 VTshift 指標規避）以及印出的 Vg = 0.6~0.8 Vd 應力條件建議。Rth/ΔT/Ion 數值一律不可引。降級提醒：摘要重建有詞序破碎，引用前建議核對 IEEE 原文。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/irps.2014.6860642
   - https://api.openalex.org/works/doi:10.1109/irps.2014.6860642?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/irps.2014.6860642

**8 與原表差異**　與原表一致，另有三項無法獨立驗證需標註。一致部分：原表記載「Abstract recommends HCI stress condition Vg = 0.6~0.8Vd to keep power/temperature reasonable (abstra…)」與「Not printed in abstract; dT numbers remain full-text-only — do not quote until read」，本次獨立查證完全吻合——摘要確實印出 Vg = 0.6~0.8Vd 的建議，且確實無任何 dT 數值。原表「不要在讀到全文前引用 dT」的告誡本次予以維持。需標註部分：原表記為「Production FinFET (16nm-class, bulk) vs planar reference」，但本次讀到的摘要未提及節點、未提及 bulk/SOI、未提及 planar 對照組，此三項本次無法驗證，列為未驗證項而非 CONFLICT（原表可能源自全文）。本次補充書目細節：IRPS 2014, pp. 4A.4.1–4A.4.4, June 2014，第一作者 S. E. Liu（TSMC），作者共 11 人全屬 TSMC。

---

## 五32 — Experimental validation of self-heating simulations and projections for transistors in deeply scaled nodes

- **DOI／識別**：`10.1109/IRPS.2014.6861186`　**來源**：IEEE　**年**：2014
- **作者／單位**：E. Bury（imec / imec the Netherlands；共同作者 B. Kaczer、P. Roussel、R. Ritzenthaler（imec）、K. Raleva（Ss. Cyril and Methodius University in Skopje）、D. Vasileska（Arizona State University）、G. Groeseneken（imec））
- **出處**：2014 IEEE International Reliability Physics Symposium (IRPS), pp. XT.8.1–XT.8.6

**1 元件**　關鍵區分：實測對象為 planar 元件（摘要明示 assess self-heating in planar devices），涵蓋 fully-depleted (FD) 架構與 FD SOI（Silicon-on-Insulator）技術脈絡；FinFET 部分僅為未來節點的投影展望，非實測。技術節點、Lg、Hfin、Wfin、堆疊數、n 或 p 型別、鰭數：全部未取得（摘要未列）。

**2 方法與 SHE 定義**　`Rth-extraction`　三段式：(1) 量測——提出一套自熱量測技術（摘要稱 a unique measurement technique for self-heating），用於評估 planar 元件的自熱；(2) 驗證——將量測結果與 finite-element simulations（有限元素模擬）比對驗證，此即標題所稱的 experimental validation；(3) 投影——對後續 FinFET 節點提出展望。共同作者 K. Raleva 與 D. Vasileska 的研究專長為元件級熱輸運與電熱蒙地卡羅／聲子模型，故全文可能含較細緻的熱輸運處理，但摘要未提及，不作推測。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE 聲子模型：皆未取得。

**3 關鍵定量結果**　未取得任何數值。摘要通篇無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度，亦無對應偏壓（VGS/VDS/TA）。摘要逐字片段（原文英文）：「we provide perspectives for upcoming FinFET nodes」，明確界定 FinFET 部分為展望性質。另摘要定性指出微縮帶來的代價即為 device self-heating。判定：所有量測值、模擬值與投影數值均屬「僅圖層級或全文限定」，本次未取得。Unpaywall 確認 is_oa=false、oa_status="closed"、best_oa_location=null。

**4 TCAD 校準用途**　不可直接校準，理由有二且第二項為硬性限制：(1) 本次僅取得摘要，無任何 Rth、ΔT 數值可用於設定 thermode SurfaceResistance；(2) 更根本的是，本文實測元件為 planar／FD SOI，不是 FinFET——使用者做的是矽 FinFET，本文的量測數值即使取得也不能直接搬用，因為 planar 與 FinFET 的散熱幾何完全不同（FinFET 鰭體細窄、三面被閘極與介電包覆，熱阻高出甚多）。可用的間接價值僅一項：本文是「自熱量測 vs FEM 模擬」的交叉驗證範式，若使用者要建立自家 deck 的驗證流程（先量測、再比對模擬、最後外推節點），本文可作為方法論架構的引證，屬流程參考而非數值校準。

**5 批判**
   1. 無數值可判定，原因：僅取得摘要，摘要未印出任何 ΔIon%、ΔT 或 Rth 數值，無法對照判準帶（bulk 3-12%／SOI 8-17%）、交叉比值（0.10-0.20 %/K）或 Rth 區間。全文閉鎖（Unpaywall is_oa=false、oa_status=closed），不從標題、作者或年份推測內容。
   2. 元件類型錯配是本卡最關鍵的警示：標題含 transistors in deeply scaled nodes、內文談 FinFET，極易被誤引為 FinFET 實測資料，但摘要明白界定實測僅在 planar devices，FinFET 只是 perspectives（展望）。使用者若在論文中把本文列為 FinFET 自熱實測依據，屬事實性誤引。原表已正確識破此點。
   3. 投影性結論的可信度隨外推距離衰減：2014 年對 upcoming FinFET nodes 的展望，其外推鏈為 planar 實測 → FEM 校準 → FinFET 幾何投影，每一步都疊加假設。與其把本文當成 FinFET 數值來源，不如當成方法論先驅；後續 imec 同團隊（如五28，E. Bury 亦為共同作者）才有直接的 bulk FinFET FEM 結果，證據層級更高。
   4. FEM 熱邊界條件未取得，而這正是自熱模擬結論最大的敏感源：基板底部固定溫度面的位置、接觸熱阻、BOX 厚度與熱導率設定會直接決定所得 Rth。摘要完全未交代邊界設定，也無網格收斂性或誤差棒說明。
   5. 與五28 為同一團隊研究線（E. Bury、R. Ritzenthaler、G. Groeseneken 皆重複出現，imec）：五32（IRPS 2014，planar 實測 + FinFET 展望）與五28（IEDM 2015，bulk FinFET FEM）構成前後作，五28 可視為五32 展望的兌現。兩篇不可當作獨立來源互相佐證，引用時應併述以免證據重複計數。
   6. FD SOI 與 planar 的量測結果不可外推至 bulk FinFET：BOX 阻斷向下散熱使 FD SOI 熱阻偏高，而 bulk FinFET 鰭底直通基板；兩者散熱拓樸相反，任何從本文取得的熱阻量級都不適用於使用者的 bulk deck。

**6 可引用性**　B（只能引用定性結論）— 僅摘要層級且無數值，可引用其定性與方法學結論（微縮帶來自熱代價、提出自熱量測技術並以 FEM 交叉驗證、對後續 FinFET 節點提出投影）。引用時必須明確標註其實測對象為 planar／FD SOI 元件、FinFET 僅為展望，否則構成誤引；數值一律不可引。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1109/irps.2014.6861186
   - https://api.openalex.org/works/doi:10.1109/irps.2014.6861186?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/irps.2014.6861186
   - https://api.unpaywall.org/v2/10.1109/IRPS.2014.6861186

**8 與原表差異**　與原表一致。原表記載「實測為平面（FD）元件；FinFET 部分僅為有限元素模擬展望；摘要無數值（未提 Rth/dT 具體數字）；摘要未給；全文未讀」，本次獨立查證完全吻合並可逐字佐證：摘要確實載明 assess self-heating in planar devices 與 provide perspectives for upcoming FinFET nodes，確實無任何數值。原表對「實測 planar、FinFET 僅展望」這個易誤引點的識別，本次確認正確。本次補充原表未載之書目細節：IRPS 2014, pp. XT.8.1–XT.8.6, June 2014，第一作者 E. Bury（imec），共同作者含 K. Raleva（Ss. Cyril and Methodius University, Skopje）與 D. Vasileska（Arizona State University）兩位元件熱輸運專家；並確認與五28 為同一 imec 研究線。無衝突、無錯誤。

---

## 五33 — Analytical Thermal Model for Self-Heating in Advanced FinFET Devices With Implications for Design and Reliability

- **DOI／識別**：`10.1109/TCAD.2013.2248194`　**來源**：IEEE　**年**：2013
- **作者／單位**：Chuan Xu（Department of Electrical and Computer Engineering, University of California, Santa Barbara, CA, USA）；共同作者 Seshadri Kolluri (UCSB)、Kazuhiko Endo (National Institute of Advanced Industrial Science and Technology, AIST, Japan)、Kaustav Banerjee (UCSB)
- **出處**：IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 32, no. 7, pp. 1045–1058

**1 元件**　摘要逐字僅提及「a wide range of multifin devices」與可延伸到「production level FinFET (or Tri-gate FET) structures involving metal-gates, body-tied bulk FinFETs, and trench contacts」。技術節點、bulk/SOI 基礎元件別、Lg、Hfin、Wfin、n or p、具體鰭數範圍 全部未取得（全文 closed access，摘要未揭露）。可確認的僅有：元件為多鰭 (multifin) FinFET，且模型可延伸至 body-tied bulk FinFET。

**2 方法與 SHE 定義**　`model`　解析熱模型（analytical thermal model），涵蓋 steady-state 與 transient stress 兩種條件。校準與驗證鏈逐字為「3-D self-consistent electrothermal simulations, tuned with experimentally measured electrical characteristics, were used to understand the nature of self-heating in FinFETs and calibrate the proposed model」，並「comparing it against finite element simulations」。瞬態模型用於估算熱時間常數與 ESD power-to-failure 敏感度。求解器名稱（Sentaurus/GARAND 等）未取得；熱邊界條件、thermode 位置與 SurfaceResistance 設定未取得；有無 hydrodynamic / BTE / 聲子模型未取得（皆未在可取得的摘要與 metadata 中揭露）。

**3 關鍵定量結果**　未取得任何數值。全文 closed access（Unpaywall oa_status = closed，無 repository copy），摘要與 metadata 未印出 Ion 下降 %、Rth、ΔT 或峰值晶格溫度，亦未給對應 VGS/VDS/TA。可引的僅為方法論句：「The model has been applied to carry out a detailed sensitivity analysis of self-heating with respect to various FinFET parameters and structures, which are critical for improving circuit performance and electrical overstress/electrostatic discharge (ESD) reliability.」與「The transient model has been used to estimate the thermal time constants of these devices and predict the sensitivity of power-to-failure to various device parameters」。狀態：非「原文印出數字」，亦非「僅圖層級」——是完全未取得（連圖都看不到）。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何 Rth、ΔT、Ion 或熱時間常數的數值，也未取得熱邊界條件與接觸熱阻的設定，無法轉換成 thermode SurfaceResistance 量級或可比對的 ΔT。潛在價值（需先取得全文才能兌現）：本文提供 multifin FinFET 熱阻對幾何參數的解析敏感度框架，以及 metal-gate / trench-contact / body-tied bulk FinFET 的模型修正項——後者正對應使用者 bulk Si FinFET deck 中「閘極堆疊與接觸是否為有效散熱路徑」的建模抉擇。建議列為優先取得全文的名單。

**5 批判**
   1. 無數值可判定，原因：全文為 closed access（Unpaywall 查無任何 OA location），摘要與 metadata 皆未印出 Ion 下降 %、Rth 或 ΔT，因此無法與 bulk 3–12% / SOI 8–17% 判準帶或 ΔIon%/ΔT ≈ 0.10–0.20 %/K 交叉比值做任何比對。
   2. 這是「解析模型 + FEM 驗證」型論文，其結論的可移植性完全取決於熱邊界假設（基板散熱路徑、BEOL、接觸熱阻）——而摘要對此隻字未提，因此無法判斷模型是否偏絕熱或偏導熱，也無法判斷其 Rth 是否落在 single-fin 1–4 MK/W 帶內。
   3. 模型以「experimentally measured electrical characteristics」調校，但未說明量測元件的世代、量測技術（DC 或 RF）與元件數，糾纏因子（access resistance、metal gate 的橫向導熱、量測元件的封裝熱阻）無法排除；摘要亦無誤差棒或重複性描述。
   4. 外推能力存疑：宣稱涵蓋「a wide range of multifin devices」但未給鰭數範圍與幾何範圍，且併鰭之間的熱耦合是強非線性效應，單一幾何族外推到使用者的 deck 需重新驗證。
   5. 分類正確（model，非 ET-vs-ISO、非 ta_sweep），但正因為是模型論文，若被當成「SHE 對飽和 Ion 影響」的數值來源會是誤引——本文的下游應用面向是 EOS/ESD 可靠度與熱時間常數，不是 DC 飽和區 Ion 退化。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可引用「FinFET 自熱已有可用的解析熱模型並經 3-D 電熱模擬與 FEM 驗證」這一存在性陳述，以及其 ESD/瞬態熱時間常數的研究定位；但無任何可引用的數字，對使用者「SHE 對飽和 Ion 的影響」也無直接定性因果結論。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/tcad.2013.2248194?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/tcad.2013.2248194
   - https://api.crossref.org/works/10.1109/tcad.2013.2248194
   - https://api.unpaywall.org/v2/10.1109/tcad.2013.2248194?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「SOI/bulk multifin FinFET structures（analytical model vali…）／Rth/dT sensitivity vs fin geometry is figure-level; not accessible without full text」——本次核實：multifin 與 body-tied bulk FinFET 皆逐字出現於摘要，「Rth/dT 對 fin 幾何的敏感度分析」也逐字對應摘要的 sensitivity analysis 句；但摘要並未逐字寫出基礎元件為 SOI（僅 bulk 有逐字依據），此點原表略為超前，屬記述精度而非錯誤，故不標 CONFLICT。本次補齊：完整標題、四位作者與單位（UCSB ×3、AIST ×1）、卷期頁 32(7):1045–1058、Unpaywall 確認 closed 無 OA 版本。

---

## 五34 — Self-heat reliability considerations on Intel's 22nm Tri-Gate technology

- **DOI／識別**：`10.1109/IRPS.2013.6532036`　**來源**：IEEE　**年**：2013
- **作者／單位**：C. Prasad（Logic Technology Development Quality and Reliability, Intel Corporation, Hillsboro, OR, USA）；全篇 22 位作者皆隸屬 Intel Corporation（含 L. Jiang、D. Singh、M. Agostinelli、C. Auth、P. Bai、T. Eiles、J. Hicks、C.-H. Jan、K. Mistry、S. Natarajan、B. Niu、P. Packan、D. Pantuso、I. Post、S. Ramey、A. Schmitz、B. Sell、S. Suthram、J. Thomas、C. Tsai、P. Vandervoorn）
- **出處**：2013 IEEE International Reliability Physics Symposium (IRPS), pp. 5D.1.1–5D.1.5

**1 元件**　Intel 22 nm 量產 Tri-Gate（bulk FinFET）製程技術。摘要逐字僅寫「Intel's 22nm process technology」，未揭露 Lg、Hfin、Wfin、鰭數/指數、n or p 分列資料，亦未指明 bulk 或 SOI（Intel 22 nm Tri-Gate 為 bulk 屬產業公開常識，但本次未在所讀文字中取得逐字佐證，故不列為已驗證事實）。

**2 方法與 SHE 定義**　`未取得`　摘要僅逐字寫「This paper describes various measurements on self-heat performed on Intel's 22nm process technology, and outlines its reliability implications. Comparisons to thermal modeling results and analytical data show excellent matching.」——未點名任何具體量測技術（未說明是 gate-resistance 法、RF/Y 參數法、pulsed-vs-DC、還是 TRE），故 method_type 不敢歸入五類任一，填「未取得」。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE 皆未取得（本文為量測＋熱模型比對，非公開的 TCAD deck 論文）。

**3 關鍵定量結果**　未取得任何數值。全文 closed access（Unpaywall oa_status = closed）。摘要唯一的結果陳述為定性句：「Comparisons to thermal modeling results and analytical data show excellent matching.」無 Ion 下降 %、無 Rth、無 ΔT、無峰值晶格溫度，亦無對應 VGS/VDS/TA。狀態：完全未取得，非「原文印出數字」亦非「僅圖層級」。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何 Rth、ΔT 或 Ion 數值，也未取得量測技術與熱模型的邊界設定，無法轉成 thermode SurfaceResistance 或可比對的 ΔT。唯一可用的是「定位論據」：可支持「22 nm 量產 bulk tri-gate 的自熱已被實測、且與熱模型／解析資料吻合良好」這一背景陳述，用於論文引言說明 SHE 在量產 FinFET 已是既定議題；對 deck 數值校準本身無貢獻。

**5 批判**
   1. 無數值可判定，原因：全文封閉且摘要僅 2 句、無任何數字，無法比對 bulk 3–12% 判準帶、single-fin 1–4 MK/W Rth 帶或 ΔIon%/ΔT ≈ 0.10–0.20 %/K 比值。
   2. 「excellent matching」是無定量指標、無誤差棒、無擬合優度的宣稱，屬工業論文常見寫法；即使取得全文，此類宣稱也不能當成使用者 deck 的驗證門檻。
   3. 分類風險：本文為可靠度（reliability considerations）導向，量測面向是自熱對 BTI/HCI/EM 等退化機制的影響，與使用者關心的「飽和區 Ion 電熱 vs 等溫差值」不是同一量測面；若被歸入 ET-vs-ISO 類別會是分類錯誤，故本卡 method_type 保留為未取得。
   4. 量產製程的糾纏因子無法拆解且不會被揭露：22 nm Tri-Gate 的應力工程（eSiGe/應力襯層）、BEOL 金屬層密度、封裝與測試環境熱阻都會同時影響量測到的自熱，Intel 不會公布幾何，因此即使有數字也難以對齊到使用者自建的理想化 deck 幾何。
   5. 無誤差棒、無元件數、無重複性資訊（摘要層級不可判定）；且 2013 年 22 nm 世代與使用者若模擬先進節點（3–14 nm 級）的功率密度差距大，量級外推需另有依據。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可引用「Intel 已在 22 nm 量產 Tri-Gate 上實測自熱並與熱模型比對」作為 SHE 在量產 FinFET 具實務重要性的佐證；無任何數字可引，定性結論也僅止於「吻合良好」這種不可操作的陳述。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps.2013.6532036?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps.2013.6532036
   - https://api.crossref.org/works/10.1109/irps.2013.6532036
   - https://api.unpaywall.org/v2/10.1109/irps.2013.6532036?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「Intel 22nm bulk tri-gate (FinFET) production technology／not accessed (full text paywalled)／not accessed」——本次同樣未能取得全文（Unpaywall 確認 closed、無 repository copy、無 OA location），維持相同判定。本次新增取得的資訊：完整摘要逐字（原表未載）、22 位作者全名單與 Intel Hillsboro 單位、頁碼 5D.1.1–5D.1.5、DOI 經 Crossref 核實正確。註記一項精度差異（非 CONFLICT）：原表寫「bulk tri-gate」，但本次所讀文字未逐字出現 bulk，該分類來自產業常識而非本次一手佐證。

---

## 五35 — Experimental analysis and modeling of self heating effect in dielectric isolated planar and fin devices

- **DOI／識別**：`未取得（Crossref 與 OpenAlex 均查無此文 DOI；請以 IEEE Xplore document 6576663 定位）`　**來源**：IEEE　**年**：2013
- **作者／單位**：S. Lee（IBM Corporation, United States）；共 17 位作者全數隸屬 IBM（R. Wachnik、P. Hyde、L. Wagner、J. Johnson、A. Chou、Arvind Kumar、T. Yoshida、T. Standaert、B. Greene、T. Yamashita、K. Balakrishnan、H. Bu、S. Springer、G. Freeman、W. K. Henson、E. Nowak）。摘要與 metadata 未提供各作者的細部部門單位。
- **出處**：Symposium on VLSI Technology（2013 Symposium on VLSI Technology, Digest of Technical Papers）；IEEE Xplore document 6576663

**1 元件**　介電質隔離（dielectric isolated / SOI）的 planar 元件與 fin 元件（FinFET）兩類，以「45nm planar SOI」作為定量比較基準。摘要逐字僅稱 FinFET 側為「the scaled FinFET on dielectric devices」，未給 FinFET 的節點數字、Lg、Hfin、Wfin、鰭數/指數、n or p。可確認：兩類元件皆為介電質隔離（SOI 類），非 bulk。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗量測 + 可縮放緊湊模型（scalable compact model）。摘要逐字指出熱路徑評估不可只看介電質隔離：「The flow of heat generated at the drain junction may be impeded by dielectric isolation but an assessment must also account for conduction of heat through the gate stack and through the device contacts, and its impact on device characteristics should be captured by the scalable model to enable accurate circuit design.」量測輸出包含 normalized thermal resistance 與 self-heating 的 characteristic time constant，故歸類為 Rth-extraction。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE 均未取得（非 TCAD deck 論文）。註記：網路搜尋結果的合成敘述提到量測用 Time-Resolved Emission (TRE)，但該說法來自搜尋引擎的二手綜述、未經一手全文確認，故不採信、不列為方法事實。

**3 關鍵定量結果**　僅取得定性結論，無任何印出數字。逐字引用：「A quantitative comparison to 45nm planar SOI shows that while the scaled FinFET on dielectric devices show higher normalized thermal resistance, as expected from device scaling, the characteristic time constant for self heating is still well below the operating frequency of typical logic circuits, hence resulting in negligible self heating effect. For cases where the self heating becomes a factor, e.g., in high-speed I/O circuits, the same design methods can be applied for both planar and FinFET devices on dielectric isolation.」未給 Rth 數值、未給 τth 數值、未給 ΔT、未給 Ion 下降 %，亦未給對應 VGS/VDS/TA。狀態：摘要層級定性，非「原文印出數字」；未取得全文故連圖層級也無法讀取。

**4 TCAD 校準用途**　不可直接校準（無任何數值），但有兩項 deck 設計層級可用啟示：(1) 熱邊界不可只留 BOX 一條路徑——原文明示評估必須計入 gate stack 與 device contacts 的導熱，對應 TCAD 中閘極與源汲接觸 thermode 不應設為完全絕熱，否則 Rth 會被系統性高估、Ion 下降被誇大（正是判準帶中「>20% 代表 thermode 過絕熱」的典型成因）。(2) 提供方向性 sanity check：介電質隔離 FinFET 的 normalized Rth 應高於 45 nm planar SOI，可用來檢查模擬出的 Rth 趨勢是否至少方向正確。數值校準（SurfaceResistance 量級、ΔT 對齊）則完全不可用。

**5 批判**
   1. 無數值可判定，原因：摘要僅給方向性比較（higher normalized thermal resistance），未印出 Rth、τth 或 ΔT 任何一個數字，無法與 single-fin 1–4 MK/W 或多鰭多指 RF 結構約 34 kK/W 的 Rth 判準帶比對，也無法比對 SOI 8–17% 的 Ion 下降帶。
   2. 最大誤引風險：「negligible self heating effect」是「在典型邏輯電路操作頻率下、動態熱時間常數不足以建立穩態溫升」的動態論點，不等於 DC 飽和區靜態自熱可忽略。使用者做 DC 電熱 vs 等溫模擬時若援引此句反推 Ion 下降應該很小，會是嚴重的語境錯置。
   3. 比較組不對等且 normalized 定義不明：45 nm planar SOI 對上更先進節點的 FinFET，節點世代差異與架構差異糾纏在一起；摘要未說明 normalized thermal resistance 是對什麼歸一化（每單位通道寬度？每鰭？每有效面積？），不同歸一化基準會改變結論量值甚至方向。
   4. IBM 量產導向論文，元件幾何（Hfin、Wfin、Lg、鰭數）完全未揭露，無法對齊任何 deck 幾何；摘要亦無誤差棒、量測元件數或重複性描述。
   5. 書目缺陷：本文在 Crossref 與 OpenAlex 均無 DOI 記錄，原表 doi 欄實際填的是 IEEE Xplore 連結。引用時須改以會議名＋digest 頁碼或 IEEE Xplore document number 定位，否則 bib 驗證會失敗。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：可引用「介電質隔離的 scaled FinFET 其 normalized 熱阻高於 45 nm planar SOI」與「自熱熱流評估必須計入 gate stack 與 device contacts 的導熱路徑」兩點；「negligible self heating」一句因語境限定於邏輯電路操作頻率下的動態行為，引用時必須連同限定條件一併寫出，否則會被誤讀。無任何數字可引。

**7 取得狀態**　摘要
   - https://api.openalex.org/works?filter=title.search:Experimental%20analysis%20and%20modeling%20of%20self%20heating%20effect%20in%20dielectric%20isolated%20planar%20and%20fin%20devices&per-page=5
   - https://api.crossref.org/works?query.bibliographic=Experimental+analysis+and+modeling+of+self+heating+effect+in+dielectric+isolated+planar+and+fin+devices&rows=3

**8 與原表差異**　CORRECTION（書目層級）：原表 doi 欄填的是 https://ieeexplore.ieee.org/document/6576663 而非 DOI。經 Crossref（題名檢索無命中）與 OpenAlex（有此文記錄但 doi 欄為 null）雙重查核，本文確實無註冊 DOI，建議 bib 改以「2013 Symposium on VLSI Technology (VLSIT), IEEE Xplore doc. 6576663」定位。內容層面與原表一致：原表 orig 記「dielectric-isolated (SOI) FinFET vs 45nm planar SOI／abstract: scaled FinFET-on-dielectric shows higher normalized thermal resistance than 45nm planar SOI, as …」，本次由 OpenAlex 取得完整摘要逐字核實相符，無衝突。本次補齊：完整標題、17 位 IBM 作者全名單、會議全名（Symposium on VLSI Technology）、摘要下半段關於 τth 與 high-speed I/O 的結論（原表被截斷）。註記：IEEE Xplore 頁面本次 WebFetch 回傳空白內容，故未列入 sources。

---

## 五36 — Assessment of NBTI in Presence of Self-Heating in High-k SOI FinFETs（Crossref 題名字串因 LaTeX 標記呈現為 "High- $k$ SOI FinFETs"）

- **DOI／識別**：`10.1109/LED.2012.2213572`　**來源**：IEEE　**年**：2012
- **作者／單位**：Udit Monga（Department of Electronics and Telecommunications, University Graduate Center (UNIK), Norwegian University of Science and Technology (NTNU), Kjeller, Norway）；共同作者 Sourabh Khandelwal (UNIK/NTNU)、Jasmin Aghassi-Hagmann (UNIK/NTNU，另掛 Intel)、J. Sedlmeir (UNIK/NTNU，另掛 Intel)、Tor A. Fjeldly (UNIK/NTNU)
- **出處**：IEEE Electron Device Letters, vol. 33, no. 11, pp. 1532–1534

**1 元件**　high-k 閘介電層的 SOI FinFET。由摘要的負偏壓條件（Vgs = −2 V、Vds = −1 V）與 NBTI 主題可推定為 p-channel 元件，但原文摘要未逐字寫出 p-FinFET，此為推定而非已驗證事實。節點、Lg、Hfin、Wfin、鰭數/指數、BOX 厚度 全部未取得（摘要未揭露、全文 closed access）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　實驗 NBTI 應力量測（非 TCAD 模擬），以「有無功率耗散」建立自熱的有／無對照，屬 ET-vs-ISO 的實驗類比。逐字條件：無自熱組「The NBTI stress in the absence of self-heating (SH) is performed at two different temperatures, i.e., T = 25°C and 125°C, at bias conditions: gate voltage Vgs = -2 V and drain voltage Vds = 0 V」；有自熱組「the stress is performed at room temperature and at Vgs = -2 V and Vds = -1 V」。注意本篇同時內含 ta_sweep（25 °C vs 125 °C），但該溫度掃描是用來建立無自熱下的溫度基準線，SHE 訊號僅來自 Vds = −1 V 那一組。量測儀器、應力／量測時間、ΔVth 抽取判準、元件幾何皆未取得；無求解器、無熱邊界條件、無 thermode／SurfaceResistance（非模擬論文）。

**3 關鍵定量結果**　無任何自熱量化數值。摘要逐字結論：「It has been observed that NBTI in the presence of SH causes a significant shift in the threshold voltage.」摘要中唯一印出的數字是偏壓與環境溫度條件（Vgs = −2 V、Vds = 0 V / −1 V、T = 25 °C 與 125 °C），屬「原文印出數字」但只是實驗條件、不是結果量值。未給 ΔVth 數值、未給 ΔT、未給 Rth、未給 Ion 下降 %、未給峰值晶格溫度。狀態：結果層面完全未取得（全文 closed，圖層級亦無法讀取）。

**4 TCAD 校準用途**　不可直接校準，理由：無 Rth、無 ΔT、無 Ion 下降 % 可餵入 deck，且元件幾何完全未揭露、無法對齊。唯一可用處是實驗設計的類比：本文以 Vds = 0 V（零耗散功率＝等效等溫參考）對照 Vds ≠ 0 V（有耗散＝電熱條件），正是使用者在 TCAD 中做 ET-vs-ISO 對照的實驗對應版本，可在論文中引為「有／無自熱對照設計」的方法論先例。另可作為提醒：若 deck 要延伸到可靠度預測，應力偏壓（|Vgs| 遠大於 VDD）下的功率密度與溫升不可由 VDD = 0.7 V 操作點線性外推。

**5 批判**
   1. 無數值可判定，原因：摘要僅寫「significant shift in the threshold voltage」，未印出 ΔVth、ΔT 或任何熱量值，無法換算 ΔIon%/ΔT ≈ 0.10–0.20 %/K 的交叉檢核比值，也無法比對 SOI 8–17% 的 Ion 下降判準帶。
   2. 分類陷阱（本批最需警覺的一篇）：本文同時含 ta_sweep（25 °C vs 125 °C，改的是環境溫度、不是 SHE）與有／無自熱對照。若只看溫度掃描很容易被誤歸為 SHE 研究；真正的 SHE 訊號只存在於 Vds = −1 V 的那一組。引用時必須把兩者拆開陳述。
   3. 嚴重的變數糾纏：Vds 從 0 V 變到 −1 V 時，同時改變了「自熱溫升」與「通道橫向電場」兩個變數，後者會引入 hot-carrier / mixed-mode 退化成分。摘要無法拆分兩者貢獻，因此「significant shift 是自熱造成的」這個因果宣稱本身就不是單變數比較的結果。
   4. 操作點錯配：Vgs = −2 V 的應力偏壓遠高於使用者關心的 VDD ≈ 0.7 V 飽和區操作點；功率密度差異達數量級，其溫升與退化量不可外推到 0.7 V 的 Ion 分析。
   5. 無誤差棒、無量測元件數、無重複性描述；元件幾何（Hfin/Wfin/鰭數/BOX 厚度）完全未揭露，而 SOI FinFET 的 Rth 對這些幾何極度敏感，因此連自熱溫升的量級都無從估計。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：可引用「在 high-k SOI FinFET 上，自熱存在時的 NBTI 應力會造成顯著的 Vth 位移」，以及其有／無自熱的實驗對照設計；但引用時必須註明 Vds 同時改變電場與溫度、因果歸屬未被拆分，且無任何數值可引。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/led.2012.2213572?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/led.2012.2213572
   - https://api.crossref.org/works/10.1109/led.2012.2213572
   - https://api.unpaywall.org/v2/10.1109/led.2012.2213572?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「high-k SOI FinFET (silicon)／not quantified in abstract／VERIFIED from abstract: no-SH NBTI stress at Vgs=-2V, Vds=0V at T=25C and 125C; with-SH stress at ro…」——本次由 OpenAlex 取得完整摘要，四項條件（Vgs = −2 V、Vds = 0 V、T = 25/125 °C、含 SH 為室溫且 Vds = −1 V）全部逐字核實相符，被截斷的尾段補齊為「the stress is performed at room temperature and at Vgs = -2 V and Vds = -1 V」。無衝突、無錯誤。本次補齊：完整標題、第一作者單位（UNIK/NTNU, Kjeller, Norway）、卷期頁 33(11):1532–1534、Unpaywall 確認 closed。

---

## 五37 — RF Extraction of Self-Heating Effects in FinFETs

- **DOI／識別**：`10.1109/TED.2011.2162333`　**來源**：IEEE　**年**：2011
- **作者／單位**：Sergej Makovejev（School of Electrical, Electronic and Computer Engineering, Newcastle University, Newcastle upon Tyne, U.K.）；共同作者 Sarah H. Olsen（Newcastle University）、Jean-Pierre Raskin（Université catholique de Louvain, UCLouvain, Belgium）
- **出處**：IEEE Transactions on Electron Devices, vol. 58, no. 10, pp. 3335–3341

**1 元件**　n-channel SOI FinFET（摘要逐字「The dynamic self-heating effect is characterized in n-channel SOI FinFETs」）。SOI 且明示為厚 BOX 結構（「the presence of a thick buried oxide with low thermal conductivity」）。掃描的幾何變數為 fin width、number of parallel fins、fin spacing。節點、Lg、Hfin、實際 Wfin 數值範圍、鰭數範圍、BOX 厚度數值 皆未取得（全文 closed access）。

**2 方法與 SHE 定義**　`Rth-extraction`　射頻（RF）抽取法量測動態自熱與熱阻。方法動機逐字：「Due to the shrinking of device dimensions in the nanometer scale, the thermal time constant that characterizes the dynamic self-heating is significantly reduced, and radio frequency extraction techniques are needed.」物理背景逐字：非平面架構的自熱源自「confinement and increased phonon boundary scattering」，且 SOI 中「a thick buried oxide with low thermal conductivity, which prevents effective heat removal from the device active region to the Si substrate」。本文為實驗量測論文：無 TCAD 求解器、無熱邊界條件設定、無 thermode 位置或 SurfaceResistance、無 hydrodynamic/BTE 模型描述。摘要亦未說明 RF 量測的 de-embedding 程序或所用頻段。

**3 關鍵定量結果**　僅取得定性結論，無印出數值。逐字引用：「It is experimentally confirmed that the fin width and the number of parallel fins are the most important parameters for thermal management in FinFETs, whereas fin spacing plays a less significant role.」未印出 Rth 數值、未印出熱時間常數 τth、未給 ΔT、未給 Ion 下降 %、未給對應 VGS/VDS/TA。狀態：摘要層級定性結論；全文 closed access（Unpaywall 確認無任何 OA location、無 repository copy），原表所記的 figure-level 數值本次仍未取得，故無法確認圖中數值。

**4 TCAD 校準用途**　不可直接校準（無任何 Rth/τth 數值），但有三項 deck 級可用啟示：(1) 參數掃描優先序——Wfin 與並聯鰭數是 Rth 的主導因子、fin spacing 次要，可用來設計使用者 deck 的幾何掃描順序，並對模擬得到的 Rth 趨勢做方向性 sanity check（若模擬顯示 fin spacing 主導，代表 deck 的側向熱路徑或 STI 熱導設定可疑）。(2) SOI 厚 BOX 是主要熱阻來源，對應 deck 中 BOX 底部 thermode 的位置與 SurfaceResistance 設定；使用者若模擬 bulk Si FinFET，本文 Rth 量級系統性偏高，不可沿用。(3) 明示並聯鰭數為主導因子，等於警告 single-fin Rth（1–4 MK/W 帶）不可簡單除以鰭數外推到多鰭結構——鰭間熱耦合是非線性的。

**5 批判**
   1. 無數值可判定，原因：全文 closed access，摘要未印出任何 Rth 或 τth 值，無法與 single-fin 1–4 MK/W 或多鰭多指 RF 結構約 34 kK/W 的判準帶比對；原表已標記為 figure-level 未驗證，本次取得鏈（Semantic Scholar / OpenAlex / Unpaywall / 機構庫搜尋）全數落空，未能改善此狀態。
   2. RF 抽取法的系統性偏差來源未被摘要交代：Y 參數中的自熱訊號與 trap-related 低頻色散、以及摘要自己點名的 access resistance / capacitance 增量，都落在相近頻段，若 de-embedding 不當會把非熱效應誤計為熱阻。摘要未說明 de-embedding 程序，可信度無法獨立評估。
   3. 架構偏差：本文為厚 BOX 的 SOI FinFET，其 Rth 系統性高於 bulk FinFET（BOX 阻斷了往基板的主散熱路徑）。使用者若模擬 bulk Si FinFET，直接沿用此 Rth 量級會導致 thermode 過絕熱、Ion 下降被誇大到 20% 以上的異常區。
   4. 幾何外推受限：僅掃 fin width / fin number / fin spacing 三個變數，未涵蓋 Hfin、Lg、接觸與 BEOL 熱路徑；且為 2011 年世代元件，功率密度與現今先進節點差距大，量級外推需另有依據。
   5. 無誤差棒、無量測元件數與重複性描述（摘要層級不可判定）；「fin spacing plays a less significant role」是相對強弱的定性排序，未給定量門檻，無法轉成 deck 的可驗證判準。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：可引用「fin width 與並聯鰭數是 FinFET 熱管理的最重要參數、fin spacing 影響較小」與「奈米尺度元件熱時間常數大幅縮短故需 RF 抽取技術」兩項；數值（Rth vs 幾何）須取得全文才能引用，本次未取得。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2011.2162333?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2011.2162333
   - https://api.crossref.org/works/10.1109/ted.2011.2162333
   - https://api.unpaywall.org/v2/10.1109/ted.2011.2162333?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「n-channel SOI FinFETs, various fin width / fin number / fi…／figure-level, not verified／not verified (full text not accessed)」——本次核實：n-channel SOI FinFET 與 fin width / fin number / fin spacing 三變數皆逐字出現於摘要，且摘要進一步給出強弱排序（Wfin 與鰭數主導、fin spacing 次要），此為原表被截斷處的補齊。全文仍未取得，figure-level 數值維持未驗證。本次補齊：完整標題、第一作者 Sergej Makovejev 全名與 Newcastle University 單位、Raskin 的 UCLouvain 單位、卷期頁 58(10):3335–3341、DOI 經 Crossref 核實正確、Unpaywall 確認 closed。無衝突、無錯誤。

---

## 五38 — Thermal-aware device design of nanoscale bulk/SOI FinFETs: Suppression of operation temperature and its variability

- **DOI／識別**：`10.1109/IEDM.2011.6131672`　**來源**：IEEE　**年**：2011
- **作者／單位**：Tsunaki Takahashi（Department of Physical Electronics, Tokyo Institute of Technology, Meguro, Tokyo, Japan）；共同作者 Nobuyasu Beppu、Kunro Chen、Shunri Oda、Ken Uchida（皆 Tokyo Institute of Technology）
- **出處**：2011 International Electron Devices Meeting (IEDM), pp. 34.6.1–34.6.4

**1 元件**　奈米尺度 bulk FinFET 與 SOI FinFET 兩者並列比較（摘要逐字「The self-heating effects in Bulk/SOI FinFETs have been systematically investigated and compared」）。摘要點名的設計變數為 extension length（延伸區長度）與 MOS 界面熱阻。技術節點、Lg、Hfin、Wfin、鰭數/指數、n or p、基板厚度 皆未取得（全文 closed access）。

**2 方法與 SHE 定義**　`model`　電熱模擬研究（原表記為 electrothermal simulation；摘要本身僅寫「systematically investigated and compared」，未點名求解器）。分析內容含四項：bulk vs SOI 的 lattice temperature 比較、散熱路徑（heat dissipation paths）解析、device-parameter 對熱特性的依賴性、以及 MOS 界面熱阻（thermal resistance at the MOS interface）的影響權重。求解器名稱（Sentaurus/GARAND 等）、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic/BTE/聲子模型 全部未取得。重要限定：摘要未說明是否設有等溫（isothermal）對照組，故不歸類為 ET-vs-ISO，改列 model。

**3 關鍵定量結果**　僅取得定性結論，無印出數值。三段逐字引用：(1)「It is demonstrated that lattice temperature is significantly lower in Bulk FinFETs owing to the larger heat dissipation to the Si substrate.」(2)「It is demonstrated that the Bulk FinFETs show greater temperature fluctuations resulting from device parameter variations. The fluctuation can be greatly suppressed by miniaturizing the extension length.」(3)「It is shown that the impact of thermal resistance at the MOS interface is more significant in SOI FinFETs than in Bulk FinFETs.」未印出 lattice temperature 絕對值、未給 ΔT、未給 Rth、未給 Ion 下降 %、未給對應 VGS/VDS/TA。狀態：摘要層級定性；全文未取得，圖層級數值無法讀取。

**4 TCAD 校準用途**　部分可用（無數值校準，但有結構性設定指引）：(1) 最直接的一項——原文明示 MOS 界面熱阻在 SOI FinFET 的影響顯著大於 bulk FinFET，對應 TCAD 中界面 thermode 的 SurfaceResistance；使用者做 bulk Si FinFET 時，界面熱阻的敏感度應相對低，若 deck 對 SurfaceResistance 極度敏感，代表底部基板熱路徑可能被錯誤地阻斷。(2) bulk 的主散熱路徑是 Si 基板，deck 的底部 thermode 應設在基板深處且不可過度絕熱，否則會落入判準帶「Ion 差 >20% 代表 thermode 過絕熱」的異常區。(3) extension length 是溫度變異的關鍵幾何，值得納入參數掃描。不可用於數值校準，理由：無任何印出的 ΔT、Rth 或 Ion 數值。

**5 批判**
   1. 無數值可判定，原因：全文 closed access（Unpaywall 確認無 OA location），摘要與 metadata 未印出 lattice temperature、ΔT、Rth 或 Ion 下降 %，因此無法比對 bulk 3–12% / SOI 8–17% 的判準帶，也無法計算 ΔIon%/ΔT ≈ 0.10–0.20 %/K 的交叉檢核比值。
   2. 分類界線需守住：摘要未說明有無等溫對照組，本卡因此歸為 model 而非 ET-vs-ISO；若引用時聲稱本文提供「SHE 對飽和 Ion 的影響量」會是過度解讀——本文的觀測量是 lattice temperature 與其變異，不是汲極電流退化。
   3. 熱邊界主導結論量值：bulk 顯著低於 SOI 這個結論完全取決於基板熱路徑的邊界設定（基板厚度、底部 thermode 位置與熱阻），而摘要對此隻字未提。方向性結論可信（BOX 阻熱是公認物理），但溫差量級不可移植到使用者的 deck。
   4. 兩個指標易被混淆：「bulk 的 lattice temperature 較低」與「bulk 的溫度變異較大」是不同維度的結論，引用時若混寫會被誤讀為自相矛盾；且「變異較大」的成因（device parameter variation 的傳遞）與自熱強度本身無直接關係。
   5. 純模擬且摘要未提實驗校驗，亦無誤差棒或統計不確定度描述；2011 年的元件世代與功率密度假設與現今先進節點差距大，單一幾何族外推風險未經評估。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論：可引用三項——bulk FinFET 的 lattice temperature 顯著低於 SOI FinFET（因往 Si 基板的散熱較大）、bulk FinFET 的溫度變異較大且可由微縮 extension length 大幅抑制、MOS 界面熱阻對 SOI FinFET 的影響大於 bulk FinFET。無任何數字可引，故不能作為 deck 的數值校準來源。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iedm.2011.6131672?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/iedm.2011.6131672
   - https://api.crossref.org/works/10.1109/iedm.2011.6131672
   - https://api.unpaywall.org/v2/10.1109/iedm.2011.6131672?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「nanoscale bulk FinFET vs SOI FinFET (electrothermal simula…)／not quantified in accessible text; abstract: bulk FinFET lattice temperature significantly lower than SOI FinFET owing t…／not accessed」——本次由 OpenAlex 取得完整摘要，該句逐字核實為「lattice temperature is significantly lower in Bulk FinFETs owing to the larger heat dissipation to the Si substrate」，完全相符。無衝突、無錯誤。本次補齊原表未載的兩項摘要結論：bulk 的溫度變異較大且可由微縮 extension length 抑制、以及 MOS 界面熱阻對 SOI 的影響大於 bulk（後者對使用者的 thermode SurfaceResistance 設定最有參考價值）。另補齊：完整標題、五位作者與 Tokyo Institute of Technology 單位、頁碼 34.6.1–34.6.4、DOI 經 Crossref 核實正確。

---

## 五39 — Modulating self-heating effects in FinFETs through doping engineering

- **DOI／識別**：`10.1063/5.0309190`　**來源**：非　**年**：2026
- **作者／單位**：Chenkun Deng（Key Laboratory of Thermal Science and Power Engineering of Ministry of Education, Department of Engineering Mechanics, Tsinghua University, Beijing 100084, China）；共同作者 Zhenglai Tang、Yang Shen、Bingyang Cao（皆清華大學同單位）
- **出處**：Applied Physics Letters, vol. 128, no. 6, art. no. 063502（AIP Publishing；線上發表日 2026-02-09）

**1 元件**　FinFET，摘要僅稱「widely adopted in advanced nodes」與「devices with reduced feature sizes」。技術節點數字、bulk 或 SOI、Lg、Hfin、Wfin、鰭數/指數、n or p 全部未在摘要揭露（全文為 AIP 付費牆，PDF 直取被 Cloudflare 阻擋，HTTP 403）。摘要點名的唯一結構要素是 device extension region（延伸區）的摻雜濃度梯度。

**2 方法與 SHE 定義**　`model`　雙尺度耦合模擬：「electro-thermal simulations based on the drift-diffusion model」結合「phonon Monte Carlo (MC) simulations」。分析主軸為熱源機制分解——Joule heat 與 Thomson heat 的相對貢獻隨操作偏壓改變。緩解手段為摻雜工程：降低延伸區的摻雜濃度梯度。求解器名稱（Sentaurus/GARAND 等）未取得；熱邊界條件、thermode 位置與 SurfaceResistance 未取得；載子輸運明示為 drift-diffusion（即非 hydrodynamic）；聲子側使用 phonon Monte Carlo（非解析式 BTE 求解）；DD 與 phonon MC 的耦合是單向或自洽亦未說明。

**3 關鍵定量結果**　原文印出數字（摘要層級逐字核實，Semantic Scholar 與 OpenAlex 兩獨立來源一致）：(1)「Thomson heat provides a pronounced contribution, approximately 16%, to the maximum device temperature rise.」(2)「the peak Thomson heat is reduced by 66% and the hotspot temperature rise is decreased by 13%」（降低延伸區摻雜濃度梯度後）。(3) 偏壓相依的機制轉換逐字：「While Joule heat is the primary heat generation mechanism under the saturation bias, the contribution from Thomson heat becomes significant under the typical CMOS operating bias, emerging as the dominant driver of heat generation non-uniformity due to its highly localized distribution in devices with reduced feature sizes.」(4) 定性宣稱「without decreasing the electrical performance」。未取得：Ion 下降 %、Rth、ΔT 絕對值、峰值晶格溫度絕對值，以及對應的 VGS / VDS / TA 具體數值（摘要僅以「saturation bias」與「typical CMOS operating bias」定性描述偏壓）。

**4 TCAD 校準用途**　部分可用。可用處：(1) 熱源項設定——在典型 CMOS 操作偏壓下 Thomson heat 約佔最高元件溫升的 16%，代表 deck 若只開 Joule heating 項會低估熱點溫升約一成；Sentaurus 等工具中的 Thomson/Peltier 熱源項應明確開啟並記錄於 deck。(2) 對使用者研究區間的直接支持——原文明示飽和偏壓下 Joule heat 為主要生熱機制，這正是使用者關心的飽和區 Ion 分析區間，可作為「飽和區以 Joule 為主的一階簡化可接受」的文獻依據。(3) 參數掃描設計——延伸區摻雜濃度梯度是熱點溫升的可調旋鈕（峰值 Thomson heat −66% 對應熱點溫升 −13%），可納入 deck 的敏感度掃描。不可用處：無 Rth、無 ΔT 絕對值、無 Ion 下降 %、無幾何與熱邊界資訊，因此無法設定 thermode SurfaceResistance 的數值量級，也無法對齊幾何或做 ΔIon%/ΔT 比值檢核。

**5 批判**
   1. Ion 面向無數值可判定，原因：摘要未印出任何 Ion 下降 % 或 ΔT 絕對值，無法比對 14nm n 7.26%/p 8.91%、3nm bulk n 10.6%/p 21.6% 等核心錨點，也無法算 ΔIon%/ΔT ≈ 0.10–0.20 %/K。其印出的三個百分比（16%、66%、13%）屬熱源分解與溫升的相對變化，與判準帶是不同維度的量，絕不可混用或當成 Ion 下降值引用。
   2. 分類正確且值得註記：本文的偏壓對比是「saturation bias vs typical CMOS operating bias」——這是熱源機制隨偏壓改變的分析，既不是 ET-vs-ISO（無等溫對照），也不是 ta_sweep（未改環境溫度）。原表已標 reclassified，判定合理。
   3. 熱邊界完全未揭露，而 16% 這個數字對它高度敏感：Thomson heat 是與電流方向和溫度梯度耦合的局域項，若邊界偏絕熱則 Joule 主導的整體體加熱被放大、局域 Thomson 佔比被稀釋；反之邊界偏導熱則 Thomson 佔比被凸顯。沒有 thermode 位置與 SurfaceResistance 資訊，就無法判斷 16% 是否可移植到使用者的 deck。
   4. 幾何完全未揭露（無節點、無 Lg、無 Hfin/Wfin、未說明 bulk 或 SOI），而 Thomson heat 的重要性明確被歸因於「devices with reduced feature sizes」的局域化——這代表結果對特徵尺寸強烈相依，卻沒有尺寸數字可對齊，單一幾何的外推能力完全無從評估。
   5. 模型層面：drift-diffusion 無法描述非局域熱載子輸運，在奈米尺度的熱源定位上可能與 hydrodynamic 或完整 BTE 結果有系統性差異；且 DD 與 phonon MC 的耦合方式（單向餵入或自洽迭代）未說明，phonon MC 亦無統計不確定度或誤差棒描述。
   6. 「without decreasing the electrical performance」是無數字的定性宣稱，而降低延伸區摻雜梯度通常會抬高寄生串聯電阻、拉低 Ion——此宣稱必須有全文的 Ion/Ron 數據佐證才可引用，僅憑摘要引用會有過度宣稱風險。

**6 可引用性**　A（可直接引用數字）— 可直接引用數字：16%（Thomson heat 對最高元件溫升的貢獻）、66%（峰值 Thomson heat 降幅）、13%（熱點溫升降幅）三者皆為摘要逐字印出，並經 Semantic Scholar 與 OpenAlex 兩個獨立來源核實一致。但引用時必須同時標註三項限定：偏壓僅寫「typical CMOS operating bias」而無具體電壓值、無任何幾何與熱邊界資訊、且這三個數字不是 Ion 下降值，不可用作 SHE-on-Ion 的校準錨點。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1063/5.0309190?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1063/5.0309190
   - https://api.crossref.org/works/10.1063/5.0309190
   - https://api.unpaywall.org/v2/10.1063/5.0309190?email=<your_email>

**8 與原表差異**　與原表一致。原表 orig 記「先進節點 Si FinFET／Thomson heat 貢獻最大元件溫升約 16%；降低延伸區摻雜梯度後峰值 Thomson heat 減 66%、熱點溫升降 13%——三個數字皆與摘要逐字核實 相符／saturation bias vs 典型 CMOS 操作偏壓（摘要未給具體電壓值）」——本次以 Semantic Scholar 與 OpenAlex 兩個獨立來源重新逐字核實，三個百分比（16%/66%/13%）與偏壓描述全部相符，原表 verdict 'reclassified' 判定合理。本次補齊：APL 卷期與文章編號 128(6):063502、線上發表日 2026-02-09、第一作者 Chenkun Deng 與清華大學工程力學系熱科學與動力工程教育部重點實驗室單位、方法細節（drift-diffusion 電熱模擬 + phonon Monte Carlo 雙尺度耦合）。註記：AIP 全文與 PDF 本次嘗試取得失敗（文章頁 HTTP 403、article-pdf 連結被 Cloudflare 攔截），Unpaywall 亦確認 oa_status = closed，故維持摘要層級。

---

## 五40 — Effect of Gate Oxide and Back Oxide Materials on Self-Heating Effect in FinFET

- **DOI／識別**：`10.26565/2312-4334-2025-3-35`　**來源**：非　**年**：2025
- **作者／單位**：第一作者 M.M. Khalilloev（Urgench State University named after Abu Rayhan Biruni, Urgench, Uzbekistan；通訊作者 x-mahkam@urdu.uz）。共同作者：B.O. Jabbarova（同校）、F. Eshchanov（Agency for Assessment of Knowledge and Skills, Khorezm Regional Department, Urgench, Uzbekistan）、A.E. Atamuratov（同校）
- **出處**：East European Journal of Physics（East Eur. J. Phys.），Issue 3, pp. 353-356，ISSN 2312-4334，CC BY 4.0 開放取用

**1 元件**　n 通道矽 SOI FinFET（原文：FinFET 基於 silicon-on-insulator 技術，通道底部接 back oxide）。TiN 閘極。Lgate = 10 nm；Tsi（channel thickness）= 9 nm；Wb（channel width）= 22 nm；gate oxide 為 HfO2 或 Si3N4，tEOT = 1.0-1.5 nm；BOX 材料為 SiO2 / HfO2 / SiO2+Si3N4，Tbox = 10-1000 nm。S/D 摻雜 Nd = 5×10^18 cm^-3 (n-type)；通道摻雜 Na = 1×10^16 cm^-3 (p-type)。技術節點未標示；鰭數/指數未標示（結構圖為單鰭剖面）。非 GAA / nanosheet / CFET。

**2 方法與 SHE 定義**　`ET-vs-ISO`　Sentaurus TCAD 3D 模擬。原文：「the drift-diffusion transport model in conjunction with the thermodynamic transport model was used」；量子效應用 Density gradient 量子修正；含 doping-dependent mobility 與 high-field velocity saturation；因使用 high-k HfO2 而納入 Coulomb 與 phonon scattering 以描述介面遷移率退化。校準方式：以 Lgate = 25 nm、Vds = 50 mV 的實驗 Id-Vg 與模擬對照（Fig.2，對應參考文獻 [8][9][10]）。【關鍵缺口】全文未給任何 thermode 位置、SurfaceResistance 數值或熱邊界條件描述；無 hydrodynamic、無 BTE、無聲子輸運模型；且無等溫（isothermal）對照組，method_type 標為 ET-vs-ISO 屬五選一下的強制歸類，實際為「純電熱參數掃描、無等溫基準」。

**3 關鍵定量結果**　全篇只報通道中心晶格溫度，【無 Ion 下降 %、無 Rth、無 ΔT 明確定義】。(1) 僅圖層級（需自讀原圖）：Fig.3 通道中心晶格溫度 vs gate oxide tEOT 1.0-1.5 nm，縱軸範圍 320-380 K，涵蓋 HfO2/Si3N4 閘氧 × SiO2/HfO2/SiO2+Si3N4 背氧各組合；Fig.3 本身未標注偏壓。(2) 僅圖層級：Fig.5 通道中心晶格溫度 vs TBOX 10-1000 nm，縱軸範圍 300-550 K；圖內偏壓標注為原文印出：「Gate oxide (HfO2) tEOT=1.2 nm, VDS=0.75 V; VG=1.5 V」。(3) 原文印出數字（結論段）："the maximal difference in the temperatures lies in the range between 50 and 170 K for BOX thicknesses from 100 to 1000 nm"；"The maximal temperature difference in using different considered gate oxide materials is approximately 10K in all considered ranges of oxide thicknesses"。(4) 原文印出（Table 2 熱導率 Kb, W m^-1 K^-1）：HfO2 = 2.3、SiO2 = 1.4、Si3N4 (SiO2+Si3N4) = 18.5。(5) 定性原文："the lattice temperature very slowly decreased with increasing the gate oxide thickness"；"the combination SiO₂+Si₃N₄ shows the lowest temperature values, which can be attributed to its highest thermal conductivity"。(6) 僅圖層級：Fig.4 汲極電流 ID 縱軸 3.0-4.5×10^-6 A（BOX 為 HfO2）。(7) 原文給出解析式 ΔT = (Pt · Tbox)/(Kb · A)，Pt 為通道電流產生的熱功率、Kb 為氧化層熱導率、A 為氧化層與通道接觸面積。

**4 TCAD 校準用途**　可對齊的幾何錨點：Lg = 10 nm、Tsi = 9 nm、Wfin = 22 nm、Tbox 10-1000 nm 的 SOI n-FinFET，可當使用者 deck 的幾何參照之一。最大可用價值是【BOX 厚度→溫度的敏感度曲線】：TBOX 由 10 nm 掃到 1000 nm 時通道中心溫度由約 300 K 升至約 550 K，可用來 sanity-check 使用者 deck 中「BOX 厚度／底部熱路徑長度」這一自由度的量級——若 deck 的 Tbox 僅數十 nm 卻算出上百 K 的 ΔT，代表底部 thermode 過絕熱。Table 2 的三種氧化物熱導率（HfO2 2.3 / SiO2 1.4 / Si3N4 系 18.5 W m^-1 K^-1）可直接抄進 deck 材料參數。ΔT = Pt·Tbox/(Kb·A) 可作為 deck 中底部熱阻的一階解析檢核式。【不可用於】thermode SurfaceResistance 校準（全文零數值）；【不可用於】Ion 退化校準（完全未報 Ion 下降 %）。

**5 批判**
   1. 無 Ion 下降 % 可判定，原因：本文只報通道中心晶格溫度，全篇無電熱 vs 等溫的 Ion 對照，也無 Rth。若改以 ΔT 側面判定則明確落在判準帶外：Fig.5 在 TBOX=1000 nm 時 ΔT 達約 250 K，而判準帶隱含的 ΔT 上限為 7-11% ÷ 0.10-0.20 %/K ≈ 35-110 K；且偏壓 VG=1.5 V 遠高於判準帶定義的 VDD≈0.7 V，屬重度過驅動情境，溫度絕對值不可直接搬用。厚 BOX 的高溫是刻意做出的病態案例，不能當標準矽 FinFET 錨點。
   2. 熱邊界條件完全未揭露：無 thermode 位置、無 SurfaceResistance、未說明 BOX 下方是理想散熱面還是絕熱面。TBOX 增加→溫度上升的單調趨勢在物理上正確，但斜率大小完全由未公開的底部邊界決定，因此這條曲線只能當定性趨勢，不能當定量校準來源。
   3. 內部一致性疑點：本文自述機制為「熱導率越低→溫度越高」，Table 2 給 SiO2 (1.4) < HfO2 (2.3) < SiO2+Si3N4 (18.5)。依此邏輯 BOX 為 SiO2 時應最熱、HfO2 次之、SiO2+Si3N4 最涼。原表記載的「HfO2 BOX 最高」與此推論方向相反（見 diff_note，已標 CONFLICT）。另 Si3N4 系取 18.5 W m^-1 K^-1 偏高（非晶 Si3N4 薄膜文獻值分佈甚廣），此參數選擇會系統性放大 SiO2+Si3N4 的優勢。
   4. 單一幾何、單一工作點、無誤差棒、無網格收斂測試、無重複性檢驗。Fig.3 甚至未標注偏壓，讀者無法確認 Fig.3 與 Fig.5 是否為同一工作點，這使 320-380 K 這組數字失去可引用性。
   5. 校準點與應用點不匹配：模型僅以 Lgate = 25 nm、Vds = 50 mV（線性區/次臨界）的實驗 I-V 校準，卻用來預測 Lgate = 10 nm、VDS = 0.75 V 飽和區的自熱。通道長度差 2.5 倍、偏壓區間完全不同，飽和區熱源分佈的可信度未經任何驗證。
   6. 糾纏因子：改變閘氧材料同時改變了介電常數、熱導率、實體厚度與汲極電流（Fig.4 顯示 ID 隨材料變化），本文自己也承認「the Joule heat generation rate depends on the drain current」，但未做固定功率下的純散熱比較，因此「HfO2 閘氧較涼」有多少來自散熱、多少來自電流較小，無法分離。

**6 可引用性**　C（僅可當背景引用）— 全文取得且方法段完整，但沒有任何 Ion 退化數字、沒有 Rth、熱邊界條件完全未揭露，主要結果僅存在於未標偏壓的圖中；只能當「BOX 材料與厚度顯著影響 SHE」的背景與趨勢引用，不宜引用其溫度絕對值。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.26565/2312-4334-2025-3-35?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://periodicals.karazin.ua/eejp/article/download/26421/24097

**8 與原表差異**　大部分與原表一致：標題、2025 年、DOI、n 通道矽 FinFET(SOI)、TiN 閘極、Lgate=10 nm、Tsi=9 nm、Wb=22 nm、gate oxide tEOT 1.0-1.5 nm、Fig.3 縱軸約 320-380 K、Fig.5 隨 TBOX 10→1000 nm 由約 300 K 升至約 550 K、Fig.5 偏壓 VDS=0.75 V / VG=1.5 V / gate oxide HfO2 tEOT=1.2 nm — 本次全部在全文中逐項確認。【CONFLICT】原表記載 Fig.5 中「HfO2 BOX 最高」；本次全文只印出「SiO₂+Si₃N₄ 最低」而未指出何者最高，且本文 Table 2 的熱導率為 SiO2 1.4 < HfO2 2.3，依本文自述機制應為 SiO2 BOX 最熱、HfO2 較涼，與原表方向相反。兩說並列、不覆蓋原表，需使用者自行重讀 Fig.5 的三條曲線判定何者為最高。補充原表未記載者：結論段原文印出的「BOX 材料間最大溫差 50-170 K（TBOX 100-1000 nm）」與「閘氧材料間最大溫差約 10 K」、Table 2 三個熱導率數值、S/D 與通道摻雜濃度、校準條件（Lgate=25 nm, Vds=50 mV）、解析式 ΔT = Pt·Tbox/(Kb·A)。原表 verdict=value_corrected 的既有記載未見錯誤。

---

## 五41 — Comparative study of the self-heating effect in the accumulation and inversion mode FinFETs

- **DOI／識別**：`10.48550/arXiv.2402.10858（本批清單給的是 arXiv URL：https://arxiv.org/abs/2402.10858；arXiv:2402.10858 [physics.app-ph]）`　**來源**：非　**年**：2024
- **作者／單位**：第一作者 A.E. Atamuratov（Physics department, Urgench State University, Urgench, Uzbekistan）。共同作者：B.O. Jabbarova（同系）、E.Sh. Xaitbayev（Master student, 同校）、D.R. Rajapov（Master student, 同校）、M.M. Khalilloev（同系）
- **出處**：arXiv 預印本（physics.app-ph），arXiv:2402.10858，2024/02/16 投稿。稿件採 IEEE 會議雙欄模板，但頁首版權行仍為未填的佔位符「XXX-X-XXXX-XXXX-X/XX/$XX.00 ©20XX IEEE」，未見任何正式會議或期刊出處，亦無同儕審查紀錄。

**1 元件**　兩顆同幾何對照元件：SOI FinFET（inversion mode）與 SOI JL FinFET（accumulation mode / junctionless）。共同幾何（Table I，原文印出）：Lgate = 10 nm；Tsi（channel thickness）= 9 nm；Wb（channel width）= 22 nm；Tbox（back oxide thickness）= 145 nm；gate oxide 為 HfO2，tox = 6.7 nm（teff = 1.2 nm）。摻雜：JLFinFET 通道 N = 5×10^18 cm^-3 (n-type)；FinFET 通道 1×10^16 cm^-3 (p-type)，S/D 皆為 5×10^18 cm^-3 (n-type)。n 通道。技術節點未標示；鰭數/指數未標示（單鰭結構圖）。非 GAA / nanosheet / CFET。

**2 方法與 SHE 定義**　`ET-vs-ISO`　TCAD Sentaurus。原文：「To account for thermic effects the thermodynamic transport model with quantum correction is used」；mobility model 納入 doping dependence 與 high-field velocity saturation。校準：以 Barraud et al. 2012（IEEE EDL 33(9), 1225-1227）的 SOI JL FinFET 實驗 Id-Vg 對照模擬曲線（Fig.2）。【關鍵缺口】全文未給 thermode 位置、SurfaceResistance、任何熱邊界條件，亦未標注環境溫度 TA；無 hydrodynamic、無 BTE、無聲子輸運模型；無等溫對照組。method_type 標為 ET-vs-ISO 為強制歸類，實際為「JL vs inversion 兩結構在相同幾何/相同熱邊界下的電熱對照」。

**3 關鍵定量結果**　只有晶格溫度與載子密度，【無 Ion 下降 %、無 Rth；因未標 TA 故亦無法算出 ΔT】。(1) 僅圖層級（需自讀原圖）：Fig.4 沿通道方向的晶格溫度分佈，inversion FinFET（曲線 1）落在 368-370 K 的斷軸刻度帶、JL FinFET（曲線 2）落在 455-458 K 的斷軸刻度帶；【圖說偏壓為原文印出】："Vd=0.75V Vg=1.6V"。(2) 原文印出數字（正文）："In the case of a constant doping profile, the lattice temperature in the channel center is higher by 75-85 K than in the analytical doping profile, depending on the doping depth."。(3) 僅圖層級：Fig.6 通道中心晶格溫度 vs S/D 摻雜深度 L（橫軸 24-42 nm），縱軸斷軸刻度為 364 / 377 / 437 / 460 K，並標出 JLFinFET 與 FinFET 兩個水平參考位置。(4) 僅圖層級：Fig.7 通道中心「eCurrent density [A/cm2]」縱軸 1.8×10^18 - 2.7×10^18（單位標示存疑，見 critique 第 4 點）。(5) 定性原文："the lattice temperature in the channel center is higher in junctionless (JL), accumulation mode FinFET than in inversion mode FinFET with the same parameters"；"With increasing the doping depth along the channel the temperature aspires to the value which corresponds to the temperature of JL FinFET with the same geometry"。

**4 TCAD 校準用途**　可直接對齊的幾何：Lg = 10 nm、Tsi = 9 nm、Wfin = 22 nm、Tbox = 145 nm 的 SOI n-FinFET，且 gate oxide 同時給出實體厚度 6.7 nm 與 teff = 1.2 nm（HfO2），可整組抄進 deck。最有價值者為【同幾何、同熱邊界下 inversion vs JL 的溫差約 87 K（約 369 K vs 約 456 K @ Vd=0.75 V, Vg=1.6 V）】：這是一個「散熱路徑固定、只改熱源強度」的乾淨對照，可用來檢查使用者 deck 中「Ion 提高 N 倍 → 通道溫升提高多少」的線性度是否合理（若 deck 中電流翻數倍而 ΔT 幾乎不動，代表 thermode 貼太近通道）。【不可用於】thermode SurfaceResistance 校準（零數值）；【不可用於】ΔT 絕對值校準（未標 TA，無法計算 ΔT）；【不可用於】Ion 退化校準（未報）。另 Vg=1.6 V 遠高於使用者關心的 VDD≈0.7 V，溫度絕對值不可搬用。

**5 批判**
   1. 無 Ion 下降 % 可判定，原因：全篇無電熱 vs 等溫的 Ion 對照。若強行以 TA=300 K 推估（本文未標 TA，此為外加假設）：inversion FinFET ΔT≈69 K、JL FinFET ΔT≈156 K。前者以 0.10-0.20 %/K 換算對應 7-14% Ion 降，數字看似落在 SOI 判準帶 8-17% 內，但那是在 Vg=1.6 V 的重度過驅動下取得，與判準帶定義的 VDD≈0.7 V 條件不符，應判為帶外情境；JL FinFET 的 156 K 明確帶外（換算 >20% Ion 降，觸發「SHE 過強、thermode 可能過絕熱」紅線），且 junctionless 本就是判準帶明文排除的特例。
   2. 未標注環境溫度 TA 是本文最嚴重的量測學缺陷：讀者無法把 368-370 K 換算成 ΔT，也就無法與任何其他文獻或使用者的 deck 做交叉檢核。這一項缺失使本文所有溫度數字在校準上失效。
   3. 熱邊界完全未揭露（thermode 位置、SurfaceResistance、BOX 下方是否理想散熱皆無），而 Tbox = 145 nm 已屬相當厚的 BOX，容易造成過絕熱。因此 ΔT 的絕對值不可信，只有 JL-vs-inversion 的「相對差」有意義。
   4. 圖表品質問題：Fig.7 縱軸標為「eCurrent density [A/cm2]」但數值為 1.8-2.7×10^18；10^18 A/cm² 在物理上不可能（矽的擊穿電流密度低數個數量級），研判應為 Sentaurus 的 eDensity [cm^-3] 被誤標為電流密度。此類單位標示錯誤會連帶降低對其他圖數值的信心。
   5. 糾纏因子未分離：JL vs inversion 的差異同時混入通道摻雜（5×10^18 vs 1×10^16，相差 3 個數量級）造成的遷移率退化、Vth 差異與 Ion 差異。本文自述「difference in the channel lattice temperature ... is defined only by the difference in the heat generation rate」，但並未把 Ion 或耗散功率歸一化後再比溫度，因此「JL 較熱」有多少是結構本質、多少只是該偏壓點下電流較大，無從分離。
   6. 預印本狀態與嚴謹度：採 IEEE 會議模板但版權行仍是未填佔位符，無正式出處、無同儕審查；全文無誤差棒、無網格收斂測試、無重複性檢驗，且校準只做 Id-Vg（次臨界/線性），未校準飽和區輸出特性。

**6 可引用性**　C（僅可當背景引用）— 未經同儕審查的預印本；缺 TA 導致無法計算 ΔT、無 Ion 退化數字、無 Rth，且有明顯的圖軸單位標示錯誤。只能當「JL/accumulation mode FinFET 自熱比 inversion mode 嚴重」與「S/D 摻雜輪廓影響通道溫度」的定性背景引用。

**7 取得狀態**　全文
   - https://arxiv.org/abs/2402.10858
   - https://arxiv.org/pdf/2402.10858

**8 與原表差異**　與原表一致。原表「SOI FinFETs, Lg = 10 nm, Tsi = 9 nm, fin width Wb = 22 nm」「Confirmed from Fig. 4: channel lattice T ~368.5-370.5 K (inversion FinFET) vs ~455-458 K (JL FinFET)」「Fig. 4 temperature readout at Vd = 0.75 V, Vg = 1.6 V (printed in Fig. 4 caption)」本次在全文中全部確認，Fig.4 圖說確實逐字印出「Vd=0.75V Vg=1.6V」；本次讀到的 Fig.4 縱軸斷軸刻度為 368/369/370 與 455/456/457/458，與原表的 368.5-370.5 / 455-458 判讀相容，無衝突。補充原表未記載者：Tbox = 145 nm、gate oxide HfO2 tox = 6.7 nm (teff = 1.2 nm)、JL 與 inversion 的通道/S-D 摻雜濃度、constant vs analytical 摻雜輪廓的溫差「75-85 K」（原文印出）、Fig.6 縱軸刻度 364/377/437/460 K、校準來源為 Barraud et al. 2012 EDL、以及 Fig.7 縱軸單位標示錯誤（eCurrent density [A/cm2] 值域 10^18，疑為 eDensity [cm^-3]）。原表 verdict=confirmed 成立。另註：本文未標注環境溫度 TA，原表亦未主張 TA，兩者一致。

---

## 五42 — Integrated modeling of Self-heating of confined geometry (FinFET, NWFET, and NSHFET) transistors and its implications for the reliability of sub-20 nm modern integrated circuits

- **DOI／識別**：`10.1016/j.microrel.2017.12.034`　**來源**：非　**年**：2018
- **作者／單位**：第一作者 W. Ahn（Woojin Ahn），School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN, USA。共同作者：S.H. Shin、C. Jiang、H. Jiang、M.A. Wahab、M.A. Alam（皆為 Purdue ECE；Alam 為通訊作者）。單位來源：OpenAlex 作者機構欄位。
- **出處**：Microelectronics Reliability（Elsevier），Volume 81, pp. 262-273

**1 元件**　未取得。僅能由標題得知涵蓋 FinFET / NWFET（nanowire FET）/ NSHFET（nanosheet FET）三種受限幾何架構與 sub-20 nm 節點；依反幻覺紀律，未取得內文即不填寫節點、bulk/SOI、Lg、Hfin/Wfin/TNS/WNS、n/p 型別、鰭數等任一項。

**2 方法與 SHE 定義**　`未取得`　未取得。取得鏈全數嘗試結果：(1) Semantic Scholar API 回傳 abstract = null，並明示「The following paper fields have been elided by the publisher: {'abstract'}」；(2) OpenAlex abstract_inverted_index 為 null，closed access，無 OA PDF；(3) Crossref 無 abstract 欄位；(4) ScienceDirect 出版者頁（S0026271417305929）回 HTTP 403；(5) Dialnet 頁面連線被拒（ECONNREFUSED）；(6) 作者 Alam 研究群官方論文頁僅列出書目條目、未附任何 PDF 連結。標題含「Integrated modeling」，但依反幻覺紀律不由標題推定求解器、熱邊界、thermode 或模型設定。

**3 關鍵定量結果**　未取得。無任何 Ion 下降 %、Rth、ΔT、峰值晶格溫度或偏壓條件。（註：搜尋引擎回傳的摘要式敘述未經任何一手頁面驗證，本卡一律不採計。）

**4 TCAD 校準用途**　不可直接校準，理由：本次完全未取得內文或摘要，沒有任何一個數字可餵給使用者的 deck。唯一可用的是書目定位——這是 Purdue Alam 研究群 2018 年發表於 Microelectronics Reliability 的 12 頁長文（vol.81, pp.262-273），主題涵蓋 FinFET/NWFET/NSHFET 三種受限幾何的自熱整合建模與 sub-20 nm IC 可靠度，可作為本領域的入口文獻。建議使用者透過機構訂閱取得全文後再重建本卡。旁證：本批的 五41（arXiv:2402.10858）將本篇列為其參考文獻 [3]，可從該處確認其在領域中的定位。

**5 批判**
   1. 無數值可判定，原因：Semantic Scholar、OpenAlex、Crossref 三個 metadata 來源的 abstract 欄位皆為空（S2 明示係出版者主動遮蔽），出版者頁面 403，且未找到任何開放全文或機構 repository 版本，因此連摘要層級的數字都不存在，無法與 3-12%（bulk）、8-17%（SOI）、0.10-0.20 %/K 或 1-4 MK/W 任一判準帶對照。
   2. 取得性風險本身即為一項評估結論：本篇為 Elsevier 付費牆文獻，且連摘要都無法從公開 API 取得。若使用者要在論文中引用其數字，必須自行透過訂閱取得原始 PDF，絕不可依賴任何二手轉述（包含搜尋引擎摘要、引用它的後續論文的轉述、或 AI 生成的摘要）——本領域的 deep-research 引用不可信教訓正適用於此。
   3. 分類與外推風險：本篇同時涵蓋 FinFET、NWFET、NSHFET 三種架構。日後取得全文時務必逐圖確認引用的數字對應哪一種架構與哪一個節點，不可把 NWFET/NSHFET 的 Rth 或 ΔT 誤植為 FinFET 的值。本卡刻意將 device 欄留為「未取得」即為避免此陷阱。
   4. 篇幅 12 頁（262-273）且標題為「Integrated modeling ... and its implications」，型態上可能為整合／回顧型長文，其中數字有相當比例可能是彙整他人量測結果。取得全文後若要引用數字，需追溯到原始出處，不宜當一手數據引用。
   5. 本篇被本批 五41 引用為 [3]，顯示其為此研究社群的共同參考點；但「被廣泛引用」不等於「數字可信」，在未讀原文前不可據此提升可信度。

**6 可引用性**　D（不建議引用）— 本次完全未取得內文或摘要，任何數字性引用都會是幻覺；在取得訂閱全文之前不建議引用（取得全文後極可能升為 A 或 B，因其為 Purdue Alam 群的整合建模長文）。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.microrel.2017.12.034?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.microrel.2017.12.034
   - https://api.crossref.org/works/10.1016/j.microrel.2017.12.034
   - https://sites.google.com/view/alam-research-group/papers

**8 與原表差異**　與原表一致。原表記載「Sub-20 nm silicon FinFET, nanowire FET, nanosheet FET (con…」「not extracted」「n/a (full text not accessed)」，本次同樣未能取得全文或摘要，結論完全相同，無衝突。補充原表未完整記載者：完整標題（原表被刪節號截斷）、第一作者 W. Ahn 與單位 School of ECE, Purdue University, West Lafayette, IN、完整作者群六人、期刊卷期頁碼 Microelectronics Reliability 81, 262-273 (2018 年 2 月)。原表 verdict=confirmed（指書目層級已查證）成立。

---

## 五43 — Impact of self-heating effect on the performance of hybrid FinFET

- **DOI／識別**：`10.1016/j.mejo.2018.04.015`　**來源**：非　**年**：2018
- **作者／單位**：第一作者 Rajeev Pankaj Nelapati；共同作者 K. Sivasankaran。單位：Vellore Institute of Technology (VIT), Vellore, India（來源為 ResearchGate 個人檔案標題「Vellore Institute of Technology University, Vellore | VIT | Division of VLSI」與「School of Electronics Engineering (SENSE)」，非取自論文內署名頁；Crossref 與 OpenAlex 皆未提供 affiliation，論文內單位未取得）
- **出處**：Microelectronics Journal（Elsevier），Volume 76, pp. 63-68

**1 元件**　Hybrid FinFET（矽基）。摘要層級可確認被掃描的元件參數為 channel length (Lg)、fin width (Wfin)、buried oxide thickness (tbox)、device pitch (Lpitch)、fin 數 (N)。存在 buried oxide → 屬含 BOX 的 SOI 類結構。【未取得】技術節點、Lg/Wfin/Hfin/tbox 的具體數值、n 或 p 型別、實際鰭數與指數、「hybrid FinFET」的結構定義本身。非 GAA / nanosheet / CFET。

**2 方法與 SHE 定義**　`Rth-extraction`　摘要層級：TCAD 電熱模擬並萃取熱阻 Rth 對各幾何參數的依賴律。原文（摘要）："The linear dependence of thermal resistance (Rth) on Lg, Wfin, and tbox; and nonlinear dependence on Lpitch and N is studied."。【全數未取得】求解器名稱（Sentaurus / GARAND / 其他）、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型、網格設定。全文位於 Elsevier 付費牆後，Semantic Scholar 的 openAccessPdf 狀態為 CLOSED（url 為空字串），無任何 OA 版本。

**3 關鍵定量結果**　摘要層級，【原文印出數字】："It is seen that unlike trigate FinFET, hybrid FinFET have the advantage of increased drain current from 50 μA to 103 μA with an increase in Lpitch from 50 nm to 250 nm, also reduces lattice temperature from 726.5 K to 495.6 K." 即：Lpitch 由 50 nm 放寬到 250 nm 時，汲極電流由 50 μA 升至 103 μA，晶格溫度由 726.5 K 降至 495.6 K。另定性原文："The impact of variation of channel length (Lg), fin width (Wfin), buried oxide thickness (tbox), the pitch of the device (Lpitch) and a number of fins (N) on the increase in lattice temperature for hybrid FinFET is observed."。【未取得】偏壓條件 VGS / VDS / TA（摘要完全未標注）、Ion 下降 %、Rth 的絕對數值與單位、ΔT 的明確定義。若假設 TA = 300 K（本文未標，屬外加假設），則 ΔT 由約 426 K 降至約 196 K。

**4 TCAD 校準用途**　不可直接校準，理由：無偏壓條件、無 TA、無 Rth 絕對值、無 SurfaceResistance，且「hybrid FinFET」的結構定義未取得，幾何無法與使用者的標準矽 FinFET deck 對齊。唯一可用的是【趨勢與量級警示】：可用來 sanity-check 使用者 deck 的 pitch／鰭密度依賴性——緊密 pitch（50 nm）下相鄰鰭的熱耦合可讓峰值晶格溫度衝到 700 K 量級，放寬到 250 nm 才降到 500 K 量級。反向使用更有價值：若使用者在類似密集 pitch 下算出的 ΔT 只有個位數 K，代表 thermode 貼太近通道或側向散熱路徑設得過導熱；反之若使用者算出 400 K 以上的 ΔT，本篇正說明那是熱邊界過絕熱的典型徵兆，不是物理實情。

**5 批判**
   1. 數字明確落在判準帶外，原因：若取 TA = 300 K，726.5 K 對應 ΔT ≈ 426 K，遠超判準帶隱含的 ΔT 區間（7-11% ÷ 0.10-0.20 %/K ≈ 35-110 K）；以 0.10-0.20 %/K 換算將對應 43-85% 的 Ion 降，遠遠越過「飽和 Ion 差 > 20% → SHE 過強、thermode 可能過絕熱」的紅線。這強烈暗示其熱邊界接近絕熱，或 Lpitch = 50 nm 的密集陣列被設成幾乎無側向與底部散熱。此數字不可作為標準矽 FinFET 的校準錨點。
   2. 摘要完全未給偏壓（VGS / VDS）與環境溫度 TA，因此 726.5 K 在校準上是無效數字——不知道工作點就無法分辨高溫是過驅動造成、是密集陣列熱耦合造成、還是熱邊界設定造成。
   3. 糾纏因子未分離：Lpitch 增加同時改變了汲極電流（50 → 103 μA，耗散功率翻倍）與散熱面積，兩者對溫度的作用方向相反卻被綁在同一條曲線上。作者把「電流上升」與「溫度下降」同時當成優點陳述，但未做固定功率下的純散熱比較，因此無法分離幾何散熱效應與偏壓/電流效應。
   4. 「hybrid FinFET」為非標準結構且其定義未在摘要中說明，外推到標準矽 bulk/SOI FinFET 的效度未知；把它的「Rth 對 Lg/Wfin/tbox 線性、對 Lpitch/N 非線性」依賴律直接搬到標準 FinFET 需要額外證據。
   5. Rth 的「線性／非線性」宣稱在摘要中沒有附任何擬合品質指標（R²、殘差、適用範圍），也無誤差棒、網格收斂或重複性資訊；摘要層級無從判斷其建模嚴謹度。
   6. 本文報的是「lattice temperature」而非明確的 ΔT，且未說明是通道中心值、峰值還是平均值。726.5 K 若為峰值熱點溫度，其與判準帶所用的通道平均溫升不可直接互換。

**6 可引用性**　C（僅可當背景引用）— 僅取得出版者摘要；兩個原文印出的數字（726.5 K → 495.6 K、50 μA → 103 μA）因缺偏壓與 TA 而不可用於校準，且溫度量級異常、結構非標準。只適合當「device pitch 與鰭密度對自熱影響極大」的背景引用，不可引用其溫度數字作為矽 FinFET 的代表值。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2018.04.015?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1016/j.mejo.2018.04.015
   - https://ouci.dntb.gov.ua/en/works/98NdXJx4/

**8 與原表差異**　與原表一致。原表「Hybrid FinFET (silicon), variable channel length, fin widt…」「Lattice T 726.5 -> 495.6 K vs pitch (up to ~430 K above ambient at tight pitch)」「not stated at abstract level（偏壓）」本次在 Semantic Scholar 取得的出版者摘要中逐字確認，無衝突（原表的「~430 K above ambient」係以 TA=300 K 推算，本次亦確認摘要未標 TA，故該推算的假設性質應保留）。補充原表未記載者：汲極電流 50 μA → 103 μA 與對應的 Lpitch 50 nm → 250 nm 區間、Rth 對 Lg/Wfin/tbox 為線性依賴而對 Lpitch/N 為非線性依賴、被掃描參數完整清單（Lg, Wfin, tbox, Lpitch, N）、期刊卷頁 Microelectronics Journal 76, 63-68、第一作者與 VIT Vellore 單位（單位來源為 ResearchGate 個人檔案，非論文署名頁）。原表 verdict=confirmed 成立。

---

## 五44 — Analysis on Self-Heating Effect in 7 nm Node Bulk FinFET Device

- **DOI／識別**：`10.5573/jsts.2016.16.2.204`　**來源**：非　**年**：2016
- **作者／單位**：第一作者 Sung-Won Yoo（Department of Electrical and Computer Engineering and Inter-university Semiconductor Research Center (ISRC), Seoul National University, Seoul 141-744, Republic of Korea）。共同作者：Hyunsuk Kim（同單位）、Myounggon Kang（Korea National University of Transportation, Department of Electronics Engineering, 50 Daehak-ro, Chungju-City, Chungbuk, Republic of Korea）、Hyungcheol Shin（SNU，通訊作者 hcshin@snu.ac.kr）。研究由 Samsung Electronics、ISRC 與 Brain Korea 21 Plus 支持。
- **出處**：Journal of Semiconductor Technology and Science (JSTS)，Vol.16, No.2, April 2016, pp. 204-209（ISSN 1598-1657 / 2233-4866）

**1 元件**　7 nm 節點 non-rectangular **bulk** FinFET（非 SOI、非 GAA、非 nanosheet、非 CFET）。元件參數依 ITRS 2013 roadmap Low Power (LP) 模式訂定。完整自熱模擬結構含 metal contact via 與 contact pad：via 材料為 tungsten (W)、pad 為 copper (Cu)，整體結構被 SiO2 包覆；通道含 LDD 區。n 通道（VGS = VDS = +0.78 V）。Fin height 以「2 nm/div」、Fin width 以「0.4 nm/div」的相對刻度掃描，【絕對 Hfin / Wfin / Lg 數值未印出】。主體為單元件單鰭；另模擬兩元件經 interconnect 相連（一開一關）與兩元件串聯兩種電路情境。

**2 方法與 SHE 定義**　`Rth-extraction`　Sentaurus device simulator，3D。載子與晶格溫度用 **Hydrodynamics charge balance model**（原文："Hydrodynamics charge balance model was used in order to consider local lattice and carrier temperature"）。熱邊界條件（本卡對使用者 deck 最關鍵的一句，原文）："thermal boundary condition at each node (gate, source, drain, and substrate) was specified from surface resistance"，並額外考慮各介面的 thermal resistance（"thermal resistance at various interface was also considered"）——【但四個節點的 SurfaceResistance 數值全文未印出】。降維熱導率原文印出："Thermal conductivity values at narrow Fin, S/D region and Bulk Si are 0.25, 0.62, 1.5 W/K·cm, respectively"（即 25 / 62 / 150 W·m^-1·K^-1）。Rth 萃取法：建立含五個節點（gate / source / drain / substrate / hot spot）的等效熱路，熱源置於 hot spot，各 Rth 由「ΔTLmax 對耗散功率」的線性斜率在限定熱路徑假設下取得（Fig.4）。無 BTE、無明確聲子輸運模型。

**3 關鍵定量結果**　【本文不做電熱 vs 等溫的 Ion 對照，故無 Ion 下降 %】。以下除註明者外皆為原文印出數字，偏壓為 VGS = VDS = 0.78 V、operation temperature（TA）= 300 K：(1) 峰值晶格溫度，原文："In this simulation, the TL of hot spot is 337.1 K"（→ ΔTLmax = 37.1 K）；熱點位置原文："the hot spot ... exists in the drain & Fin bottom region"。(2) 熱阻（Fig.4(b) 圖內標注，原文印出）：Rth(Gate) = 3.45 K/mW、Rth(Source) = 2.06 K/mW、Rth(Drain) = 1.96 K/mW、Rth(Substrate) = 1.18 K/mW、Rth(Total) = 1.05 K/mW；原文結論："Rth of gate is the largest, whereas Rth of substrate is the smallest. This means that the largest portion of heat caused by joule heating flows through the substrate."（單位一致性存疑，見 critique 第 2 點）。(3) Rth 隨溫度（Fig.7(b) 圖內標注，原文印出）：Rth(300K) = 1.05、Rth(325K) = 1.07、Rth(350K) = 1.10、Rth(375K) = 1.13 K/mW；原文："The Rth value increases with increasing TL (8% increase from 300 K to 375 K)"。(4) 互連情境，原文："The temperature of hot spot is 329.3 K which is smaller than that of hot spot in single Bulk FinFET device (337.1 K)"。(5) 串聯情境，原文："The temperature of hot spot is 320.4 K ... the fact that voltage applied on transistor 1 is approximately 0.59 V which is smaller than supply voltage (0.78 V)"。(6) 短通道指標，原文："drain induced barrier lowering (DIBL) value is extracted to 37.0 mV/V"（於 VDS = 0.05 V 與 0.78 V 兩條轉移曲線間萃取，T = 300 K）。(7) 僅圖層級（需自讀原圖）：Fig.5(a) ΔTLmax 隨 Fin height 增加由約 30 K 升至約 40 K（VGS=VDS=0.78 V）；Fig.6(a) ΔTLmax 隨 Fin width 增加由約 38.0 K 降至約 36.0 K（VGS=VDS=0.78 V）；Fig.7(a) ΔTLmax 隨 operation temperature 280→400 K 由約 34 K 升至約 44 K；Fig.3(b)(c) 沿通道方向與鰭高方向的 TL 分佈，縱軸 300-345 K；Fig.4(b)/5(b)/6(b)/7(b) 橫軸耗散功率 0-40「mW」。

**4 TCAD 校準用途**　【本批對使用者 TCAD deck 校準價值最高的一篇。】(1) 熱邊界架構可直接照抄：thermode 應設在 gate / source / drain / substrate 四個接點，各自以 SurfaceResistance 型熱邊界描述，而非把接點設成理想等溫面——這正是判準帶中「thermode 貼太近通道→SHE 被抹掉」的正確解方，也是使用者 deck 最關鍵的設定決策。(2) 降維熱導率可直接抄進 deck：窄鰭 0.25、S/D 區 0.62、bulk Si 1.5 W/K·cm（= 25 / 62 / 150 W·m^-1·K^-1），這是 7 nm 級 bulk FinFET 的合理取值，可用來校準 ThermalConductivity 模型的薄膜退化程度。(3) ΔT 錨點：VGS = VDS = 0.78 V、TA = 300 K 下 ΔTLmax = 37.1 K。使用者在 VDD ≈ 0.7 V 的 bulk FinFET 上應落在同一量級（數十 K）；若差一個數量級就必須回頭檢查 thermode 位置與 SurfaceResistance。(4) 可 sanity-check 的比值：以 ΔT = 37.1 K 搭配交叉檢核比值 0.10-0.20 %/K，預期 Ion 下降約 3.7-7.4%，恰落在 bulk 判準帶 3-12% 的下半段，並與核心錨點「14nm FinFET n 7.26% @VDS=0.7V」「bulk FinFET 7.8%（STI 研究）」同量級——這是本批唯一能與核心錨點形成閉環交叉檢核的一篇。(5) 熱阻分配比例可用於檢查 deck 各 thermode 的相對熱阻是否合理：Rth(Gate) : Rth(Source) : Rth(Drain) : Rth(Substrate) ≈ 3.45 : 2.06 : 1.96 : 1.18，且基板應為主要散熱路徑。(6) 熱點位置錨點：drain 側與鰭底交界，可用來驗證 deck 溫度分佈是否合理。【注意】SurfaceResistance 的絕對數值本文未給，仍需另尋來源；Rth 的功率單位需先做單位重建（見 critique 第 2 點）。

**5 批判**
   1. ΔT 落在判準帶內：VGS = VDS = 0.78 V、TA = 300 K 下 ΔTLmax = 37.1 K，以交叉檢核比值 0.10-0.20 %/K 換算對應 3.7-7.4% 的 Ion 降，落在 bulk 判準帶 3-12% 內，且與核心錨點 14nm FinFET n 7.26%、bulk FinFET 7.8% 同量級，判為帶內。惟必須明確標示：本文並未實際報告 Ion 退化 %，上述為以判準帶比值反推的推算值，不是原文數字，論文中引用時務必註明。
   2. 【本卡最重要的一點：Rth 單位嚴重存疑】本文印出 Rth(Total) = 1.05 K/mW = 1.05×10^3 K/W，比判準帶的 single-fin 1-4 MK/W 低約 3 個數量級。用本文自身數字做內部一致性檢查：ΔT = 37.1 K ÷ 1.05 K/mW → 耗散功率 ≈ 35.3 mW；在 0.78 V 下等於 ≈ 45 mA 汲極電流，單根 7 nm 節點的鰭絕無可能承載此電流。反之若 Fig.4/5/6/7 橫軸的「Power [mW]」實為 μW，則耗散功率 ≈ 35.3 μW → Id ≈ 45 μA（對 7 nm LP 單鰭完全合理），且 Rth(Total) = 1.05 MK/W **恰好落在 1-4 MK/W 判準帶內**。因此高度懷疑本文功率軸單位為 μW 誤植為 mW。使用者若要引用此 Rth，必須以「Rth(Total) ≈ 1.05 MK/W」的重建解讀使用，並在論文中明確註記此單位推論。
   3. 熱邊界的關鍵參數缺席：本文明確採用 surface resistance 型熱邊界（做法正確，避免理想等溫接點把 ΔT 抹掉），但四個節點的 SurfaceResistance 數值一個都沒印出，各介面的 thermal resistance 值亦未給。因此本文只能提供「架構」而不能提供「參數」，要完整重現其結果需另尋來源或聯繫作者。
   4. 幾何參數不完整：Fin height / Fin width 掃描僅給相對刻度（2 nm/div、0.4 nm/div）而無絕對值，ITRS 2013 LP 7 nm 的實際 Hfin / Wfin / Lg 也未印出。這使「ΔTLmax 隨 Fin height 由約 30 K 升至約 40 K」這條敏感度曲線無法定量對齊到使用者的幾何，只能取其趨勢與斜率符號。
   5. 【分類陷阱警示】Fig.7 是 operation temperature 掃描（280-400 K），本質是 ta_sweep，量的是「環境溫度改變如何放大自熱幅度」，不是 SHE 本身。使用者若把 Fig.7(a) 的 ΔTLmax 上升（約 34 K → 約 44 K）誤讀成自熱造成的溫升，就會犯下判準明列的 ta_sweep 誤判。本篇真正的 SHE 錨點是 Fig.3/Fig.4 的 37.1 K；Fig.7 的正確用途是校準「Rth 的溫度係數」（+8% / 75 K）。
   6. 互連（329.3 K）與串聯（320.4 K）情境不是等偏壓比較：串聯時 Tr.1 實際只承受約 0.59 V 而非 0.78 V，溫度下降有相當比例來自偏壓下降而非散熱路徑改善，本文自己也承認此點。引用時絕不可把 320.4 K 表述成「互連散熱使溫度降低 17 K」。相對地，一開一關的 329.3 K 情境偏壓未變，才是較乾淨的互連散熱證據。
   7. 無誤差棒、無網格收斂測試、無與實驗量測的自熱驗證。全文唯一的電性對照指標是 DIBL = 37.0 mV/V，且未附實驗數據比對。Fig.2 的 ID 軸為 A.U.（arbitrary units），連 Ion 絕對值都無法讀出——這正是本文無法提供 Ion 退化 %、也無法讓讀者自行驗證上述功率單位疑義的根本原因。

**6 可引用性**　A（可直接引用數字）— 全文取得、方法段與偏壓條件完整標注，多個關鍵數字為原文印出且無歧義，可直接引用：ΔTLmax = 37.1 K（hotspot TL = 337.1 K）@ VGS=VDS=0.78 V / TA=300 K、降維熱導率 0.25 / 0.62 / 1.5 W/K·cm、DIBL = 37.0 mV/V、互連 329.3 K、串聯 320.4 K（含 Tr.1 實際壓降約 0.59 V 的但書）、Rth 溫度係數 +8%（300→375 K）。唯一例外是 Rth 絕對值系列（1.05-3.45 K/mW）：引用時必須附註單位一致性疑義並說明重建為 MK/W 的依據（見 critique 第 2 點），不可原樣照抄。

**7 取得狀態**　全文
   - https://koreascience.kr/article/JAKO201614137726152.pdf
   - https://api.openalex.org/works/doi:10.5573/jsts.2016.16.2.204
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.5573/jsts.2016.16.2.204?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf

**8 與原表差異**　與原表一致並大幅補充。原表「7nm node 非矩形 bulk FinFET(ITRS 2013 LP),含 W contact via 與 C…」「ΔTLmax~37.1 K(hotspot TL=337.1 K @TA=300K)」「兩元件互連(一開一關)時 hotspot 329.3 K」「兩管串聯時 320.4 K(Tr.1 實際壓降僅約 0.59 V,非等偏壓比較)」「VGS=VDS=0.78 V, TA=300 K(Figs.5-7 標注)」「DIBL=37.0 mV/V」本次全部在全文中逐字確認，無任何衝突，原表判讀精確。補充原表未記載者：(a) 求解器為 Sentaurus device simulator + Hydrodynamics charge balance model；(b) 熱邊界為 gate/source/drain/substrate 四節點的 surface resistance 型（數值未印出）；(c) 降維熱導率 narrow Fin / S/D / bulk Si = 0.25 / 0.62 / 1.5 W/K·cm；(d) 熱阻 Rth(Gate/Source/Drain/Substrate/Total) = 3.45 / 2.06 / 1.96 / 1.18 / 1.05 K/mW，主要散熱路徑為基板；(e) Rth 隨溫度 1.05 / 1.07 / 1.10 / 1.13 K/mW（300/325/350/375 K，+8%）；(f) 熱點位於 drain 與鰭底交界；(g) contact pad 材料為 Cu、結構被 SiO2 包覆；(h) 完整四位作者與 SNU/ISRC、韓國交通大學單位。另標【CORRECTION 候選 — 指向原文而非原表】：本文 Rth 的功率單位 mW 與元件物理不自洽（會推得單鰭 45 mA），依內部一致性推論應為 μW，重建後 Rth(Total) = 1.05 MK/W 正好落入 1-4 MK/W 判準帶，詳見 critique 第 2 點；此為本次新增發現，原表未涉及 Rth 故無衝突。

---

## 五45 — DC self-heating effects modelling in SOI and bulk FinFETs

- **DOI／識別**：`10.1016/j.mejo.2015.02.003`　**來源**：非　**年**：2015
- **作者／單位**：第一作者 B. González（Universidad de Las Palmas de Gran Canaria, Spain；通訊作者）。共同作者：J.B. Roldán（Universidad de Granada, Spain）、B. Iñiguez（Universitat Rovira i Virgili, Spain）、A. Lázaro（Universitat Rovira i Virgili, Spain）、A. Cerdeira（CINVESTAV, Mexico）。單位來源：OpenAlex 作者機構欄位。
- **出處**：Microelectronics Journal（Elsevier），Volume 46, Issue 4, pp. 320-326

**1 元件**　奈米級矽 **SOI 與 bulk FinFET 兩者皆涵蓋**；模型由 single-fin 元件推廣到 multi-fin / multi-finger 元件。摘要僅陳述「different gate lengths and biases」與「multi-fin devices with multiple fingers」。【未取得】技術節點、Lg 的具體數值、Hfin / Wfin / tbox 幾何、n 或 p 型別、實際鰭數與指數。非 GAA / nanosheet / CFET。

**2 方法與 SHE 定義**　`model`　摘要層級：建立 DC 熱效應之解析（compact）模型，同時納入 self-heating effects (SHEs)、velocity saturation 與 short-channel effects。SHE 以**等效熱路（equivalent thermal circuit）**求得的熱阻進行深入分析，並納入元件內超薄膜的**熱導率退化**（原文："accounting for the degraded thermal conductivity of the ultrathin films within the device"）。驗證流程：single-fin 元件的熱阻先在不同閘長與偏壓下，以 **Sentaurus Device** 數值模擬的輸出特性與元件溫度做比對驗證（原文："comparing the modelled output characteristics and device temperatures with numerical simulations obtained using Sentaurus Device"），再以電路分析推廣到多鰭多指（原文："the thermal model is extended by circuital analysis to multi-fin devices with multiple fingers"）。【全數未取得】Sentaurus 的熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型、網格設定。

**3 關鍵定量結果**　【未取得任何數值】。摘要層級僅有定性條列（原文）："Self-heating has been included in a drain current model for SOI and bulk FinFETs." 與 "The FinFET thermal resistance model includes the role of multiple fingers and fins."。無 Rth 數值、無 ΔT、無峰值晶格溫度、無 Ion 下降 %、無任何偏壓條件（VGS / VDS / TA）。

**4 TCAD 校準用途**　不可直接校準，理由：本次未取得任何 Rth / ΔT / Ion 退化的數值，摘要層級完全不含數字。【但方法論價值明確】本篇是本批唯一同時處理 SOI 與 bulk FinFET、且明確以等效熱路把「單鰭 Rth」串接推廣到「多鰭多指 Rth」的建模文獻，正好對應判準帶中「single-fin Rth 約 1-4 MK/W」與「多鰭多指 RF 結構約 34 kK/W」這兩個相差約兩個數量級的量級之間的橋樑。使用者若需在論文中解釋自己的 deck 從單鰭外推到多鰭時 Rth 為何下降兩個數量級，這是應優先取得全文並引用的方法來源。另「超薄膜熱導率退化」的建模，可作為 deck 中必須開啟 ThermalConductivity 薄膜退化模型的定性依據。

**5 批判**
   1. 無數值可判定，原因：全文位於 Elsevier 付費牆後；Semantic Scholar 標示的 GREEN OA PDF（ULPGC accedaCRIS）與其 handle 頁本次實測皆回 HTTP 403，無法取得。因此連一個 Rth 或 ΔT 數字都沒有，無法與 1-4 MK/W、34 kK/W 或 0.10-0.20 %/K 任一判準帶對照。
   2. 【取得性陷阱，重要】Semantic Scholar 的 openAccessPdf 欄位指向 accedacris.ulpgc.es 的一個檔案並標為 GREEN / CC-BY-NC-ND，看似可用；但該 URL 在搜尋結果中的頁面標題顯示為另一篇論文（"Optimisation of the δ-Doped Layer Concentration"），且本次 403 無法驗證其內容。使用者切勿把該連結當成本篇全文引用——這是 metadata 聚合器常見的 OA 連結錯配，若據以引用會產生對不上原文的引用錯誤。
   3. 方法論本質：這是 compact model / 解析建模論文，不是元件量測或純 TCAD 數值研究，其 Rth 是模型輸出並以 Sentaurus 反向驗證，屬「二次結果」。若使用者拿它的 Rth 去校準自己的 TCAD deck，等於用一個以 TCAD 校準過的解析模型再去校準 TCAD，存在循環驗證風險；引用前必須確認其 Sentaurus 熱邊界設定與使用者 deck 一致。
   4. 摘要未給任何幾何、偏壓，也未說明 SOI 與 bulk 兩者的 Rth 差距。判準帶中 bulk 3-12% 與 SOI 8-17% 的分帶差異，正是本篇最可能直接回答的問題，但沒有全文就完全無法取用——這使本篇成為本批中「取得全文的邊際效益最高」的一篇。
   5. 年代較早（2015）且未指明技術節點。把 2015 年的超薄膜熱導率退化模型參數直接套用到使用者關心的先進節點前，需檢查該模型的適用膜厚範圍與聲子平均自由程假設是否仍成立。
   6. 無誤差棒、無重複性或收斂性資訊；摘要層級亦無從判斷其對 multi-fin 熱耦合（相鄰鰭之間的熱串擾）是否採用純電阻網路近似而忽略了分佈式熱擴散。

**6 可引用性**　C（僅可當背景引用）— 僅取得摘要層級、零數值；只能當「SOI/bulk FinFET 自熱之熱阻等效電路建模，並含多鰭多指推廣」的方法背景引用，不可引用任何數字。取得訂閱全文後有機會升為 A（其單鰭→多鰭 Rth 換算正是使用者最需要的環節）。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2015.02.003?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.mejo.2015.02.003
   - https://api.crossref.org/works/10.1016/j.mejo.2015.02.003

**8 與原表差異**　原表記載為「奈米級 SOI 與 bulk Si FinFET, 單 fin 至 multi-fin/multi-finger」「not accessed」「not accessed」，本次仍未取得全文，故結果欄維持「未取得」，與原表無衝突。但本次補上了原表所無的摘要層級資訊：完整作者群五人與五個單位（ULPGC / Universidad de Granada / URV ×2 / CINVESTAV）、期刊卷期頁碼（Microelectronics Journal 46(4), 320-326, 2015）、方法為含 SHE + velocity saturation + short-channel effects 的解析模型、以等效熱路求 Rth、納入超薄膜熱導率退化、single-fin 先以 Sentaurus Device 在不同閘長與偏壓下驗證後再以電路分析推廣到 multi-fin/multi-finger。原表對元件的描述（單 fin 至 multi-fin/multi-finger）本次獲摘要證實。另新增一項取得性警訊（非原表錯誤）：Semantic Scholar 標示的 GREEN OA PDF 連結疑似錯配到他篇論文且實測 403，不可作為本篇全文來源，詳 critique 第 2 點。原表 verdict=confirmed（書目層級）成立。

---
