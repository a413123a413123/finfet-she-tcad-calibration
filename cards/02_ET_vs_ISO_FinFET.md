# 第二章 · ET-vs-ISO｜矽 FinFET

_模擬中 SHE 的正確定義：同一 deck 開／關晶格加熱之差_

原表 16 篇｜本檔 16 篇｜取得層級：摘要 8、全文 5、僅metadata 3

## 二01 — Impact of Self-Heating on Negative-Capacitance FinFET: Device-Circuit Interaction

- **DOI／識別**：`10.1109/TED.2021.3059180`　**來源**：IEEE　**年**：2021
- **作者／單位**：Om Prakash（Karlsruhe Institute of Technology, KIT, Germany）；共同作者 Girish Pahwa（UC Berkeley，另 NYCU 學術頁列 International College of Semiconductor Technology, NYCU）、Chetan Kumar Dabhi（IIT Kanpur）、Yogesh Singh Chauhan（IIT Kanpur）、Hussam Amrouch（Chair for Semiconductor Test and Reliability (STAR), University of Stuttgart，通訊作者）
- **出處**：IEEE Transactions on Electron Devices（Vol. 68, No. 4, pp. 1420–1424, 論文編號 9377672）

**1 元件**　14-nm 節點 negative capacitance (NC)-FinFET，與同節點 FinFET 對照；閘極堆疊含 ferroelectric (FE) 層（MFIS 型）。bulk/SOI 未載、Lg 未載、Hfin/Wfin 未載、n/p 未載、鰭數未載——摘要僅稱「14-nm NC-FinFET」，全文付費牆未取得。

**2 方法與 SHE 定義**　`model`　3-D thermal TCAD，摘要稱 "after careful calibration with measurements"；分析涵蓋寬頻率範圍（broad range of frequency）；再以 TCAD 校準的 BSIM-CMG 精簡模型做電路級（ring oscillator）模擬，並納入 physics-based NC 模型。核心方法貢獻是「首次分析通道到 gate-stack 的非均勻溫度分布」並提出 gate-stack 溫度與通道溫度的關係式，用以正確計算 Landau–Khalatnikov 模型中溫度相依的 α 參數 → 故 method_type 判為 model（惟其底層分析亦具 ET-vs-ISO 性質，摘要未明言，此為判斷而非原文陳述）。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載，未取得。

**3 關鍵定量結果**　摘要未印任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度；本次僅取得摘要，任何數值皆為圖層級且未取得。可逐字引用之定性結論："On account of the thermal insulating properties of the gate-stack, the ferroelectric (FE) layer is found to be cooler than the channel region under the impact of SHE."；"using the channel temperature to evaluate the temperature-dependent parameter α ... result in a significant overestimation of SHE-induced degradations, such as in the NC voltage gain"；"The SHE is found to dominate for both FinFET and NC-FinFET in the gigahertz range"。偏壓（VGS/VDS/TA）摘要未載。

**4 TCAD 校準用途**　不可直接校準，理由：摘要無任何 Ion%、ΔT、Rth 數值，全文付費牆未取得。但有兩點可直接寫進 deck 的設計紀律：(1) 閘極堆疊為熱絕緣體，gate-stack 溫度顯著低於通道溫度——若使用者把 thermode 放在閘極上方或用 gate 節點溫度代表通道溫度，會系統性低估通道峰值 TL；反之用通道溫度代表整個 stack 則高估退化。(2) SHE 在 GHz 頻段主導 → DC 電熱模擬給出的是 worst-case 上界，可作為使用者飽和區 DC deck 結果的解讀邊界。

**5 批判**
   1. 無數值可判定，原因：摘要未印任何 Ion 下降 %、ΔT 或 Rth，Unpaywall 確認 is_oa=false、無任何 OA 全文，IITK nanolab 出版頁亦未掛 PDF；因此無法對「7-11% / 0.10-0.20 %/K」判準帶做帶內外判定。
   2. 糾纏因子極重：本篇同時含 negative capacitance（鐵電負電容）與 NC-FinFET 特有的 α 溫度相依，判準帶明文將 negative capacitance 列為糾纏因子。即使日後取得全文，其 NC-FinFET 數字不可直接對齊使用者的標準矽 FinFET deck；只有其中作為 baseline 的純 14-nm FinFET 曲線才可能可用。
   3. 分類為 model 屬判斷而非原文陳述：摘要的第一貢獻是溫度映射關係式（model），但「analyze the impact of SHE」的敘述亦可歸 ET-vs-ISO。若使用者的分類表要求單一標籤，需自行決定；本卡已把判斷依據寫在 method_detail，不要當成原文分類。
   4. 熱邊界條件完全不透明：摘要未載 thermode 位置、SurfaceResistance、環境溫度、有無 hydrodynamic/BTE。判斷「是否過絕熱／過導熱」在僅有摘要的條件下無從進行。
   5. 無誤差棒與重複性資訊：TCAD 單一幾何、無變異性統計（同組另有 statistical variability 的工作，但不在本篇範圍內）。

**6 可引用性**　B（只能引用定性結論）— 摘要提供了明確且可逐字引用的定性結論（FE 層比通道冷、以通道溫度估 α 會顯著高估 SHE 退化、SHE 在 GHz 頻段主導），但完全沒有可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2021.3059180?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2021.3059180
   - https://scholar.nycu.edu.tw/en/publications/impact-of-self-heating-on-negative-capacitance-finfet-device-circ
   - https://api.unpaywall.org/v2/10.1109/ted.2021.3059180
   - https://www.iitk.ac.in/nanolab/Publications.html

**8 與原表差異**　與原表一致。原表 verdict=plausible_unveri、記「全文付費牆、摘要無 %、找不到開放 PDF」——本次以 Semantic Scholar 取得完整摘要逐字確認「確無任何 Ion% 與溫度數值」，並以 Unpaywall 獨立確認 is_oa=false（無任何 OA location），故原表判斷成立。本次補全：完整標題、卷期頁碼 68(4):1420–1424、論文編號 9377672、五位作者單位（KIT / UC Berkeley（NYCU 頁另列 NYCU ICST）/ IITK / IITK / Univ. Stuttgart STAR）。

---

## 二02 — Transistor Self-Heating: The Rising Challenge for Semiconductor Testing

- **DOI／識別**：`10.1109/VTS50974.2021.9441002`　**來源**：IEEE　**年**：2021
- **作者／單位**：Om Prakash（Karlsruhe Institute of Technology, KIT, Germany）；共同作者 Chetan K. Dabhi（IIT Kanpur, India）、Yogesh S. Chauhan（IIT Kanpur, India）、Hussam Amrouch（University of Stuttgart, Germany）
- **出處**：2021 IEEE 39th VLSI Test Symposium (VTS)（pp. 1–7）

**1 元件**　n-type 與 p-type FinFET，以 Intel 14 nm 量測資料校準。bulk/SOI、Lg、Hfin/Wfin、鰭數皆未載於摘要。摘要另以背景方式提及 FinFET / nanowire / nanosheet 等 3-D 結構與 SiGe 材料（屬背景敘述，非本篇模擬對象）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　「mature Technology CAD (TCAD) simulations」——求解器名稱未載於摘要；以 Intel 14 nm 量測資料校準 n/p FinFET，再仔細校準工業標準精簡模型 BSIM-CMG 以重現所有量測，目的是讓電路設計者能在大型電路上評估 SHE 對效能與功耗的影響，並開發能揭露 SHE 的 Design-for-Testing 方法。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載，全文付費牆未取得。

**3 關鍵定量結果**　摘要未印任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度（與原表「已證實摘要確無任何 Ion % 數值」一致）。可逐字引用之方法陳述："we investigate the impact of self-heating effects on n-type and p-type FinFET transistors calibrated with Intel 14 nm measurement data using mature Technology CAD (TCAD) simulations"；定性結論："generated heat within the transistor's channel is trapped inside"。本篇數值僅圖層級且未取得。【外部可溯源錨點，出自另一篇論文，不是本篇】Klemme, Salamin, Amrouch, "Upheaving Self-Heating Effects from Transistor to Circuit Level using Conventional EDA Tool Flows", DATE 2023（開放 PDF，本次已下載並抽取文字）明載其 BSIM-CMG 是 "calibrated against Intel 14 nm measurements [9], including accurate calibration for SHE [2]"，而其參考文獻 [2] 正是本篇（二02）。該文 Fig. 2「DC analysis of transistor self-heating」標註 pFinFET "91.6 °C @0.7 V"、nFinFET "65.9 °C @0.7 V"（1–8 fins），並註明 "Note that the presented SHE temperature is an additional temperature increase that comes on top of the die's temperature." — 即 ΔT ≈ 65.9 K (n) / 91.6 K (p) @ 0.7 V。再次強調：這是 DATE 2023 印出的數字，不可標成本篇二02 的數字。

**4 TCAD 校準用途**　本篇本身不可直接校準（摘要無數字）。但它是使用者判準帶中「14nm FinFET n 7.26% / p 8.91% @VDS=0.7V」錨點的 SHE 校準源頭：由 DATE 2023 明確引用鏈 [2]→本篇 可得同一 14 nm 模型的 ΔT ≈ 66 K (n) / 92 K (p) @0.7 V（額外溫升，疊加於晶片溫度之上）。用法：若使用者 deck 在 VDD=0.7 V 跑出 ΔT 遠低於 60 K 或遠高於 100 K，thermode 的 SurfaceResistance 量級即需重設；並可用 7.26/65.9 = 0.110 %/K、8.91/91.6 = 0.097 %/K 做 ΔIon%/ΔT 交叉檢核。注意 DATE 的 ΔT 是含 1–8 fins 的 SPICE/BSIM-CMG 結果，不是單鰭 TCAD 值。

**5 批判**
   1. 無數值可判定（本篇），原因：摘要純為 SHE 對半導體測試之挑戰論述，未印任何 Ion%、ΔT 或 Rth，Unpaywall 確認 is_oa=false。若改用外部溯源鏈的數字（DATE 2023，ΔT 65.9/91.6 K @0.7 V）搭配使用者錨點 7.26%/8.91%，則 ΔIon%/ΔT = 0.110 / 0.097 %/K：n 型落在 0.10–0.20 判準帶內，p 型 0.097 略低於下限（邊界值），整體與判準帶自洽。
   2. 論文定位偏測試方法學（DfT）而非元件物理量測：其貢獻是「讓電路設計者能評估 SHE」，因此即使取得全文，元件層級的 Ion% 表格未必存在，可能只有溫度與延遲/功耗曲線。引用前應先確認全文是否真的印出飽和 Ion 退化百分比。
   3. 熱邊界條件不透明且無誤差棒：摘要未載 thermode 位置、SurfaceResistance、TA、有無 hydrodynamic/BTE。無法判定其 SHE 是否過絕熱；唯一的間接證據是它以 Intel 14 nm 實測校準，這比純模擬可信，但校準的是電性而非熱阻。
   4. 跨文引用風險：本卡 results 中的 65.9/91.6 °C 出自 DATE 2023（Klemme/Salamin/Amrouch），不是本篇。若寫進論文，必須引 DATE 2023 而非 VTS 2021，否則構成錯誤歸屬。
   5. 分類無誤（非 ta_sweep）：摘要明確是 SHE 本體研究（通道內熱被侷限），不是改環境溫度的 ta_sweep。

**6 可引用性**　B（只能引用定性結論）— 摘要只能支撐定性結論（3-D 侷限結構 + 低熱導材料導致通道內侷限自熱、以 Intel 14 nm 實測校準 n/p FinFET TCAD 與 BSIM-CMG），無任何可直接引用的數字；數字須改引 DATE 2023 或取得本篇全文。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/vts50974.2021.9441002?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/vts50974.2021.9441002
   - https://api.unpaywall.org/v2/10.1109/vts50974.2021.9441002
   - https://past.date-conference.com/proceedings-archive/2023/DATA/306.pdf
   - https://www.iitk.ac.in/nanolab/Publications.html

**8 與原表差異**　與原表一致。原表 verdict=confirmed、記「已證實摘要確無任何 Ion % 數值」「TCAD 以 Intel 14nm 量測數據校準」——本次逐字複核摘要，兩點皆成立。本次補全：頁碼 pp. 1–7、作者單位（KIT / IITK / IITK / Univ. Stuttgart）。新增（非原表內容、且屬他文）：經 DATE 2023 開放 PDF 建立的引用鏈證據，其 SHE 校準明示來自本篇，並印出 ΔT 65.9 °C(n) / 91.6 °C(p) @0.7 V——此為外部佐證，非本篇數值，無 CONFLICT。

---

## 二03 — A Junctionless Accumulation Mode NC-FinFET Gate Underlap Design for Improved Stability and Self-Heating Reduction

- **DOI／識別**：`10.1109/TED.2020.2997848`　**來源**：IEEE　**年**：2020
- **作者／單位**：Manoj Kumar（IEC Group (DWLC Lab), IIT Delhi, New Delhi, India）；共同作者 Kritika Aditya、Abhisek Dixit（同單位 IIT Delhi）
- **出處**：IEEE Transactions on Electron Devices（Vol. 67, Issue 8, pp. 3424–3430）

**1 元件**　7-nm 技術節點的 metal-ferroelectric-insulator-semiconductor (MFIS) 型 junctionless accumulation mode (JAM) negative capacitance (NC)-FinFET，與 conventional NC-FinFET 對照。bulk/SOI 未載、Lg 未載、Hfin/Wfin 未載、鰭數未載；通道為 accumulation mode（junctionless），n/p 未明載於摘要。掃描變數為 gate 對 source/drain 的 junction overlap（underlap）長度。

**2 方法與 SHE 定義**　`ET-vs-ISO`　3-D TCAD simulations（求解器名稱未載於摘要）；掃描 gate 至 source/drain 的 junction overlap 長度以觀察 GIDL；核心比較方式是「with and without the self-heating effect (SHE)」（即電熱 vs 等溫）下的 ION/IOFF 比與 peak transconductance gm；另掃描 gate metal work function 對遲滯行為的影響，並比較次臨界區的 transconductance generation factor (TGF)。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載，全文付費牆未取得。

