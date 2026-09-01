# 第七章 · ta_sweep（非 SHE）

_改的是環境溫度，不可當 SHE 劣化基準引用_

原表 4 篇｜本檔 4 篇｜取得層級：摘要 3、全文 1

## 七01 — Design Optimization of Three-Stacked Nanosheet FET From Self-Heating Effects Perspective

- **DOI／識別**：`10.1109/TDMR.2022.3181672`　**來源**：IEEE　**年**：2022
- **作者／單位**：第一作者 Sunil Rathore（VLSI Design and Nano-Scale Computational Lab, PDPM Indian Institute of Information Technology Design and Manufacturing (IIITDM) Jabalpur, Jabalpur, India）。共同作者：Rajeewa Kumar Jaisawal、P.N. Kondekar、Navjeet Bagga（皆為同一實驗室與單位）。單位來源：Crossref 與 OpenAlex 的 affiliation 欄位。
- **出處**：IEEE Transactions on Device and Materials Reliability，Volume 22, Issue 3, pp. 396-402

**1 元件**　Three-stacked Si **nanosheet FET (NSFET)**，GAA 三層堆疊。兩種底部絕緣方案對照：partially depleted silicon-on-diamond (PDSOD) NSFET vs partially depleted silicon-on-insulator (PDSOI) NSFET，兩者 footprint area 相同。nanosheet thickness (TNS) 為掃描變數但【具體數值未取得】。【未取得】技術節點、Lg、WNS、堆疊間距 / inner spacer 尺寸、n 或 p 型別、鰭數或指數。非 FinFET、非 CFET。

**2 方法與 SHE 定義**　`ET-vs-ISO`　摘要層級："Using extensive TCAD simulations"——【求解器名稱未指明】。掃描變數為 ambient temperature 與 nanosheet thickness。關鍵材料參數為原文印出：crystalline diamond 熱導率 kth = 2000 W·m^-1·K^-1，SiO2 熱導率 kth = 1.4 W·m^-1·K^-1。【全數未取得】熱邊界條件、thermode 位置與 SurfaceResistance 設定、有無 hydrodynamic / BTE / 聲子模型、是否納入介面熱阻 (thermal boundary resistance)、網格設定。本篇位於 IEEE 付費牆後（S2 與 OpenAlex 皆標示無 OA 版本，openAccessPdf url 為空），ieeexplore.ieee.org/document/9792450 抓取回空內容。method_type 標為 ET-vs-ISO 為強制歸類，實際主軸是 PDSOD vs PDSOI 兩種 BOX 材料的電熱對照，摘要並未證實存在等溫對照組。

**3 關鍵定量結果**　【摘要層級僅有定性描述，無任何數字化的 Ion 下降 %、Rth、ΔT 或峰值晶格溫度】。原文印出的量化資訊只有兩個材料熱導率：diamond kth = 2000 W·m^-1·K^-1、SiO2 kth = 1.4 W·m^-1·K^-1。定性原文（逐字）："It raises the device's lattice temperature several degrees higher than the ambient temperature and degrades the driving current."；"we have investigated the potential of crystalline diamond to mitigate the SHE-induced degradation in a partially depleted silicon-on-diamond Nanosheet FET (PDSOD NSFET)"；"our analysis reveals that PDSOD NSFET is a viable alternative to alleviate the SHE-induced thermal degradation for the same footprint area of SiO2 used in PDSOI NSFET"。無任何偏壓條件（VGS / VDS / TA）在摘要中標明。【未採計線索，特此揭露】網路搜尋摘要中曾出現「surface scattering 造成 PDSOD 相對 PDSOI 約 1.26% 的汲極電流退化」之說法，但本次未能造訪任何實際印出該數字的一手頁面，依反幻覺紀律不列為本文結果，僅供使用者取得全文後查證。

**4 TCAD 校準用途**　不可直接校準，理由：摘要層級沒有任何 Ion 下降 %、Rth、ΔT 或溫度數字可餵給 deck，且架構為 three-stacked GAA nanosheet 而非使用者研究的矽 FinFET，幾何完全無法對齊。可用的僅兩項：(1) 材料熱導率對照（diamond 2000 vs SiO2 1.4 W·m^-1·K^-1）可作為 deck 中 BOX 材料替換實驗的參數來源；(2) 定性量級錨點——本文自述 SHE 使晶格溫度「several degrees higher than the ambient」，這個「數 K」的量級與本批 五43 的約 426 K、五41 的約 156 K 形成強烈對比，可反過來當作判斷「哪些文獻的熱邊界過絕熱、哪些可能貼太近通道」的參照尺。對使用者而言，本篇的主要價值在於建立領域全貌（GAA/nanosheet 分支的 SHE 緩解路線），而非 deck 數值校準。

