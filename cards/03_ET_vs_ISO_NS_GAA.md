# 第三章 · ET-vs-ISO｜nanosheet / GAA

_相鄰技術，趨勢對照用_

原表 14 篇｜本檔 14 篇｜取得層級：摘要 7、全文 5、僅metadata 2

## 三01 — Influences of Source/Drain Extension Region on Thermal Behavior of Stacked Nanosheet FET

- **DOI／識別**：`10.1109/ted.2024.3351596`　**來源**：IEEE　**年**：2024
- **作者／單位**：Shobhit Srivastava（第一作者），Department of Electronics Engineering, VLSI Design Group, Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat, Gujarat, India；共同作者 Sourabh Panwar、M. Shashidhara、Abhishek Acharya（同單位），Lomash Chandra（Dept. of ECE, IIT Roorkee），Neeraj Mishra（IDLab, Ghent University, Belgium）
- **出處**：IEEE Transactions on Electron Devices, Vol. 71, No. 3, pp. 2171–2176

**1 元件**　Stacked nanosheet FET（GAA 堆疊奈米片），核心變數為 source/drain extension length LEXT，自 2 nm 掃到 8 nm。技術節點、Lg、奈米片厚度 TNS 與寬度 WNS、堆疊層數、n 或 p 通道、指數：摘要未載明，未取得（需全文）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　摘要自述為「A well-calibrated numerical-simulation-based study」，即經校準的數值模擬（TCAD），但摘要未指名求解器（推測 Sentaurus，屬推測，未取得）。SHE 的處理方式：摘要以「ION degradation (~10%) due to the self-heating effect (SHE)」「gm degradation (~15%) due to SHE」「ΔG ... in self-heating condition」等措辭陳述，可判定為含 SHE 與不含 SHE 兩組解的對照（ET-vs-ISO）。熱邊界條件、thermode 位置、SurfaceResistance 數值、有無 hydrodynamic／BTE／聲子模型：摘要全部未載，未取得。

**3 關鍵定量結果**　以下皆為摘要中原文印出數字（IEEE 全文為付費牆，未取得）。ION：「it holds a smaller penalty in ION degradation (~10%) due to the self-heating effect (SHE)」，對應 LEXT = 8 nm；LEXT = 2 nm 的對應百分比未印出。gm：「The longer extension lengths (2–8-nm increase) provide a lesser transconductance (gm) degradation (~15%) due to SHE」。共源放大器增益退化：「a smaller degradation ΔG (from ~12.4% to ~6.6%) in gain with longer extension length」，且 LEXT = 8 nm 相對 2 nm 在無自熱時提供約 1.87× 電壓增益、在自熱條件下增至約 1.97×。非 SHE 的伴隨結果：LEXT 由 2 nm 增至 8 nm 時 IOFF 降低 16×、次臨界擺幅降低約 9 mV/dec、VT 變化約 15 mV、傳播延遲降低約 20%。最佳化結論：「the optimum LEXT would be 5–6 nm」。偏壓（VGS / VDS / TA）：摘要未載，未取得。Rth：未取得。ΔT／峰值晶格溫度：未印出於摘要（摘要僅提到「Considering lattice heat due to SHE」），未取得。

**4 TCAD 校準用途**　不可直接校準 thermode，理由：熱邊界條件、thermode 位置、SurfaceResistance、ΔT、Rth 全部未取得，且連偏壓與奈米片幾何都未印於摘要，沒有任何一個量可對回使用者的 deck 參數。可用之處僅有兩點：(1) sanity check——若使用者把 deck 改成堆疊 nanosheet，SHE 造成的 Ion 下降約 10% 是一個合理的量級參考（但這是 LEXT = 8 nm 這個「最有利」條件下的值，是下界不是典型值）；(2) 設計啟示——S/D extension 長度是 SHE 強度的一階旋鈕，拉長 extension 會同時降低絕對 ION 又降低 SHE 百分比，使用者在做 FinFET SHE 掃描時若 S/D extension 長度沒固定，會把幾何效應誤讀成 SHE 強度變化。

**5 批判**
   1. 判準帶判定：~10% 這個數值落在判準帶的數值區間內（bulk 3–12%、核心錨點 7–11% 都涵蓋 10%），但元件類別在判準帶之外——判準帶是為標準矽 FinFET 訂的，本文是 GAA 堆疊 nanosheet，幾何侷限更強、散熱路徑被 inner spacer 與 sheet 間介電層切斷，理論上應比 FinFET 更嚴重。因此「剛好落在 FinFET 帶內」反而值得懷疑：可能是 LEXT = 8 nm 這個最有利條件、也可能是熱邊界偏導熱。無偏壓、無 ΔT 可做 %/K 交叉檢核，無法判斷是哪一種。
   2. 數字的條件被摘要的敘述方式遮蔽：~10% 是在 LEXT = 8 nm 時的「smaller penalty」，也就是整個 LEXT 掃描中退化最小的那一點。若引用成「stacked nanosheet FET 的 SHE 約 10%」會系統性低估——LEXT = 2 nm 的值更大但未印出。這是本卡最容易被誤用的地方。
   3. 缺 %/K 交叉檢核所需的第二個量：完全沒有 ΔT 或峰值晶格溫度數字，因此無法算 ΔIon%/ΔT 比值，也就無法判斷 thermode 是過絕熱還是過導熱。這是把它排除在「可校準」之外的決定性理由。
   4. 含糾纏因子：LEXT 掃描同時改變了 access resistance、Cgg、VT（約 15 mV 漂移）、IOFF（16×）與 SS（9 mV/dec），這些全部會影響 ON 電流與功耗，進而回頭改變自熱功率。摘要把 ION 退化 10% 單獨歸因於 SHE，但在 VT 漂移 15 mV 的情況下，SHE 與靜電效應並未乾淨分離。
   5. 分類無誤，但「well-calibrated」未說明校準對象：摘要自稱經良好校準卻未指出對到哪一組實驗資料或哪一個工業元件，這在只有摘要的情況下無法查證，屬於不可驗證的自我宣稱。
   6. 無誤差棒、無重複性資訊：純模擬論文，摘要未提供任何不確定度或參數敏感度範圍。

**6 可引用性**　A（可直接引用數字）— ~10% ION 退化、~15% gm 退化、ΔG 12.4% → 6.6%、IOFF 16×、SS 9 mV/dec、最佳 LEXT 5–6 nm 這些數字都是 IEEE 官方摘要中逐字印出的，可直接引用並標明條件（LEXT = 8 nm）。但因偏壓與熱邊界未取得，引用時必須連同「條件未載明」一起註記，不可當作 TCAD 校準錨點使用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2024.3351596?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/TED.2024.3351596
   - https://api.openalex.org/works/doi:10.1109/ted.2024.3351596

**8 與原表差異**　與原表一致。原表記載的「Stacked nanosheet FET with S/D extension length LEXT swept…、~10% ION degradation attributed to SHE at LEXT = 8 nm（longer extension lowers absolute ION but carries a smaller SHE penalty）、bias: not stated in abstract、dT: not printed in abstract」全部與 IEEE 官方摘要逐字核對相符，無衝突。本次補充原表未載的出處與數字：期刊卷期頁碼 IEEE T-ED Vol. 71, No. 3, pp. 2171–2176（Crossref）；完整作者名單含 M. Shashidhara（Semantic Scholar 的作者清單漏列此人，Crossref 完整，非原表問題）；第一作者單位 SVNIT Surat；摘要另印出 gm 退化 ~15%、ΔG 由 ~12.4% 降至 ~6.6%、IOFF 降 16×、SS 降 ~9 mV/dec、VT 變化 ~15 mV、延遲降 ~20%、最佳 LEXT = 5–6 nm。OpenAlex 確認 oa_status = closed、無任何 repository 全文，故全文確實無法取得。

---

## 三02 — Electro-Thermal Characteristics of Junctionless Nanowire Gate-All-Around Transistors Using Compact Thermal Conductivity Model

- **DOI／識別**：`10.1109/ted.2023.3268249`　**來源**：IEEE　**年**：2023
- **作者／單位**：Nitish Kumar（第一作者），Centre for Applied Research in Electronics (CARE), Indian Institute of Technology Delhi, New Delhi, India；共同作者 Sushil Kumar、Pragyey Kumar Kaushik、Ankur Gupta、Pushpapraj Singh（皆同單位）
- **出處**：IEEE Transactions on Electron Devices, Vol. 70, No. 6, pp. 2934–2940

**1 元件**　sub-5 nm 技術節點的 junctionless nanowire（JL-NW）gate-all-around 電晶體，製作於 silicon-on-insulator (SOI) 晶圓上（摘要明言薄主動層會限制 Si 熱導率並激化 SHE）。Lg、奈米線直徑／截面、堆疊或並列根數、n 或 p 通道：摘要未載明，未取得。摻雜組合涵蓋 phosphorus/boron 與 arsenic/boron 兩種。

**2 方法與 SHE 定義**　`model`　求解器：Sentaurus TCAD（摘要明確提到與 Sentaurus 內建的 Connelly thermal conductivity model, CN-TCM 做比較）。方法主體是熱導率模型本身：作者提出並升級既有的 compact thermal conductivity model (C-TCM)，加入 phosphorus 摻雜效應，使其可處理任意 phosphorus/boron 或 arsenic/boron 摻雜組合，並宣稱以已發表的實驗資料驗證。對照組為 Sentaurus 的 CN-TCM，摘要指出「The CN-TCM is only valid for undoped conditions at room temperature」。另含環境溫度 TA 變異分析（ta_sweep 成分）。熱邊界條件、thermode 位置、SurfaceResistance 數值、有無 hydrodynamic／BTE／聲子輸運求解：摘要未載，未取得。

**3 關鍵定量結果**　以下為摘要中原文印出數字（IEEE 全文付費牆，未取得）。ON 電流與遷移率：「SHE rises the peak of TL, causing ~10% ON-current and ~0.7% mobility degradation」。閘極漏電：「gate leakage current (IG) is enhanced by a factor of ~55」（SHE 對 HCI 的影響）。晶格溫度：摘要僅定性陳述「the nonuniform lattice temperature (TL) and heat generation were observed along the channel length due to the non-uniformity κ of the device」，未印出任何 TL 數值或 ΔT（未取得，且非圖層級——連圖說都沒讀到）。偏壓（VGS / VDS / TA）：摘要未載明具體數值，僅說明是 on-state 並含 TA 變異；未取得。Rth：未印出（未取得）。

**4 TCAD 校準用途**　不可直接校準 thermode，理由：Rth、SurfaceResistance、ΔT、峰值 TL、偏壓全部未取得，且元件是 junctionless nanowire GAA 而非矽 FinFET。真正對使用者 deck 有價值的是一個模型層級的警告：摘要明確指出 Sentaurus 內建的 Connelly 熱導率模型（CN-TCM）「只在未摻雜、室溫條件下有效」。使用者的 FinFET deck 若沿用 Sentaurus 預設 Connelly 模型，而通道／S/D 有重摻雜、或要掃 TA，則熱導率會被系統性算錯，ΔT 與 Ion 下降幅度都會偏掉——這會直接汙染 thermode 校準的結果。因此本文的實用價值是：提醒使用者在 deck 裡明確檢查 Thermal Conductivity 模型的適用範圍與摻雜相依性，必要時改用摻雜相依的熱導率模型或自訂 κ(N, T)。~10% 的 ON 電流退化只能當數量級 sanity check，不可當 FinFET 錨點。

**5 批判**
   1. 判準帶判定：~10% 落在判準帶的數值區間內（bulk 3–12%、SOI 8–17% 都涵蓋 10%），但元件明確被判準帶排除——判準帶注明「排除 DMG / junctionless 特例」，而本文正是 junctionless nanowire GAA on SOI。junctionless 元件的通道全程重摻雜，其熱導率被雜質散射壓低、且遷移率的溫度相依性與反轉型元件不同，因此 10% 這個數字不能與 14nm FinFET 的 7.26%/8.91% 或 3nm bulk 的 10.6%/21.6% 並列比較。
   2. 數字是模型相依的，不是元件相依的：本文的核心貢獻是自家的 C-TCM 熱導率模型。~10% 這個 ON 電流退化是在 C-TCM 之下算出來的；若改用 Sentaurus 預設的 CN-TCM，同一顆元件會得到不同的 ΔT 與退化百分比（這正是本文要證明的事）。所以引用這個數字時必須連模型一起講，否則等於引用了一個沒有定義的量。
   3. 分類陷阱在場：摘要同時含 TA 變異分析（ambient temperature variation）與 SHE 分析。TA sweep 是改環境溫度，不是自熱——若把 TA 掃描下的電流變化誤讀成 SHE，會嚴重高估。本卡把 method_type 定為 model 而非 ET-vs-ISO，正是因為論文主體是熱導率模型；~10% 是模型的應用結果，TA 掃描是第三條獨立的軸，三者不可混淆。
   4. 缺 %/K 交叉檢核：完全沒有 ΔT 或峰值 TL 數值，無法計算 ΔIon%/ΔT，因此無法判斷其熱邊界是過絕熱或過導熱。摘要只說 TL 沿通道不均勻，這是 SHE 論文的通例陳述，資訊量為零。
   5. 含糾纏因子且量級可疑：IG 增強 ~55× 是把 SHE 與 HCI 綁在一起的結果，並非純 SHE。~55× 這個量級對閘極漏電而言極大，在只有摘要、沒有偏壓與氧化層厚度的情況下無法判斷合理性，引用風險高。
   6. 模型驗證僅自述：摘要宣稱 C-TCM「validated with reported experimental data」，但未指出對到哪一組實驗、涵蓋什麼摻雜濃度與溫度範圍。無誤差棒、無重複性資訊。