**3 關鍵定量結果**　原文印出數字（摘要）：lattice temperature TL = 321 K。逐字引用："It also gives stable peak transconductance (gm) with and without SHE consideration due to reduced lattice temperature (TL = 321 K)."；另一逐字定性句："the proposed JAM NC-FinFET provides superior ON-state current (ION) to OFF-state current (IOFF) ratio with and without the self-heating effect (SHE)"。摘要未印任何 Ion 下降 %、未印 Rth、未印峰值晶格溫度以外的溫度、未印偏壓（VGS/VDS/TA 皆未載）。ION/IOFF 與 gm 的 with/without SHE 比較僅為圖層級，需自讀原圖（付費牆，本次未取得）。

**4 TCAD 校準用途**　僅可作弱 sanity check，不建議直接校準。可用處：若假設 TA=300 K（論文未印 TA，此為假設），TL=321 K 對應 ΔT≈21 K，可作為 7-nm 級鰭式結構在「已做過熱優化（underlap + junctionless）」條件下的 ΔT 下界參考；使用者標準矽 FinFET deck 若在同節點跑出 ΔT 遠低於 20 K，thermode 很可能貼太近通道。不可用之處：本篇通道是 junctionless accumulation mode 且含鐵電負電容，判準帶明文將 junctionless 與 negative capacitance 列為排除／糾纏特例，其 Ion 與溫度不可與標準矽 FinFET 直接對齊。

**5 批判**
   1. 判準帶判定：僅有 TL = 321 K 一個數字，無 Ion 下降 %，因此 ΔIon%/ΔT 交叉檢核無法執行；若以 TA=300 K 假設換算 ΔT≈21 K，對 7-nm 級元件屬偏低的一端，但因本篇 device 是判準帶明列的排除特例（junctionless、negative capacitance），嚴格說「不適用該判準帶」，不應據此判斷使用者 deck 的對錯。
   2. 糾纏因子最重的一篇：同時疊加 junctionless accumulation mode 通道、ferroelectric 負電容、gate underlap 工程三個變因。321 K 是「提案結構」的值，論文本身把低溫度歸功於這些工程手段，故此數字本質上是優化後結果，不是標準 FinFET 的自熱基線。
   3. 單一幾何、無誤差棒：摘要未提任何變異性、重複性或誤差範圍；TCAD 單點結果。
   4. 偏壓完全缺失：摘要未載 VGS/VDS/TA，321 K 沒有對應偏壓即無法用於任何定量比對——引用時必須註明「偏壓未載」。
   5. 分類無誤（非 ta_sweep）：其比較軸是 with/without SHE，不是掃環境溫度，符合 ET-vs-ISO。

**6 可引用性**　A（可直接引用數字）— TL = 321 K 是摘要原文印出的數字，可直接逐字引用；但引用時必須完整標註其為 7-nm JAM NC-FinFET（junctionless + 負電容 + underlap 優化後）的值且偏壓未載，不可當成標準矽 FinFET 的自熱溫度。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2020.2997848?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2020.2997848
   - https://api.unpaywall.org/v2/10.1109/ted.2020.2997848

**8 與原表差異**　與原表一致。原表 verdict=confirmed、記「7-nm-node junctionless accumulation-mode NC…」「no % printed in abstract；ION/IOFF 與 peak gm 以 with/without self-heating 呈現為 figure level」「TL = 321 K confirmed in abstract」——本次逐字複核摘要，三點全部成立，無衝突。本次補全：完整標題、卷期頁碼 67(8):3424–3430、三位作者單位（IEC Group (DWLC Lab), IIT Delhi）。

---

## 二04 — Thermal-Aware Shallow Trench Isolation Design Optimization for Minimizing I_OFF in Various Sub-10-nm 3-D Transistors

- **DOI／識別**：`10.1109/TED.2018.2882577`　**來源**：IEEE　**年**：2019
- **作者／單位**：Ilho Myeong（Inter-University Semiconductor Research Center, School of Electrical Engineering and Computer Science, Seoul National University, Seoul, South Korea）；共同作者 Dokyun Son（SNU）、Hyunsuk Kim（SNU）、Myounggon Kang（Korea National University of Transportation）、Jongwook Jeon（Konkuk University）、Hyungcheol Shin（SNU）
- **出處**：IEEE Transactions on Electron Devices（Vol. 66, Issue 1, pp. 647–654）

**1 元件**　sub-10-nm 3-D 電晶體三種架構並列：bulk FinFET、SOI FinFET、vertical FET (VFET)。bulk FinFET 另分 high performance (HP) 與 low power (LP) 兩套 STI 設計；SOI FinFET 與 VFET 則提出不區分 HP/LP 的單一設計。Lg、Hfin/Wfin、鰭數、n/p 皆未載於摘要（全文付費牆未取得）。設計變數為 STI 材料種類與 STI 厚度。

**2 方法與 SHE 定義**　`ET-vs-ISO`　依摘要：以 STI 材料類型與 STI 厚度所導致的 interface trap density (Dit) 差異來解釋 IOFF 趨勢；同時分析各結構隨 STI 設計變化的 max lattice temperature (TL,max)、thermal resistance (Rth) 與 on-current (ION) degradation rate；最後比較 HCI/BTI 壽命隨元件溫度（由 STI 設計決定）的變化。故本篇同時具 ET-vs-ISO（ION degradation rate）與 Rth-extraction 兩種性質，主軸判為 ET-vs-ISO。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載，本次未取得全文。

**3 關鍵定量結果**　摘要未印任何數值，但明確確認三個量都有被分析——逐字引用："Max lattice temperature (TL,max)/thermal resistance (Rth)/on current (ION) degradation rate according to STI design in each structure are also analyzed."（僅圖／表層級，數值在全文，本次未取得）。【原表既有記載，本次未能獨立驗證】bulk FinFET 全 SiO2 STI 基準之 ION degradation rate = 7.8%；改用全 Al2O3 降至 3%（HP 方案，IOFF +36%）；另有上層 20 nm SiO2 / 下層 80 nm Al2O3 的混合方案。偏壓（VGS/VDS/TA）在摘要與本次可讀文本中皆未載明。

**4 TCAD 校準用途**　目前不可直接校準，理由：本次僅取得摘要，7.8% / 3% / Rth / TL,max 的實際數值與其對應偏壓皆未取得。但這是本批七篇中對使用者 deck 潛在價值最高的一篇——它是少數同時給出 TL,max、Rth 與 ION degradation rate 三者、且橫跨 bulk FinFET / SOI FinFET / VFET 的研究，取得全文後可一次校準 thermode 的 SurfaceResistance（由 Rth 反推）、驗證 ΔT，並用 ION degradation rate 對齊判準帶。原表記載的 bulk FinFET 7.8% 即為使用者判準帶「bulk FinFET 7.8%（STI 研究）」錨點本身，取得全文是後續最高優先度動作。

**5 批判**
   1. 判準帶判定：本次讀到的內容無任何數值，無法獨立判定；依原表既有記載的 bulk FinFET 7.8%，落在判準帶 bulk 3–12% 之內（且接近標準矽 FinFET 7–11% 的中段），與判準帶自洽——但需注意此 7.8% 正是判準帶錨點來源之一，用它去驗證判準帶構成循環論證，只能當一致性檢查而非獨立驗證。
   2. STI 材料替換是強耦合變因：把 SiO2 換成 Al2O3 同時改變熱導率與 interface trap density (Dit)，摘要明言 IOFF 趨勢是用 Dit 差異解釋。因此「ION degradation 從 7.8% 降到 3%」不是純熱效應的結果，含 interface traps 這個糾纏因子；同時 IOFF +36% 顯示這是效能/漏電的取捨，不是免費的熱改善。
   3. 熱邊界條件不透明：STI 材料本身就是元件的熱邊界，此類研究對 thermode 放在 STI 外側或基板底部極度敏感。摘要未載 thermode 位置與 SurfaceResistance，無法判定 7.8% 基準是否偏絕熱。
   4. 三種架構（bulk / SOI / VFET）不可互相外推：SOI 因 BOX 阻熱，其退化率理應高於 bulk（判準帶亦分列 bulk 3–12% 與 SOI 8–17%），使用者若比對務必挑對架構。
   5. 年份與版本需留意：OpenAlex 記為 2018（TED Early Access），實際刊出為 Vol. 66, Issue 1（2019 年 1 月號）；引用時用 2019 較安全，兩者不衝突。
   6. 無誤差棒與重複性：TCAD 設計掃描，摘要未提任何統計或變異性資訊。

**6 可引用性**　B（只能引用定性結論）— 本次僅取得摘要，只能支撐定性結論（STI 材料與厚度會同時改變 Dit、TL,max、Rth、ION degradation rate 與 HCI/BTI 壽命）；原表的 7.8%/3%/IOFF+36% 雖經原目錄查證，但本次無法獨立複核，數字引用前建議取得全文並核對其偏壓條件。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2018.2882577?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2018.2882577
   - https://api.unpaywall.org/v2/10.1109/ted.2018.2882577
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/TED.2018.2882577/citations?fields=title,contexts&limit=100

**8 與原表差異**　與原表一致（無衝突）。原表 verdict=confirmed 記載的 bulk FinFET 7.8% → Al2O3 3%（HP，IOFF +36%）與 20 nm SiO2 / 80 nm Al2O3 混合方案，本次僅取得摘要，未能獨立驗證亦未查到相反證據（已嘗試 Unpaywall、S2、OpenAlex、Crossref、S2 引用文脈探勘與 SNU 機構庫搜尋，皆無全文）；摘要逐字確認 TL,max / Rth / ION degradation rate 三者確實都在本篇分析範圍內，與原表方向一致。年份備註：OpenAlex publication_year=2018（Early Access），S2 與原表為 2019（TED Vol.66 Iss.1，2019 年 1 月號）——原表 2019 正確，非 CORRECTION。本次補全：完整標題、卷期頁碼 66(1):647–654、六位作者單位（SNU ISRC / 韓國交通大學 / 建國大學）。

---

## 二05 — Study of Self-Heating Effects in Silicon Nano-Sheet Transistors

- **DOI／識別**：`10.1109/EDSSC.2018.8487097`　**來源**：IEEE　**年**：2018
- **作者／單位**：G. Chalia（Department of Electrical Engineering, Indian Institute of Technology Gandhinagar, Palaj, Gujarat, India）；共同作者 Ravi S. Hegde（同單位 IIT Gandhinagar）
- **出處**：2018 IEEE International Conference on Electron Devices and Solid State Circuits (EDSSC)（中國深圳）

**1 元件**　矽 lateral Gate-All-Around (GAA) Nanosheet FET (NSFET)，含 single-channel 與 multi-channel 兩種；對照組為 single-channel FinFET，兩者 footprint 相同且 IOFF 相近。技術節點、Lg、TNS/WNS、堆疊層數、n/p、鰭數皆未載於摘要（全文付費牆未取得）。另有幾何縮放（geometry scaling）掃描。

**2 方法與 SHE 定義**　`ET-vs-ISO`　TCAD 模擬（求解器名稱未載於摘要）；比較方式為在相同 footprint 與相近 IOFF 條件下，比較 NSFET 與 FinFET 因 SHE 造成的 ON-current 退化百分比；另掃描幾何縮放對 SHE 的影響以評估 NSFET 的抗自熱韌性。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載，未取得。

**3 關鍵定量結果**　原文印出數字（摘要）。逐字引用："TCAD results show a 1.8% degradation in ON-current (ION) for a NSFET in comparison to 2.4% for a FinFET with identical footprint and similar OFF-current (IOFF) values."；結論句："we conclude that NSFET exhibits better resilience to SHE in comparison to the FinFET"。即 NSFET ΔIon = 1.8%、FinFET ΔIon = 2.4%。摘要未印 Rth、未印 ΔT、未印峰值晶格溫度、未印任何偏壓（VGS/VDS/TA 皆未載）。

**4 TCAD 校準用途**　可作為「SHE 偏弱側」的邊界對照，但不建議用來校準 thermode。用法：本篇 FinFET 的 2.4% 明顯低於使用者判準帶 bulk 3–12% 的下緣，因此若使用者 deck 在 VDD≈0.7 V 跑出 7–11%，不應把本篇的 2.4% 當成使用者 deck 過強的證據——更可能是本篇的熱邊界較導熱（thermode 較貼近通道）或偏壓較低。另可用其 NSFET/FinFET 比值（1.8/2.4 ≈ 0.75）做「GAA 相對 FinFET 的相對趨勢」定性檢核，但注意此比值方向與多數後續 nanosheet 自熱文獻（GAA 因四面包覆而更嚴重）相反，屬需要警覺的異常點。

**5 批判**
   1. 判準帶判定：落在判準帶「外」（偏低側）。FinFET 2.4%、NSFET 1.8% 皆低於 bulk 3–12% 的下緣，但都大於 1%，故不屬於「SHE 被邊界條件完全抹掉」。可能原因有三：(a) thermode 設得較貼近通道或 SurfaceResistance 太小（過導熱）；(b) 偏壓低於 0.7 V（摘要未載偏壓，無法排除）；(c) 未納入 fin/sheet 內的聲子邊界散射造成的熱導率縮減——2018 年不少 nanosheet 研究仍用 bulk Si 的 κ，會系統性低估 SHE。
   2. 結論方向與領域主流相反：本篇稱 NSFET 比 FinFET 更抗自熱（1.8% < 2.4%），但 GAA nanosheet 通道被閘極四面包覆、且底部常有 BOX 或內間隔物阻熱，多數後續文獻反而認為 GAA 自熱更嚴重。此差異很可能來自「相同 footprint」的比較基準（NSFET 有效寬度較大、電流密度較低）而非本質熱行為，引用時必須連同 identical footprint 的條件一起引，否則會誤導。
   3. 無 ΔT、無 Rth，交叉檢核無法執行：只有 ΔIon% 而沒有溫度，ΔIon%/ΔT 的 0.10–0.20 %/K 判準無從套用；也無法反推 thermode 的 SurfaceResistance 量級。
   4. 偏壓完全缺失且無誤差棒：摘要未載 VGS/VDS/TA，1.8%/2.4% 沒有對應偏壓；單一幾何、無變異性或重複性資訊。
   5. 分類無誤（非 ta_sweep）：其比較軸是 SHE 造成的 ION 退化，不是環境溫度掃描。