**5 批判**
   1. 無數值可判定，原因：IEEE 付費牆，Semantic Scholar / OpenAlex / Crossref 皆只有摘要、無 OA 版本，IEEE Xplore 頁面抓取回空內容。摘要唯一的量化描述是 "several degrees higher than the ambient temperature"；若此「數 K」為真，以 0.10-0.20 %/K 換算僅對應 <1% 的 Ion 降，會壓在判準帶「飽和 Ion 差 < 1% → SHE 被邊界條件抹掉、thermode 可能貼太近通道」的紅線上。但 "several degrees" 是摘要的修辭性措詞而非量測值，不足以據此定罪，必須取得全文的實際 ΔT 才能判定帶內或帶外。
   2. 架構不匹配：本篇是 three-stacked GAA nanosheet FET，不是使用者研究的矽 FinFET。nanosheet 的熱侷限機制（堆疊層之間經 inner spacer 的串聯熱路、上層 sheet 距基板最遠）與 FinFET 的鰭底垂直散熱路徑本質不同，Rth 與 ΔT 皆不可互相搬用；引用時必須明確標示架構差異。
   3. 糾纏因子明顯：PDSOD vs PDSOI 的比較同時改變了 BOX 的熱導率（相差約 1400 倍）與其介電常數、介面性質與載子散射環境。摘要涉及 diamond 的 surface scattering 議題，代表電性退化與熱性改善混在同一組對照中；作者是否有做「固定電性條件下的純熱比較」，摘要未說明，這會影響其結論的可歸因性。
   4. 【分類陷阱】摘要明示 "the impact of varying the ambient temperature and nanosheet thickness"——ambient temperature 掃描屬 ta_sweep，量的是環境溫度效應，不是 SHE 本身。本篇同時包含 ta_sweep 與結構/材料對照兩種實驗，使用者若取用其數字，必須逐圖確認屬於哪一種，否則會犯下判準明列的 ta_sweep 誤判為 SHE 的陷阱。本卡 method_type 標為 ET-vs-ISO 係就其主軸而定，屬強制歸類，摘要並未確認存在等溫對照組。
   5. 「diamond BOX」在 2022 年屬研究性材料而非量產方案，且 2000 W·m^-1·K^-1 是單晶金剛石的體材料值；實際薄膜品質、晶界與 Si/diamond 介面熱阻 (TBR) 都會大幅打折。摘要未說明是否納入介面熱阻，若未納入將系統性高估 PDSOD 的散熱優勢。
   6. 無誤差棒、無網格收斂測試、無實驗對照資訊（摘要層級無從判斷）。IEEE TDMR 為可靠的同儕審查期刊，但本次取得層級不足以評估其內部嚴謹度，不可以期刊聲譽代替對數字的查證。
   7. 本卡刻意排除了搜尋引擎轉述的「約 1.26% 汲極電流退化」數字。此數字若為真，將落在判準帶「飽和 Ion 差 < 1%」紅線附近，是判斷其 thermode 是否貼太近通道的關鍵證據——但在取得一手全文之前，任何引用該數字的行為都是幻覺風險。

**6 可引用性**　C（僅可當背景引用）— 僅取得出版者摘要，零可用數值（只有兩個材料熱導率常數），且架構為 three-stacked nanosheet FET 而非矽 FinFET。只能當「高熱導率 BOX 材料（diamond）可緩解 SHE」與「GAA/nanosheet 分支 SHE 議題」的背景引用；任何數字性引用都必須先取得 IEEE 全文。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/tdmr.2022.3181672?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/TDMR.2022.3181672
   - https://api.crossref.org/works/10.1109/TDMR.2022.3181672

**8 與原表差異**　與原表一致。原表「Three-stacked Si nanosheet FET; partially-depleted silicon…」與「Abstract states SHE 'raises lattice temperature several degrees above ambient and degrades the driving current…'」「not accessed（結果）」本次在 Semantic Scholar 與 OpenAlex 的出版者摘要中逐字確認（原文為 "It raises the device's lattice temperature several degrees higher than the ambient temperature and degrades the driving current."），無衝突。補充原表未記載者：完整標題、四位作者與單位（VLSI Design and Nano-Scale Computational Lab, PDPM IIITDM Jabalpur, India）、卷期頁碼（IEEE TDMR 22(3), 396-402, 2022）、對照組為 PDSOD vs PDSOI 且 footprint 相同、diamond kth = 2000 與 SiO2 kth = 1.4 W·m^-1·K^-1（原文印出）、掃描變數含 ambient temperature 與 nanosheet thickness（後者為 ta_sweep 混入之警示）。另記一項【未採計線索】：搜尋結果中出現「約 1.26% 汲極電流退化（PDSOD vs PDSOI，surface scattering 所致）」的敘述，因無法造訪任何印出該數字的一手頁面，本卡不列入 results，僅在此備註供使用者取得 IEEE 全文後查證。原表 verdict=confirmed 成立。