**6 可引用性**　A（可直接引用數字）— ~10% ON-current 退化、~0.7% 遷移率退化、IG 增強 ~55× 均為 IEEE 官方摘要逐字印出，可直接引用；原表所引「SHE rises the peak of TL, causing ~10% ON-current [degradation]」也已逐字核對相符。但因元件屬 junctionless GAA、數字又與作者自家 C-TCM 模型綁定，引用時必須同時標注元件類別與模型，且不可用作矽 FinFET 的校準錨點。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2023.3268249?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/TED.2023.3268249
   - https://api.openalex.org/works/doi:10.1109/ted.2023.3268249

**8 與原表差異**　與原表一致。原表記載「sub-5 nm 節點 junctionless 奈米線 GAA(SOI)、SHE 造成約 10% ON-current 劣化、摘要逐字確認『SHE rises the peak of TL, causing ~10% ON-current [degradation]』、bias: on-state（摘要未列 VGS/VDS 數值）、dT: 通道內非均勻 TL 峰值（摘要無數值）」全部逐字核對相符，無衝突。本次補充原表未載的內容：完整標題含「Using Compact Thermal Conductivity Model」（論文主體其實是熱導率模型 C-TCM，而非單純 SHE 模擬）；同一句摘要還印出 ~0.7% mobility degradation；另印出 gate leakage current 增強 ~55×；摘要明言 Sentaurus 內建的 Connelly 熱導率模型「only valid for undoped conditions at room temperature」——這是本文對使用者 deck 最有價值的一句；出處為 IEEE T-ED Vol. 70, No. 6, pp. 2934–2940，第一作者單位為 IIT Delhi CARE（Crossref）。OpenAlex 確認 oa_status = closed。

---

## 三03 — Device Design Aware and Interface Thermal Resistance Assisted Self-Heating Analysis in Nanosheet FET

- **DOI／識別**：`10.1109/icee56203.2022.10117683`　**來源**：IEEE　**年**：2022
- **作者／單位**：Sunil Rathore（第一作者），ECE Department, PDPM Indian Institute of Information Technology, Design and Manufacturing (IIITDM) Jabalpur, India；共同作者 Shashank Kumar Banchhor（Dept. of ECE, IIT Roorkee）、Rajeewa Kumar Jaisawal（IIITDM Jabalpur）、Ankit Dixit（Electronics and Nanoscale Engineering, University of Glasgow, Scotland）、Pravin N. Kondekar、Navjeet Bagga（IIITDM Jabalpur）
- **出處**：2022 IEEE International Conference on Emerging Electronics (ICEE), pp. 1–4

**1 元件**　Gate-all-around nanosheet FET（NSHFET）為主體，並與 SOI FinFET 及 bulk FinFET 做公平比較。技術節點、Lg、奈米片厚度 TNS 與寬度 WNS、堆疊層數、n 或 p 通道、鰭數／指數：摘要未載明，未取得（需全文）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　求解器：摘要自述「well-calibrated TCAD models」，未指名工具（IIITDM Jabalpur 該組慣用 Sentaurus，但摘要未載，屬推測，未取得）。分析軸有三：(i) GAA NSHFET 內的空間晶格溫度 TD 梯度；(ii) 掃描 drain、source、gate 三個電極的熱接觸電阻 Rth,DSG——摘要原文「the impact of varying the drain, source, and gate electrode thermal contact resistances (Rth,DSG)」，這在 Sentaurus 中即對應 Thermode 的 SurfaceResistance；(iii) SOI FinFET / bulk FinFET / NSHFET 三者在 SS、DIBL、drain current 百分比變化上的公平比較（百分比變化即含 SHE 與不含 SHE 的對照，故歸為 ET-vs-ISO）。Rth,DSG 的具體掃描範圍與單位、熱邊界其餘設定、有無 hydrodynamic／BTE／聲子模型：摘要未載，未取得。

**3 關鍵定量結果**　全部數值未取得。IEEE 全文為付費牆，OpenAlex 確認 oa_status = closed 且無任何 repository 全文，Semantic Scholar 亦無 openAccessPdf。摘要僅有定性陳述，無任何印出的數字：無 Ion 下降 %、無 Rth 數值、無 ΔT、無峰值晶格溫度、無偏壓（VGS / VDS / TA）。摘要中與結果最接近的逐字句為：「a fair comparison of electrical and thermal characteristics of SOI FinFET, bulk FinFET, and NSHFET based on the percentage change in subthreshold slope (SS), drain-induced barrier lowering (DIBL), drain current」——確認論文內文確實以 drain current 的百分比變化做三種架構的比較，但數值僅存在於全文的圖表中，本次未能取得，屬「未取得」而非「僅圖層級」（連圖說都未讀到）。

**4 TCAD 校準用途**　不可直接校準，理由：所有數值（Rth,DSG 掃描範圍、Ion 下降 %、ΔT、峰值 TL、偏壓）都未取得。這一點特別可惜，因為就研究設計而言，本文是本批七篇中概念上最貼近使用者需求的一篇——它正是在掃 drain/source/gate 電極的熱接觸電阻（等同 Sentaurus thermode 的 SurfaceResistance），而且同時給出 bulk FinFET、SOI FinFET、NSHFET 三者的並列比較，若能取得全文，其 Rth,DSG 掃描範圍與對應的 drain current 百分比變化可以直接當成 thermode 設定的校準曲線。強烈建議使用者透過學校 IEEE Xplore 訂閱取得全文（DOI 10.1109/ICEE56203.2022.10117683，document 10117683），優先看 Rth,DSG 掃描那張圖與三架構比較表。

**5 批判**
   1. 判準帶判定：無數值可判定，原因：僅取得摘要，全文為 IEEE 付費牆（OpenAlex 確認 closed、無 repository 版本），摘要通篇無任何印出的百分比、溫度或熱阻數字，因此既無法判斷是否落在 bulk 3–12% / SOI 8–17% 帶內，也無法做 %/K 交叉檢核。
   2. 研究設計本身值得肯定但無法查證：摘要宣稱做了「fair comparison」三架構比較，但公平比較的條件（是否對齊 Ioff、Vt、DIBL？是否對齊有效通道寬度或驅動電流？）完全未說明。SHE 比較最常見的失真來源就是三種架構的有效寬度與偏壓沒對齊，這在只有摘要時無從檢驗。
   3. 會議論文篇幅限制帶來的固有風險：ICEE 為 4 頁會議論文（Crossref 顯示 pp. 1–4），即使取得全文，方法細節（熱導率模型、基板厚度、熱沉位置、Rth,DSG 的絕對數值與單位）也可能相當簡略，未必足以完整重建 deck。引用前應先確認全文是否真的給出 Rth,DSG 的數值範圍而非僅給相對趨勢。
   4. 分類判定：本文不是 ta_sweep 陷阱（摘要未提環境溫度掃描），也不是 Rth-extraction（作者是「施加／掃描」熱接觸電阻，不是從量測反萃取 Rth），歸為 ET-vs-ISO 是基於摘要明確的「percentage change in ... drain current」措辭。但這個歸類本身是從摘要推得，若取得全文發現百分比變化是指幾何間的變化而非 SHE on/off 的變化，分類需要修正。
   5. 出處資訊有一項第三方錯誤需留意：Semantic Scholar 把 venue 標成「International Conference on E-Business and E-Government」，這是縮寫 ICEE 撞名造成的資料庫誤植。正確場次為 2022 IEEE International Conference on Emerging Electronics (ICEE)。使用者若直接抄 Semantic Scholar 的 BibTeX 會引錯會議名。
   6. 無誤差棒、無重複性、無實驗校準證據可查：摘要自述 well-calibrated 但未指出校準對象。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用。全文未取得、摘要零數字，只能用來支持「已有研究以電極熱接觸電阻為旋鈕分析 NSHFET 的 SHE，並對 SOI FinFET / bulk FinFET / NSHFET 做過並列比較」這類文獻脈絡陳述，不可引用任何數值。若使用者能取得全文，本篇的評級有機會升到 A。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/icee56203.2022.10117683?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/ICEE56203.2022.10117683
   - https://api.openalex.org/works/doi:10.1109/icee56203.2022.10117683

**8 與原表差異**　與原表一致。原表記載「GAA 奈米片 FET(NSHFET)，並與 SOI FinFET、bulk FinFET 做電熱特性公平比較；figure-level（摘要逐字證實以 drain current 百分比變化比較三者，數值僅在內文圖表，未能取得）；bias: 未載於摘要（未讀取全文）；dT: 空間晶格溫度梯度（數值在全文，未讀取）」全部與 IEEE 官方摘要逐字核對相符，本次同樣未能取得全文，維持原判定，無衝突。補充原表未載的出處：2022 IEEE International Conference on Emerging Electronics (ICEE), pp. 1–4，第一作者 Sunil Rathore（IIITDM Jabalpur），共同作者含 University of Glasgow 的 Ankit Dixit（Crossref）。CORRECTION（針對 Semantic Scholar 資料庫，非針對原表）：S2 將 venue 誤植為「International Conference on E-Business and E-Government」，正確為 2022 IEEE International Conference on Emerging Electronics (ICEE)，證據 URL：https://api.crossref.org/works/10.1109/ICEE56203.2022.10117683 。OpenAlex 確認 oa_status = closed、any_repository_has_fulltext = false，全文確實無開放取用版本。

---

## 三04 — Geometrical influence on Self Heating in Nanowire and Nanosheet FETs using TCAD Simulations

- **DOI／識別**：`10.1109/edtm47692.2020.9117971`　**來源**：IEEE　**年**：2020
- **作者／單位**：Min Jae Kang（第一作者），Imperial College London, UK（依 Crossref 該篇未附單位欄，單位依會議與作者群公開資訊為 Imperial College London，屬佐證非原文印出）；共同作者 Ilho Myeong、Kristel Fobelets
- **出處**：2020 4th IEEE Electron Devices Technology & Manufacturing Conference (EDTM), pp. 1–4

**1 元件**　堆疊式 nanowire GAA-FET 與單層 nanosheet GAA-FET 的對照，另含幾何最佳化後的堆疊 nanosheet（維持與單層 nanosheet 相同的總通道表面積）。技術節點、Lg、奈米線直徑、奈米片寬度 WNS 與厚度 TNS、堆疊層數、n 或 p 通道、指數：摘要未載明，未取得（需全文）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　求解器：Sentaurus TCAD（摘要逐字印出「using Sentaurus TCAD」，是本批 IEEE 五篇中唯一在摘要明確指名工具者）。方法：對不同 GAA 架構（堆疊 nanowire vs 單層 nanosheet vs 最佳化堆疊 nanosheet）模擬 SHE，並以「SHE on-current degradation」百分比比較，即含自熱與不含自熱兩組解的對照（ET-vs-ISO）。關鍵設計約束：比較是在「for the same output current」（相同輸出電流）條件下進行，而非固定 VDD。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic／BTE／聲子模型：摘要未載，未取得。（另有第三方資料提到本工作以 thermodynamic model 分析 SHE 並掃描奈米片數量與寬度，但該敘述來自搜尋結果摘要而非原文，不列為證據。）

**3 關鍵定量結果**　以下為摘要中原文印出數字（IEEE 全文付費牆，OpenAlex 確認 closed，未取得）。核心比較：「we find that for the same output current, stacked nanowire channels outperform a single nanosheet from a thermal management perspective with a SHE on-current degradation in the stacked nanowires of 3.01% compared to 6.42% for the nanosheet」——堆疊 nanowire 3.01%、單層 nanosheet 6.42%。幾何最佳化：「Improving the geometrical design of a stacked nanosheet GAA-FETs by keeping the same summed channel surface area as the single nanosheet, leads to an output current improvement of 11.1% whilst also improving degradation of on-current due to SHE by almost 1%」——輸出電流提升 11.1%，SHE 造成的 on-current 退化再改善近 1 個百分點。偏壓（VGS / VDS / TA）：摘要未載，未取得；只知道比較基準是「相同輸出電流」。Rth：未印出（未取得）。ΔT／峰值晶格溫度：未印出（未取得）。

**4 TCAD 校準用途**　部分可用，但不可直接校準 thermode。可用之處：(1) 求解器對齊——摘要確認為 Sentaurus TCAD，與使用者 deck 同工具鏈；(2) sanity check——GAA 架構下 3.01%（堆疊 nanowire）與 6.42%（單層 nanosheet）可當量級參考，兩者都低於矽 FinFET 的核心錨點 7–11%，這個「GAA 反而比 FinFET 低」的方向本身就值得使用者警覺（見 critique 第 1 點）；(3) 方法論警示——本文的比較基準是「相同輸出電流」，等於把自熱功率 P = I × V 中的 I 固定住再比，這與使用者 deck 慣用的「固定 VGS = VDS = VDD」是完全不同的歸一化方式，直接把 3.01%/6.42% 拿去對自己的固定偏壓結果會對不上。不可直接校準的理由：熱邊界、thermode 位置、SurfaceResistance、Rth、ΔT、偏壓全部未取得，沒有任何一個熱參數可搬。