**6 可引用性**　A（可直接引用數字）— 1.8%（NSFET）與 2.4%（FinFET）為摘要原文逐字印出的數字，可直接引用；但必須同時引出「identical footprint、similar IOFF」的前提，且應在文中說明偏壓未載、數值低於一般 FinFET 自熱文獻的常見區間。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/edssc.2018.8487097?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/edssc.2018.8487097
   - https://api.unpaywall.org/v2/10.1109/edssc.2018.8487097

**8 與原表差異**　與原表一致。原表 verdict=confirmed 記「FinFET: 2.4% ON-current degradation from SHE; NSFET: 1.8%（adjacent, label separately）— both CONFIRMED verbatim from abstract」「not stated in abstract（偏壓）」「dT: not in abstract」——本次自 OpenAlex 重建的完整摘要逐字複核，四點全部成立。附註：Semantic Scholar 的 abstract 欄位被出版者遮蔽（elided），本次數字實際來源為 OpenAlex abstract_inverted_index 完整重建。本次補全：作者單位（IIT Gandhinagar, Palaj, Gujarat）、會議全名與地點（EDSSC 2018, 深圳）。

---

## 二06 — 3D Coupled Electro-Thermal FinFET Simulations Including the Fin Shape Dependence of the Thermal Conductivity

- **DOI／識別**：`10.1109/SISPAD.2014.6931615`　**來源**：IEEE　**年**：2014
- **作者／單位**：L. Wang（School of Engineering, University of Glasgow, UK）；共同作者 A. R. Brown（Gold Standard Simulations Ltd, Glasgow）、M. Nedjalkov（Institute for Microelectronics, TU Wien, Austria）、C. Alexander（GSS）、B. Cheng（GSS / Univ. of Glasgow）、C. Millar（GSS）、A. Asenov（GSS / Univ. of Glasgow）
- **出處**：2014 International Conference on Simulation of Semiconductor Processes and Devices (SISPAD 2014)（日本橫濱，2014/9/9–11，pp. 269–272）

**1 元件**　奈米級 FinFET：摘要明載同時給出一個 SOI FinFET 範例與一個 bulk FinFET 範例並互相比較。技術節點、Lg、Hfin/Wfin 具體數值、n/p、鰭數皆未載於摘要（全文付費牆，Glasgow Enlighten 亦註明 Full text not currently available）。fin 形狀（height 與 width）是本篇熱導率模型的自變數。

**2 方法與 SHE 定義**　`model`　在 GARAND 'atomistic' 模擬器中自行開發並實作熱模擬模組，求解耦合的 Heat Flow + Poisson + Current Continuity 三方程（摘要層級敘述屬 drift-diffusion 等級的電熱耦合，未提及 hydrodynamic、BTE 或顯式聲子輸運求解）。核心貢獻是提出一個新的近似公式，描述 fin 內 phonon-boundary scattering 造成的熱導率縮減，該公式同時考慮 fin height 與 fin width，且為位置相依（position dependent）與溫度相依（temperature dependent）。研究對象為 FinFET 的 DC 操作。熱邊界條件、thermode 位置與 SurfaceResistance：摘要未載，未取得。

**3 關鍵定量結果**　摘要未印任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度。逐字引用（Enlighten 完整摘要）："A new approximate formula for the reduced thermal conductivity due to phonon-boundary scattering in the fin is presented which considers both the fin height and the fin width, and is both position and temperature dependent."；"Simulation results for a SOI FinFET and a bulk FinFET example are compared and analysed." — 本篇的數值全部僅圖層級且本次未取得。【外部數字，出自他文，不可標成本篇】(1) 同組 IWCE 2015（L. Wang, T. Sadi, M. Nedjalkov, A. Brown, C. Alexander, B. Cheng, C. Millar, A. Asenov, "An advanced electro-thermal simulation methodology for nanoscale device", DOI 10.1109/IWCE.2015.7301989）的引用文脈載："For this FinFET example, the simulation results indicate that the self-heating produces 8.9% degradation for the on-current." 且 "The channel length of this FinFET is 25 nm."、"An SOI FinFET is used as a test bed"。(2) SUPERTHEME 專案 self-heating 成果頁載："The reduced thermal conductivity due to the fin geometry has a dramatic effect on the self-heating, raising the peak temperature from 341 K to 433 K in the case of bulk FinFETs and from 351 K to 457 K in the case of SOI FinFETs."——該頁明確把此結果歸屬於 Wang 等人另投 IEEE TED 的 "Impact of Self-Heating on the Statistical Variability in Bulk and SOI FinFETs"，非本篇。

**4 TCAD 校準用途**　方法論上是本批對 deck 最直接相關的一篇，但數值未取得。可用之處：本篇的核心產出正是使用者 deck 中最容易設錯的一項——fin 內熱導率的幾何縮減。若使用者在 Sentaurus 中仍使用 bulk Si 的 κ，將系統性低估自熱（外部佐證：SUPERTHEME 頁指出納入縮減後 bulk 峰值溫度 341→433 K、SOI 351→457 K，屬他文數字）。實作建議：以 fin height 與 fin width 為參數、位置與溫度相依的 κ(x,T) 表或 PMI 取代常數 κ，並在 ET-vs-ISO 比較前先確認 κ 模型。不可用之處：公式本體與係數在全文中，本次未取得，無法直接抄進 deck。

**5 批判**
   1. 無數值可判定，原因：摘要無任何 Ion%、ΔT 或 Rth，Unpaywall 確認 is_oa=false，Glasgow Enlighten 明確註記無全文。若改用同組 IWCE 2015 的 8.9%（SOI FinFET、Lg=25 nm），則落在判準帶 SOI 8–17% 的下緣、亦落在 bulk 3–12% 內，方向自洽——但該 8.9% 是他文數字，不可歸給本篇。
   2. κ 縮減是把雙面刃：本篇證明納入 fin 幾何相依的 κ 縮減會大幅推高峰值溫度（他文佐證 bulk 341→433 K），意即「κ 模型」與「thermode 熱阻」是兩個會互相補償的旋鈕。使用者若同時把 κ 調低又把 thermode 設得絕熱，會疊加成過強的 SHE；除錯時應先固定 κ 模型再調 thermode。
   3. 單一範例、無誤差棒：摘要只說各給一個 SOI 與一個 bulk FinFET example，沒有統計或重複性；其變異性研究在同組另一篇（TED 投稿）中，不在本篇範圍。
   4. 熱邊界條件不透明：摘要未載 thermode 位置、SurfaceResistance、TA。GARAND 屬非商用（Gold Standard Simulations）工具，其熱邊界設定慣例與 Sentaurus 不同，直接移植數值有風險。
   5. 跨文引用風險高：本卡 results 中的 8.9%（IWCE 2015）與 341→433 K / 351→457 K（SUPERTHEME 頁歸屬於另一篇 TED 投稿）皆非本篇數字。原表已提醒「引用數字前必讀原文 ID-VD 圖」，本次證實此提醒必要。
   6. 分類為 model 屬判斷：摘要的第一貢獻是 κ 公式（model），但整篇也做了 FinFET DC 的電熱模擬；若使用者的分類表偏重「用途」，亦可歸 ET-vs-ISO。

**6 可引用性**　B（只能引用定性結論）— 可直接引用的是方法論定性結論——在 GARAND 中耦合求解 Heat Flow/Poisson/Current Continuity，並提出同時含 fin height 與 fin width、位置與溫度相依的 phonon-boundary scattering 熱導率縮減公式；本篇本身無任何可引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/sispad.2014.6931615?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/sispad.2014.6931615
   - http://eprints.gla.ac.uk/98119/
   - https://api.unpaywall.org/v2/10.1109/sispad.2014.6931615
   - https://www.supertheme.eu/en/project/highlights/self-heating.html
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/SISPAD.2014.6931615/citations?fields=title,authors,year,venue,externalIds,openAccessPdf,contexts&limit=100

**8 與原表差異**　與原表一致（無衝突）。原表 verdict=confirmed 記「GARAND 模擬，含 bulk FinFET 範例」「圖層級；% 數字未印於可取得文字（Enlighten 無全文、IEEE 阻擋）」——本次逐點證實：Enlighten 記錄頁確實註明無全文，Unpaywall is_oa=false。CORRECTION（輕微、屬補正非否定）：原表把本篇歸為「SOI FinFET（含 bulk 範例）」，摘要實際措辭是並列比較 "a SOI FinFET and a bulk FinFET example"，兩者地位對等，宜寫成「SOI 與 bulk 各一範例並比較」。另原表提到的 SUPERTHEME/TED 姊妹作，本次查得其具體數值為 341→433 K（bulk）、351→457 K（SOI），且該頁明確歸屬於 "Impact of Self-Heating on the Statistical Variability in Bulk and SOI FinFETs"（非本篇）；本次另發現同組 IWCE 2015 印出 SOI FinFET 8.9% on-current 退化（Lg=25 nm），同樣非本篇。此二者為原表未載之新增外部佐證。

---

## 二07 — Simulation of self-heating effects in 30nm gate length FinFET

- **DOI／識別**：`10.1109/ULIS.2008.4527143`　**來源**：IEEE　**年**：2008
- **作者／單位**：M. Braccioli（ARCES-DEIS, University of Bologna & IUNET, Via Venezia 52, 47023 Cesena, Italy）；共同作者 G. Curatola（NXP-TSMC Research Center, Leuven, Belgium）、Y. Yang（ECE Department, George Mason University, Fairfax, VA, USA）、E. Sangiorgi（ARCES-DEIS Univ. Bologna & IUNET）、C. Fiegna（ARCES-DEIS Univ. Bologna & IUNET）
- **出處**：2008 9th International Conference on Ultimate Integration of Silicon (ULIS)（義大利 Udine，2008/3/12–14，pp. 71–74）

**1 元件**　30 nm gate length 的奈米級 FinFET。摘要把 buried oxide thickness 列為掃描的幾何參數之一，與 SOI FinFET 架構一致（原表記為 SOI FinFET，方向相符；摘要本身未逐字使用 "SOI" 一詞）。其餘掃描幾何參數為 source/drain extension length、fin-pitch、fin height；Hfin/Wfin 具體數值、n/p、鰭數皆未載，全文付費牆未取得。

**2 方法與 SHE 定義**　`ET-vs-ISO`　三維電熱元件模擬器（three-dimensional electro-thermal device simulator，工具名稱未載於摘要），以不同溫度下的 Monte Carlo 模擬進行校準（"calibrated against Monte Carlo simulations at various temperatures"——這是輸運模型的溫度相依校準，不是環境溫度掃描實驗，故非 ta_sweep）。研究內容是 FinFET 的自熱效應及其對幾何參數（BOX 厚度、S/D extension 長度、fin pitch、fin height）的相依性。熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE/聲子模型：摘要全部未載。附註：以 MC 校準暗示其電性模型高於 drift-diffusion 等級，但摘要未明言使用 hydrodynamic，不可推斷。

**3 關鍵定量結果**　摘要未印任何 Ion 下降 %、Rth、ΔT 或峰值晶格溫度——全部未取得。摘要全文逐字（OpenAlex abstract_inverted_index 完整重建）："This paper presents a detailed thermal analysis of nanoscale FinFET devices. A three-dimensional electro-thermal device simulator, calibrated against Monte Carlo simulations at various temperatures, is adopted in order to study self-heating effects in Fin-FETs, and their dependence on geometrical parameters such as buried oxide thickness, source/drain extension length, fin-pitch and fin height." 本篇所有數值僅圖層級且本次未取得（IEEE 付費牆，Unpaywall is_oa=false，Crossref 亦無摘要）。

**4 TCAD 校準用途**　不可直接校準，理由：無任何數值。唯一可用的是實驗設計層面的指引——它明確指出 SHE 對四個幾何參數敏感：buried oxide thickness、source/drain extension length、fin-pitch、fin height。使用者可據此設計自己的敏感度分析矩陣（尤其 BOX 厚度與 fin pitch 直接決定 thermode 的等效熱阻路徑），但所有數量級仍須由本批其他文獻或自行模擬提供。

**5 批判**
   1. 無數值可判定，原因：摘要完整取得但不含任何 Ion%、ΔT、Rth 或峰值溫度；Unpaywall 確認 is_oa=false、無任何 OA location，S2 引用文脈探勘亦未撈到引用本篇的量化數字。因此無法對 7–11%（或 SOI 8–17%）判準帶做判定。
   2. 年代與節點的外推限制：2008 年的 30 nm gate length FinFET 與使用者的先進節點矽 FinFET 在 fin 尺寸、閘極堆疊材料（高 κ/金屬閘）與供應電壓上差異很大；即使取得全文，其絕對數值也只適合當歷史趨勢背景，不宜用於校準現代 deck。
   3. 關鍵風險是熱導率模型：2008 年多數電熱模擬仍以接近 bulk Si 的 κ 處理 fin，而二06 已證明 fin 幾何相依的 κ 縮減會大幅改變峰值溫度。本篇若未納入 κ 縮減，其自熱會被系統性低估——摘要無法判斷，取用前必須確認。
   4. 分類無誤（非 ta_sweep）：摘要中的 "at various temperatures" 是指模擬器對 Monte Carlo 的校準溫度點，不是把 TA 當自變數的環境溫度掃描；這正是判準帶提醒的最常見分類陷阱，本篇容易被誤判，需特別註記。
   5. 無誤差棒、無重複性、無實驗驗證：純模擬且僅以 MC 交叉校準，摘要未提任何量測驗證。

**6 可引用性**　C（僅可當背景引用）— 僅取得摘要，內容只有方法陳述與掃描參數清單，沒有任何結果數字或可獨立引用的定量結論；只能作為「SHE 對 BOX 厚度／S/D extension 長度／fin pitch／fin height 敏感」這類早期背景引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ulis.2008.4527143?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ulis.2008.4527143
   - https://api.crossref.org/works/10.1109/ulis.2008.4527143
   - https://api.unpaywall.org/v2/10.1109/ulis.2008.4527143
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ULIS.2008.4527143/citations?fields=title,contexts&limit=100