---

## 七02 — Ambient Temperature-Induced Device Self-Heating Effects on Multi-Fin Si CMOS Logic Circuit Performance in N-14 to N-7 Scaled Technologies

- **DOI／識別**：`10.1109/TED.2020.2975416`　**來源**：IEEE　**年**：2020
- **作者／單位**：Sankatali Venkateswarlu（第一作者），Department of Electrical Engineering, IIT Hyderabad, Hyderabad, India；共同作者 Kaushik Nayak（同單位）
- **出處**：IEEE Transactions on Electron Devices, vol. 67, no. 4, pp. 1530–1536（2020 年 4 月）

**1 元件**　Si 3-Fin FinFET 構成的 CMOS inverter 與 ring oscillator（RO），技術節點自 N-14 縮放至 N-7。摘要明言為「Si 3-Fin FinFET-based CMOS inverter」，故為 3 鰭、n/p 皆有（CMOS 反相器需 nFinFET + pFinFET）。bulk / SOI 未在摘要說明（同組 2018 年元件論文為 bulk，但本文未印出，不代入）。Lg、Hfin、Wfin、fin pitch 均未取得（全文封閉取用）。

**2 方法與 SHE 定義**　`ta_sweep`　「coupled hydrodynamic-thermodynamic (HD-TH) mixed-mode simulations」——HD（能量傳輸）與 TD（晶格熱傳）耦合的 mixed-mode 電路級模擬。自變數為兩個：(1) within-chip ambient temperature (TA)；(2) thermal contact resistance (TCR)，摘要明確拆成 gate / source / drain 三處的 Rth,GSD。另掃描負載電容 CL 對元件晶格溫度 TL 與傳播延遲 tpd 的影響。求解器名稱（Sentaurus / GARAND / 其他）未在摘要指明，不代入推測。熱邊界的 thermode 幾何位置與 SurfaceResistance 數值未取得。無 BTE / 聲子色散模型的相關敘述可取得。注意：本文主軸為改變環境溫度與熱接觸電阻，非 electrothermal-vs-isothermal 的 SHE 增量對照，故歸類 ta_sweep。

**3 關鍵定量結果**　僅摘要層級，全文（含圖與數值）未取得，原文印出的數字一個都拿不到。可引用的逐字英文結論句：「Our simulation results revealed that within-chip TA and Rth of gate, source, and drain (Rth,GSD) have significant effect on the logic circuit performance in terms of degradation of noise margin (NM), inverter gain (|gmax|), and increase in tpd due to SHE from N-14 to N-7 technologies.」以及方法句「The effect of the load capacitance (CL) on device lattice temperature (TL) and its impact on propagation delay (tpd) of the targeted CMOS inverter circuit are analyzed.」與「We investigated the SHE in the 3-Fin FinFET-based ring oscillator (RO) and estimated the stage delay and frequency of oscillations.」Ion 下降 %：未取得。Rth 數值：未取得。ΔT / 峰值晶格溫度：未取得。對應偏壓（VGS/VDS/TA 的具體值）：未取得。所有量化結果均屬「僅圖層級 / 正文層級，需取得全文才能讀」。

**4 TCAD 校準用途**　不可直接校準，理由：全文封閉取用，無任何 Ion%、Rth、ΔT、峰值 TL 數值可取，也沒有 thermode SurfaceResistance 的具體設定值。唯一可用於 deck 的是方法學層級的提示（來自摘要）：熱接觸電阻應分別設在 gate、source、drain 三處（Rth,GSD），而非只在 substrate 設單一 thermode；且電路級 SHE 的靈敏度旋鈕是 TA 與 Rth,GSD 兩者。若使用者的研究是元件級飽和 Ion，本文屬電路級延伸文獻，只能放在 discussion，不能餵數字進 deck。