**5 批判**
   1. 判準帶判定：3.01% 與 6.42% 都落在 bulk 判準帶 3–12% 的區間內，但都低於核心判準 7–11%，且 3.01% 正好貼在帶的下緣、逼近「小於 1% 即 SHE 被邊界抹掉」的警戒方向。可疑之處在於元件是 GAA（幾何侷限比 FinFET 更強、四面被低熱導率介電層包住），理論上退化應該高於同代 FinFET 而非低於。合理解釋有二，摘要無法區分：(a) 比較是在「相同輸出電流」下做，等於壓低了 nanowire 那組的功率密度，人為壓縮了退化幅度；(b) thermode 過於導熱（貼太近通道或 SurfaceResistance 設太小）。使用者不應把 3.01% 當成「GAA 自熱不嚴重」的證據。
   2. 歸一化方式是本卡最大的陷阱：「for the same output current」不是固定偏壓比較。在相同輸出電流下，堆疊 nanowire 的每根通道分擔的電流較小、所需 VDS 也不同，自熱功率被隱含地重新分配。這使 3.01% vs 6.42% 這個對比在物理上是「相同驅動能力下誰散熱好」，而不是「相同偏壓下誰自熱嚴重」。兩種問題的答案可以相反。
   3. 缺 %/K 交叉檢核：無 ΔT、無峰值晶格溫度、無 Rth，完全無法計算 ΔIon%/ΔT 比值來判斷熱邊界是否合理。這是把它排除在可校準之外的決定性理由。
   4. 「改善近 1%」的表述含糊：摘要說幾何最佳化「improving degradation of on-current due to SHE by almost 1%」，但未說明是絕對百分點（6.42% → 約 5.4%）還是相對改善（6.42% → 約 6.36%）。兩者差一個數量級，引用時必須註明此歧義。
   5. 單一比較、無幾何掃描細節可查：摘要只給三個構型的三個點，沒有堆疊層數或奈米片寬度的完整掃描曲線（雖然第三方摘要暗示有，但未經原文確認）。四頁會議論文（Crossref: pp. 1–4）的方法細節必然簡略。
   6. 無誤差棒、無重複性、無實驗校準：純模擬會議論文，摘要未提任何與量測資料的比對。
   7. 分類無誤：本文是乾淨的 ET-vs-ISO（SHE on-current degradation），不涉 ta_sweep 陷阱，也不是 Rth-extraction。

**6 可引用性**　A（可直接引用數字）— 3.01%、6.42%、11.1%、「almost 1%」四個數字都是 IEEE 官方摘要逐字印出的，可直接引用，且摘要同時印出了比較條件「for the same output current」與工具「Sentaurus TCAD」，條件相對完整。但引用時必須連「相同輸出電流」這個歸一化條件一起寫出，否則會被誤讀成固定偏壓下的 SHE 強度。因熱邊界與 ΔT 未取得，不可作為 thermode 校準錨點。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edtm47692.2020.9117971?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/EDTM47692.2020.9117971
   - https://api.openalex.org/works/doi:10.1109/edtm47692.2020.9117971

**8 與原表差異**　與原表一致。原表記載「Stacked nanowire vs nanosheet GAA-FETs (Sentaurus TCAD)、SHE on-current degradation 3.01% (stacked nanowires) vs 6.42% (single nanosheet) at same output current、optimized stack…、bias: not stated in abstract、dT: not printed in abstract」全部與 IEEE 官方摘要逐字核對相符，無衝突。本次補充原表被截斷的後半段數字：幾何最佳化（維持與單層 nanosheet 相同總通道表面積）帶來 output current 提升 11.1%，同時 SHE 造成的 on-current 退化再改善「almost 1%」。補充出處：2020 4th IEEE Electron Devices Technology & Manufacturing Conference (EDTM), pp. 1–4；作者 Min Jae Kang、Ilho Myeong、Kristel Fobelets（Crossref 未附單位欄）。已嘗試 Imperial College Spiral 典藏庫（DSpace discover API）搜尋此篇，無收錄；OpenAlex 確認 oa_status = closed、any_repository_has_fulltext = false，全文確實無開放取用版本。

---

## 三05 — Self-Heating and Electrothermal Properties of Advanced Sub-5-nm Node Nanoplate FET

- **DOI／識別**：`10.1109/led.2020.2998460`　**來源**：IEEE　**年**：2020
- **作者／單位**：Ilho Myeong（第一作者），Seoul National University, Department of Electrical and Computer Engineering, Seoul, Korea（Crossref 未附單位欄；單位依作者群與通訊作者 Hyungcheol Shin 的所屬推定，屬佐證非原文印出）；共同作者 Ickhyun Song、Min Jae Kang、Hyungcheol Shin
- **出處**：IEEE Electron Device Letters, Vol. 41, No. 7, pp. 977–980

**1 元件**　sub-5 nm 技術節點的 gate-all-around (GAA) nanoplate（即 nanosheet）field effect transistor。變化的 active area 規格為三項：垂直堆疊通道數（number of vertically stacked channels）、金屬閘極厚度 TM、通道寬度。Lg、奈米片厚度 TNS、通道寬度絕對值、堆疊數的掃描範圍、n 或 p 通道、指數：摘要未載明，未取得（需全文）。

**2 方法與 SHE 定義**　`未取得`　求解器：摘要僅寫「using TCAD simulations」，未指名工具（未取得；同作者群的 EDTM 2020 姊妹作使用 Sentaurus，但不可據此推定本篇）。摘要陳述以 Figure of Merit (FoM) 綜合分析 on-current degradation、time-delay、lattice temperature 與 thermal resistance，並從最大晶格溫度 TL,max 與金屬閘極厚度 TM 的角度分析 HCI/BTI 壽命變異。無法歸類 method_type 的理由：摘要雖提到 on-current degradation，但完全未說明退化的比較基準是「含 SHE vs 等溫（ET-vs-ISO）」還是「幾何參照之間的相對變化」；同時它又明確分析 thermal resistance（有 Rth-extraction 的成分），三者無法從摘要區分。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic／BTE／聲子模型：摘要未載，未取得。

**3 關鍵定量結果**　全部數值未取得。IEEE 全文為付費牆，OpenAlex 確認 oa_status = closed、any_repository_has_fulltext = false；Semantic Scholar 無 openAccessPdf；已查作者 Ickhyun Song 的實驗室出版頁（sites.google.com/view/soniclab/publication），該頁列出本篇完整書目「IEEE Electron Device Letters, vol. 41, no. 7, pp. 977-980, July 2020」但未提供任何 PDF 連結。摘要通篇無任何印出的數字：無 Ion 下降 %、無 Rth 數值、無 ΔT、無峰值晶格溫度 TL,max 數值、無偏壓（VGS / VDS / TA）。摘要中與結果最接近的逐字句為：「varying these architecture parameters not only affect overall performance ... such as on-current degradation and time-delay, but also greatly impact thermal reliability such as lattice temperature and thermal resistance」——確認論文分析了 on-current degradation、TL,max 與 thermal resistance 三個量，但數值僅存在於全文圖表，本次未取得。

**4 TCAD 校準用途**　不可直接校準，理由：僅取得摘要，Rth、SurfaceResistance、ΔT、TL,max、Ion 下降 %、偏壓全部未印出，且連 on-current degradation 的比較基準（ET vs isothermal，或幾何之間的相對比較）都無法從摘要確認——這意味著即使日後拿到一個百分比數字，也可能根本不是 SHE 的 ET-vs-ISO 差值。就題材而言本篇對使用者有間接價值（它是少數同時給出 GAA nanoplate 的 Rth 與 TL,max、並把兩者做成 FoM 的短文），若取得全文，其 thermal resistance 數值可用來與判準帶的 single-fin Rth 1–4 MK/W 做跨架構比對。建議使用者透過學校 IEEE Xplore 訂閱取得全文（DOI 10.1109/LED.2020.2998460，document 9103552），優先確認 Rth 的單位與量級、以及 on-current degradation 的比較基準。

**5 批判**
   1. 判準帶判定：無數值可判定，原因：僅取得摘要，全文為 IEEE 付費牆（OpenAlex 確認 closed、無 repository 版本，作者實驗室頁亦無 PDF），摘要通篇無任何百分比、溫度或熱阻數字，因此既無法判斷是否落在判準帶內，也無法做 ΔIon%/ΔT 交叉檢核或與 single-fin Rth 1–4 MK/W 比對。
   2. 分類無法確立，這是比缺數字更嚴重的問題：摘要說分析了 on-current degradation，但沒說退化相對於什麼。若基準是幾何參照（例如 2 層堆疊 vs 3 層堆疊），那它根本不是 ET-vs-ISO 的 SHE 量，拿去當 SHE 錨點會完全錯誤。原表把 verdict 標為 plausible_unveri 正是抓到這一點，本次查證維持該判定。
   3. 結構最佳化與熱可靠度指標被 FoM 混合：摘要說用 Figure of Merit 綜合分析 on-current degradation、time-delay、lattice temperature 與 thermal resistance。FoM 是把多個量加權合成的複合指標，其權重選擇會決定結論方向；在只有摘要、看不到 FoM 定義式的情況下，任何從 FoM 導出的「最佳結構」結論都不可驗證。
   4. 含糾纏因子：金屬閘極厚度 TM 同時是熱容／散熱路徑參數與電性參數（影響閘極電阻與寄生電容），通道寬度同時影響驅動電流與熱擴散截面。三個變數都同時動到電與熱，摘要未說明是否有做單變數控制。
   5. 延伸到 HCI/BTI 壽命是另一層外推：摘要用 TL,max 與 TM 推 HCI/BTI 壽命變異，這需要額外的退化模型與活化能假設，其不確定度遠大於 SHE 本身。這部分結論不宜引用。
   6. 篇幅限制：EDL 為 4 頁 Letter（pp. 977–980），即使取得全文，熱邊界條件與 thermode 設定也很可能只有一兩句帶過，未必足以重建 deck。
   7. 無誤差棒、無重複性、無實驗校準證據可查。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用。全文未取得、摘要零數字，且退化的比較基準無法確認（原表 verdict 為 plausible_unveri，本次維持）。只能用來支持「已有研究以 TCAD 分析 sub-5 nm GAA nanoplate FET 在堆疊數／金屬閘極厚度／通道寬度變化下的自熱與熱阻，並延伸到 HCI/BTI 壽命」這類文獻脈絡陳述，不可引用任何數值，也不可宣稱其 on-current degradation 是 ET-vs-ISO 的 SHE 量。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/led.2020.2998460?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/LED.2020.2998460
   - https://api.openalex.org/works/doi:10.1109/led.2020.2998460
   - https://sites.google.com/view/soniclab/publication

**8 與原表差異**　與原表一致，維持原表的保留判定。原表記載「Sub-5-nm 節點 GAA nanoplate(nanosheet) FET；變化堆疊通道數、金屬閘極厚度、通道寬…；圖級，% 未印於摘要；on-current degradation 隨堆疊數／閘金屬厚度／寬度分析，但退化的比較基準（ET vs isothermal 或幾何參照）無法自摘要確認；bias: 摘要未載明；dT: 圖級（TL,max 有分析），未取得」與 IEEE 官方摘要逐字核對完全相符，本次同樣未能取得全文，故 verdict 維持 plausible_unveri，method_type 據此填「未取得」而非勉強歸類，無衝突。補充原表未載的出處：IEEE Electron Device Letters, Vol. 41, No. 7, pp. 977–980, July 2020；作者為 Ilho Myeong、Ickhyun Song、Min Jae Kang、Hyungcheol Shin（原表未列共同作者 Ickhyun Song）。取得管道查證紀錄：OpenAlex 顯示 oa_status = closed、any_repository_has_fulltext = false；Semantic Scholar 無 openAccessPdf；已造訪共同作者 Ickhyun Song 的實驗室出版頁 https://sites.google.com/view/soniclab/publication ，該頁列出本篇為國際期刊論文第 35 筆並確認卷期頁碼，但未附 PDF 連結。另注意：搜尋時出現 SNU 典藏庫的 Ilho Myeong 學位論文《Self-Heating and Electrothermal Properties of Sub-5-nm 3-D Transistors》（s-space.snu.ac.kr/handle/10371/178950），標題高度相似但為不同文獻，該頁受 JS 挑戰擋住未能讀取內容，故未採用、也未將其任何內容歸屬到本篇。

---

## 三06 — Analysis of Self Heating Effect in DC/AC Mode in Multi-Channel GAA-Field Effect Transistor

- **DOI／識別**：`10.1109/TED.2019.2942074`　**來源**：IEEE　**年**：2019（Crossref issued 2019-11；OpenAlex publication_date 2019-10-03）
- **作者／單位**：Ilho Myeong（第一作者）；OpenAlex 記載的 raw affiliation 為 'University Semiconductor Research Center, Seoul, South Korea'（Hyungcheol Shin 團隊，首爾大學體系）。共同作者：Dokyun Son、Hyunsuk Kim、Hyungcheol Shin。
- **出處**：IEEE Transactions on Electron Devices（IEEE 電子元件彙刊），vol. 66, no. 11, pp. 4631–4637

**1 元件**　三通道垂直堆疊 nanowire GAA-FET（multi-channel GAA-FET）。摘要逐字為 'a three-channel nanowire-field effect transistor (FET)'。技術節點、Lg、nanowire 直徑或截面幾何、n or p 型、鰭數／指數：未取得（IEEE 全文付費牆，僅取得摘要）。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　TCAD 模擬（摘要未指名求解器名稱與版本）。方法主軸為 DC 穩態與 AC 脈衝模式的自熱對比：改變 heating time（等同 pulse time）與 cooling time、掃描元件操作頻率、掃描 duty cycle（25%、50%、75%），並自 DC 模式抽取熱阻 Rth。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic／BTE／聲子模型：全部未取得。

**3 關鍵定量結果**　原文印出數字（摘要層級）。DC 模式逐字：'In the dc mode, as ΔTmax (definition: Tmax − 300 K) increases to 65 K, the transistor suffers from an Ion degradation of 3.8% along with a Rth of 4.875 [K/µW].' 即 Ion 下降 3.8%、ΔTmax = 65 K、Rth = 4.875 K/µW = 4.875 MK/W。AC 模式逐字：'It is confirmed that ΔTmax decreases as the device operating frequency increases and ΔTmax saturates to about 40 K at 4 GHz.' Duty cycle 掃描逐字：'It shows that ΔTmax increases to 38, 42, and 45 K, respectively, and HCI and BTI lifetime can be increased up to two times and three times, respectively.'（對應 duty = 25%、50%、75%）。對應偏壓：摘要未列出 VGS／VDS 數值；環境基準溫度可由 ΔTmax 的定義推知為 300 K。峰值晶格溫度未直接印出（可由 300 + 65 = 365 K 推得，但原文未如此表述）。