**8 與原表差異**　CORRECTION（取得層級）：原表記 access 為「未取得——全文付費牆內」，本次經 OpenAlex abstract_inverted_index 成功重建並讀到完整摘要，故 access_level 應由「未取得」上修為「摘要」。證據 URL：https://api.openalex.org/works/doi:10.1109/ulis.2008.4527143 。原表其餘記載全部成立且獲本次證實：「候選條目未宣稱任何 %，摘要亦無數字」正確（摘要逐字確認無任何數值）；「30nm gate length」正確；「SOI FinFET」方向相符（摘要以 buried oxide thickness 為掃描參數，與 SOI 架構一致，惟摘要未逐字出現 SOI）。本次補全：五位作者單位（Bologna/IUNET Cesena、NXP-TSMC Leuven、George Mason Univ.）、會議全名與地點頁碼（ULIS 2008, Udine, pp. 71–74）。

---

## 二08 — Role of mechanical stress on the electrothermal and OFF state current in scaled FinFET devices

- **DOI／識別**：`10.1038/s41598-026-46949-1`　**來源**：非　**年**：2026（Semantic Scholar externalIds 與 PMC 均為 2026；PMCID PMC13226672，PMID 41965922）
- **作者／單位**：Shubham（第一作者）與 R. K. Pandey；單位：School of Electronics Engineering, Vellore Institute of Technology, Vellore 632014, India（PMC 全文原文："1School of Electronics Engineering, Vellore Institute of Technology, Vellore, 632014 India"）
- **出處**：Scientific Reports（Nature Portfolio）

**1 元件**　矽 bulk FinFET（原文："The punch-through stopper (PTS) doping profiles in the substrate are integrated with the fabrication flow for controlling the sub-fin leakage current of the bulk FinFET"），3 nm 技術節點；原文："This work mainly considers a n & p-FinFET with a 16 nm channel length, 64 nm fin height, and 5 nm fin thickness as suggested in 3 nm technology node-based FinFET design guidelines"。故 Lg=16 nm、Hfin=64 nm、Wfin=5 nm（高深寬比 tall FinFET，摘要稱 "a tall FinFET device"）。n-FinFET 與 p-FinFET 皆有：n 用 Si1−xCx S/D（碳 mole fraction 0→0.1），p 用 SiGe S/D（Ge 至 90%）。鰭數：全文未明述（fin 數量未取得），為 3D 單元件模擬。

**2 方法與 SHE 定義**　`ET-vs-ISO`　Sentaurus。原文："The FinFET is designed using Sentaurus Sprocess TCAD, and the 3D numerical simulations are performed using Sdevice TCAD." 傳輸模型為 hydrodynamic（HD）耦合量子修正漂移擴散："The HD transport mechanism, solved along with the quantum-corrected drift-diffusion (QDD) transport mechanism, extracts electrothermal parameters." 熱邊界："Thermally resistive boundary conditions (Inhomogeneous Neumann) are applied at the conducting interfaces." 即以熱阻型 thermode（Sentaurus 之 SurfaceResistance）施加於導電接觸界面，而非理想等溫面。Table 1 給出兩類熱阻：Distributed resistance 1×10⁻⁴ – 2×10⁻³ cm²K W⁻¹；Interfacial resistance 1×10⁻⁵ – 1×10⁻³ cm²K W⁻¹。初始／環境晶格溫度 300 K（"the initial lattice temperature is assumed to be 300 K"）。另有 250–350 K 環境溫度掃描，但該掃描僅用於 GIDL 研究，非 SHE 主結果（"The study is performed by varying the ambient temperature from 250 K to 350 K, with a step size of 25 K"）。無 BTE／聲子輸運模型之記載。

**3 關鍵定量結果**　【原文印出數字】n-FinFET："The ID is reduced by 10.6% due to the self-heating effects, when there are no carbon dopants in the source and drain epitaxy." 以及 "In the case of 10% carbon dopants, the ID is reduced by 8.2%." p-FinFET："the ID reduces by 21.6% due to the self-heating in the presence of 90% germanium concentration." 偏壓："the external gate bias (Vg) and drain bias (Vd) are maintained at 0.7 V, as per the IRDS framework."，TA=300 K，屬飽和區（VG=VD=0.7 V）。峰值晶格溫度："elevating the lattice temperature of n-FinFET to 363 K."（摘要與正文；先前抓取顯示對應 10% carbon 條件）與 "the lattice temperature increases to 357 K at 90% germanium concentrations." 摘要另以整數敘述："nearly 11% degradation in ID is observed in the n-FinFET due to the self-heating effects." Rth 數值：未取得（僅有上述 Table 1 之邊界熱阻範圍，非萃取之元件 Rth）。ΔT 對應：n 約 +63 K、p 約 +57 K（由 363/357 K 減 300 K 推得，原文未直接印出 ΔT）。

**4 TCAD 校準用途**　本批對 deck 最有直接價值的兩篇之一。(1) thermode 設定：可直接把 Sentaurus Thermode 的 SurfaceResistance 取在 distributed 1×10⁻⁴ – 2×10⁻³ cm²K/W、interfacial 1×10⁻⁵ – 1×10⁻³ cm²K/W 區間，並用 Inhomogeneous Neumann（熱阻型）而非固定 300 K 等溫面。(2) 幾何對齊：Lg=16 nm / Hfin=64 nm / Wfin=5 nm 的 3 nm 節點 bulk FinFET，可作為使用者 deck 的幾何模板。(3) sanity-check 錨點：VG=VD=0.7 V、TA=300 K 下 n-FinFET Ion 下降 10.6%、峰值 Tlattice≈363 K，若使用者 deck 在同偏壓下算出的 ΔIon 遠低於 7% 或高於 12%，多半是 thermode 距離或 SurfaceResistance 設錯。(4) 提醒：p 型的 21.6% 帶 90% Ge，不可直接拿來對齊純矽 p-FinFET。

**5 批判**
   1. 【判準帶】n-FinFET 落在帶內：10.6%（0% C）與 8.2%（10% C）皆位於 bulk 判準帶 3–12%，且 10.6% 與核心錨點「3nm bulk FinFET n 10.6%」完全一致；交叉比值 8.2%/63 K≈0.13 %/K、10.6%/63 K≈0.17 %/K 亦落在 0.10–0.20 %/K 帶內。p-FinFET 的 21.6% 落在帶外（>20%）：原因是該值伴隨 90% Ge 的 SiGe 源汲，Ge 含量高使晶格熱導率大幅下降並疊加應變效應，屬糾纏條件而非純矽 SHE。
   2. 熱邊界偏保守但不算過絕熱：採用有限熱阻的 Inhomogeneous Neumann 界面，Table 1 給的是「範圍」而非單一值，論文未指明各接觸實際採用哪一個值，重現時存在不可忽略的自由度；使用者若要重現 10.6%，需自行掃這個區間。
   3. 本研究的主軸是機械應變（Si1−xCx、SiGe）與 GIDL，SHE 只是其中一節：ID 的變化同時受 (a) 應變導致有效質量下降、(b) 自熱、(c) 摻雜引入的 50.79% ID 提升等多重因素交纏，抽單一「SHE 造成的 %」時必須確認比較基準是同一幾何的等溫 vs 電熱，而非跨碳濃度比較。
   4. 單一鰭／單一幾何：全文未載模擬鰭數，因此 363 K 峰值溫度無法外推到多鰭多指結構（多鰭會因鄰鰭熱耦合而更熱）。亦無誤差棒或重複性統計，屬單點 TCAD 結果。
   5. 363 K 的歸屬有歧義：摘要把 363 K 與「應變導致高能電子把動能交給晶格」連在一起敘述，而 ID 下降 10.6% 對應的是 0% 碳（無應變）條件，兩者未必同一組。用 ΔIon%/ΔT 做交叉檢核時要留意此配對風險。

**6 可引用性**　A（可直接引用數字）— 開放取用（PMC 全文），Ion 下降 %、峰值晶格溫度、偏壓、TCAD 工具與熱阻邊界條件全部逐字印在正文，可直接引用數字；唯 p 型 21.6% 引用時必須附帶 90% Ge 條件。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/s41598-026-46949-1?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC13226672/

**8 與原表差異**　與原表一致（n 10.6% / 8.2%、p 21.6%、VG=VD=0.7 V、TA=300 K、n 峰值 363 K 全部逐字核實）。新增原表未載之資訊：p-FinFET 峰值 357 K @90% Ge；Sentaurus Sprocess/Sdevice + HD + QDD；Inhomogeneous Neumann 熱阻邊界；Table 1 熱阻範圍 distributed 1e-4–2e-3、interfacial 1e-5–1e-3 cm²K/W；第一作者單位 VIT Vellore；PMCID PMC13226672。另補：250–350 K 環境溫度掃描僅用於 GIDL，非 SHE 結果，勿誤分類為 ta_sweep。

---

## 二09 — A modeling method for self-heating effect of FinFET with wide application range considering characteristic parameter

- **DOI／識別**：`10.1088/1402-4896/adb2f1`　**來源**：非　**年**：2025
- **作者／單位**：Yue Wang（第一作者）；共同作者含 Huaguo Liang、Danqing Li、Hong Zhang、Zhiwei Shao、Yuqi Pan、Maoxiang Yi、Yingchun Lu、Zhengfeng Huang。第一作者單位：未取得（Semantic Scholar 與 IOP 摘要頁均未回傳 affiliation；由共同作者群推測為合肥工業大學體系，但未經證實故記為未取得）
- **出處**：Physica Scripta（IOP Publishing）

**1 元件**　14 nm FinFET，n 型與 p 型皆有；模型另驗證延伸至 10 nm 與 7 nm 製程。幾何（Table 1，14 nm）：Gate length (LG) = 20 nm、Fin Height (HFin) = 42 nm、Fin width (WFin) = 8 nm、Fin pitch (FP) = 42 nm。bulk 或 SOI：原文未明示（未取得），但熱阻表中含 Rth(Sub) 與 Si/SiO2 界面熱阻，顯示有基板散熱路徑，行為接近 bulk。鰭數／指數：未取得。

**2 方法與 SHE 定義**　`model`　以 VGS–VTH–TSHE 的關係建立 SHE 特徵化模型（本質上是以 VTH 當溫度計的 SHE 溫度萃取法），並用 Sentaurus TCAD 做熱模擬與晶格溫度分布驗證；模型內含「有 SHE vs 無 SHE」的 DC 對照（即嵌入式 ET-vs-ISO 比較）。啟用模型（原文列舉）："high field saturation, gate electric field limited inversion, accumulation layer mobility and thin-layer mobility model, as well as the Philips unified mobility model"。熱邊界原文："thermal boundary condition of 300 K is considered at the bottom of the substrate. Equivalent boundary thermal resistances (table 2) are utilized to model the thermal behaviors at source, drain and gate contacts." Table 2 熱阻值：Rth(GSD)（gate/source/drain）= 8.0e-4 cm²KW⁻¹；Rth(Sub) = 1.0e-2 cm²KW⁻¹；R(Si/SiO2) 界面熱阻 = 2.0e-4 cm²KW⁻¹；R(Si/HfO2) 界面熱阻 = 8.3e-4 cm²KW⁻¹。無 hydrodynamic／BTE／聲子模型之記載（未取得）。

**3 關鍵定量結果**　【原文印出數字】IDS 衰減："both pFinFET and nFinFET exhibited a maximum decay of 8.91% and 7.26% in drain-source current (IDS), respectively, when affected by SHE." 最高晶格溫度："the highest lattice temperature of the transistor can reach 399.9 K"（DC 條件下；本次取得的頁面未在該句旁標出對應 VG/VD）。模型適用電壓範圍（摘要逐字）：14 nm nFinFET 於 "a voltage range of 0–0.7 V"、14 nm pFinFET 於 "−0.3−0.7 V"，兩者 "R2 goodness of fit >99.95%" 且 "error <1 °C"。Rth：本文給的是「邊界熱阻設定值」（見 method_detail 的 Table 2），非萃取出的元件 Rth（元件級 Rth 未取得）。ΔT：由 399.9 K − 300 K 推得約 +99.9 K（原文未直接印出 ΔT）。偏壓歸屬：原表已從 IOP 全文頁確認 8.91%／7.26% 對應 VDS=0.7 V（飽和區）、VGS 掃描；本次取得之頁面摘要器未能在該句旁定位到明確偏壓，故該偏壓以原表記載為準，本次未能獨立複驗。

**4 TCAD 校準用途**　本批對 deck 校準價值最高的一篇。(1) thermode SurfaceResistance 可直接抄：閘/源/汲接觸 8.0e-4 cm²K/W、基板 1.0e-2 cm²K/W、Si/SiO2 界面 2.0e-4 cm²K/W、Si/HfO2 界面 8.3e-4 cm²K/W，基板底部固定 300 K —— 這正是 Sentaurus Thermode + SurfaceResistance 的完整一組可複製設定。(2) 幾何對齊：LG=20 nm、HFin=42 nm、WFin=8 nm、FP=42 nm 的 14 nm 節點。(3) sanity-check 雙錨點：同一組設定下 n 7.26% / p 8.91%（@VDS=0.7 V，依原表）與峰值 399.9 K。使用者若照抄上述熱阻卻算出 <3% 或 >12%，代表 thermode 幾何位置（距通道距離、覆蓋面積）與本文不同，應優先檢查 thermode 是否貼在接觸表面而非通道附近。

**5 批判**
   1. 【判準帶】Ion 下降落在帶內：n 7.26%、p 8.91% 皆位於 bulk 判準帶 3–12%，且與核心錨點「14nm FinFET n 7.26% / p 8.91% @VDS=0.7V」完全吻合。但交叉檢核比值落在帶外偏低：7.26%/99.9 K ≈ 0.073 %/K、8.91%/99.9 K ≈ 0.089 %/K，低於 0.10–0.20 %/K。最可能的原因是「最大 IDS 衰減」與「最高晶格溫度 399.9 K」並非同一偏壓點（前者為飽和區 VDS=0.7 V，後者是全掃描範圍內的峰值），因此不應把兩者直接相除；使用者做交叉檢核時必須改用同一偏壓下的 ΔT。
   2. 熱邊界設定完整且偏真實（非理想等溫），這是本文最大的可用性優勢；但 Rth(Sub)=1.0e-2 cm²K/W 比接觸熱阻大一個多數量級，代表大部分熱由源/汲/閘接觸帶走而非基板 —— 這個假設若與使用者的 bulk deck（有較強基板散熱路徑）不符，會系統性高估通道溫度。
   3. 分類注意：本文核心是「特徵化模型」而非單純 SHE 模擬，7.26%／8.91% 是模型驗證過程中的 DC 對照結果。引用時必須明說是 with-SHE vs without-SHE 的 TCAD 對照，不要誤述為量測值。
   4. 單一幾何、單一鰭（鰭數未載）、無誤差棒與重複性統計；模型「延伸驗證至 10 nm 與 7 nm」的部分只給了擬合優度（R²>99.95%、誤差 <1 °C），未給對應節點的 Ion 衰減 %，不可外推。
   5. bulk/SOI 未明示是一個實質缺口：SOI 判準帶（8–17%）與 bulk（3–12%）不同，若本元件其實是 SOI，則 7.26% 會變成偏低而非帶內，結論的方向會改變。