**5 批判**
   1. 無數值可判定，原因：IEEE Xplore 封閉取用（兩次 WebFetch 皆回傳空內容），Semantic Scholar / OpenAlex / Crossref 僅提供摘要與書目，摘要中沒有印出任何百分比或溫度數字，因此無法與「標準矽 FinFET 飽和 Ion 下降 7-11%、bulk 判準帶 3-12%」或「ΔIon%/ΔT ≈ 0.10-0.20 %/K」做任何比對。
   2. 分類陷阱（本批最需注意的一點）：標題與摘要的自變數是 ambient temperature 與 thermal contact resistance，屬 ta_sweep + Rth 敏感度分析，摘要中並無 electrothermal vs isothermal 的對照組。若把本文引為「SHE 使 Ion 下降 X%」的來源，會犯與 七04 相同的歸因錯誤。
   3. 量測層級不匹配使用者需求：本文報的是電路級指標（inverter 的 noise margin、gain |gmax|、propagation delay tpd，以及 RO 的 stage delay 與振盪頻率），不是單一元件的飽和汲極電流。元件層級的 Ion 退化必須回到同一團隊 2018 年的 七03（同樣封閉取用）。
   4. 熱邊界即研究對象，不是固定設定：Rth,GSD 被當成掃描參數，因此本文任何溫升結果都是「邊界條件的函數」而非 device-intrinsic 值，不能當作 thermode 是否過絕熱 / 過導熱的絕對錨點。
   5. 純 mixed-mode 模擬，無實驗量測、無誤差棒、無重複性資訊；摘要亦未給出 CL 的數值範圍與熱邊界的具體設定，重現性不足。
   6. 外推限制：跨 N-14 到 N-7 的節點縮放，但 fin pitch、Hfin、Wfin 是否等比縮放完全不明，單一 3-fin inverter 幾何無法外推到多鰭多指的 RF 結構（判準帶中的 34 kK/W 量級）。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可逐字引用其定性結論（TA 與 Rth,GSD 會顯著劣化 NM、gain 與 tpd），但沒有任何可直接引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2020.2975416?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/TED.2020.2975416
   - https://api.crossref.org/works/10.1109/TED.2020.2975416

**8 與原表差異**　與原表一致。原表記「Multi-fin Si FinFET CMOS inverter / ring oscillator, N-14…；No device-level Ion % in abstract (confirmed)；circuit-level degradation (delay, noise margin, gain) quantifie…；not accessed (closed access)」，本次三個獨立來源（Semantic Scholar / OpenAlex / Crossref）逐項核對相符：摘要確實無元件級 Ion%，確實為封閉取用。本次補全資訊（非衝突、非更正）：完整標題結尾為「…Multi-Fin Si CMOS Logic Circuit Performance in N-14 to N-7 Scaled Technologies」（原表 title 在此處被刪節號截斷）；卷期頁碼 vol. 67, no. 4, pp. 1530–1536；節點範圍為 N-14 到 N-7（原表只寫 N-14）；作者為 2 人（Venkateswarlu、Nayak），單位 IIT Hyderabad；基金為 Visvesvaraya PhD Scheme, MeitY, India。

---

## 七03 — Ambient Temperature-Induced Device Self-Heating Effects on Multi-Fin Si n-FinFET Performance

- **DOI／識別**：`10.1109/TED.2018.2834979`　**來源**：IEEE　**年**：2018
- **作者／單位**：Sankatali Venkateswarlu（第一作者），Department of Electrical Engineering, IIT Hyderabad, Hyderabad, India；共同作者 Akhil Sudarsanan、Shiv Govind Singh、Kaushik Nayak（均為同單位）
- **出處**：IEEE Transactions on Electron Devices, vol. 65, no. 7, pp. 2721–2728（2018 年 7 月）

**1 元件**　Si 3-Fin bulk n-FinFET（摘要逐字：「a target Si 3-Fin bulk n-FinFET」），目標為 sub-14-nm 技術節點；n 型；3 鰭。另有幾何變體：tapered source and drain regions（漸縮式源汲區）作為抗 SHE 的設計方案。Lg、Hfin、Wfin、fin pitch、EOT 均未取得（全文封閉取用）。

**2 方法與 SHE 定義**　`ta_sweep`　「a 3-D quantum-corrected electrothermal numerical device analysis involving a coupled hydrodynamic and thermodynamic transport models」——3D 量子修正電熱模擬，HD（hydrodynamic）與 TD（thermodynamic）耦合。量子修正的具體模型（density-gradient / 其他）未在摘要指名。自變數為 ambient temperature (TA) 與 electrical contact temperature；thermal contact resistance 為第二個掃描量。輸出量含 device lumped thermal resistance Rth,eff（故本文同時具 Rth-extraction 成分，但主軸自變數是環境溫度，因此歸 ta_sweep）。摘要聲稱「The simulation parameters are calibrated with the state-of-the-art Si FinFET measurement data from the literature.」，但校準對象與殘差未量化。求解器名稱、thermode 幾何位置與 SurfaceResistance 數值、有無 BTE / 聲子模型，均未取得。