**4 TCAD 校準用途**　可做量級 sanity-check，不足以做完整校準。(a) Rth = 4.875 MK/W 可作為堆疊／GAA 單元件熱阻的上界參考；使用者的 single-fin FinFET 判準帶為 1–4 MK/W，若 deck 抽出的 Rth 明顯超過 4.875 MK/W，幾乎可斷定 thermode 過絕熱。(b) ΔTmax = 65 K 可作為 DC on-state 溫升的比對點。(c) ΔIon%/ΔT = 3.8/65 ≈ 0.058 %/K 可作為交叉檢核帶的下界案例（判準帶為 0.10–0.20 %/K）。(d) 不可用於幾何對齊（Lg 與通道尺寸未取得），也不可用於直接設定 thermode SurfaceResistance（原文熱邊界條件完全未取得）。

**5 批判**
   1. 判準帶判定：落在帶外偏低。Ion 下降 3.8% 只勉強觸及 bulk 3–12% 帶的最下緣，且交叉檢核比值 ΔIon%/ΔT = 3.8/65 ≈ 0.058 %/K，僅為 0.10–0.20 %/K 判準帶的三分之一到二分之一。可能原因有二且無法從摘要區分：(i) 元件是 GAA 奈米線而非 FinFET，12 nm 級短通道下準彈道／速度飽和主導，Ion 對遷移率退化的槓桿被壓縮；(ii) Ion 的抽取偏壓未揭露，若在低過驅動點抽取會系統性低估。需 IEEE 全文才能定論。
   2. 熱邊界不可查證，這是本篇最大的不可用性。Rth = 4.875 MK/W 高於 single-fin 1–4 MK/W 帶，但因 thermode 位置與接觸熱阻完全未取得，無法判定這是 GAA 四面被低導熱介電包覆的真實幾何效應，還是熱邊界條件設得過絕熱所致。
   3. 含糾纏因子：摘要後半把 duty cycle 與 HCI／BTI 壽命提升 2 倍／3 倍綁在一起，屬熱—載子注入退化的耦合外推，不是純 SHE 的電流量測；引用時不可把壽命結論當成 Ion 下降的佐證。
   4. 單一幾何、無誤差棒：純 TCAD 單點結構模擬，摘要未提供任何統計散布、重複性，也未說明是否對實測資料做過校準與校準殘差。三通道 nanowire 的結論能否外推到使用者的矽 FinFET，缺乏依據。

**6 可引用性**　A（可直接引用數字）— 摘要本身即逐字印出 Ion 下降 3.8%、ΔTmax = 65 K、Rth = 4.875 K/µW 以及 AC 頻率／duty cycle 的完整溫升值，數字可直接引用；唯引用時必須同時註明原文未揭露 Ion 的抽取偏壓。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2019.2942074?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/TED.2019.2942074
   - https://api.openalex.org/works/doi:10.1109/TED.2019.2942074

**8 與原表差異**　與原表一致。原表逐字確認的『DC Ion 劣化 3.8% 於 ΔTmax = 65 K』『AC 4 GHz 時 ΔTmax ≈ 40 K』『duty 掃描』本次全部複核成立。補充原表因截斷未完整記載者：Rth = 4.875 K/µW（= 4.875 MK/W）、duty 25/50/75% 對應 ΔTmax = 38/42/45 K、HCI/BTI 壽命 2×/3×、卷期頁碼 vol. 66, no. 11, pp. 4631–4637。仍為摘要層級，IEEE 全文未取得（Xplore 頁面為 JS 殼，抓不到內容）。

---

## 三07 — Analysis on Self-Heating Effects in Three-Stacked Nanoplate FET

- **DOI／識別**：`10.1109/TED.2018.2862918`　**來源**：IEEE　**年**：2018（Crossref issued 2018-10；OpenAlex publication_date 2018-08-29）
- **作者／單位**：Hyunsuk Kim（第一作者），School of Electrical Engineering and Computer Science, Seoul National University, Seoul, South Korea。共同作者：Dokyun Son、Ilho Myeong、Myounggon Kang、Jongwook Jeon、Hyungcheol Shin。
- **出處**：IEEE Transactions on Electron Devices（IEEE 電子元件彙刊），vol. 65, no. 10, pp. 4520–4526

**1 元件**　三層垂直堆疊 nanoplate FET（即 stacked nanoplate／nanosheet GAA），並與 FinFET 做熱通量（heat flux）對比。技術節點、Lg、nanoplate 寬度／厚度／pitch、n or p 型、鰭數：未取得。摘要提及有掃描 nanoplate width 並用 figure-of-merit 取最佳值，但未印出任何尺寸數值。

**2 方法與 SHE 定義**　`model`　TCAD 模擬（摘要未指名求解器與版本）。流程：先以實測資料做 ID–VG curve fitting 校準，再做 SHE 對電性影響的一般性分析；掃描 nanoplate width 並以 figure-of-merit factor（在納入 SHE 的前提下）挑最佳寬度；比較 FinFET 與 stacked nanoplate FET 的熱通量差異；據此提出隨汲極電壓變化的 two-step 熱阻（Rth）模型，並與 BSIM-CMG（Berkeley short-channel IGFET model — common multigate）比對；最後以七級環形振盪器（seven-stage ring oscillator）驗證電路層級 SHE。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic／BTE／聲子模型：全部未取得。

**3 關鍵定量結果**　未取得任何數值。摘要完全沒有 Ion 下降 %、Rth 數值、ΔT 或峰值晶格溫度；逐字僅有定性陳述：'The two-step Rth model in the stacked nanoplate FET matched well with the Berkeley short-channel IGFET model—common multigate model compared the other Rth models.' 與 'A seven-stage ring oscillator with the proposed Rth model was demonstrated, and SHEs in the circuit level were confirmed.' 對應偏壓：摘要未列 VGS／VDS／TA 任何數值。屬僅圖層級／正文層級（需取得 IEEE 全文自讀原圖）。

**4 TCAD 校準用途**　不可直接校準，理由：IEEE 全文付費牆，摘要未印出任何 Rth 數值、ΔT、峰值溫度或幾何尺寸，無法提供 thermode SurfaceResistance 量級，也無可對齊的幾何。概念上唯一可用的是一項定性建模指引：Rth 隨汲極電壓呈兩段式（two-step）而非常數——若使用者的 deck 用單一固定熱阻的 thermode 去擬合寬 VD 範圍，本篇提示會有系統性偏差。但這只能當建模方向，不能當數字校準。

**5 批判**
   1. 無數值可判定，原因：IEEE 全文未取得，摘要完全沒有印出任何 Ion 下降 %、ΔT 或 Rth 數值，因此既無法判定是否落在 7–11%（bulk 判準帶 3–12%）內，也無法做 ΔIon%/ΔT 的 0.10–0.20 %/K 交叉檢核。
   2. 分類提醒：本篇的核心產出是 Rth 緊湊模型（故 method_type 判為 model）而非 ET-vs-ISO 的電流對比。它很容易被當成『SHE 造成多少 Ion 下降』的引用來源而誤用；引用時必須說清楚它是熱阻建模與電路驗證論文。
   3. 外推限制：元件為三層堆疊 nanoplate，熱路徑（上層通道被下層加熱、向基板的散熱被 inner spacer 與堆疊結構阻斷）與使用者的矽 FinFET 不同構。摘要雖聲稱分析了 FinFET 與 nanoplate 的熱通量差異，但差異量值未取得，two-step Rth 行為能否直接搬到 FinFET 需另行驗證。
   4. 含糾纏因子且無誤差棒：以 figure-of-merit 選最佳 nanoplate width，會把電性（Ion、Cgg）與熱性混進同一個純量指標，最佳寬度會隨 FoM 權重定義而變動；摘要亦未提供校準殘差、誤差棒或任何重複性資訊。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論（two-step Rth 模型隨 VD 變化、與 BSIM-CMG 吻合優於其他 Rth 模型、七級 RO 層級可觀察到 SHE），無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2018.2862918?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1109/TED.2018.2862918
   - https://api.openalex.org/works/doi:10.1109/TED.2018.2862918

**8 與原表差異**　與原表一致。原表記載『Three-stacked nanoplate (nanosheet) FET；TCAD calibrated；figure-level only；no percentage printed in abstract；bias not stated in abstract；dT not printed in abstract』，本次以 Semantic Scholar 取回完整摘要逐字複核，確認摘要確實無任何數值。補充原表未載：第一作者 Hyunsuk Kim 與單位（School of Electrical Engineering and Computer Science, Seoul National University）、完整作者名單（含 Myounggon Kang、Jongwook Jeon）、卷期頁碼 vol. 65, no. 10, pp. 4520–4526。特別提醒：本次網路搜尋曾回傳一段把『Tmax 由 428 K 改善到 416 K、RTH 改善 9.3%、Hparasitic』等數值歸給本篇的摘要式回答，該內容並非來自本篇原文（無法在任何我實際讀到的來源中對應），已判定為搜尋引擎的跨論文混淆，不予採信、不列入本卡。

---

## 三08 — The Impact of Self-Heating on Single-Event Transient Effect in Triple-Layer Stacked Nanosheets: A TCAD Simulation

- **DOI／識別**：`10.3390/electronics15010085`　**來源**：非　**年**：2025 線上發表（PDF 標示 Received 17 Nov 2025 / Accepted 18 Dec 2025 / Published 24 Dec 2025；Crossref 與 OpenAlex 均記 2025），期別掛 Electronics 2026, 15, 85
- **作者／單位**：Yuanda Li（第一作者），School of Integrated Circuits, Guizhou Normal University, Guiyang 550025, China。通訊作者：Jinshun Bi、Xuefei Liu（同單位）；另有 Beijing University of Posts and Telecommunications 與中國科學院微電子研究所合著者。
- **出處**：Electronics（MDPI 開放取用期刊），2026, 15(1), Article 85

**1 元件**　三層垂直堆疊 Si nanosheet GAA FET（triple-layer stacked nanosheets），n 型。Table 1 逐字：LG（Gate Length）= 12 nm、WNS（Nanosheet Width）= 15 nm、TNS（Nanosheet Thickness）= 5 nm、LSP（Spacer Length）= 5 nm、LSD（Source/Drain Length）= 5.5 nm、EOT = 2.1 nm、CGP（Contact Gate Pitch）= 34 nm、FP（Fin Pitch）= 24 nm、Tstack = 10 nm、Tbulk = 55 nm、TFin = 50 nm、NSS（Nanosheet Spacer）= 7.7 nm、VDD = 0.65 V、gate work function 4.48 eV。閘介電堆疊為 0.6 nm SiO2 + 1.5 nm HfO2；S/D 高斯摻雜 1.0×10^21 cm^-3、通道 1.0×10^15 cm^-3、bulk 1.0×10^18 cm^-3。單一元件，未提多鰭多指。幾何依 IRDS roadmap 校準。

**2 方法與 SHE 定義**　`ET-vs-ISO`　Sentaurus TCAD P_2019.03（Sentaurus Structure Editor 建構結構 + Sentaurus Device 求解）。電性物理模型：Fermi-Dirac 分布、bandgap narrowing、SRH + Auger 複合、Philips unified mobility 搭配 Enormal 與 thin layer（庫倫散射與表面粗糙散射）、density gradient 量子修正（eQuantumPotential）、high-field saturation、hydrodynamic model；SHE 部分改採 thermodynamic model 計算晶格溫度。熱邊界條件逐字：'A fixed temperature of 300 K was set at the thermal contacts. A thermal boundary resistance of 2 × 10−6 cm2 K/W was applied to the contact electrodes, and a value of 2 × 10−4 cm2 K/W was specified for the interface between the silicon and SiO2 layers.' 熱導率設定：channel 0.0807、S/D 0.1661、bulk 1.48、oxide 0.14 W/(cm·K)。無 BTE／聲子輸運求解。作者另特別提醒實作陷阱：必須把關鍵字 'Temperature' 放進電流方程式，否則 Sentaurus 會跳過晶格溫度計算而退回等溫式。另含 AC 脈衝模擬（rise time RT = 2 ps、可調 heating time HT 與 cooling time CT）與重離子 SET 模擬（LET = 10 MeV·cm²/mg）。

**3 關鍵定量結果**　原文印出數字。DC 的 ET-vs-ISO 逐字：'The transfer characteristics presented in Figure 3a provide quantitative evidence that the SHE suppresses the on-state current (Ion) by approximately 1.81%, resulting in a 1.82% reduction in the on/off current ratio.' 對應偏壓：VDS = 0.65 V、VGS 由 0 掃到 0.65 V、熱接觸固定 300 K（該元件 Vth = 0.19 V、SS = 64.9 mV/dec）。峰值晶格溫度逐字：'Figure 4a presents the lattice temperature distribution across the cross-section, with a maximum of 472.35 K.'；結論段逐字：'lattice temperature reaches 472.35 K, whereas under AC conditions it rises to 484.56 K.' 故 DC 的 ΔT = 472.35 − 300 = 172.35 K、AC 為 184.56 K。AC 段另逐字：'The lattice temperature shows a clear positive correlation with HT, rising from 435.63 K at ...'。熱點位置為近汲極與汲極延伸區，且 Channel 1（最上層）溫度較高。SET 段落（非 SHE 對 Ion 的效應）：含 SHE 時瞬態峰值電流上升約 7.9%、收集電荷由 4.85 fC 增至 5.43 fC（約 11.9%）；以等效環境溫度 472.7 K 重做時峰值電流由 0.68 mA 升至 0.79 mA（16.1%）、電荷 4.81 → 5.43 fC（12.9%）。Rth：全文未印出。