**6 可引用性**　A（可直接引用數字）— IDS 衰減 %、最高晶格溫度、四組邊界熱阻值、幾何表、熱邊界條件均為原文印出數字並已逐字核實，可直接引用；唯偏壓歸屬（VDS=0.7 V）本次未獨立複驗，沿用原表已查證之記載。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1088/1402-4896/adb2f1?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://iopscience.iop.org/article/10.1088/1402-4896/adb2f1

**8 與原表差異**　與原表一致（n 7.26% / p 8.91%、最高晶格溫度 399.9 K、14 nm 且延伸驗證 10/7 nm 全部核實）。新增原表未載之關鍵資訊：Table 2 邊界熱阻 Rth(GSD)=8.0e-4、Rth(Sub)=1.0e-2、R(Si/SiO2)=2.0e-4、R(Si/HfO2)=8.3e-4 cm²KW⁻¹；基板底部 300 K 熱邊界；Table 1 幾何 LG=20 nm/HFin=42 nm/WFin=8 nm/FP=42 nm；模型群組（Philips unified mobility 等）；完整作者名單（Yue Wang 等 9 人）。無衝突。

---

## 二10 — Self-heating effect in nanoscale SOI Junctionless FinFET with different geometries

- **DOI／識別**：`10.48550/arXiv.2403.06271（arXiv 版）；原會議論文 10.1109/CDE52135.2021.9455728`　**來源**：非　**年**：會議論文 2021（IEEE，978-1-6654-4452-1/21，©2021 IEEE）；arXiv 預印本 v1 2024
- **作者／單位**：A. E. Atamuratov（第一作者）；單位：Physics Department, Urgench State University, Urgench, Uzbekistan。共同作者：B. O. Jabbarova、M. M. Khalilloev（同單位）、A. Yusupov（Department of Electronics and Electrical Engineering, Tashkent University of Information Technologies, Tashkent, Uzbekistan）、A. G. Loureriro（Department of Electronics and Computer Sciences, University of Santiago de Compostela, Spain）
- **出處**：2021 13th Spanish Conference on Electron Devices (CDE)，IEEE；arXiv v1 於 2024-03-10 上傳（physics.app-ph）

**1 元件**　SOI Junctionless（accumulation-mode）FinFET，n 型 Si 通道。原文幾何："the thickness of the n-Si channel TSi =9 nm, width in the base Wfinb = 22 nm and width in the channel top depend on the channel shape, which for considered trapeze cross section is Wfint=10 nm, and is zero for triangle cross section"；閘介電 "equivalent thickness of HfO2 gate oxide tox=0.9 nm"；"the width of SiO2 buried oxide (BOX) is Wbox=69.4 nm"；"The thickness of the BOX varies between Tbox=10nm and 150 nm and the length of TiN gate between Lgate=10nm and 40 nm." 校準用參考元件："gate length Lg=13 nm, equivalent gate oxide thickness tox =1.2 nm, height of the channel Tsi= 9 nm, width of the channel W=22 nm." 鰭截面三種：rectangular / trapeze / triangle。鰭數：單鰭（未明述多鰭）。非 GAA/nanosheet/CFET。

**2 方法與 SHE 定義**　`ET-vs-ISO`　原文："The device simulations were carried out using Advanced Sentaurus TCAD." 模型群："along with default carrier transport model, mobility degradation model such as doping dependence to account impurity scattering effect where considered. High field saturation model were used to take into consideration velocity saturation effect. Transverse field effect is included to involve degradation at interfaces. To account self-heating, a thermodynamic model for carrier transport, SRH (temperature dependent) models were included. Density gradient quantization model and mobility degradation due to high-k materials were also taken into consideration." 即使用 thermodynamic（非 hydrodynamic、非 BTE）自熱模型 + density-gradient 量子修正。熱邊界條件：全文未給任何 thermode 位置或 SurfaceResistance 數值（未取得）；僅定性描述散熱路徑（"heat transfer through contacts"、"more heat transfer through back oxide (bottom part of fin) than through air (top part of fin)"）。另提出 BOX 熱路徑解析式：ΔT = (Pt·Tbox)/(Kb·A)，其中 Kb 為背氧熱導率、Pt 為散熱功率、A 為與背氧的接觸面積。

**3 關鍵定量結果**　【僅圖層級，全文未印出任何 Ion 下降百分比】Ion 定性結論逐字引用："Simulation results shows, SHE in the nanoscale SOI JL FinFET induces substantial decreasing of the drain current at high drain and gate voltages." 對應圖為 Fig. 3（rectangular 截面 with/without SHE 的 Id–Vg），圖說標明 "Vds=0.75 V"（另 Fig. 2 校準用 Id–Vg 為 Vds=0.9 V）。溫度分布定性："at the middle of the length (in the channel) the temperature is lower than in lateral parts, near source and drain"。趨勢（Fig. 5、Fig. 6，僅圖層級，數值需自讀原圖）："lattice temperature is increased linearly with increasing the gate length"（Lg=10–40 nm，Tbox=145 nm）；"The lattice temperature is linearly increased with an increase in buried oxide thickness"（Tbox=10–150 nm，Lg=10 nm）。截面比較："At the same conditions highest lattice temperature in the channel is observed in transistor with rectangular cross section." Rth、ΔT、峰值晶格溫度之具體數值：全文未印出（未取得），Fig. 4–6 之縱軸數值需自讀原圖。

**4 TCAD 校準用途**　不可直接校準 Ion 下降 %，理由：全文無任何印出的百分比或溫度數值，Fig. 3–6 皆需自讀原圖；且元件為 junctionless（SHE 判準帶明文排除的特例）。可用之處有三：(1) 模型清單可直接對照使用者 deck 的最低配置（Sentaurus thermodynamic 自熱 + 溫度相依 SRH + density gradient + high-field saturation + doping-dependence mobility）；(2) ΔT = Pt·Tbox/(Kb·A) 提供一個檢查 BOX／埋氧熱阻是否設得合理的解析 sanity-check —— 若使用者在 SOI deck 中掃 Tbox 而 ΔT 不呈線性，代表熱邊界設錯；(3) 提供「通道中央溫度低於源汲兩側」這個空間分布特徵，可用來檢驗使用者 deck 的 thermode 是否貼太近通道（貼太近會把這個分布抹平）。

**5 批判**
   1. 【判準帶】無數值可判定，原因：全文未印出任何 Ion 下降百分比或晶格溫度數值，僅有 "substantial decreasing of the drain current" 這類定性敘述與圖層級趨勢；且元件為 SOI junctionless FinFET，屬判準帶明文排除的特例（junctionless 通道全域摻雜、無 p-n 接面，其自熱—電流耦合行為不可與標準矽 FinFET 直接並列）。
   2. 熱邊界條件完全未載，是本文最大的可複現性缺陷：沒有 thermode 位置、沒有 SurfaceResistance、沒有基板／接觸熱阻值，只有定性的散熱路徑敘述。任何人都無法重現 Fig. 5、Fig. 6 的絕對溫度，只能重現趨勢。
   3. 糾纏因子：Fig. 5「晶格溫度隨閘長線性上升」的解釋是以「閘極法向場涵蓋的自由電子數增加」為機制，但閘長增加同時改變飽和電流、散熱面積與功率密度，論文未把功率固定住做控制比較，因此該線性關係的物理歸因未經隔離驗證。
   4. 單一元件、單一鰭、無誤差棒、無重複性統計；且校準比對（Fig. 2）用的是文獻 [5] 的 trigate junctionless nanowire 實驗，與本文三種截面的模擬元件幾何並不完全相同（校準元件 Lg=13 nm、tox=1.2 nm，模擬元件 tox=0.9 nm、Lg 掃 10–40 nm），calibration 的可轉移性有限。
   5. 版本與年份陷阱：arXiv v1 標 2024，但這是 2021 CDE 會議論文的後上傳版（PDF 頁首明載 ©2021 IEEE、DOI 10.1109/CDE52135.2021.9455728）。引用年份應以 2021 為準，勿寫成 2024。

**6 可引用性**　B（只能引用定性結論）— 只能引用定性結論（SHE 在高 VD/VG 下顯著降低汲極電流、晶格溫度隨 Lg 與 Tbox 線性上升、通道中央溫度低於側邊、矩形截面最熱）與模型清單；全文無可引用的數字，Ion% / ΔT / Rth 一律缺席。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/arXiv:2403.06271?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://arxiv.org/abs/2403.06271
   - https://arxiv.org/pdf/2403.06271

**8 與原表差異**　與原表一致（Lg 10–40 nm、Si 通道厚度、僅圖層級無印出 %、逐字引用 "SHE in the nanoscale SOI JL FinFET induces subs…" 已在全文第 2 頁核實、Fig. 3 之 VDS=0.75 V、晶格溫度隨 Lg 上升等全部核實）。新增原表未載之資訊：完整作者單位（Urgench State University / TUIT / USC Santiago de Compostela）；tox(HfO2)=0.9 nm、Wbox=69.4 nm、Wfinb=22 nm、Wfint=10 nm、TSi=9 nm、TiN gate；Tbox 掃 10–150 nm；Fig. 5 之 Tbox=145 nm、Fig. 6 之 Lg=10 nm；模型清單（thermodynamic + 溫度相依 SRH + density gradient）；ΔT=Pt·Tbox/(Kb·A) 解析式；Fig. 2 校準用 Vds=0.9 V；會議全名 2021 13th Spanish Conference on Electron Devices (CDE)。無衝突。

---

## 二11 — Impact of Variation in Fin Thickness and Self-Heating on the Output Characteristics of Triangular Gate FinFETs

- **DOI／識別**：`10.1007/s12633-023-02835-3`　**來源**：非　**年**：2024（線上 2024-01-04；印刷期別 2024 年 4 月）
- **作者／單位**：M. Hemalatha（第一作者）；單位：Department of ECE, Thiagarajar College of Engineering, Madurai, India。共同作者：N. B. Balamurugan（同單位）、M. Suguna（Department of CSE, Thiagarajar College of Engineering）、D. Sriram Kumar（Department of ECE, National Institute of Technology Tiruchirappalli, India）
- **出處**：Silicon（Springer Nature），Vol. 16, Issue 5, pp. 2253–2266

**1 元件**　Triangular Gate FinFET（TG-FinFET），研究變數為 fin thickness 變異。技術節點、Lg、Hfin、Wfin 具體數值、n/p 型、鰭數、bulk/SOI：全部未取得（Springer 全文與摘要頁經 idp.springer.com 認證重導、ResearchGate 與 colab.ws 皆回 403；OpenAlex 與 Crossref 之 abstract 欄位皆為 null）。原表記載為「Triangular-gate silicon FinFET (TG-FinFET), fin thickness …」，本次無法補完。

**2 方法與 SHE 定義**　`未取得`　未取得。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、是否採用 hydrodynamic／BTE／聲子模型，皆無任何可讀取的來源。本次取得之最完整敘述僅為搜尋引擎回傳的出版者摘要片段，其中提到研究對象為 fin thickness 變異與自熱對 TG-FinFET 輸出特性及晶格溫度的影響，未及方法細節。

**3 關鍵定量結果**　未取得（原表記為 plausible_unveri，本次仍無法突破）。唯一取得的定性片段（來源為搜尋引擎回傳之 Springer 摘要文字，非直接載入之出版者頁面）：SHE 導致平均電子速度下降與平均電子遷移率劣化。Ion 下降 %、Rth、ΔT、峰值晶格溫度、對應偏壓（VGS/VDS/TA）：全部未取得。原表註記「% still not obtained — abstract numerals are truncated in BOTH Springer render and colab.ws mirror ('SHE causes an avera…')」，本次以四條路徑（Semantic Scholar API、OpenAlex、Crossref、Springer/ResearchGate/colab.ws 直取）重試，全部失敗，證實原表判斷。

**4 TCAD 校準用途**　不可直接校準，理由：本次未取得任何數值（Ion%、ΔT、Rth、偏壓皆無），亦未取得元件幾何與熱邊界設定，無任何可餵給 deck 的參數或可對齊的幾何。此外元件為 triangular-gate 特殊閘極形狀，即使日後取得數值，也不能直接對齊使用者的標準矩形鰭 FinFET —— 三角閘的截面積與散熱路徑與矩形鰭不同（可對照二10 的結論：相同底寬下矩形截面最熱）。

**5 批判**
   1. 【判準帶】無數值可判定，原因：兩次獨立查證（原表一次、本次一次）都未能取得任何 Ion 下降百分比、ΔT 或 Rth；Springer 全文需訂閱、ResearchGate/colab.ws 回 403、OpenAlex 與 Crossref 的 abstract 欄位皆為 null，摘要數字在所有可及的 render 中都被截斷。
   2. 分類風險未解：標題同時包含「fin thickness 變異」與「self-heating」，在無法讀到方法段的情況下，無法排除該文的溫度結果其實來自環境溫度掃描（ta_sweep）而非真正的 with-SHE / without-SHE 電熱對照 —— 這正是本領域最常見的分類陷阱，在取得全文前不應把此文列為 ET-vs-ISO 證據。
   3. 糾纏因子明顯：三角閘幾何本身就會改變閘控能力、有效通道截面與散熱路徑，fin thickness 變異又是第二個變數，兩者與 SHE 三重交纏；即使取得百分比，也難以抽出「純 SHE」的貢獻。
   4. 無誤差棒、無重複性資訊可判定（連結果本身都未取得）；且期刊 Silicon 屬材料導向期刊，元件模擬細節（熱邊界、thermode）在該刊常被簡略處理，即使取得全文也未必有可複製的 SurfaceResistance 設定。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用。可驗證的只有書目層級事實（題目、作者、單位、期刊卷期頁碼、年份）與「該文研究 TG-FinFET 的 fin thickness 變異與自熱」這個主題陳述；沒有任何可引用的數字，連摘要全文都未能直接載入，因此不宜作為定量或定性結論的依據。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s12633-023-02835-3?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1007/s12633-023-02835-3
   - https://api.crossref.org/works/10.1007/s12633-023-02835-3