**3 關鍵定量結果**　僅摘要層級，全文（含 Rth,eff 數值、ΔT、Ion 退化 %、對應 VGS/VDS/TA）未取得，原文印出的數字一個都拿不到。可引用的逐字英文結論句：「The simulation predictions establish the fact that the thermal contact resistances and the within-chip ambient temperature ( T_A ) have adverse effects on device lumped thermal resistance ( R_th,eff ) and performance metrics.」；「The numerical device simulations quantitatively predicted the impact of ambient and electrical contact temperatures on device short-channel effect immunity and performance.」；「Finally, we have numerically analyzed the FinFET design solutions (tapered source and drain regions) to improve the tolerance against the ambient temperature-induced SHE.」；機制句：「The ambient heat energy coupling through the thermal contact resistances will strongly impact device SHE in FinFETs due to increase in the surface-to-volume ratio of confined geometry thin Si Fin.」Ion 下降 %：未取得。Rth,eff 數值：未取得（僅知有此量）。ΔT / 峰值晶格溫度：未取得。全部量化結果屬「僅圖層級 / 正文層級」。

**4 TCAD 校準用途**　不可直接校準，理由：無任何 Rth,eff、ΔT、Ion% 數值可取，也沒有 thermode 位置與 SurfaceResistance 的具體設定值，無法用來對照判準帶中的 single-fin Rth 1-4 MK/W。可用於 deck 的僅方法學層級（來自摘要）：(1) 3-fin bulk n-FinFET 的自熱應以 HD + TD 耦合並加量子修正求解，與使用者 deck 的模型選擇一致；(2) 熱接觸電阻應設在電性接點（source / drain / gate）上，且必須理解 Rth,eff 是「邊界設定的函數」而非元件固有值；(3) 若使用者要做幾何抑制實驗，tapered S/D 是文獻已驗證的方向。

**5 批判**
   1. 無數值可判定，原因：IEEE Xplore 封閉取用（WebFetch 回傳空內容），僅由 Semantic Scholar / OpenAlex 取得摘要；摘要明確使用「quantitatively predicted」但未印出任何數字，Rth,eff、ΔT、Ion 退化 % 全部在正文與圖中，因此無法比對 single-fin Rth 1-4 MK/W 或飽和 Ion 下降 3-12%（bulk）的判準帶。
   2. 分類陷阱：本文自變數為 ambient temperature 與 electrical contact temperature，屬 ta_sweep；摘要中完全沒有 electrothermal vs isothermal 的對照設計。把本文引為「SHE 使飽和 Ion 降 X%」的數字來源將是錯誤歸因——這正是本批（七 系列）三篇共通的分類陷阱。
   3. 熱邊界即研究對象：thermal contact resistance 被當成掃描參數而非固定設定，所以本文的 Rth,eff 與溫升都是邊界條件的函數。這使它無法作為判斷「thermode 是否貼太近通道 / 是否過絕熱」的獨立錨點，反而只能說明該敏感度存在。
   4. 糾纏因子：tapered source/drain 同時改變寄生電阻、電流路徑與熱擴散截面，SHE 容忍度的改善無法與電性（Rsd 降低）改善解耦；摘要亦同時討論 short-channel effect immunity，電、熱、SCE 三者混在同一組幾何變化中。
   5. 純數值模擬，無自量測、無誤差棒、無重複性資訊；雖聲稱以文獻量測資料校準，但校準的目標曲線、擬合殘差、被校參數清單皆未在可取得的摘要中交代。
   6. 外推限制：單一 3-fin bulk n-FinFET 幾何，未報 p 型對照（無法檢核核心錨點中 n/p 不對稱，如 14nm 的 n 7.26% / p 8.91%），也無法外推至多鰭多指 RF 結構（34 kK/W 量級）或 SOI/GAA/nanosheet。

**6 可引用性**　B（只能引用定性結論）— 僅取得摘要，可逐字引用其定性結論（熱接觸電阻與 within-chip TA 會惡化 Rth,eff 與元件性能、tapered S/D 可提升容忍度），但沒有任何可直接引用的數字。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2018.2834979?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/TED.2018.2834979