**4 TCAD 校準用途**　本批對使用者 deck 最直接可用的一篇。(a) 可直接抄用的 thermode／介面熱阻量級：接觸電極熱邊界電阻 2 × 10^-6 cm²·K/W、Si/SiO2 介面分佈式熱阻 2 × 10^-4 cm²·K/W、熱接觸固定 300 K——這正對應 Sentaurus 中 Thermode 的 SurfaceResistance 與區域介面熱阻設定，可當使用者 FinFET deck 的起始值。(b) 可比對的 ΔT：DC 172.35 K、AC 184.56 K（絕對值 472.35 / 484.56 K）於 VDD = 0.65 V。(c) 可對齊的幾何：Lg = 12 nm、CGP = 34 nm、FP = 24 nm，與先進節點 FinFET 的 CPP／fin pitch 同量級。(d) 最有價值的實作 sanity-check：作者明示若電流方程未帶 'Temperature' 關鍵字，Sentaurus 會靜默跳過晶格溫度計算——這正是使用者 deck 出現『SHE 被完全抹掉、Ion 差 < 1%』時應優先排查的第一個實作陷阱。

**5 批判**
   1. 判準帶判定：落在帶外，且存在嚴重的內部矛盾。Ion 只降 1.81%，遠低於標準判準值 7–11%（bulk 帶 3–12%）；更關鍵的是交叉檢核比值 ΔIon%/ΔT = 1.81 / 172.35 ≈ 0.011 %/K，比 0.10–0.20 %/K 帶低了一整個數量級。判讀：172 K 的溫升本身極大（所以不是『熱被邊界抹掉』那一類），但電流幾乎不動，指向 Ion 的抽取過驅動偏低（VDD = 0.65 V、Vth = 0.19 V，過驅動僅 0.46 V）且 12 nm 通道以速度飽和／準彈道為主導，使遷移率退化的槓桿被壓縮。無論成因為何，這個 1.81% 不可拿來當『SHE 造成多少 Ion 下降』的代表值。
   2. 熱邊界偏絕熱且瓶頸單一：Si/SiO2 介面熱阻 2 × 10^-4 cm²·K/W 比接觸電極的 2 × 10^-6 cm²·K/W 高兩個數量級，作者自己也承認 'The high resistance at the oxide/semiconductor interface represents the critical bottleneck for heat dissipation'。472 K 的高溫因此幾乎是這個單一參數選擇的直接產物。使用者若照抄 2 × 10^-4 而自身結構未同樣被 SiO2 全包，就會複製出不屬於自己元件的高溫。
   3. 分類正確但主軸不是 SHE：method_type 判為 ET-vs-ISO 成立（Fig. 3a 確有 with/without SHE 對比），但論文重心是 SHE × 單粒子瞬態（SET）耦合，SHE-DC 只是鋪陳。引用時務必不要把 SET 段的 7.9%／11.9%／16.1% 誤讀成 Ion 下降百分比。
   4. 糾纏因子與單位瑕疵：SET 段把 SHE 與重離子入射、寄生 BJT（PBJT）觸發綁在一起，無法分離。另 Table 1 把 Roxide/si 的單位印成 'W/cm−2·K'，與正文的 'cm2 K/W' 互相矛盾（正文才是對的），照抄表格單位會在 deck 中錯兩個數量級。全篇為單一結構確定性模擬，無誤差棒、無重複性統計、無多結構變異分析。

**6 可引用性**　A（可直接引用數字）— MDPI 開放取用全文取得，Ion −1.81%、on/off ratio −1.82%、Tmax 472.35 K（DC）／484.56 K（AC）以及兩個熱邊界電阻值皆為原文印出數字且偏壓條件明確，可直接引用；但必須連同『ΔIon%/ΔT 比判準帶低一個數量級』的告誡一併引用。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/electronics15010085?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://mdpi-res.com/d_attachment/electronics/electronics-15-00085/article_deploy/electronics-15-00085.pdf
   - https://api.openalex.org/works/doi:10.3390/electronics15010085

**8 與原表差異**　與原表一致，並補足細節。原表記載的『Triple-layer stacked Si nanosheet GAA FET, Lg = 12 nm』『Ion suppressed by ~1.81%；on/off ratio −1.82%』『VDD = 0.65 V, VGS 掃 0–0.65 V, TA = 300 K』『~472 K lattice temperature』全部逐字複核成立，精確值為 DC 472.35 K、AC 484.56 K。補充原表未載者：WNS = 15 nm、TNS = 5 nm、CGP = 34 nm、FP = 24 nm、NSS = 7.7 nm、Sentaurus TCAD P_2019.03、hydrodynamic + thermodynamic 模型、熱邊界電阻 2 × 10^-6（接觸電極）／2 × 10^-4 cm²·K/W（Si/SiO2 介面）、Vth = 0.19 V、SS = 64.9 mV/dec、SET 段的 7.9%／11.9%／16.1%／12.9%。年份狀況與原表註記一致：PDF 頁眉為 'Electronics 2026, 15, 85'，Published 2025-12-24，Crossref 與 OpenAlex 均記 2025，非錯誤。

---

## 三09 — Systematic performance benchmarking of nanosheet and FinFET: An intrinsic self-heating perspective

- **DOI／識別**：`10.1016/j.microrel.2025.115588`　**來源**：非　**年**：2025（Crossref issued 2025-02；OpenAlex publication_date 2025-01-08）
- **作者／單位**：Sunil Rathore（第一作者），OpenAlex 記載單位為 Manipal Academy of Higher Education。共同作者：Rajeewa Kumar Jaisawal、Suneet Kumar Agnihotri（GLA University）、Navneet Gandhi（Indian Institute of Information Technology Design and Manufacturing, Jabalpur）、P. N. Kondekar、Navjeet Bagga。
- **出處**：Microelectronics Reliability（Elsevier），vol. 165, article 115588

**1 元件**　未取得。由標題可知涉及垂直堆疊 nanosheet FET 與 multi-fin FinFET 的對比，但技術節點、Lg、sheet／fin 幾何（Hfin、Wfin、TNS、WNS、堆疊數）、n or p 型、鰭數／片數，皆無法從任何我實際讀到的來源證實。

**2 方法與 SHE 定義**　`未取得`　未取得。取得鏈全數失敗：ScienceDirect 文章頁（www 與非 www 兩種主機名）皆回 HTTP 403；Semantic Scholar Graph API 的 abstract 與 tldr 欄位均為 null；Crossref 無 abstract 欄位；OpenAlex 記 open_access.is_oa = false、oa_status = closed、any_repository_has_fulltext = false、abstract_inverted_index 為空；TU Wien 的 in4.iue.tuwien.ac.at 鏡像（該站確實藏有本作者群另一篇 Solid-State Electronics 全文）無此篇（404）；scholar.archive.org 被 bot 防護攔截；OUCI 聚合站為 JS 渲染無法取得內容。求解器、熱邊界、thermode 位置與 SurfaceResistance、有無 hydrodynamic／BTE 全部未取得。

**3 關鍵定量結果**　未取得。無任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度可引用，亦無任何可標註的偏壓條件。附註（不列為結果、不列入 sources）：網路搜尋引擎曾回傳幾句疑似本篇摘要的文字，但我並未實際造訪並讀到承載該文字的頁面，依反幻覺紀律不採計。

**4 TCAD 校準用途**　不可直接校準，理由：完全無法取得內容，沒有任何 thermode 設定、Rth、ΔT 或幾何可餵給 deck。但需向使用者標記優先度：這是本批唯一在同一篇內把 nanosheet 與 multi-fin FinFET 以等效有效面積並排做本質自熱對比的論文，主題與使用者的矽 FinFET SHE 研究最貼近。若使用者具備 ScienceDirect 機構權限，這篇應列為第一順位自行下載並補讀。

**5 批判**
   1. 無數值可判定，原因：Elsevier 付費牆，摘要層級以上的內容全數無法取得，因此無法判定 Ion 下降是否落在 7–11%（bulk 判準帶 3–12%）內，也無法做 ΔIon%/ΔT 的 0.10–0.20 %/K 交叉檢核，更無從檢視 Rth 是否落在 1–4 MK/W 帶。
   2. 潛在分類風險（取得全文後必須先驗）：同一作者群的相關工作（例如本批三11）習慣把 ambient temperature 掃描與 SHE 寫在同一篇。若本篇亦然，日後引用時要先確認所引數字是 ET-vs-ISO 的等溫對照，還是 ta_sweep 的環境溫度效應——後者不是自熱。
   3. 書目層面已做三源交叉驗證但內容不可信：Crossref（vol. 165, 115588, issued 2025-02）、OpenAlex（2025-01-08）、Semantic Scholar 三者的標題、作者與年份完全一致，書目可安全入 bib；但『可信的書目』不等於『可信的內容』，目前只能作存在性引用。
   4. 無法評估熱邊界是否過絕熱或過導熱、單一幾何能否外推、是否含糾纏因子、有無誤差棒與重複性——這四項全部待取得全文後補齊，目前一律視為未知而非合格。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用（『已有研究對 nanosheet 與 multi-fin FinFET 做過本質自熱的系統性對比』這類存在性陳述），書目資訊三源一致可安全列入參考文獻；但任何數字、任何方法細節都不得引用。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.microrel.2025.115588?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.microrel.2025.115588
   - https://api.crossref.org/works/10.1016/j.microrel.2025.115588

**8 與原表差異**　與原表一致。原表 verdict 為 plausible_unveri，記載『Not obtained — no % accessible (abstract-level only; ScienceDirect 403 blocks full text)；bias not extracted；dT not extracted』。本次重試全部取得管道（ScienceDirect www 與非 www 均 403、TU Wien 鏡像 404、scholar.archive.org 被 bot 防護擋、OUCI 為 JS 渲染、Semantic Scholar／Crossref／OpenAlex 皆無 abstract）後仍為未取得，維持原判。補充原表未載之書目：vol. 165, article 115588；第一作者 Sunil Rathore，OpenAlex 記單位 Manipal Academy of Higher Education；完整作者六人名單。

---

## 三10 — Accurate Evaluation of Electro-Thermal Performance in Silicon Nanosheet Field-Effect Transistors with Schemes for Controlling Parasitic Bottom Transistors

- **DOI／識別**：`10.3390/nano14121006`　**來源**：非　**年**：2024（OpenAlex publication_date 2024-06-10）
- **作者／單位**：Jinsu Jeong（第一作者），Department of Electrical Engineering, Pohang University of Science and Technology (POSTECH), Pohang 37673, Republic of Korea。共同作者：Sanguk Lee、Rock-Hyun Baek（同單位，通訊作者）。
- **出處**：Nanomaterials（MDPI 開放取用期刊），2024, 14(12), Article 1006

**1 元件**　sub-3 nm 節點三層垂直堆疊 Si nanosheet FET（NSFET），n 型與 p 型皆有評估。Table 1 逐字：Contact poly pitch (CPP) = 42 nm、Sheet pitch (SP) = 60 nm、Gate length (Lg) = 12 nm、Spacing thickness (Tsp) = 10 nm、Inner-spacer length (Lis) = 5 nm、NS width (WNS) = 25 nm、NS thickness (TNS) = 5 nm、HfO2 厚 1.1 nm、IL 厚 0.6 nm、Operating voltage (VDD) = 0.7 V、BOX thickness (TBOX) = 10 nm、Over-etched S/D depth (TSD) = 0–6 nm。三種抑制寄生底層電晶體（trpbt）方案並列比較：Conv（傳統 punch-through stopper）、TIS（trench inner-spacer）、BOX（bottom oxide）。單元件評估 + 3 級環形振盪器 3D mixed-mode 模擬。

**2 方法與 SHE 定義**　`ET-vs-ISO`　Synopsys Sentaurus Process 與 Sentaurus Device（版本 S-2021.06-SP1），製程與元件模擬全流程。載子輸運採自洽 hydrodynamic 模型並據以計算元件溫度；另含 inversion/accumulation layer 遷移率模型（涵蓋庫倫、聲子、表面粗糙散射）、low-field ballistic mobility（短通道額外貢獻）、SRH + Auger、Hurkx 帶對帶穿隧、density gradient 量子修正、deformation potential（應變致能帶變化）、Slotboom 帶隙窄化。熱導率 κ 由聲子波茲曼輸運方程（BTE）搭配鬆弛時間近似自洽計算，並考慮尺寸、摻雜類型與濃度、合金組成與晶格溫度相依；Table 2 列 300 K 的 κ（W·m^-1·K^-1）：Si substrate 170、NS channel n/p 10.0/9.5、PTS_Conv,TIS 36.5、PTS_BOX 37.0、SiC0.02/SiGe0.5 S/D 30.0/13.5、IL 1.4、HfO2 2.3、low-k 與 BOX 0.7、STI 1.4、WFM 19.2、silicide 25、M0 150。熱邊界條件逐字：'For the thermal boundary condition, the adiabatic sidewalls along with the contact thermal resistivities of the substrate (rth,sub) and the BEOL (rth,BEOL) to be connected to the heat sink at 300 K were assumed. The rth,sub and rth,BEOL were calculated on a Si substrate with dimensions of 5 × 5 µm2 (area), a thickness of 50 µm, and a BEOL height of 1 µm (contact-M10).'——即 rth 由上述實體幾何推算，論文本身未印出其數值。