**8 與原表差異**　與原表一致（原表 verdict = plausible_unveri，本次重試四條路徑仍未取得數值，確認原表判斷正確）。新增原表未載之資訊：完整作者名單與單位（M. Hemalatha / N. B. Balamurugan / M. Suguna，Thiagarajar College of Engineering, Madurai；D. Sriram Kumar，NIT Tiruchirappalli）；卷期頁碼 Silicon 16(5):2253–2266。無衝突。

---

## 二12 — Physical insights of interface traps and self-heating effect on electrical response of DMG FinFETs in overlap and underlap configurations: analog/RF perspective

- **DOI／識別**：`10.1088/1402-4896/ad16b0`　**來源**：非　**年**：2023-12-29 線上出版（Crossref published date）；期別為 Vol. 99 Issue 1（2024 年 1 月號）。原表記 2024，指的是期別年。
- **作者／單位**：Rashi Chaudhary（第一作者）與 Rajesh Saha。單位：本次未從 Semantic Scholar 或 Crossref 取得本文之 affiliation（未取得）；同組作者在同期 Microelectronics Journal 論文（二13、二14）之 OpenAlex 記載為 Malaviya National Institute of Technology Jaipur（Chaudhary）與 NIT Silchar / MNIT Jaipur（Saha），僅供參考、非本文原文證據。
- **出處**：Physica Scripta（IOP Publishing），Vol. 99, Issue 1, Article 015406

**1 元件**　SOI Dual-Material-Gate（DMG）FinFET，三種組態：conventional、gate-overlap、gate-underlap。原表記 Lg = 16 nm（conventional）。本次僅取得摘要，元件節點、Hfin、Wfin、氧化層厚度、功函數配置、underlap/overlap 長度、n/p 型、鰭數皆未從本次來源取得（未取得）；IOP 全文頁本次遭 Radware bot 驗證重導，無法載入。

**2 方法與 SHE 定義**　`ET-vs-ISO`　未取得（本次僅取得 Crossref 沉積之出版者摘要，未能載入 IOP 全文）。可從摘要確認的方法輪廓：先做「acceptor 界面陷阱電荷（ITCs）單獨」與「self-heating 單獨」的獨立模擬對照（"the independent simulations for acceptor ITCs and Self-heating in conventional device"），再做兩者疊加的累積效應分析，並區分 Uniform 與 Gaussian 兩種陷阱分布。求解器名稱、熱邊界條件、thermode 位置與 SurfaceResistance、是否用 hydrodynamic/BTE：全部未取得。原表註記偏壓為 VDS = 0.5 V、VGS 掃 0→1.5 V（已由原表從 IOP 頁面核實），本次無法獨立複驗。

**3 關鍵定量結果**　【原文印出數字，來源為 Crossref 沉積之出版者摘要，逐字】SHE 單獨 vs ITCs 單獨："performance degradation caused by Self-heating is more prominent (25.03%) than uniform acceptor ITCs (9.46%)"。SHE 與 ITCs 疊加後的汲極電流退化："the degradation in drain current is higher in overlap configuration (45.2%, 54.5%) as compared to conventional (30.4%, 40.96%) and underlap (37.2%, 52.8%) configurations for both Uniform and Gaussian trap distributions, respectively." 偏壓：摘要未載；依原表已核實之記載為 VDS = 0.5 V、VGS 掃 0→1.5 V。ΔT、峰值晶格溫度、Rth：摘要無數值（原表已核實「摘要無數值」），本次亦未取得。

**4 TCAD 校準用途**　不可直接校準 thermode／Rth，理由：本次未取得任何熱邊界設定、Rth 或 ΔT 數值，且 IOP 全文無法載入。有限的可用性有二：(1) 可作為「SHE 單獨貢獻遠大於界面陷阱單獨貢獻」（25.03% vs 9.46%）的定性對照，提醒使用者若 deck 中同時開了 interface trap 模型，會把 SHE 的效應高估；(2) 可作為反向 sanity-check —— 25.03% 已遠超標準矽 FinFET 判準帶上限（12%），若使用者的純矽 FinFET deck 算出這個量級，幾乎可斷定 thermode 過絕熱或偏壓／元件設定與標準情境不符。另注意其 VDS=0.5 V 低於使用者的 0.7 V 情境，功率密度基準不同。

**5 批判**
   1. 【判準帶】25.03%（SHE 單獨、conventional）落在判準帶外且遠超上限，30.4%–54.5%（SHE+ITCs）更是嚴重超出。但這不等於論文有錯：判準帶明文排除 DMG 特例，本元件為 SOI + 雙材料閘（DMG）通道工程 + 界面陷阱疊加，屬多重糾纏條件；SOI 埋氧的低熱導率本就使 SHE 遠強於 bulk（SOI 帶 8–17% 亦不足以涵蓋 25%），合理推測其熱邊界比一般 bulk 設定更絕熱。此數字不可用於使用者的矽 bulk FinFET deck 校準。
   2. 糾纏因子是本文的結構性問題：DMG 通道工程 + overlap/underlap 幾何 + 兩種陷阱分布（Uniform/Gaussian）+ SHE，四個變數同時作用。摘要中 45.2%/54.5% 等數字全部是「SHE 與 ITCs 累積」的結果，唯一乾淨的純 SHE 數字只有 conventional 的 25.03%。引用時務必區分。
   3. 偏壓歸屬未在本次獨立複驗：摘要未載偏壓，原表記 VDS=0.5 V、VGS 掃 0→1.5 V。若 25.03% 是在 VGS=1.5 V 這種遠高於 VDD 的過驅動點取得，則功率密度遠大於使用者的 0.7 V 情境，百分比自然被放大 —— 這是判準帶外的另一個合理解釋，需全文才能釐清。
   4. 「degradation in drain current」的定義未在摘要中界定：是飽和區 ION、是峰值 gm 對應點、還是整條 ID–VG 曲線上的最大差值，三者數值可差一倍以上。無全文即無法確定，這使 25.03% 難以與其他論文的 Ion 下降 % 並列比較。
   5. 年份標註需留意：Crossref 線上出版日為 2023-12-29，Semantic Scholar 標 year=2023，而期別為 Vol. 99 Issue 1（2024）。引用時建議寫 2024（期別年）並註明線上 2023-12-29，避免與同組作者其他論文混淆。

**6 可引用性**　A（可直接引用數字）— 25.03%、9.46%、45.2%/54.5%、30.4%/40.96%、37.2%/52.8% 全部逐字印在出版者沉積於 Crossref 的正式摘要中，可直接引用數字。但引用時必須同時載明：SOI + DMG + 界面陷阱之糾纏條件、以及僅 25.03% 為純 SHE 貢獻 —— 這些數字不能被當作標準矽 FinFET 的 SHE 幅度代表值。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1088/1402-4896/ad16b0?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.crossref.org/works/10.1088/1402-4896/ad16b0

**8 與原表差異**　與原表一致（SHE 單獨 25.03%、conventional 30.4%/40.96%、overlap 45.2%/54.5%、underlap 37.2%/52.8%、摘要無溫度數值 —— 全部逐字核實）。新增原表未載之資訊：uniform acceptor ITCs 單獨貢獻 9.46%；卷期頁碼 Physica Scripta 99(1):015406。年份需註記（非錯誤，僅需標清）：Crossref 線上出版日 2023-12-29、Semantic Scholar 記 year=2023，而期別為 2024；原表記 2024 對應期別年，合理。偏壓 VDS=0.5 V / VGS 0→1.5 V 本次因 IOP 遭 bot 驗證阻擋而未能獨立複驗，沿用原表已核實之記載。

---

## 二13 — Analysis of thermal stability in underlap and overlap DMG FinFETs including self-heating effects

- **DOI／識別**：`10.1016/j.mejo.2024.106152`　**來源**：非　**年**：2024（Crossref 印刷期別 2024 年 4 月；OpenAlex 線上出版日 2024-03-09）
- **作者／單位**：Rashi Chaudhary（第一作者）；單位：Malaviya National Institute of Technology Jaipur, India。共同作者：Rajesh Saha（National Institute of Technology Silchar, India）、Menka Yadav（Malaviya National Institute of Technology Jaipur, India，通訊作者，ORCID 0000-0003-1700-8343）
- **出處**：Microelectronics Journal（Elsevier），Vol. 146, Article 106152

**1 元件**　SOI Dual-Material-Gate（DMG）FinFET，三種組態：conventional、gate-underlap、gate-overlap（與二12、二14 同一作者群、同一元件家族）。技術節點、Lg、Hfin、Wfin、氧化層、功函數、underlap/overlap 長度、n/p 型、鰭數：本次全部未取得（ScienceDirect 與 dl.acm.org 直取皆回 HTTP 403；OpenAlex 與 Crossref 之 abstract 欄位皆為 null；Semantic Scholar abstract 為 null）。原表記載與二12 同組、Lg 同級（16 nm 級），僅供參考。

**2 方法與 SHE 定義**　`ET-vs-ISO`　未取得。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、是否使用 hydrodynamic/BTE/聲子模型，本次皆無可讀取來源。可確認的方法輪廓（來源為搜尋引擎回傳之 ScienceDirect 摘要文字，該頁面本身直取回 403）：比較有／無 SHE 下 conventional、underlap、overlap 三種 DMG FinFET 的 DC 特性與熱參數，計算 ION、IOFF、gm,max、ION/IOFF 比與 DIBL 的下降率。是否含 Rth 萃取：搜尋摘要提及計算熱參數，但本次無法直接驗證，記為未取得。

**3 關鍵定量結果**　【摘要層級數字；但本次的取得管道為搜尋引擎回傳的出版者摘要文字，ScienceDirect 與 dl.acm.org 頁面直取皆回 HTTP 403，故未列入 sources】SHE 造成之最大 ON-current 下降 41.73%（gate-overlap 組態，但該組態的絕對 ION 仍為三者最大）；最大 off-current 下降 69.01%（gate-underlap 組態）。此二數值與原表記載完全一致，構成兩次獨立查證的雙來源吻合。偏壓（VGS/VDS/TA）、ΔT、峰值晶格溫度、Rth 數值：全部未取得（原表亦記「摘要未載（全文未讀取）」「摘要無數值」）。

**4 TCAD 校準用途**　不可直接校準，理由：無偏壓條件、無 ΔT、無 Rth、無熱邊界設定，41.73% 這個數字缺少可對齊的操作點，餵不進 deck。唯一的可用方式是反向 sanity-check：41.73% 遠超標準矽 FinFET 判準帶（bulk 3–12%、SOI 8–17%），可作為「什麼樣的設定會產生過強 SHE」的參照 —— SOI + DMG + gate-overlap 三重條件疊加。使用者若在純矽 bulk FinFET deck 中出現 40% 量級的 Ion 下降，應立刻檢查 thermode 是否被移除或 SurfaceResistance 是否設得過大（過絕熱）。

**5 批判**
   1. 【判準帶】41.73% 落在判準帶外，遠超 20% 的「SHE 過強」門檻。但判準帶明文排除 DMG 特例，且本元件為 SOI（埋氧低熱導率）+ 雙材料閘 + gate-overlap 通道工程三重糾纏，與標準矽 FinFET 不可直接並列；此數字不能用來質疑論文，也不能用來校準使用者的 deck。
   2. 無偏壓即無意義：ON-current 下降 41.73% 若取自高過驅動點（同組作者的二12 記載 VGS 掃至 1.5 V），功率密度遠高於使用者的 VDD≈0.7 V 情境，百分比自然被放大。在取得全文確認偏壓前，此數字不可與 7–11% 這類 0.7 V 錨點並列比較。
   3. 糾纏因子：overlap 設計的有效通道長度較短、閘控較強，其 ON 電流基數本來就最大，因此「下降百分比最大」與「絕對電流仍最大」同時成立 —— 摘要自己也點明這件事。用百分比排序來判斷「哪個結構抗自熱較好」會得到錯誤結論，必須看絕對值。
   4. 取得管道有瑕疵，需標示：本次未能直接載入任何出版者頁面（ScienceDirect 403、dl.acm.org 403、x-mol 需登入、scholar.archive.org 500），41.73%/69.01% 是由搜尋引擎回傳的出版者摘要文字取得。雖與原表完全一致，但嚴格說仍非第一手直讀，寫進論文前建議透過機構訂閱補一次全文核對。
   5. 無誤差棒與重複性資訊；亦無 ΔT 或 Rth 可做 ΔIon%/ΔT 交叉檢核，因此無法判斷 41.73% 究竟是熱邊界過絕熱造成，還是偏壓點造成。

**6 可引用性**　B（只能引用定性結論）— 可引用定性結論（SHE 下 gate-overlap 的 ON 電流跌幅最大但絕對 ION 仍最高、underlap 的 OFF 電流跌幅最大）。41.73%/69.01% 兩個數字雖經兩次獨立查證吻合，但本次無法直接載入出版者頁面、且完全缺少偏壓條件，因此不建議當作可直接引用的定量錨點；若必須引用數字，應先取得全文補齊偏壓。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2024.106152?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.mejo.2024.106152
   - https://api.crossref.org/works/10.1016/j.mejo.2024.106152