**8 與原表差異**　與原表一致。原表記「Si 3-fin bulk n-FinFET, sub-14-nm technology node；No % in abstract (confirmed)；performance-metric degradation vs TA and TCR is figure-level only；not accessed (closed access)」，本次兩個獨立來源核對相符：元件確為 Si 3-Fin bulk n-FinFET、確為 sub-14-nm 節點、摘要確實無百分比、確為封閉取用（Semantic Scholar 標 status: CLOSED，OpenAlex best_oa_location 為 None）。本次補全資訊（非衝突、非更正）：完整標題結尾為「…Multi-Fin Si n-FinFET Performance」；卷期頁碼 vol. 65, no. 7, pp. 2721–2728；作者共 4 人（Venkateswarlu、Sudarsanan、Singh、Nayak），單位 IIT Hyderabad；摘要另揭露有 tapered source/drain 的抗 SHE 設計方案與 Rth,eff 這個 lumped 熱阻量。註：七02 是本篇同團隊的電路級後續研究（2020, TED 67(4)），兩者為系列文。

---

## 七04 — Study on the regulation factors and mechanism of self-heating effects in non-rectangular 14 nm bulk FinFET

- **DOI／識別**：`10.1088/1361-6641/ad689f`　**來源**：非　**年**：2024
- **作者／單位**：Zhaohui Qin（第一作者），Institute of Microelectronics, Chinese Academy of Sciences（中國科學院微電子研究所），No. 3 Beitucheng West Road, Chaoyang District, Beijing 100029, China；共同作者 Lan Chen、Renjie Lu、Yali Wang、Xiaoran Hao、Rong Chen、Yan Sun、Qin Du（全部同單位）
- **出處**：Semiconductor Science and Technology（IOP Publishing）, vol. 39, no. 9, article 095008

**1 元件**　14 nm bulk FinFET，非矩形（non-rectangular, NR）fin：fin 上半部為圓柱梯形（cylindrical trapezoidal）結構。原文印出幾何：「L_gate: Channel length 16 nm; H_fin: Fin height 32 nm; W_fin: Fin width 10 nm」。FinAngle 掃描 84°、86°、88°、90°（90° 即傳統矩形 fin）。n 型（全篇以 electron carrier temperature 與 electron mobility 論述）。鰭數未取得（原文未印出，推測為單鰭，不代入）。註：首輪擷取曾出現「gate oxide thickness 0.15 nm」，第二輪逐字核對未再出現且該數值物理上不合理（疑為介面層或 EOT 誤植），標為存疑、不建議引用。

**2 方法與 SHE 定義**　`ta_sweep`　Sentaurus TCAD。載子與量子模型：「the density gradient model were selected as quantum effects and high field saturation model was used」；遷移率：「the inverse evolution layer and accumulation layer mobility of the carrier mobility and the Lombard model were selected」（即 Lombardi 表面遷移率模型 + 反轉/累積層分量）；熱傳輸：「Hydrodynamic transpost model (HD) and thermodynamic (TD) model are used for thermal simulation」。熱邊界（thermode）設定為本文對 TCAD deck 最有價值的部分，原文逐字：「the boundary thermal resistances of the source, drain and gate are set to have the same value, resulting in R_th,GSD = 8 × 10−4 cm2 K W−1」；「a better simulation of thermal effects sets the substrate boundary to have a relatively high value, R_th,Sub = 1 × 10−2 cm−2 K W−1」（後者單位印為 cm−2 K W−1，應為 cm2 K W−1 之印刷錯誤）。偏壓：Vdd = 800 mV，Vgs = 0.8 V，Vds 取 0.05 V（線性）與 0.8 V（飽和）。TA 掃描 220 K → 400 K。無 BTE、無聲子色散 / 邊界散射模型。全文無 electrothermal-vs-isothermal 對照組，亦無 pulsed-vs-DC 量測。同時含 Rth-extraction 成分（Fig. 7/9/11 為 Rth vs FinAngle / vs TA / vs 摻雜），但主軸自變數為環境溫度與幾何，故歸 ta_sweep。