**3 關鍵定量結果**　原文印出數字，但 SHE-vs-noSHE 的電流差本身是僅圖層級。Fig. 2 圖說逐字：'Transfer characteristics and Ion for various TSD with and without SHE in (a) Conv, (b) TIS, and BOX schemes (the transfer curves with and without SHE almost overlaps).' 方向性結論逐字：'First, in all schemes, the Ion under the SHE (Ion_SHE) is larger than that without SHE (Ion_noSHE) in nFETs, whereas it is smaller in pFETs (Figure 3a).' 交叉點逐字：'Vco is defined as the VGS at which Ids_SHE = Ids_noSHE.' 與 'As a result, Vco was determined at a lower VGS in pFETs than in nFETs (0.8 V for nFETs and −0.65 V for pFETs).' 因 VDD = 0.7 V < 0.8 V，nFET 在 on-state 反而是 SHE 令電流略增；pFET 之 |VDD| = 0.7 V > |−0.65 V|，SHE 令電流略減。方案間差（非 SHE-vs-noSHE）逐字：'the TIS scheme has a 3.1% higher Ion_SHE value compared to the BOX scheme, although both schemes have almost the same Ion_noSHE value'（nFET）與 'for pFETs, the TIS scheme has a 2.2% higher Ion_SHE value than the BOX scheme'。溫度逐字：'Nevertheless, the BOX scheme in n/pFETs still exhibits 59.6 and 50.4 K higher Tmax_on compared with those of the TIS scheme.' 偏壓逐字定義：'Ion was defined as Ids at |VGS| = |VDS| = 0.7 V'，Ioff 為 VGS = 0 V、|VDS| = 0.7 V（Conv 的 TSD = 0 nm 固定在 1 nA 以做公平比較），熱沉 300 K。RO 暫態：Conv／TIS／TIS-full 在操作 1 ns 後 Tmax 為 nFET 314.0 K、pFET 310.0 K，BOX 方案再高約 2.6 K（n）／2.1 K（p）；Tmax_10cy 差距逐字：'The Tmax_10cy differences increase from 1.5 K (1.7 K) with CL = 1 fF to 4.8 K (3.0 K) with CL = 10 fF for n(p)FET.' Rth：全文未印出。單元件穩態的 Tmax 絕對值為圖層級（Fig. 3b、Fig. 5a），僅 RO 段印出 314.0／310.0 K。

**4 TCAD 校準用途**　(a) 本批可對齊幾何最完整的一篇：Lg = 12 nm、WNS = 25 nm、TNS = 5 nm、CPP = 42 nm、sheet pitch = 60 nm、VDD = 0.7 V，且 Table 2 給了 12 個區域的 300 K 熱導率，可直接抄進 deck 的材料熱參數（特別是 low-k/BOX = 0.7、STI = 1.4、Si substrate = 170 W·m^-1·K^-1）。(b) 熱邊界方法論可整套抄用：側壁絕熱 + 基板與 BEOL 以接觸熱阻接到 300 K 熱沉，且明確給出推算 rth 所用的實體尺寸（5×5 µm² 面積、50 µm 厚基板、1 µm BEOL 至 M10），使用者可用同一套幾何自行推導 thermode SurfaceResistance，而非憑空猜值。(c) 極有價值的 sanity-check 反例：本篇顯示在 VDD 0.7 V、Lg 12 nm 下 SHE 對 Ion 幾乎不動甚至反向（nFET 的 Vco = 0.8 V 高於 VDD）。若使用者的 FinFET deck 也跑出 < 1% 的 SHE 影響，本篇提供了判別法——看 Vco 落在 VDD 的哪一側：若 Vco > VDD，代表載子濃度上升仍主導，並不必然是 thermode 貼太近。(d) 不可用於直接取得 SurfaceResistance 數值，因 rth,sub 與 rth,BEOL 的數字全文未印出。

**5 批判**
   1. 判準帶判定：落在帶外，屬『飽和 Ion 差小於 1%』一側，但成因不是 thermode 貼太近。Fig. 2 圖說明言 with/without SHE 曲線幾乎重疊，且 nFET 在 0.7 V 時 SHE 反而使 Ion 略增（Vco = 0.8 V 高於 VDD）。同時方案間 Tmax_on 可差 59.6 K，證明溫度並未被邊界條件抹平。因此這是載子濃度上升與遷移率下降在該偏壓恰好抵消（交叉點落在 VDD 附近），而非熱模型失效——這對使用者判別自家 deck『SHE 太小』時是最有價值的物理對照。
   2. 最容易被誤引的數字：3.1%（n）與 2.2%（p）是 TIS 方案相對 BOX 方案的 Ion_SHE 差，不是 SHE 相對 no-SHE 的差；原文同一句已註明兩方案的 Ion_noSHE 幾乎相同。把 3.1% 當成『SHE 造成 3.1% 下降』會構成實質性誤引，需在筆記中明確標紅。
   3. 熱邊界偏導熱（偏保守）：側壁絕熱，但基板厚 50 µm、面積 5×5 µm² 直接接 300 K 熱沉，屬相對容易散熱的設定；59.6 K 的方案間差主要來自 BOX（κ = 0.7 W·m^-1·K^-1）阻斷向下熱路徑，而非通道本身被悶住。若把這套邊界移植到 SOI FinFET 會低估溫升（SOI 判準帶為 8–17%）。
   4. 糾纏因子與外推限制：Ion 同時被寄生底層電晶體漏電汙染——原文逐字 'On-state current (Ion) also increases with increasing TSD as the leakage current in the trpbt contributes to Ion'，故 Conv 方案的 Ion 變化混有非 SHE 成因。另 n/p 的 Tmax 差主要源自 SiGe0.5（13.5）與 SiC0.02（30.0 W·m^-1·K^-1）源汲極熱導率不同，是材料選擇造成，不能外推到使用者的矽 FinFET。全篇為單一結構確定性模擬，無誤差棒與重複性統計。

**6 可引用性**　A（可直接引用數字）— MDPI 開放取用全文，幾何表（Table 1）、熱導率表（Table 2）、59.6／50.4 K、3.1%／2.2%、Vco = 0.8 V 與 −0.65 V、RO 的 314.0／310.0 K 與 1.5 → 4.8 K 皆為原文印出數字且偏壓明確；唯引用 3.1%／2.2% 時必須註明那是方案間差而非 SHE 效應。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/nano14121006?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC11206696/
   - https://mdpi-res.com/d_attachment/nanomaterials/nanomaterials-14-01006/article_deploy/nanomaterials-14-01006.pdf
   - https://api.openalex.org/works/doi:10.3390/nano14121006

**8 與原表差異**　與原表一致，並附一項重要澄清。原表記載的『sub-3 nm 節點 Si 堆疊奈米片 FET（n 與 p），Lg = 12 nm、WNS = 25 nm、TNS = 5 nm』『圖級、無單一 %：Ion_SHE 在 Vco 以上低於 Ion_noSHE（Vco = +0.8 V nFET／−0.65 V pFET，全文逐字確認）；Vco 以下 SHE 略增電流』『TIS 之 Ion_SHE 比 BOX 高（3.1% n／2.2% p）』『VDD = 0.7 V（Table 1），熱邊界 heat sink 300 K』『DC：TIS 比 BOX 低 59.6 K(n)/50.4 K(p)』全部逐字複核成立。補充原表未載：CPP = 42 nm、sheet pitch = 60 nm、Tsp = 10 nm、Lis = 5 nm、TBOX = 10 nm、TSD = 0–6 nm、Sentaurus S-2021.06-SP1、自洽 hydrodynamic + 聲子 BTE(RTA) 算 κ、側壁絕熱、Table 2 全部 12 項熱導率、RO 段 314.0／310.0 K 與 1.5→4.8 K。需澄清一點（避免後續誤用，非原表之錯）：rth,sub 與 rth,BEOL 的『數值』全文並未印出，原文只給了推算所用的實體尺寸（5×5 µm²、50 µm 厚基板、1 µm BEOL 到 M10）；若有人假設本篇可直接抄到現成的接觸熱阻數值，該假設不成立。

---

## 三11 — Trap and self-heating effect based reliability analysis to reveal early aging effect in nanosheet FET

- **DOI／識別**：`10.1016/j.sse.2022.108546`　**來源**：非　**年**：2023（Crossref issued 2023-02，正式卷期為 vol. 200, Feb 2023；PDF 頁首標示 'Available online 1 December 2022'，OpenAlex 因此記 publication_date 2022-12-01）
- **作者／單位**：Sunil Rathore（第一作者），VLSI Design and Nano-scale Computational Lab, Electronics and Communication Engineering Department, PDPM-IIITDM, Jabalpur 482005, India。共同作者：Rajeewa Kumar Jaisawal、P. N. Kondekar（同單位）、Navjeet Bagga（Indian Institute of Technology Bhubaneswar, Odisha, India，通訊作者）。
- **出處**：Solid-State Electronics（Elsevier），vol. 200, article 108546

**1 元件**　垂直三層堆疊 Si nanosheet FET（NSFET），sub-5 nm 技術節點。Table 1 逐字：Gate Length (LG) 12 nm、Eff. Oxide Thick. 0.9 nm、Spacer Length (LSP) 5 nm、Sheet Thickness 5 nm、Sheet Width (W) 25 nm、Sheet Spacing 11 nm。閘金屬為 TiN（功函數經調校以擬合實測 IDS–VGS）。n 型（轉移特性圖標註 VDS = +0.7 V）。單元件，未提多鰭多指或多元件陣列。S/D pad 與通道為均勻摻雜，延伸區用高斯摻雜。

**2 方法與 SHE 定義**　`ET-vs-ISO`　Sentaurus TCAD。核心模型逐字：'the quantum-corrected DD model coupled with hydrodynamic and thermodynamic models is employed to capture the SHE-induced thermal degradation for the sub-5-nm technology node to precisely predict the nanometer geometry effects.' 亦即量子修正 drift-diffusion 為骨幹，耦合 hydrodynamic 與 thermodynamic 模型算 SHE。晶格溫度所需的熱導率 kth 由聲子波茲曼方程（BTE）配合鬆弛時間近似（RTA）計算（論文列出 kth 積分式），並考慮聲子平均自由程與聲子邊界散射造成的奈米尺度 kth 下降。其他模型：MLDA（modified local density approximation，通道量子侷限）、IAL 遷移率模型、high-field saturation（短通道效應）、high-k 遷移率退化模型（remote phonon 與 remote Coulomb scattering）、SRH 產生復合，以及 statistical impedance field method（配 Poisson 分布）處理介面陷阱變異。熱邊界條件、thermode 位置與 SurfaceResistance 數值：全文完全未載明。另含 ambient temperature 掃描 250–400 K（ta_sweep 成分，非自熱）。

**3 關鍵定量結果**　無任何 SHE 相關數字被印出（全文 7 頁逐頁檢視）。SHE 對電流的影響只在 Fig. 2(c) 以 with/without SHE 的 IDS–VGS 對比呈現，屬僅圖層級（需自讀原圖）。正文逐字僅有定性敘述：'In NSFET, the channel regions are surrounded by the low thermal conductivity material, i.e., SiO2, which confines the heat flux in the channel direction [Fig. 2 (a-b)]. This causes an increase in the lattice temperature, resulting in SHE-induced performance degradation (Fig. 2 c).' 熱點位置逐字（Fig. 2 圖說）：'the maximum temperature is accumulated towards the channel/drain interface due to the low thermal conductivity material wrapped around the channel.' 對應偏壓：轉移特性圖標註 VDS = 0.7 V、VGS 掃 0–0.7 V，baseline 為 T = 300 K；環境溫度另掃 250 K 至 400 K。峰值晶格溫度、ΔT、Rth：全文皆未印出任何數值。老化部分：EOL 定義為 Vth 偏移 ±50 mV，圖中出現 TA = 387 K 與 TA = 366 K 兩個標註（屬 ta_sweep 下的壽命終點溫度，不是自熱溫升）。

**4 TCAD 校準用途**　(a) 可對齊幾何：LG = 12 nm、sheet 厚 5 nm／寬 25 nm／間距 11 nm、EOT 0.9 nm、spacer 5 nm，是一組完整可複製的三層 NSFET 結構參數。(b) 可抄用的模型組合先例：量子修正 DD + hydrodynamic + thermodynamic，且 kth 用聲子 BTE-RTA 而非常數——使用者決定 deck 要不要開聲子／BTE 模型時，這是一個具體且同節點的先例。(c) 可 sanity-check 的定性判準：熱點應落在 channel/drain 介面而非通道中央；若使用者的 FinFET deck 熱點位置不在汲極端，thermode 位置或熱導率設定極可能有誤。(d) 不可用於數值校準，理由：全文未印出任何 Ion 下降 %、ΔT、峰值溫度或 Rth，也未載明 thermode 位置與 SurfaceResistance，無法提供任何可比對的量級。

**5 批判**
   1. 無數值可判定，原因：已取得 TU Wien 鏡像的完整全文（7 頁）並逐頁檢視，確認沒有任何 SHE 造成的 Ion 下降百分比、ΔT 或 Rth 數字被印出，SHE 效應僅存在於 Fig. 2(c) 的曲線對比。因此既不能判定是否落在 7–11%（bulk 判準帶 3–12%）內，也無法做 ΔIon%/ΔT 的 0.10–0.20 %/K 交叉檢核。
   2. 分類陷阱（本批最需警戒的一篇）：第 3.2 節『Effect of ambient temperature』是把 TA 從 250 K 掃到 400 K，屬環境溫度掃描（ta_sweep）而非自熱；Fig. 5、Fig. 7 的所有 Vth 偏移、SS 變化，以及 TA = 387 K／366 K 的 EOL 標註全屬 ta_sweep 產物。若把這些溫度當作自熱溫升引用，就是判準帶明列的分類誤植。真正的 ET-vs-ISO 對照只有 Fig. 2(c) 一張圖。
   3. 糾纏因子極重、無乾淨對照組：全篇主變數是 Si/SiO2 介面陷阱電荷（施體／受體、能階位置、峰值濃度掃描）與 SHE 的耦合，所有 Vth、SS、ION、IOFF 的變化都同時被陷阱與溫度驅動，論文並未提供把純 SHE 貢獻分離出來的實驗設計。想引用『SHE 單獨造成多少退化』的讀者在本篇找不到乾淨數據。
   4. 熱邊界完全不可查證，熱模型實質不可重現：全文未寫 thermode 位置、熱沉溫度、接觸熱阻或任何邊界設定，只說通道被低熱導率 SiO2 包覆造成熱通量受限。配合『沒有印出任何溫度數值』這一點，讀者無從判斷模型是否過絕熱，也無法複製。另為單一結構確定性模擬，僅陷阱變異用統計方法處理，Ion 與 ΔT 皆無誤差棒。