**8 與原表差異**　與原表一致（41.73% ON-current 最大跌幅發生於 gate-overlap 且其絕對 ION 仍最大、69.01% off-current 最大跌幅發生於 underlap、摘要未載偏壓與溫度數值 —— 均與原表吻合）。新增原表未載之資訊：完整作者單位（Chaudhary 與 Yadav 於 MNIT Jaipur、Saha 於 NIT Silchar，Yadav 為通訊作者）；卷期 Microelectronics Journal 146:106152；線上出版日 2024-03-09。取得限制須標明：本次 ScienceDirect（S0026269224000648）與 dl.acm.org 直取皆回 HTTP 403，兩個百分比係經搜尋引擎回傳之出版者摘要文字取得，非第一手直讀頁面，故未列入 sources。無衝突。

---

## 二14 — Impact of self-heating on RF/analog and linearity parameters of DMG FinFETs in underlap and overlap configurations

- **DOI／識別**：`10.1016/j.mejo.2023.105765`　**來源**：非　**年**：2023（Crossref 期別 2023 年 5 月；OpenAlex 線上出版日 2023-03-24）
- **作者／單位**：Rashi Chaudhary（第一作者）；單位：Malaviya National Institute of Technology Jaipur, India。共同作者：Rajesh Saha（同單位，通訊作者，ORCID 0000-0003-3108-6081）
- **出處**：Microelectronics Journal（Elsevier），Vol. 135, Article 105765

**1 元件**　SOI Dual-Material-Gate（DMG）FinFET，三種組態：conventional、overlap、underlap（與二12、二13 同一元件家族）。技術節點、Lg、Hfin、Wfin、氧化層厚度、雙材料閘功函數、underlap/overlap 長度、n/p 型、鰭數：本次全部未取得（ScienceDirect 直取回 HTTP 403 或重導至 linkinghub；Semantic Scholar、OpenAlex、Crossref 之 abstract 欄位皆為 null；scribd 鏡像僅有預覽頁無正文）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　未取得。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE，本次皆無可讀取來源。可確認的方法輪廓（來源為搜尋引擎回傳之出版者摘要文字，頁面本身 403）：以 TCAD 模擬比較有／無自熱下 SOI DMG FinFET 三種組態的 RF/analog 與線性度參數（gm、gd、本質增益、VIP2、VIP3、IIP3、1 dB 壓縮點）。

**3 關鍵定量結果**　【摘要層級數字；取得管道為搜尋引擎回傳的出版者摘要文字，ScienceDirect 頁面直取回 HTTP 403，故未列入 sources】gm,max 退化：conventional 8%、overlap 28.3%、underlap 6.9%。gd 下降：conventional 30.3%、overlap 40.9%、underlap 33.3%。本質增益（intrinsic gain）峰值上升：52.4%、28.1%、57.7%（conventional/overlap/underlap）。線性度參數 VIP2、VIP3、IIP3、1 dB 壓縮點在自熱下劣化。Ion 下降 %：摘要無（原表已核實「摘要無 Ion %」）。偏壓（VGS/VDS/TA）、ΔT、峰值晶格溫度、Rth：全部未取得。上述 gm/gd 數值與原表記載完全一致，構成兩次獨立查證的雙來源吻合。

**4 TCAD 校準用途**　不可直接校準，理由：無 Ion 下降 %、無 ΔT、無 Rth、無熱邊界設定、無偏壓，沒有任何可餵進 deck 的量化參數。間接可用性有一：gm 與 gd 的退化幅度不一致（gd 退化 30–41% 遠大於 gm 退化 7–28%）提供一個 deck 自檢的定性期待 —— 使用者若在飽和區加入自熱，應同時看到輸出電導的顯著改變（自熱在飽和區會產生負微分電阻傾向），若 deck 只有 Ion 下降而 gd 幾乎不動，代表熱電耦合可能沒有真正在偏壓點上收斂。

**5 批判**
   1. 【判準帶】無數值可判定，原因：摘要無任何 Ion 下降百分比（此點原表已核實、本次確認），全部可得數字皆為 gm、gd、本質增益等小訊號參數，判準帶（飽和 Ion 下降 7–11%、ΔIon%/ΔT 0.10–0.20 %/K）無法套用；亦無 ΔT 可做交叉檢核。
   2. 與使用者主題的相關性偏低：本文的落點是 RF/analog 與線性度（VIP2/VIP3/IIP3/1 dB 壓縮點），不是飽和區汲極電流。對「SHE 對飽和 Ion 的影響」這個主軸只能提供周邊佐證。
   3. 糾纏因子：SOI + DMG 雙材料閘 + overlap/underlap 通道工程三重疊加，且 overlap 的 gm 退化（28.3%）是 underlap（6.9%）的四倍，這個差異同時受有效通道長度、閘控強度與熱路徑影響，摘要層級無法拆解歸因。
   4. 取得管道有瑕疵，需標示：本次未能直接載入 ScienceDirect 或任何出版者頁面（403 / 重導至 linkinghub / scribd 僅預覽），數值係由搜尋引擎回傳之出版者摘要文字取得。雖與原表逐項吻合，仍非第一手直讀，正式引用前建議補全文。
   5. 無誤差棒、無重複性統計、無偏壓標註；且 gd「下降 30.3%」與本質增益「上升 52.4%」在物理上是同一件事的兩面（Av=gm/gd），摘要把兩者並列成兩組數字，易造成重複計數的錯覺，引用時應擇一。

**6 可引用性**　B（只能引用定性結論）— 可引用定性結論（自熱使 gm 退化、gd 下降、本質增益上升、線性度參數劣化，且 overlap 組態受自熱影響最大）。gm/gd 三組百分比雖經兩次查證吻合，但完全缺少偏壓與溫度條件、且本次無法直接載入出版者頁面，作為定量錨點的可信度不足；對使用者的飽和 Ion 主題亦無直接數字可用。

**7 取得狀態**　僅metadata
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.mejo.2023.105765?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1016/j.mejo.2023.105765
   - https://api.crossref.org/works/10.1016/j.mejo.2023.105765

**8 與原表差異**　與原表一致（摘要無 Ion %、gm,max 退化 8%/28.3%/6.9%、gd 退化 30.3%/40.9%/33.3%、對應 conventional/overlap/underlap 之順序 —— 全部吻合）。新增原表未載之資訊：本質增益峰值上升 52.4%/28.1%/57.7%；線性度參數 VIP2、VIP3、IIP3、1 dB 壓縮點因 gm2、gm3 上升而劣化；卷期 Microelectronics Journal 135:105765；作者單位 MNIT Jaipur、Saha 為通訊作者（ORCID 0000-0003-3108-6081）；線上出版日 2023-03-24（Crossref 期別 2023 年 5 月）。取得限制須標明：ScienceDirect（S0026269223000782）直取回 403、scribd 鏡像僅預覽頁，數值係經搜尋引擎回傳之出版者摘要文字取得，非第一手直讀頁面，故未列入 sources。無衝突。

---

## 二15 — An Investigation into the Comprehensive Impact of Self-Heating and Hot Carrier Injection

- **DOI／識別**：`10.3390/electronics11172753`　**來源**：非　**年**：2022
- **作者／單位**：Yan Liu（第一作者）, School of Microelectronics, Dalian University of Technology, Dalian 116000, China；通訊作者 Yanhua Ma、Yuchun Chang（同單位）；共同作者 Zhaojie Yu（China Electronic Product Reliability and Environmental Testing Research Institute, Guangzhou）、Shanshan Lou、Yang Qu
- **出處**：Electronics (MDPI), Vol. 11, Issue 17, Article 2753（Communication 類型）

**1 元件**　22 nm 節點三維 n 通道 bulk FinFET（NFinFET，取自 Sentaurus TCAD application library）。Lg = 22 nm、Fin Height HFin = 40 nm、Fin Width WFin = 17 nm、Tox = 1 nm、high-k(HfO2) THf = 2 nm。原文 Table 2 另列 NS/D = 5×10^15 cm^-3、Nsub = 1×10^15 cm^-3。鰭數／指數：原文未載明（未取得）。另有 65 nm 與 22 nm planar NMOS 作為 2D 電熱模擬參考元件（Lg 65/22 nm、Tox 0.6 nm、THf 20 nm、Xj 40 nm、halo 4×10^18 cm^-3、NS/D 1.5×10^20 cm^-3）。

**2 方法與 SHE 定義**　`ET-vs-ISO`　求解器：Sentaurus TCAD（原文明言元件取自 Sentaurus application library）。遷移率模型：Lombardi piezoresistance + high-field saturation。傳輸模型：hydrodynamic（算 carrier temperature）＋ thermodynamic（算 lattice temperature）耦合，並額外把 temperature model 耦合進 solver 以模擬 SHE。熱邊界條件：原文寫「the ambient temperature was set to 300 K for the thermal boundary condition」。thermode 位置：由原文「the increasing SR offers a low-speed thermal conduction path for heat flow from the source and drain contacts」可判定熱抽出路徑在 source/drain 接觸。SurfaceResistance：原文以符號 SR 表示 thermal surface resistance，Table 1/2 列出掃描區間 SR = 1×10^-5 ~ 1×10^-4 cm^2·K·W^-1，示例圖用 SR = 5×10^-5 cm^2·K·W^-1。熱導率設定（Table 3，單位 W·K^-1·cm^-1）：SiO2 0.014、Si (bulk) 1.48、Si (Fin) 0.13、Poly Si 1.5、HfO2 0.023、Si3N4 0.185、TiN 0.192。無 BTE／聲子輸運求解，僅以「Si (Fin) 熱導率降到 0.13」唯象代表 phonon-boundary scattering。HCI 部分另用 trap degradation model + lucky electron injection model，初始界面陷阱濃度假設 1×10^8 cm^-3。

**3 關鍵定量結果**　Ion 下降 %：全文（含摘要、結論、所有內文）完全沒有出現百分號，我已對全文文字做過 % 字元掃描，結果為零筆——即本文未印出任何 SHE 造成的電流下降百分比，屬「僅圖層級（需自讀 Figure 6 / Figure 7 原圖）」。定性結論為原文印出：「the drain current in the linear region is almost unchanged, while the drain saturation current is reduced under the self-heating effect」（Figure 6，比較 w/o SHE 與 w/ SHE 的 Id-Vd；該圖對應的 SR 值原文未標明）。峰值晶格溫度（原文印出數字）：「the increasing SR raises the maximum lattice temperature from 314.37 K to 360.76 K」，對應 SR 由 1×10^-5 增至 1×10^-4 cm^2·K·W^-1；以 TA = 300 K 為基準，ΔT 由 14.37 K 增至 60.76 K。遷移率（原文印出數字）：同一 SR 掃描下「a reduction in electron mobility from 790.254 cm^2 V^-1 s^-1 to 705.194 cm^2 V^-1 s^-1」（下降 10.8%）。偏壓：Table 1/2 給 Vds = 0–1 V、Vgs = 0–1 V；TA = 300 K。Table 4 印出 SR 由 1×10^-5 到 1×10^-4（9 檔）× 時間 10 s~10^6 s 的 Total Heat 與 Electric Power 完整數值表（例：SR=1×10^-5, t=10 s 時 Total Heat 5.46388×10^-5 W、Electric Power 5.71516813464×10^-5 W）。Rth：未印出（未取得）。

**4 TCAD 校準用途**　本批最可直接餵進使用者 deck 的一張卡。(1) thermode SurfaceResistance 量級：可直接採用 1×10^-5 ~ 1×10^-4 cm^2·K/W 這個掃描區間當作 bulk FinFET 的合理上下界，thermode 掛在 source/drain 接觸。(2) 材料熱導率可整組抄用（Si bulk 1.48 vs Si fin 0.13 W·K^-1·cm^-1，即鰭內 Si 熱導率降 11.4×，這是唯象代 phonon boundary scattering 的關鍵設定，使用者若用 Sentaurus 預設 Si 熱導率會嚴重低估 SHE）。(3) ΔT sanity check：同一元件同一偏壓下，SR=1e-5 給 ΔT=14.37 K、SR=1e-4 給 ΔT=60.76 K；用判準帶的 0.10–0.20 %/K 交叉檢核可反推 Ion 下降約 1.4–2.9%（過導熱、SHE 被邊界抹掉）到 6.1–12.2%（落在 bulk 判準帶 3–12% 上緣）。使用者可用這條線把自己的 thermode 夾在中間，例如目標 7–11% 對應 ΔT 約 40–70 K。(4) 幾何可對齊：Lg 22 nm / HFin 40 nm / WFin 17 nm 與典型矽 FinFET deck 同量級。(5) 求解器組態可對齊：hydrodynamic + thermodynamic 雙耦合是本文明確使用的組合。

**5 批判**
   1. 判準帶判定：無 Ion 下降 % 數值可直接判定（全文零筆百分號，屬圖層級）。改以 ΔT 交叉檢核則落在帶內偏上：SR=1e-4 時 ΔT=60.76 K，乘 0.10–0.20 %/K 得 6.1–12.2%，正好覆蓋 bulk 判準帶 3–12%；但 SR=1e-5 時 ΔT 僅 14.37 K，反推 1.4–2.9%，接近「SHE 被邊界條件抹掉」的下緣警戒。也就是說本文的 SR 掃描區間剛好橫跨「thermode 貼太近」到「合理」兩個極端，使用者不能只挑一個端點當標準值。
   2. 熱邊界描述不完整：原文只寫 ambient 300 K 為熱邊界，並未交代 thermode 究竟掛在哪幾個接觸（gate 有沒有掛？基板底部是不是 isothermal？）、也沒給 die/package 級的熱阻。整篇對 SHE 強度的控制只靠 SR 一個旋鈕，這使 ΔT 完全由使用者自選的 SR 決定，外推到別人的 deck 時必須連 SR 定義一起搬。
   3. 單一幾何無法外推：只有一顆 22 nm NFinFET、單一 HFin/WFin，沒有鰭數／指數掃描，也沒有 p 通道對照。使用者若要做 n/p 對比或多鰭效應，本文提供不了。
   4. 含明顯糾纏因子：本文的主軸其實是 SHE × HCI 交互作用（trap degradation + lucky electron injection，初始陷阱 1×10^8 cm^-3），Figure 6 之後的所有輸出特性變化都混入了界面陷阱。純 SHE 的乾淨對照只有 Figure 6 一張。
   5. 資料可信度疑點：Table 2 把 NFinFET 的 source/drain 濃度列為 NS/D = 5×10^15 cm^-3，比 substrate 1×10^15 只高 5 倍，這對 S/D 區而言物理上不合理（Table 1 的 planar NMOS 是 1.5×10^20），高度疑似排版或抄寫錯誤。使用者若照抄這張表會做出完全不同的元件。
   6. 無誤差棒、無重複性檢驗、無實驗校準：純模擬 Communication，未與任何量測資料比對，Table 4 卻給到小數點後 11 位（5.71516813464×10^-5 W），有效位數遠超模擬可信度。