**3 關鍵定量結果**　全文取得，以下皆為原文印出數字（逐字引用）。峰值溫度 @ Vds = Vgs = 0.8 V、TA = 300 K：「The peak temperatures of electron carrier temperature and lattice temperature are 2663 K and 419.3 K, respectively.」→ 自熱溫升 ΔT ≈ 119 K（ΔT 為本人由 419.3 − 300 反算，原文未直接印出）。FinAngle 掃描（84°/86°/88°/90°）：「the corresponding maximum lattice temperature (T_L, max) is 383.34 K, 409.528 K, 419.342 K and 436.812 K」；「As the FinAngle increases from 84° to 90°, the I_off is increased from 3.45 × 10−11 to 5.94 × 10−11 A」；「the maximum ratio of I_on/I_off is 5.09 × 105」。環境溫度掃描（TA 300 → 400 K，Vgs = Vds = 0.8 V）：「the T_L,max from 419.342 to 520.688 K (with 84.92% increase)」、「resulting in current 2.33051 × 10−5 to 2.3257 × 10−5 A (with 0.21% decrease)」。環境溫度降溫（TA 300 → 220 K）：「T_L,max decreased from 419.342 to 338.331 K (with 19.32% decrease), resulting in an increase in current 2.3257 × 10−5 to 2.3501 × 10−5 A (with 0.87% increase)」。次臨界特性（TA 300 → 400 K）：「when the ambient temperature increases from 300 K to 400 K, the V_th drops from 0.322 to 0.253 mV (nearly 21.5% degradation)」（單位 mV 應為 V，原文印刷錯誤）；「the SS increased from 64.36 to 86.26 mV/dec (34% increase)」。摻雜研究：「as the N_ext increases, the T_L,max and R_th of the device increase」。結論句：「thermal resistance and lattice temperature can be reduced by reducing the FinAngle and whereas decreasing the W_eff. Higher ambient temperatures will deteriorate self-heating effect, resulting in degradation of threshold voltage and lower electron mobility.」重要缺項：Rth 的絕對值僅圖層級（Fig. 7 = Rth vs FinAngle、Fig. 9 = T_L,max 與 Rth vs TA、Fig. 11 = Rth vs 摻雜），全文未印出任何 K/W 數值，需自讀原圖；且全文沒有 electrothermal 對 isothermal 的 Ion 差值，因此本文無法提供任何「SHE 造成的飽和 Ion 下降 %」。

**4 TCAD 校準用途**　這是本批唯一能直接餵給 deck 的論文。(1) thermode SurfaceResistance 量級可直接抄：source / drain / gate 三處 thermode 設同值 R_th,GSD = 8 × 10⁻⁴ cm²·K·W⁻¹（= 8 × 10⁻⁸ m²·K·W⁻¹），substrate thermode 設 R_th,Sub = 1 × 10⁻² cm²·K·W⁻¹（比 GSD 大逾一個數量級，代表刻意讓基板散熱路徑變差）。(2) 可比對的 ΔT 錨點：14 nm bulk、Lg = 16 nm、Hfin = 32 nm、Wfin = 10 nm、Vg = Vd = 0.8 V、TA = 300 K 時 T_L,max = 419.3 K，即 ΔT ≈ 119 K；使用者若在相近幾何與偏壓下算出 ΔT 遠低於此，代表 thermode 太導熱（或貼太近通道），遠高於此則過絕熱。(3) 可對齊的幾何：矩形 fin 對應 FinAngle = 90°，T_L,max = 436.812 K；使用者的矩形 14 nm deck 應以此點對標，而非以 88° 的 419.342 K。(4) 可 sanity-check 的模型組合：density gradient（量子）+ HD + TD + Lombardi 遷移率 + high-field saturation。(5) 明確不可用之處：本文的 0.21% / 0.87% 電流變化是環境溫度掃描結果，不是 electrothermal-vs-isothermal 差值，絕對不能填入 SHE Ion 下降 % 的判準比對。