**6 可引用性**　B（只能引用定性結論）— 全文已取得，但 SHE 部分只能引用定性結論（熱點位於 channel/drain 介面、SiO2 包覆造成熱通量受限、SHE 造成效能退化）與幾何／模型設定；沒有任何 SHE 數值可引用。

**7 取得狀態**　全文
   - https://in4.iue.tuwien.ac.at/pdfs/sispad2022/Trap-and-self-heating-effect-based-reliability-analysis-to_2023_Solid-State-.pdf
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.sse.2022.108546?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.sse.2022.108546
   - https://api.crossref.org/works/10.1016/j.sse.2022.108546

**8 與原表差異**　與原表一致。原表記載的『Vertically three-stacked Si nanosheet FET, LG = 12 nm』『NO numeric % anywhere in full text』『Fig. 2(c) (p.3) shows ION degradation in IDS-VGS with vs without SHE (baseline)』『VDS = 0.7 V throughout；VGS 掃 0–0.7 V』『Not printed numerically；hotspot located at ...』本次以 TU Wien 鏡像全文（7 頁完整 PDF）逐頁複核，全部成立。補充原表未載：完整 Table 1 幾何（EOT 0.9 nm、LSP 5 nm、sheet 厚 5 nm／寬 25 nm／間距 11 nm）、模型為量子修正 DD 耦合 hydrodynamic + thermodynamic、kth 由聲子 BTE-RTA 計算、閘金屬 TiN、ambient 掃描範圍 250–400 K、EOL 定義為 Vth 偏移 ±50 mV、圖中 TA = 387 K 與 366 K 標註、第一作者單位 PDPM-IIITDM Jabalpur 與通訊作者 Navjeet Bagga（IIT Bhubaneswar）。年份小差異備註（非錯誤、不改）：Crossref 與 Semantic Scholar 記 2023（vol. 200, Feb 2023），OpenAlex 記 2022-12-01，PDF 頁首為 'Available online 1 December 2022'；原表填 2023 與正式卷期一致，維持不變。

---

## 三12 — The Impact of Ambient Temperature on Electrothermal Characteristics in Stacked Nanosheet Transistors with Multiple Lateral Stacks

- **DOI／識別**：`10.3390/nano13222971`　**來源**：非　**年**：2023（OpenAlex publication_date 2023-11-18）
- **作者／單位**：Peng Zhao（第一作者），Integrated Circuit Advanced Process R&D Center 與 State Key Lab of Fabrication Technologies for Integrated Circuits, Institute of Microelectronics of the Chinese Academy of Sciences, Beijing 100029, China（兼 School of Integrated Circuits, University of Chinese Academy of Sciences, Beijing 100049）。共同作者：Lei Cao、Guilei Wang（Beijing Superstring Academy of Memory Technology）、Zhenhua Wu、Huaxiang Yin。
- **出處**：Nanomaterials（MDPI 開放取用期刊），2023, 13(22), Article 2971

**1 元件**　三層垂直堆疊 nanosheet 電晶體（Nch = 3），含 n 型（NMOS）與 p 型（PMOS），並有實際製程流程（含 STI、sub-fin、dummy gate removal、GeSi）。量測元件逐字：'The nanosheet width (WNS) is about 30 nm, and the nanosheet thickness (TNS) is about 10 nm'；LG = 30, 40, 60, 500 nm；橫向堆疊數 Nstack = 2, 4, 8, 16, 32。TCAD 模擬單元逐字：'The LG, WNS, and TNS are set to 16, 20, and 6 nm, respectively'，模擬另涵蓋 Nstack = 1（Rth 與 ΔTmax 的基準點）。

**2 方法與 SHE 定義**　`ta_sweep`　Sentaurus TCAD（參考文獻列 Sentaurus Device User Guide, Version P-2019.03, Synopsys）。SHE 以熱力學模型計算，逐字：'The SHE is calculated with the thermodynamic model (TD model).' 全文未載明 thermode 位置、熱邊界條件、熱沉溫度或 SurfaceResistance；無 hydrodynamic／BTE／聲子輸運模型的描述。量測端使用 Agilent 半導體參數分析儀，環境溫度自 −50 °C 掃至 125 °C（25 °C 步進）；模擬端 Tamb 自 300 K 掃至 400 K。分析工具包含溫度相依 backscattering 模型（解釋 IDS 變化）、每 stack 電流與 Vth 的溫度係數（β、η）、零溫度係數偏壓點 VZTC。Rth 定義逐字：'Rth = ∆Tmax/total heat (K/µW)'。注意：本篇雖含 ET-vs-ISO 成分（Fig. 10a）與 Rth 抽取，但主軸與絕大多數圖表皆為環境溫度掃描，故 method_type 判為 ta_sweep。

**3 關鍵定量結果**　熱參數為原文印出數字；SHE 對電流的影響為僅圖層級。熱參數逐字：'The ∆Tmax and Rth in the devices with Nstack = 1 under Tamb = 300 K are 149 K and 2.59 K/µW, respectively, as shown in Figure 12.'，對應偏壓見 Fig. 12 圖說逐字：'When VGS = VDS = 0.7 V, (a) ∆Tmax and (b) Rth variations relative to the devices with Nstack = 1 under Tamb = 300 K.' 即 ΔTmax = 149 K（推得峰值晶格溫度約 449 K）、Rth = 2.59 K/µW = 2.59 MK/W，條件為 Nstack = 1、Tamb = 300 K、VGS = VDS = 0.7 V。SHE-vs-noSHE 逐字（僅定性、無 %）：'Figure 10a shows that the IDS with the SHE is lower than that without the SHE at larger VGS. At VGS = VDS = 0.7 V, the on-state IDS (ION) degradation with the SHE is lower than that without the SHE as Tamb increases, as shown in Figure 10b.' 量測端的 IDS 變化（Fig. 4、Fig. 5）是相對 Tamb = −50 °C 的正規化變化，屬環境溫度效應而非自熱；Vth = 300 mV／−300 mV @ Tamb = 25 °C（NMOS／PMOS，量測於 LG = 500 nm、Nstack = 2、VDS = ±0.9 V、Vov = ±0.43 V）。全文無任何 SHE 造成的 Ion 下降百分比。

**4 TCAD 校準用途**　(a) 本批唯一可直接做 Rth sanity-check 的數字：Rth = 2.59 K/µW（= 2.59 MK/W）於 VGS = VDS = 0.7 V、Tamb = 300 K、Nstack = 1，且 Rth 定義（ΔTmax / total heat）明確寫出，使用者可用完全相同的定義從自己的 deck 抽 Rth 直接比對——2.59 MK/W 正落在 single-fin 1–4 MK/W 判準帶內。(b) 偏壓 0.7 V 與使用者設定一致，ΔTmax = 149 K 可當溫升上界參考（三層堆疊 GAA 比 FinFET 更熱侷限，FinFET 應顯著低於此值）。(c) 提供 Nstack 由 1 掃到 32 的熱串擾（thermal crosstalk）趨勢與每 stack Rth 的變化方向，可用來檢查 deck 在多鰭排列時鄰鰭互熱是否被合理捕捉。(d) 不可用於 thermode 或 SurfaceResistance 設定，理由：全文未寫任何熱邊界條件、熱沉位置或接觸熱阻。

**5 批判**
   1. 判準帶判定：Rth 落在帶內、ΔIon% 無數值可判定。Rth = 2.59 MK/W 落在 single-fin 1–4 MK/W 判準帶內（元件是三層堆疊 GAA，落在帶中上緣合理）。但 ΔTmax = 149 K 若套上 0.10–0.20 %/K 的交叉檢核帶，推得的 Ion 下降應在 15–30%，遠超 7–11% 帶——而論文根本沒印出 Ion 下降百分比，故無法驗證，也絕不可自行相乘外推。這是本篇最大的引用限制。
   2. 分類陷阱（判準帶明列的最常見錯誤，本篇正是典型）：全篇主軸是環境溫度掃描（量測 −50 ~ 125 °C、模擬 300 ~ 400 K），Fig. 4 至 Fig. 9 的所有 IDS 變化、β、η、VZTC 都是 ta_sweep 的環境溫度效應，不是自熱。真正的 ET-vs-ISO 只有 Fig. 10a 一張圖且無數字。若把 ta_sweep 的電流退化當成自熱造成的 Ion 下降引用，即為分類誤植。
   3. 熱邊界完全未揭露，使 Rth 只能當量級參考：全文只寫用 thermodynamic model 算 SHE，沒有 thermode 位置、熱沉溫度、接觸熱阻或 SurfaceResistance 的任何描述。ΔTmax = 149 K 這麼高的溫升，究竟是堆疊幾何真實的熱侷限、還是邊界設得過絕熱，無從判斷；因此 2.59 MK/W 雖落在判準帶內，仍不是可複製的校準點。
   4. 幾何不一致與外推限制：量測元件（WNS ≈ 30 nm、TNS ≈ 10 nm、LG 30–500 nm）與模擬元件（LG/WNS/TNS = 16/20/6 nm）尺寸並不相同，論文用前者建立趨勢、用後者跑 SHE，兩者之間的橋接未被量化。此外 Rth 的絕對值只在 Nstack = 1 給出，其他 Nstack 僅以相對變化呈現；n/p 差異被歸因於 PMOS 電流密度較大導致散射加劇，混有載子種類與材料因素。全篇為確定性模擬加單批量測，未報告誤差棒或重複性。

**6 可引用性**　A（可直接引用數字）— MDPI 開放取用全文，ΔTmax = 149 K 與 Rth = 2.59 K/µW 是原文印出數字，且偏壓（VGS = VDS = 0.7 V、Tamb = 300 K、Nstack = 1）與 Rth 的定義都明確寫出，可直接引用；唯必須同時註明全文沒有任何 Ion 下降百分比，且論文主體為 ta_sweep 而非 SHE。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/nano13222971?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://mdpi-res.com/d_attachment/nanomaterials/nanomaterials-13-02971/article_deploy/nanomaterials-13-02971.pdf
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC10675435/
   - https://api.openalex.org/works/doi:10.3390/nano13222971

**8 與原表差異**　CORRECTION（圖號）＋其餘與原表一致。原表『3 層垂直堆疊奈米片電晶體、1–32 個橫向 stack；模擬單元 Lg = 16 nm、WNS = 20 nm、TNS = 6 nm』『圖級、無印出 %；全文確認無任何明確 SHE 電流下降 %（僅正規化 ΔIDS/IDS 形式）』『VGS = VDS = 0.7 V、TA = 300 K（SHE 數值）；另有 TA 掃描』『ΔTmax = 149 K（Nstack = 1、VGS = VDS = 0.7 V、Tamb = 300 K）』全部逐字複核成立。CORRECTION：原表記『Fig. 10b 顯示高 VGS 時含 SHE 之 IDS 低於不含 SHE』，正文逐字為『Figure 10a shows that the IDS with the SHE is lower than that without the SHE at larger VGS』，而 Fig. 10b 是「相對 Tamb = 300 K 的 IDS 變化率（with/without SHE）」；正確圖號應為 Fig. 10a。證據 URL：https://mdpi-res.com/d_attachment/nanomaterials/nanomaterials-13-02971/article_deploy/nanomaterials-13-02971.pdf （Fig. 10 圖說原文：'(a) The transfer characteristics of NSFET (Nstack = 1) with/without the SHE as the Tamb increases from 300 K to 400 K, (b) IDS variations relative to the IDS at Tamb = 300 K with/without the SHE'）。補充原表未載：Rth = 2.59 K/µW 及其定義 Rth = ΔTmax/total heat、量測元件 WNS ≈ 30 nm／TNS ≈ 10 nm／LG = 30, 40, 60, 500 nm、Nch = 3、量測 Tamb 範圍 −50 ~ 125 °C（25 °C 步進）與模擬 300 ~ 400 K、Sentaurus P-2019.03 + thermodynamic model、Vth = ±300 mV @ 25 °C、第一作者 Peng Zhao 與中科院微電子所單位。

---

## 三13 — Investigation of Analog/RF and linearity performance with self-heating effect in nanosheet FET

- **DOI／識別**：`10.1016/j.mejo.2023.105904`　**來源**：非　**年**：2023（OpenAlex 與 Semantic Scholar 均記 2023；IIT Bhubaneswar 作者頁記 Jul. 2023）
- **作者／單位**：Sunil Rathore（第一作者），Indian Institute of Information Technology Design and Manufacturing (IIITDM) Jabalpur, India；共同作者 Rajeewa Kumar Jaisawal (IIITDM Jabalpur)、P. N. Kondekar (IIITDM Jabalpur)、Navjeet Bagga (Indian Institute of Technology Bhubaneswar，通訊作者)
- **出處**：Microelectronics Journal（Elsevier），Volume 139, Article 105904

**1 元件**　垂直堆疊 GAA nanosheet FET（NSFET）。本次僅取得 metadata：標題與作者機構確認，但節點、Lg、TNS/WNS、堆疊片數、n/p 型別、鰭數／指數等幾何參數本次全部未取得（Elsevier ScienceDirect 403、ResearchGate 403、ADS 405、x-mol 為 CAPTCHA 頁不予繞過）。原表記載為「垂直堆疊 GAA nanosheet FET（3 片）」，本次無法獨立複驗。

**2 方法與 SHE 定義**　`ET-vs-ISO`　未取得。本次未能讀到方法段，無法確認求解器（推測 Sentaurus 但無證據，不予採信）、熱邊界條件、thermode 位置、SurfaceResistance 設定，亦無法確認是否啟用 hydrodynamic 或 BTE／聲子模型。method_type 之 ET-vs-ISO 係沿用原表記載「有／無 lattice heating 比較」，非本次驗證所得。