**6 可引用性**　A（可直接引用數字）— 已取得 CC-BY 全文，SR 掃描區間、材料熱導率表、314.37 K→360.76 K、遷移率 790.254→705.194 cm^2/V·s 皆為原文逐字印出的數字，可直接引用；唯獨「Ion 下降百分比」全文未印，該項只能引用定性結論或自行讀圖。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/electronics11172753?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.3390/electronics11172753
   - https://mdpi-res.com/d_attachment/electronics/electronics-11-02753/article_deploy/electronics-11-02753.pdf

**8 與原表差異**　與原表一致。原表記載的「22 nm n-channel bulk FinFET、L=22 nm、fin height 40 nm、figure-level only 無 % 印出、TA=300 K、Vds 0-1 V / Vgs 0-1 V (Table 2)、最大晶格溫度 314.37 K → 360.76 K」全部逐字核對無誤，且逐字引用「the drain current in the linear region is almost unchanged, while the drain saturation...」也與全文相符。本次補充原表未載的項目：WFin = 17 nm、Tox = 1 nm、THf = 2 nm、SR 掃描區間 1×10^-5 ~ 1×10^-4 cm^2·K·W^-1（示例值 5×10^-5）、Table 3 完整熱導率清單（Si fin 0.13 vs Si bulk 1.48 W·K^-1·cm^-1）、遷移率 790.254 → 705.194 cm^2/V·s、thermode 熱流路徑在 source/drain 接觸。無衝突、無錯誤。

---

## 二16 — Dynamic Self-Heating Effects of Bulk and SOI FinFET with Realistic Device Structure（韓文標題：실제적 구조를 가진 벌크 및 SOI FinFET에서 발생하는 동적 self-heating 효과）

- **DOI／識別**：`10.5573/ieie.2015.52.10.064`　**來源**：非　**年**：2015
- **作者／單位**：Heesang Ryu（유희상，第一作者，學生會員），Department of Electronics and Information Engineering, Korea University（高麗大學校 電子及情報工學科），韓國；共同作者 Hayun Cecillia Chung（정하연，助理教授）、Ji-Woon Yang（양지운，通訊作者、副教授，jyang@korea.ac.kr），同系所
- **出處**：Journal of the Institute of Electronics and Information Engineers（IEIE，전자공학회 논문지），Vol. 52, No. 10, pp. 64–69（論文編號 2015-52-10-8）

**1 元件**　Bulk FinFET 與 SOI FinFET 對照（3D TCAD，同時比較 simplified structure 與 realistic structure 兩種建模）。共同幾何：Lg = 25 nm、Hfin = 40 nm、Wfin = 13 nm（另有 Wfin 9–15 nm 掃描）、gate oxide 1.1 nm、S/D extension length 10 nm、S/D doping 1×10^20 cm^-3。Bulk：channel doping 1×10^18 cm^-3、STI 厚 60 nm、gate workfunction 4.67 eV、無 BOX。SOI：channel doping 1×10^15 cm^-3、BOX 20 nm、gate workfunction 4.70 eV、無 STI。Realistic structure 額外含 selective epitaxy 形成的 raised source/drain（RS/D），橫、縱各 45 nm、高 40 nm。n 通道（由 gate workfunction 與 S/D n+ 判定）；單鰭，Id 以 (Hfin + Wfin) normalize。節點對應為 22 nm 級以下代工元件（研究計畫名稱明載「22nm급 이하 파운드리 소자 및 PDK 기술개발」）。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　求解器：3D TCAD，參考文獻 [8] 明列 Sentaurus Device User Guide, Ver. C-2009.06（Synopsys）。熱邊界條件（本文最有價值的部分，原文明確印出）：每顆 FinFET 上方的 PreMetalDielectric (PMD) 厚度假設 200 nm，PMD 之上放 isothermal 300 K heat sink；元件下方鋪 1.8 μm 厚 Si 基板層，基板底部再放 isothermal 300 K heat sink（此設定引自參考文獻 [6] Braccioli et al.）。也就是說本文用的是「幾何延伸 + 遠端等溫壁」而非 thermode SurfaceResistance 集總熱阻——原文未給任何 SurfaceResistance 數值（未取得）。SHE 開關：以 w/o SHE 與 w/ SHE 兩組解對照（等效 ET-vs-ISO）。公平比較程序：調整 gate workfunction 與 channel doping，使 bulk 與 SOI 兩結構的 DIBL、Vt、off current 對齊後才比 SHE。穩態條件：Vd = Vg = DC 1.0 V。動態條件：Vd 固定 DC 1.0 V，Vg 施加脈衝，peak 1.0 V、pulse width 100 ns、rise time 與 fall time 各 1 ns；另做 pulse width 1–6 ns 掃描。無 hydrodynamic／BTE／聲子模型的敘述（未取得）。

**3 關鍵定量結果**　穩態 ET-vs-ISO（原文印出數字，韓文正文）：Vg = Vd = 1.0 V、TA = 300 K 下，無 SHE 時 Id = SOI 1.28 mA/μm、Bulk 1.21 mA/μm（SOI 比 bulk 高 0.07 mA/μm）；考慮 SHE 後 SOI 降為 1.04 mA/μm、bulk 降為 1.05 mA/μm。對應 Figure 3 圖內標註（原文印出數字，但以圖註形式）：(a) realistic SOI FinFET 標 19%、(b) realistic bulk FinFET 標 14%。以正文 mA/μm 反算則為 SOI 18.75%、bulk 13.2%——bulk 的圖註 14% 與反算值 13.2% 有捨入落差，須註明。英文摘要逐字：「The degradation of drive current in SOI FinFET is severer than that of bulk one in steady-state condition」與「the dynamic self-heating effects of SOI FinFETs are comparable to those of bulk FinFETs for high speed logic operation」。Wfin 依存性（僅圖層級，Figure 4）：Wfin 由 9 nm 掃到 15 nm，Id degradation 縱軸範圍 8–24%，realistic 結構的退化一律小於 simplified 結構，且 degradation 隨 Wfin 增大而上升（原文解釋為 Lg 固定 25 nm 時 Wfin 變大導致短通道效應與 Id 上升，進而抬高晶格溫度）。動態（僅圖層級，Figure 5–8）：Figure 5 溫度縱軸範圍 SOI 到 525 K、bulk 到 500 K（軸範圍非曲線峰值，實際峰值需自讀原圖）；Figure 6 為 Id degradation 對 pulse width 1–6 ns，縱軸 0–20%，pulse 越窄 degradation 越小、SOI 下降尤其陡；Figure 8 為 SOI 與 bulk 的 degradation 差距，pulse 越窄差距越小。Rth：未印出數值（原文僅定性說 realistic 結構因磊晶 S/D 體積變大使 RTH 下降、bulk 的 CTH 大於 SOI）。峰值晶格溫度數值：未印出（僅圖層級）。

**4 TCAD 校準用途**　熱邊界條件可整組直接抄進 deck：PMD 200 nm 之上 isothermal 300 K heat sink＋元件下方 1.8 μm Si 基板底部 isothermal 300 K heat sink。這是「不用 thermode 集總熱阻、改用幾何延伸＋遠端等溫壁」的標準做法，可與二15 的 SurfaceResistance 做法互為對照，兩者交叉檢核出的 ΔT / Ion 下降應落在同一帶內。幾何可直接對齊：Lg 25 nm、Hfin 40 nm、Wfin 13 nm、Tox 1.1 nm、S/D ext 10 nm、S/D 1×10^20、bulk channel 1×10^18 / SOI 1×10^15、bulk STI 60 nm、SOI BOX 20 nm、WF 4.67/4.70 eV。ET-vs-ISO 校準錨點（可直接對數字）：Vg = Vd = 1.0 V、TA = 300 K → bulk FinFET 1.21 → 1.05 mA/μm（13.2%，圖註 14%）、SOI FinFET 1.28 → 1.04 mA/μm（18.75%，圖註 19%）。注意 Id 是以 (Hfin + Wfin) 而非 (2Hfin + Wfin) normalize，使用者若用不同 normalize 定義，絕對電流會差近兩倍，但百分比不受影響。另可抄「RS/D 45 × 45 × 40 nm 磊晶體積」這個關鍵幾何——本文明確指出磊晶 S/D 把 RTH 拉低、使 realistic 結構的退化系統性小於 simplified 結構，這是使用者若只建簡化結構會系統性高估 SHE 的直接證據。動態部分可抄脈衝設定：Vg peak 1.0 V、pw 100 ns、tr/tf 1 ns，以及 pw 1–6 ns 掃描。

**5 批判**
   1. 判準帶判定：兩個數字都落在判準帶之上（帶外偏高）。bulk 13.2–14% 高於 bulk 判準帶 3–12% 上緣；SOI 18.75–19% 高於 SOI 判準帶 8–17% 上緣。原因明確且可解釋：偏壓是 Vg = Vd = 1.0 V，而非判準帶所設定的 VDD ≈ 0.7 V。功率密度大致隨 VDD 的超線性關係上升，1.0 V 對 0.7 V 已足以把退化推高 3–7 個百分點。所以這不是 thermode 過絕熱，而是偏壓不同——使用者若要對錨點，必須先把 VDD 拉到 1.0 V 再比，或把本文數字往下修正後才與 14nm 7.26%/8.91% 那組錨點並列。
   2. 數字內部有捨入不一致：Figure 3(b) 圖註標 14%，但正文印出的 1.21 → 1.05 mA/μm 反算是 13.2%；SOI 的 19% 對 18.75% 則一致。差 0.8 個百分點雖小，但表示正文的 mA/μm 是四捨五入到小數第二位後的值，使用者引用時應同時標出兩個來源，不要只引 14%。
   3. 熱邊界偏導熱而非偏絕熱，且缺 thermode 熱阻：本文以 200 nm PMD 與 1.8 μm Si 基板後直接接 isothermal 300 K，完全沒有 contact／interface 熱阻（SurfaceResistance = 0 的等效）。真實元件在 M1/via 與 silicide 界面都有可觀的界面熱阻，因此本文的 ΔT 與退化幅度應屬「下界估計」。這與二15（用 SurfaceResistance 集總熱阻）是兩種相反的偏誤方向，使用者最好兩種都跑一次夾出上下界。
   4. 單一 Lg、單鰭、僅 n 通道：Lg 固定 25 nm，只掃 Wfin 9–15 nm，沒有多鰭／多指結構，也沒有 p 通道對照，因此無法外推到 RF 多鰭多指結構的 34 kK/W 那個量級，也無法談 n/p 不對稱。
   5. 分類須留意：本文標題與主要貢獻是動態（pulsed）SHE，但第 III-1 節的 19%/14% 是穩態 ET-vs-ISO 的結果。兩者不可混用——使用者要拿去校準 DC deck 的只能用 III-1 的穩態數字，Figure 6 的 pulse width 依存曲線是另一個物理量（熱時間常數 vs 脈衝寬度），不能直接當 DC SHE 的錨點。本文沒有 ta_sweep，不涉及該陷阱。
   6. 無誤差棒、無重複性、無實驗驗證：純 TCAD，未與任何量測比對；Sentaurus 版本 C-2009.06（2009 年版）的熱導率與遷移率模型參數在今天已相當老舊，鰭內 Si 薄膜熱導率是否有降階處理原文完全沒交代，這會直接放大或縮小 ΔT。
   7. 可貴的方法論貢獻：simplified vs realistic 結構的系統性比較（Figure 4、Figure 7）量化了「只建簡化結構會高估 SHE」這件事，且指出 SOI 在高速動態下的退化縮減比 bulk 更明顯，因此常被引用的「SOI SHE 遠比 bulk 嚴重」在 ns 級邏輯操作下並不成立。這是本文最值得引的定性結論。

**6 可引用性**　A（可直接引用數字）— 已取得 KoreaScience 免費全文 PDF，穩態 Id 數值（1.28/1.21 → 1.04/1.05 mA/μm）、圖註 19%/14%、完整結構參數表與熱邊界設定（PMD 200 nm + 1.8 μm 基板 + isothermal 300 K）皆為原文印出，可直接引用；唯 Wfin 依存與動態部分僅圖層級，引用時須標明為讀圖值。正文為韓文、摘要為英文，引用逐字英文句只能取自摘要。

**7 取得狀態**　全文
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.5573/ieie.2015.52.10.064?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://koreascience.or.kr/article/JAKO201531362063346.page
   - https://koreascience.kr/article/JAKO201531362063346.pdf

**8 與原表差異**　CORRECTION（原表資訊不完整，非錯誤）。原表記「figure-level；已證實摘要僅定性…無任何 %；bias:摘要未載；dT:摘要無數值」，該判定在只讀到摘要的前提下正確。本次自 KoreaScience 取得免費全文 PDF（6 頁，pp. 64–69），因此可補正：(1) 偏壓實為 Vd = Vg = DC 1.0 V、TA = 300 K，原文明載；(2) 原文正文印出 Id 數值 SOI 1.28 → 1.04 mA/μm、bulk 1.21 → 1.05 mA/μm，Figure 3 圖內標註 SOI 19%、bulk 14%，並非「無任何 %」；(3) 完整結構參數表與熱邊界（PMD 200 nm + isothermal 300 K、基板 1.8 μm + isothermal 300 K、RS/D 45×45×40 nm）皆可取得；(4) dT 仍為圖層級（Figure 5 溫度軸到 525 K / 500 K），此點與原表一致。另一項 CORRECTION 針對 Semantic Scholar 而非原表：S2 將第一作者列為「Hee-Uk Ryu」，原文 PDF 自署英文名為「Heesang Ryu」（유희상），應以原文為準；S2 亦未收錄本文摘要（回傳 abstract: null），venue 欄為空，正確刊名為 Journal of the Institute of Electronics and Information Engineers, Vol. 52, No. 10。證據 URL：https://koreascience.kr/article/JAKO201531362063346.pdf

---