**5 批判**
   1. 判準帶判定：判定為「判準帶外，但不構成 SHE 的反例」。本文唯一的電流變化數字（TA 300→400 K 時 Ion −0.21%）遠低於 bulk 判準帶 3-12%，原因不是 SHE 太弱，而是該數字根本不是 SHE 增量——本文完全沒有 electrothermal vs isothermal 對照組。交叉檢核可證：TA = 300 K 時 T_L,max = 419.342 K 反推自熱溫升 ΔT ≈ 119 K，套用 ΔIon%/ΔT ≈ 0.10-0.20 %/K，應對應 12-24% 的 Ion 下降；本文報的 0.21% 與此差約兩個數量級，明確證實 0.21% 不可當 SHE%。此與原表判定「此為 ta_sweep，不得計入 SHE%」完全一致。
   2. 原文內部數字定義不一致（嚴重，引用前必須自行重算）：「T_L,max from 419.342 to 520.688 K (with 84.92% increase)」的標準相對變化實為 +24.2%；84.92% 只有在以 300 K 時的自熱溫升 ΔT = 119.342 K 為分母時才成立（101.346 / 119.342 = 84.92%），而同一段落的 19.32% 卻是用標準相對變化算的（81.011 / 419.342 = 19.32%）。同一段兩個百分比用了兩套定義且原文未說明，任何引用都必須回到絕對溫度值重算。
   3. 其他數字瑕疵，反映編輯品質偏低：降溫段「increase in current 2.3257 × 10−5 to 2.3501 × 10−5 A (with 0.87% increase)」以 TA = 400 K 的電流 2.3257e-5 為起點而非 300 K 的 2.33051e-5，以 300 K 為基準重算應為 +0.84%；V_th「drops from 0.322 to 0.253 mV」單位應為 V（322 → 253 mV）；R_th,Sub 單位印為 cm⁻²·K·W⁻¹ 亦為印刷錯誤（應為 cm²·K·W⁻¹）。
   4. 分類陷阱的直接證據：SS 從 64.36 → 86.26 mV/dec（+34%）與理想 kT/q 標度 400/300 = +33.3% 幾乎完全吻合，說明該組數據是純環境溫度效應（ta_sweep），不含任何額外的自熱增量資訊。這是本卡最重要的分類佐證，也是使用者最該避免的誤引用。
   5. 熱邊界疑似偏絕熱：TA = 300 K、Vg = Vd = 0.8 V 下 T_L,max ≈ 419 K（ΔT ≈ 119 K）對 14 nm bulk FinFET 偏高。原文明白承認 substrate thermode 被刻意設成高熱阻（1 × 10⁻² 相對 GSD 的 8 × 10⁻⁴，高逾一個數量級），但 bulk 元件的主要散熱路徑正是基板矽襯底；此設定會系統性放大自熱。使用者照抄前應做敏感度掃描，確認未落入「thermode 過絕熱」區。
   6. 糾纏因子與外推限制：FinAngle 同時改變有效通道寬度 W_eff、Ioff（3.45e-11 → 5.94e-11 A）與熱擴散截面，熱與電無法解耦，故「降低 FinAngle 可降低 Rth 與 T_L,max」這個結論同時混入了 Weff 縮小造成的功率下降；Rth 只有圖層級、全文無 K/W 數值，無法與 single-fin 1-4 MK/W 判準對照；純模擬、單一幾何、無誤差棒與重複性資訊；鰭數未說明，無法外推至多鰭多指結構。

**6 可引用性**　A（可直接引用數字）— 幾何（Lg 16 / Hfin 32 / Wfin 10 nm）、thermode 熱阻設定（R_th,GSD = 8 × 10⁻⁴、R_th,Sub = 1 × 10⁻² cm²·K·W⁻¹）與各 FinAngle 下的 T_L,max 絕對值均為原文印出且已逐字核對，可直接引用；但論文自算的百分比（84.92%、0.87%）定義不一致且部分單位誤植，引用百分比前必須自行由絕對值重算，且 0.21%/0.87% 絕不可標示為 SHE 造成的 Ion 下降。

**7 取得狀態**　全文
   - https://iopscience.iop.org/article/10.1088/1361-6641/ad689f
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1088/1361-6641/ad689f?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1088/1361-6641/ad689f

**8 與原表差異**　與原表一致。原表記載的每一項均逐字核對相符：14 nm bulk FinFET、圓柱梯形（非矩形）fin、FinAngle 84°-90° 掃描、TA 300→400 K 時驅動電流僅 −0.21%（2.33051e-5 → 2.3257e-5 A）、TA 220 K 時 +0.87%、Vgs = Vds = 0.8 V、TA = 300-400 K 另有 220 K 點、此為 ta_sweep 不得計入 SHE%、論文無 electrothermal-vs-isothermal 對照。本次新增（補充，非衝突）：Lgate 16 nm / Hfin 32 nm / Wfin 10 nm；FinAngle 84/86/88/90° 對應 T_L,max = 383.34 / 409.528 / 419.342 / 436.812 K；峰值電子載子溫度 2663 K、峰值晶格溫度 419.3 K；thermode 設定 R_th,GSD = 8 × 10⁻⁴ cm²K/W、R_th,Sub = 1 × 10⁻² cm²K/W；Ioff 3.45e-11 → 5.94e-11 A、Ion/Ioff 最大 5.09 × 10⁵；Vth 322 → 253 mV（−21.5%）、SS 64.36 → 86.26 mV/dec（+34%）；工具為 Sentaurus TCAD，模型為 density gradient + HD + TD + Lombardi + high-field saturation；Rth 絕對值僅圖層級（Fig. 7/9/11）。另註：以下屬「原文自身」的內部不一致，非原表錯誤——84.92% 的百分比基準與同段 19.32% 不同、0.87% 的起始值取錯、Vth 單位誤植為 mV、R_th,Sub 單位誤植為 cm⁻²K/W，證據 URL 為 https://iopscience.iop.org/article/10.1088/1361-6641/ad689f ，已詳列於 critique。

---