**3 關鍵定量結果**　未取得（原文印出數字本次無法存取）。本次取得之內容僅限標題、作者、機構、期刊、卷期頁碼，無任何 Ion 下降 %、Rth、ΔT、峰值晶格溫度或偏壓條件。原表已查證記載（視為既有事實，本次未複驗）：摘要印有 ON current 降低 9.4%，但該數字對應 250→400 K 之環境溫度變化（含 SHE 累積效應），依分類法應歸 ta_sweep 而非純 SHE；有／無 lattice heating 之 Ion% 仍為圖形層級，摘要未印出；dT 摘要未給出。本次無任何可逐字引用之英文結果句。

**4 TCAD 校準用途**　不可直接校準，理由：本次未取得任何數值、幾何或熱邊界設定，無法提供 thermode SurfaceResistance 量級、ΔT 比對值或可對齊之幾何。即便採信原表記載的 9.4%，該值為 250→400 K 環境溫度掃描結果，屬 ta_sweep 類別，與使用者要做的「同一 TA 下 ET vs ISO」不是同一件事，直接拿來當 SHE 校準標的會系統性高估。另本篇為 GAA nanosheet 而非 FinFET，幾何與熱路徑（底部 sheet 被 inner spacer 與低導熱層包圍）與 FinFET 不同，橫向外推需另行論證。

**5 批判**
   1. 無數值可判定，原因：本次取得鏈（Semantic Scholar API 回傳 abstract=null、OpenAlex abstract_inverted_index=null、ScienceDirect 403、ResearchGate 403、ADS 405、x-mol CAPTCHA）全數未能取得摘要或全文，因此沒有任何 Ion 下降 %、ΔT 或 Rth 可與 bulk 3-12% / SOI 8-17% 判準帶或 0.10-0.20 %/K 比值做比對。
   2. 分類陷阱高風險：原表已標記其摘要層級的 9.4% 對應 250→400 K 溫度變化，這正是「ta_sweep 被誤當 SHE」的典型案例。任何後續引用若把 9.4% 當作等溫 vs 電熱的 SHE 造成之 Ion 降幅，即為錯誤引用。建議只要用到此數字就必須同時標註溫度區間。
   3. 糾纏因子與外推疑慮：本篇主軸為 analog/RF 與 linearity FOM（gm、fT、線性度指標），這類 FOM 對通道遷移率、寄生電容與偏壓點高度敏感，SHE 之影響會與 RF 萃取條件糾纏；且 GAA nanosheet 的堆疊間熱阻不對稱（底部 sheet 較熱）使單一幾何結論難以外推至 FinFET。
   4. 可重現性資訊缺失：未取得誤差棒、網格收斂性、熱模型參數（聲子邊界散射造成的薄膜熱導率折減）等資訊，無從判斷其電熱解的數值可靠度。

**6 可引用性**　C（僅可當背景引用）— 本次只驗證到書目層級（標題／作者／機構／卷期頁），完全無內容可引用；僅能當「GAA nanosheet FET 之 SHE 對 analog/RF 與線性度有影響」的背景文獻列名，不得引用任何數字或定量結論。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2023.105904?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.mejo.2023.105904
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2023.105904/citations?fields=title,abstract,contexts,intents&limit=20
   - https://secs.iitbbs.ac.in/index.php/navjeet-bagga/

**8 與原表差異**　與原表一致（無衝突）。補充資訊：本次由 OpenAlex 補全作者機構（前三位為 IIITDM Jabalpur，通訊作者 Navjeet Bagga 為 IIT Bhubaneswar）與卷期資訊（Microelectronics Journal Vol. 139, Art. 105904），此為原表未載之新增 metadata。取得層級降級說明：原表曾讀到摘要（記有 9.4%），本次取得鏈全數失敗僅拿到 metadata，故 access_level 標為「僅metadata」，原表的 9.4% 與「3 片堆疊」記載本次未能獨立複驗，沿用但已標明來源為原表。

---

## 三14 — Self-heating effect on logic performance of 6T-SRAM based on CFET device

- **DOI／識別**：`10.35848/1347-4065/ac3c1b`　**來源**：非　**年**：2022（IOP 頁面標示 Published 8 February 2022，Vol. 61 Issue SC；OpenAlex 記線上日期 2021-11-22、Semantic Scholar 記 year=2021，屬 online-first 與正式卷期年份差異）
- **作者／單位**：Songhan Zhao（第一作者），Institute of Microelectronics, Peking University, China；共同作者 Yandong He、Xiaoyan Liu、Gang Du（通訊作者），均為 Institute of Microelectronics, Peking University
- **出處**：Japanese Journal of Applied Physics（JJAP），Volume 61, Issue SC, Article SC1010

**1 元件**　CFET（vertically stacked N-over-P）。原文印出之元件參數："gate length (15 nm), Fin width (30 nm), gate oxide thickness (1.5 nm)"。研究兩種 CFET 型態：fin-based CFET（FBC-CFET，比較 1／2／3 fin）與 sheet-based CFET（SBC-CFET，two-channel），並與 lateral-standard CMOS（LS-CMOS）對照。VDD 範圍 0.7 V 至 1.0 V（0.7 V 為基準，另做 VDD scaling）。非 FinFET 單體元件研究，n 與 p 為垂直堆疊之互補對。nanosheet 之 WNS／TNS 與 SBC-CFET 堆疊數細節本次未取得。

**2 方法與 SHE 定義**　`ET-vs-ISO`　TCAD 電熱模擬（有 SHE vs 無 SHE 對照）。原文逐字："The device simulation experiment was performed using the TCAD-sentaurus tool, in which the hydrodynamic and thermodynamic models are enabled to associate the SHE"。熱邊界／thermode 設定原文逐字："Thermal electrodes were arranged at the top of the metal interconnect and the base of the silicon substrate, with an interface thermal resistance of 2 × 10−8 K • m2 W−1"。通道熱導率原文逐字："thermal conductivities of the NFET (8.07 W m−1 • K−1) and the PFET (6.12 W m−1 • K−1) channels"。啟用 hydrodynamic + thermodynamic；未見 BTE 或顯式聲子模型之敘述（但通道熱導率已被折減至約 6-8 W/m·K，遠低於塊材 Si，隱含已納入奈米尺度聲子邊界散射）。

**3 關鍵定量結果**　【原文印出數字】溫升："Under the stress of a single read operation, the temperature rise of the device is approximately 10 K"（對應偏壓：SRAM 單次 read 操作；VDD 基準 0.7 V）。電路層級延遲：read access time（RAT）"prolonged from 20.75 to 23.03 ps"、write access time（WAT）"extended from 1.29 to 1.38 ps"（有 SHE vs 無 SHE）；由此二組原文數字本人換算得 RAT +11.0%、WAT +7.0%（換算為本人算術，非原文印出）。雜訊邊限：write noise margin 由 316 mV 降至 296 mV；read noise margin 由 132 mV 降至 111.2 mV；另於 1.0 V 供應電壓應力下 RNM 由 168 mV 降至 139 mV（減少 29 mV）。多鰭效應（3-fin vs 1-fin，非 SHE 效應）：RAT 由 35.5 ps 改善至 19.5 ps、WAT 由 2.3 ps 改善至 0.87 ps、RNM 由 72 mV 改善至 150 mV。【明確缺項】元件層級 Ion 下降 % 未印出——本次以逐字擷取方式向全文查詢「device-level Ion / drain-current degradation percentage」，回覆為未見；本文只量化到電路層級。Rth 未以 K/W 形式印出（僅給界面熱阻面密度 2×10⁻⁸ K·m²/W）；峰值晶格溫度絕對值未取得（僅給 ΔT≈10 K）。

**4 TCAD 校準用途**　高價值，但用途限定在「熱邊界設定」而非「Ion% 校準」。(1) thermode SurfaceResistance 量級可直接對齊：原文界面熱阻 2×10⁻⁸ K·m²/W，換算為 Sentaurus SurfaceResistance 慣用單位 = 2×10⁻⁴ K·cm²/W（單位換算為本人算術：1 m² = 10⁴ cm²）。使用者若在 deck 中把 thermode 放在 substrate 底部與 metal 頂部，此值可作為第一版設定與敏感度掃描中心點。(2) thermode 位置策略可直接複製：頂部金屬互連 + 底部矽基板兩處熱電極，避免把 thermode 貼在通道旁而抹掉 SHE。(3) 通道熱導率折減值可直接餵入：NFET 通道 8.07 W/m·K、PFET 通道 6.12 W/m·K，這是奈米通道薄膜熱導率的合理量級，比用塊材 Si 148 W/m·K 更貼近實況。(4) 可 sanity-check：本文 Sentaurus 設定下單次 read 溫升約 10 K；使用者的 FinFET deck 若在類似 VDD（0.7 V）與類似 thermode 配置下算出 ΔT 遠大於數十 K，應懷疑 thermode 過絕熱。(5) 不可用於 Ion% 校準：本文未印出元件層級 Ion 下降 %，且元件為 CFET 非 FinFET。

**5 批判**
   1. 判準帶判定：本篇無元件層級 Ion 下降 % 可直接落入 bulk 3-12% / SOI 8-17% 判準帶。可做的是間接交叉檢核——原文 ΔT≈10 K，若套用交叉檢核比值 0.10-0.20 %/K，推得對應 Ion 降幅僅約 1-2%，落在判準帶下緣之下；但這不構成「SHE 被抹掉」的結論，因為 10 K 是 SRAM 單次 read 之短脈衝動態溫升（讀取窗口僅數十 ps 量級），本質上不等同 DC 飽和區穩態電熱條件，兩者不可直接互比。此點須在引用時明講，否則會誤判此篇的熱邊界過導熱。
   2. 分類正確性佳但層級錯配：method_type 屬 ET-vs-ISO（有／無 SHE 對照）無疑義，不是 ta_sweep 陷阱。但本篇的量化出口全在電路層級（RAT/WAT/RNM/WNM），要餵給元件層級 TCAD deck 只能取其「熱邊界設定」而非「結果數值」，這是使用時最容易搞混的地方。
   3. 元件參數存疑，需自讀原圖確認：原文印出 "Fin width (30 nm)" 搭配 gate length 15 nm 的 CFET，30 nm 對 fin width 而言異常偏大（先進 FinFET 之 Wfin 通常 5-10 nm），此值較可能實為 fin pitch、device width 或圖中另一標註被誤植。引用前務必回原文 Table/Fig. 核對，不可直接把 30 nm 當作 Wfin 填入 deck。
   4. 數字內部一致性有一處待查：WAT 1.29 ps 與 RAT 20.75 ps 相差逾 16 倍，write 比 read 快一個數量級在 6T-SRAM 中並非典型（write 通常受 write-assist 路徑限制），顯示兩者的延遲定義（起訖節點、判準電壓）不同。引用 WAT 數字前需確認其定義，否則跨文獻比較會失真。此外本次兩次抓取同一頁面時，摘取模型對 RAT 劣化幅度分別給出 9.9% 與約 10-11%，而由原文 ps 數值換算應為 11.0%——故本卡一律以原文 ps 值為準，百分比標明為本人換算。
   5. 糾纏因子與外推限制：CFET 為 N-over-P 垂直堆疊，上層元件的散熱必須穿過下層，熱路徑與單層 FinFET 本質不同；且本文同時掃 fin 數（1/2/3）與 sheet 型態（FBC vs SBC），幾何與 SHE 兩個變因在部分比較中未完全解耦（例如 3-fin 的 RNM 改善 72→150 mV 主要來自驅動電流增加而非熱效應）。單一 15 nm Lg 幾何無法外推至其他節點。
   6. 缺誤差棒與重複性資訊：純 TCAD 模擬，未見網格收斂測試、熱模型參數不確定度或多組設定之敏感度分析；界面熱阻 2×10⁻⁸ K·m²/W 為單一給定值，未說明其來源或掃描範圍，使用者採用時應自行做 ±1 個數量級的敏感度掃描。

**6 可引用性**　A（可直接引用數字）— 可直接引用其原文印出之數字與模擬設定（Sentaurus + hydrodynamic/thermodynamic、thermode 位置、界面熱阻 2×10⁻⁸ K·m²/W、通道熱導率 8.07／6.12 W/m·K、ΔT≈10 K、RAT 20.75→23.03 ps、RNM 132→111.2 mV 等），因本次確實讀到全文之方法段與結果段文字。但引用範圍必須限定在 CFET-SRAM 電路層級與熱邊界設定；本篇不提供元件層級 Ion 下降 %，不得用來支撐任何 FinFET 飽和 Ion 降幅之宣稱。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.35848/1347-4065/ac3c1b?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.35848/1347-4065/ac3c1b
   - https://iopscience.iop.org/article/10.35848/1347-4065/ac3c1b

**8 與原表差異**　與原表一致，並大幅補強。原表已記之項目本次全部複驗成立：CFET（vertically stacked N-over-P）、fin-based CFET（FBC-CFET）分類、device-level Ion % NOT reported（本次向全文逐字查詢仍為未見，獨立確認）、SRAM read/write operation 偏壓情境、RNM −29 mV、單次 read 溫升約 10 K。本次新增原表未載之關鍵資料（對使用者 TCAD deck 最有價值）：求解器與模型（TCAD-Sentaurus + hydrodynamic + thermodynamic）、thermode 位置（metal interconnect 頂部與 silicon substrate 底部）、界面熱阻 2×10⁻⁸ K·m²/W、通道熱導率 NFET 8.07／PFET 6.12 W/m·K、Lg 15 nm／fin width 30 nm／tox 1.5 nm、VDD 0.7-1.0 V、RAT 20.75→23.03 ps、WAT 1.29→1.38 ps、WNM 316→296 mV、RNM 132→111.2 mV、3-fin vs 1-fin 對照數字，以及卷期 Vol. 61 Issue SC Art. SC1010。年份備註（非 CORRECTION）：原表記 2022，IOP 頁面 Published 8 February 2022 支持原表；Semantic Scholar 記 2021、OpenAlex 記 2021-11-22 係 online-first 日期，屬資料庫慣例差異而非原表錯誤，引用時建議寫 Jpn. J. Appl. Phys. 61 (2022) SC1010。

---
