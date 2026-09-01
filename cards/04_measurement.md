# 第四章 · 量測 pulsed-vs-DC / TRE

_實體元件的 SHE 定義：DC 與脈衝 I-V 之差_

原表 8 篇｜本檔 8 篇｜取得層級：摘要 7、全文 1

## 四01 — In-Situ Monitoring of Self-Heating Effect in Aggressively Scaled FinFETs and Its Quantitative Impact on Hot Carrier Degradation Under Dynamic Circuit Operation

- **DOI／識別**：`10.1109/irps45951.2020.9129591`　**來源**：IEEE　**年**：2020
- **作者／單位**：Yiming Qu（第一作者），College of Information Science & Electronic Engineering, Zhejiang University, China；共同作者含 Jiwu Lu（Hunan University, College of Electrical and Information Engineering）、Junkang Li、Zhuo Chen、Jie Zhang（Zhejiang University）、Chunlong Li（Institute of Microelectronics, Chinese Academy of Sciences）、Shiuh-Wuu Lee、Yi Zhao（通訊，Zhejiang University）
- **出處**：2020 IEEE International Reliability Physics Symposium (IRPS)，pp. 1-6

**1 元件**　Aggressively scaled SOI FinFETs（摘要原文即以 "aggressively scaled SOI FinFETs" 描述）。技術節點、Lg、Hfin／Wfin、n/p 型別、鰭數與指數本次全部未取得（IEEE Xplore 全文與元件表在付費牆內；ieeexplore.ieee.org 文件頁回傳空內容、PDF 端點回傳 HTTP 418；OpenAlex 明示無 open access 版本）。與 四02／四03／四04 同屬浙江大學趙毅團隊之 sub-ns 量測系列。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　實驗量測（非 TCAD），採 sub-nanosecond 電性特性化技術。摘要原文："Self-heating effect (SHE) in aggressively scaled SOI FinFETs is experimentally and quantitatively investigated by utilizing a sub-nanosecond (ns) characterization technique." 掃描加熱／冷卻時間以分離熱時間常數："A 3D mapping of the channel temperature rise is obtained under different heating (the transistor is turned ON with a current flowing through the channel) and cooling (the transistor is turned OFF) time ranging from 500 ps to 10 μcs."（原文如此印出「μcs」，應為「μs」之排印，引用時建議寫 10 μs 並註明）。另有 in-situ 即時通道溫度監測："the real-time channel temperature is electrically monitored with a sub-nanosecond resolution during the whole stress phase"。無求解器、熱邊界條件、thermode 或 SurfaceResistance 設定可言（純量測）；HCI 部分另有數位電路應用之模擬："the impact of SHE during HCI stress is also simulated in the real digital circuit applications"，但模擬設定未取得。

**3 關鍵定量結果**　未取得（原文印出之數字在付費牆內）。本次取得之最高層級為完整摘要，摘要中無任何 Ion 下降 %、Rth（K/W）、ΔT（K）或峰值晶格溫度之具體數值。可引用之定性結論（摘要原文逐字）："It is observed that SHE could be alleviated or almost totally suppressed when the heating time is small enough and the cooling time is reasonably long." 以及 "the hot carrier degradation (HCD) lifetime can be precisely projected no matter SHE exists or not during the stress phases of HCD stress"。時間尺度為唯一可引用之量化資訊：加熱／冷卻時間掃描範圍 500 ps 至 10 μs；溫度解析度 sub-nanosecond。ΔT 之 3-D 通道溫升圖存在但為圖層級且本次未能存取（需自讀原圖）。偏壓條件（VGS/VDS/TA）摘要未載明。

**4 TCAD 校準用途**　不可直接校準（數值層面），理由：未取得任何 ΔT、Rth 或 Ion% 數值，也無 thermode／SurfaceResistance 可對齊（本篇為量測論文，本就沒有這些模擬參數）。但有兩項間接可用之校準指引：(1) 熱時間常數的實驗界限——本文以 500 ps 至 10 μs 的加熱時間掃描證實 SHE 在夠短的加熱時間下可被幾乎完全抑制，這替使用者的暫態電熱模擬（TransientTemperature / 脈衝 I-V 模擬）提供了時間軸掃描範圍的合理設定，也暗示 SOI FinFET 的熱時間常數落在此區間內。(2) 邊界條件 sanity-check——若使用者的 SOI deck 在 sub-ns 脈衝下仍算出顯著 SHE，與本文實驗趨勢矛盾，代表熱容或界面熱阻設定有問題。數值校準仍須依賴其姊妹篇（四02 JEDS 2019）之 ΔT 數據。

**5 批判**
   1. 無數值可判定，原因：IEEE 付費牆使本次僅取得摘要，摘要中不含 Ion 下降 %、ΔT（K）與 Rth，因此無法與 SOI 8-17% 判準帶或 0.10-0.20 %/K 交叉檢核比值做任何比對。摘要僅給出時間尺度（500 ps-10 μs）與定性抑制結論。
   2. 元件資訊嚴重不足，橫向可比性受限：連 SOI FinFET 的節點、Lg、Hfin、Wfin、鰭數都未取得，而 SHE 強度對 fin 幾何與 BOX 厚度極度敏感（BOX 為主要熱阻來源）。在未知幾何下，任何把本文結論外推到使用者 bulk FinFET deck 的做法都缺乏依據——SOI 與 bulk 的熱路徑本質不同（bulk 有矽基板散熱路徑，SOI 被 BOX 阻斷）。
   3. 糾纏因子明顯：本文的主軸是 SHE 對 hot carrier degradation（HCD）的量化影響，SHE 與 HCI 兩個機制在應力階段互相耦合——通道溫升同時改變載子能量分布與界面態產生率。要從本文萃取「純 SHE 造成的 Ion 降幅」必須先解耦 HCD 造成的不可逆退化，摘要層級無法判斷作者是否做了此解耦。
   4. 分類無 ta_sweep 陷阱，但有另一種混淆風險：本文屬 pulsed-vs-DC（加熱／冷卻時間掃描），不是改環境溫度。然而其「SHE 幾乎完全被抑制」之結論成立條件是「加熱時間夠短且冷卻時間夠長」，這是動態開關條件，與使用者關心的 DC 飽和區穩態 SHE 是相反的操作象限。若被引用成「先進 FinFET 的 SHE 不嚴重」即屬誤引。
   5. 無誤差棒與重複性資訊：摘要未提及量測重複次數、跨晶片變異或溫度校正的不確定度。sub-ns 量測的溫度萃取通常仰賴「電流-溫度校正曲線」，該校正本身的誤差會直接傳遞到 3-D 溫升圖，摘要層級無從評估。

**6 可引用性**　B（只能引用定性結論）— 僅可引用定性結論與時間尺度（SHE 在加熱時間夠短、冷卻時間夠長時可被緩解或幾乎完全抑制；加熱／冷卻時間掃描 500 ps-10 μs；sub-ns 解析度即時通道溫度監測），這些均有摘要逐字原文支撐。所有 ΔT、Rth、Ion% 數字均在付費牆內未取得，不得引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps45951.2020.9129591?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/irps45951.2020.9129591

**8 與原表差異**　與原表一致。原表記載之要點本次全部複驗成立：Aggressively scaled SOI FinFETs、浙江大學 Yi Zhao 團隊、數值未在可及材料中印出、摘要確認 SHE 在加熱時間短且冷卻時間足夠長時被抑制、應力階段偏壓、3-D 通道溫升圖 vs 加熱時間。本次新增原表未載之項目：完整標題補全（原表為刪節號截斷）、第一作者為 Yiming Qu（Zhejiang University）而非僅記團隊、共同作者機構（Hunan University、中科院微電子所）、會議全名與頁碼（IRPS 2020, pp. 1-6）、加熱／冷卻時間掃描的具體範圍 500 ps 至 10 μs、以及摘要末段另含數位電路應用中 HCI 應力下 SHE 影響之模擬。排印註記：摘要原文印為 "10 μcs"，判定為 "10 μs" 之排印錯誤（依 500 ps 起始之對數掃描慣例），已在 method_detail 標明，此為原文排印問題非原表錯誤。

---

## 四02 — Impact of Self-Heating Effect on Transistor Characterization and Reliability Issues in Sub-10 nm Technology Nodes

- **DOI／識別**：`10.1109/jeds.2019.2911085`　**來源**：IEEE　**年**：2019
- **作者／單位**：Yi Zhao（第一作者兼通訊），Zhejiang University, China；共同作者 Yiming Qu，Zhejiang University
- **出處**：IEEE Journal of the Electron Devices Society（JEDS），Volume 7, pp. 829-836

**1 元件**　FinFET 與 FDSOI（fully depleted silicon-on-insulator）兩類結構，訴求對象為 sub-10 nm 技術節點。本次僅取得摘要，其中未印出 Lg、Hfin/Wfin、節點、n/p 型別與鰭數。原表已查證記載（本次未能複驗）：Lg=20 nm bulk 與 SOI FinFET、14 nm 多鰭 FinFET（在 scope 內）、Lg=30 nm 級 planar 對照。本篇為 Gold OA（CC-BY-NC-ND，OpenAlex 與 Semantic Scholar 皆標 GOLD），但 IEEE 之 OA PDF 端點（ielx7/6245494/8656606/08691399.pdf）本次回傳 HTTP 418、stamp.jsp 亦 418、DOAJ 頁 403、web.archive.org 遭工具封鎖，故實質未取得全文。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　實驗量測，採 ultra-fast sub-1 ns 脈衝 I-V 技術，掃描不同開關速度以分離 SHE。摘要原文："by utilizing the ultra-fast sub-1 ns measurement technique, I–V characteristics of FinFETs and FDSOI devices at different switch speeds are obtained"。並做時間解析之通道溫度追蹤："dynamic SHE phenomena as well as the time-resolved channel temperature change during transistor's switch on and off are able to be experimentally observed"。另用快速量測萃取彈道傳輸效率："more accurate device parameters like ballistic transport efficiency are extracted by the ultra-fast measurements"。無求解器、熱邊界條件、thermode 位置或 SurfaceResistance（純量測論文，不適用）。

**3 關鍵定量結果**　未取得（本次僅達摘要層級；Gold OA PDF 端點被伺服器拒絕）。摘要中無 Ion 下降 %、Rth（K/W）、ΔT（K）或峰值晶格溫度之數字。摘要唯一可引用之量化性陳述（逐字）："it is experimentally confirmed that several nanoseconds are required to heat up the channel of transistors by the direct electrical characterization and, therefore, in sub-10 nm devices, SHE might be alleviated under high frequency/speed operations."——「several nanoseconds」為熱建立時間的量級陳述，非精確數值。原表已查證記載（視為既有事實，本次未能複驗）：FinFET 之 pulsed-vs-DC 為圖層級（Fig. 4，四種開關速度之 ID-VD，速度愈快 Ion 愈高；SOI FinFET 之 pulsed-vs-DC on-current 差異為所受測結構中最嚴重），全文未印出單一 FinFET 之 Ion 降幅 %；FinFET 通道達熱平衡升溫約 60 K，planar bulk 僅約 10 K；HCI 應力 VG=VD=1.1 V；彈道傳輸量測 298-423 K。以上數字本次無獨立來源可佐證，引用時須標明來源為原表既有查證。

**4 TCAD 校準用途**　間接可用，數值校準須依賴原表既有記載且應標明未複驗。(1) 若採信原表之「FinFET 通道熱平衡升溫約 60 K、planar bulk 約 10 K」，這是使用者 deck 最直接的 ΔT 比對錨點：在 HCI 應力偏壓（VG=VD=1.1 V，高於一般 VDD 0.7 V）下的穩態通道升溫量級。使用者在 VDD=0.7 V 下應預期 ΔT 明顯低於 60 K（功率隨 VDD 超線性下降），若在 0.7 V 就算出 60 K 以上，代表 thermode 過絕熱。(2) 交叉檢核：以 ΔT≈60 K 搭配 0.10-0.20 %/K 比值推得 Ion 降幅約 6-12%，恰落在 bulk 3-12% 判準帶上緣與 SOI 8-17% 帶內，可作為 deck 自洽性驗算（此推算為本人算術，非原文）。(3) 熱時間常數：摘要之「several nanoseconds 才能把通道加熱起來」可直接用於設定暫態模擬的時間網格與脈衝寬度。(4) 不可用於：thermode SurfaceResistance 之絕對值（本篇為量測，無此參數）。

**5 批判**
   1. 判準帶判定（間接）：本次摘要層級無 Ion% 可判。若採信原表記載之 ΔT≈60 K（FinFET，HCI 應力 VG=VD=1.1 V），套用 0.10-0.20 %/K 交叉檢核比值推得 Ion 降幅約 6-12%，落在 bulk 3-12% 判準帶內、SOI 8-17% 帶之下緣附近，與核心錨點（14 nm FinFET n 7.26% / p 8.91% @VDS=0.7 V）量級相容。但須注意 60 K 對應的是 1.1 V 應力偏壓而非 0.7 V VDD，兩者功率密度差距大，直接比對會高估；此為間接推論，非本篇印出之結論。
   2. OA 卻取不到，取得層級與宣稱不符：本篇被 OpenAlex/Semantic Scholar/DOAJ 標為 Gold OA（CC-BY-NC-ND / CC-BY-SA），但 IEEE 之 OA PDF 端點對非瀏覽器請求回傳 HTTP 418，DOAJ 頁 403。這代表「標為 OA」不等於「可程式化取得」，後續補查此篇需人工在瀏覽器開啟 IEEE Xplore 或 DOAJ 落地頁。原表記載的 60 K / 10 K 數字因此在本輪無法獨立複驗。
   3. 糾纏因子：本篇同時處理 SHE、HCI 可靠度與彈道傳輸效率萃取三件事，且量測涵蓋 298-423 K（環境溫度掃描）。這使本篇同時具有 pulsed-vs-DC 與 ta_sweep 兩種成分——引用時必須確認所引數字屬於哪一組實驗。特別是「彈道傳輸量測 298-423 K」若被當成 SHE 造成的溫升效應，即為典型的 ta_sweep 誤分類。
   4. 結構混雜且缺單一 % 出口：同一篇涵蓋 FinFET（bulk 與 SOI）與 FDSOI、以及 planar 對照，各自熱路徑不同（SOI/FDSOI 受 BOX 阻熱、bulk 有基板散熱），原表明載「全文未印出單一 FinFET %」，代表本篇天然不適合當作 Ion% 的定量引用來源，只能提供 ΔT 與趨勢。
   5. 誤差棒與重複性未知：摘要未提及量測重複性、晶片間變異或溫度萃取校正之不確定度。sub-1 ns 量測的溫度是由電流間接反推，校正曲線誤差會直接放大到 ΔT，而 60 K 這類數字若無誤差棒，用作 deck 校準目標時應保留至少 ±20% 的容許帶。

**6 可引用性**　B（只能引用定性結論）— 本次僅取得摘要，可直接引用的只有定性結論與量級陳述（sub-1 ns 脈衝量測可觀察動態 SHE 與時間解析通道溫度；加熱通道需要 several nanoseconds；因此 sub-10 nm 元件在高頻／高速操作下 SHE 可能被緩解）。原表記載之 60 K / 10 K 為既有查證事實但本次未複驗，若要寫進論文須先人工取得全文確認頁碼與圖號，屆時可升為 A。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/jeds.2019.2911085?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/jeds.2019.2911085
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/jeds.2019.2911085/citations?fields=title,contexts&limit=40

**8 與原表差異**　與原表一致（無數值衝突）。原表記載之「全文未印出單一 FinFET Ion 降幅 %」與本次摘要內容相容（摘要確實無 %）。本次新增原表未載之項目：完整標題補全、作者為 Yi Zhao 與 Yiming Qu 兩人（Zhejiang University）、卷期頁碼（JEDS Vol. 7, pp. 829-836）、Gold OA 狀態與 DOAJ 記錄、以及摘要逐字之「several nanoseconds 才能加熱通道」結論。取得層級說明：原表顯然曾讀到全文（記有 Fig. 4、60 K/10 K、VG=VD=1.1 V、298-423 K），本次因 IEEE OA PDF 端點回傳 HTTP 418、DOAJ 403、web.archive.org 被工具封鎖而僅達摘要，故原表之 60 K / 10 K 等數字本卡沿用但明確標註「來源為原表、本次未複驗」，未逕自覆蓋亦未當作本次查證所得。

---

## 四03 — Ultra fast (<1 ns) electrical characterization of self-heating effect and its impact on hot carrier injection in 14nm FinFETs

- **DOI／識別**：`10.1109/iedm.2017.8268520`　**來源**：IEEE　**年**：2017
- **作者／單位**：Yiming Qu（第一作者），Zhejiang University, China；共同作者 Xi Lin、Junkang Li、Ran Cheng、Xiao Yu、Zejie Zheng、Jiwu Lu、Yi Zhao（Zhejiang University）與 Bing Chen（Hunan University）
- **出處**：2017 IEEE International Electron Devices Meeting (IEDM)

**1 元件**　14 nm 節點 Si FinFET（摘要標題與內文均明載 "14 nm FinFETs"）。Lg、Hfin、Wfin、n/p 型別、鰭數與指數本次未取得（IEDM 全文在付費牆內；Semantic Scholar 標示 abstract 已被出版者 elided、openAccessPdf 為 CLOSED；ieeexplore 文件頁回傳空內容）。摘要來源為 OpenAlex 之 abstract_inverted_index 逐字重建。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　實驗量測（非 TCAD），採 sub-1 ns 超快脈衝 I-V。摘要原文："We demonstrate electrical characterizations within sub-1 ns to investigate the self-heating effect (SHE) in 14 nm FinFETs, for the first time." 量測速度："Thanks to extremely fast I-V measurement speed (~500 ps), the heat generation and dissipation process in the transistor channel are precisely captured." 溫度萃取方法（本篇最具方法論價值處）："Furthermore, the unique correlation between channel temperature and drain current at different gate and drain biases is obtained. With this correlation, the transient and static channel temperatures could be extracted for devices with any working conditions and switching speeds." 無求解器、熱邊界條件、thermode 或 SurfaceResistance（純量測，不適用）；HCI 部分以真實電路應力（GHz 隨機訊號）進行。

**3 關鍵定量結果**　未取得具體數值（IEDM 全文在付費牆內）。摘要層級可引用之定性／方法論結論（逐字原文）："The impact of SHE on HCI degradation under real circuit stress is also investigated, showing that even under high frequency (GHz with random signals), SHE still has significant impact on HCI degradation in 14 nm FinFETs." 唯一可引用之量化資訊為量測速度 ~500 ps 與 sub-1 ns 之時間解析度。無 Ion 下降 %、無 Rth（K/W）、無 ΔT（K）、無峰值晶格溫度；偏壓條件僅泛稱 "different gate and drain biases"，未印出具體 VGS/VDS/TA。pulsed-vs-DC 之 ID 差異為圖層級（需自讀原圖），本次未能存取。

**4 TCAD 校準用途**　不可直接校準（數值層面），理由：未取得任何 ΔT、Rth 或 Ion% 數值，且本篇為量測論文，本就不含 thermode／SurfaceResistance 等模擬參數可供對齊。可用之處有二：(1) 方法論對齊——本篇建立「通道溫度 vs 汲極電流」的校正關係，使任意工作條件下的暫態與穩態通道溫度皆可被萃取；使用者若要把 TCAD 的 ΔT 與實驗比對，本篇正是說明實驗端 ΔT 如何被定義與取得的方法依據，可避免拿模擬的「峰值晶格溫度」去對實驗的「等效通道平均溫度」而產生系統性偏差。(2) 幾何對齊——本篇是 14 nm 節點 FinFET，與使用者判準帶的核心錨點（14 nm FinFET n 7.26% / p 8.91% @VDS=0.7 V）同節點，具幾何可比性；但本篇本身不提供該 % 數字。

**5 批判**
   1. 無數值可判定，原因：IEDM 論文全文在付費牆內，Semantic Scholar 之 abstract 欄位已被出版者移除，本次僅能透過 OpenAlex 之 inverted index 重建摘要，其中不含任何 Ion 下降 %、ΔT 或 Rth，因此無法與 bulk 3-12% 判準帶或 0.10-0.20 %/K 比值比對。
   2. 與 四01／四02／四04 高度重疊，須避免重複計數：本篇與 四01（IRPS 2020）、四02（JEDS 2019）、四04（TED 2017）同為浙江大學趙毅團隊之 sub-ns 脈衝量測系列，四03 是其中最早的 14 nm FinFET IEDM 版本。文獻回顧若把四篇並列當作四個獨立證據，會高估此方法路線的證據獨立性——它們共用同一套量測平台、同一群樣品來源與同一套溫度校正方法，系統誤差不獨立。
   3. 結論方向與 四01／四02 表面相反，需小心引用：本篇強調「即使在 GHz 隨機訊號的高頻條件下，SHE 對 14 nm FinFET 的 HCI 退化仍有顯著影響」；而 四01（2020）與 四02（2019）強調「加熱時間夠短時 SHE 可被緩解／sub-10 nm 高頻下 SHE 可能被減輕」。兩者未必矛盾（一個談 HCI 累積退化、一個談瞬時電流），但若在同一段文獻回顧中並置而不說明其量測量不同，會產生自相矛盾的敘述。
   4. 糾纏因子：SHE 與 HCI 在本篇是耦合量測——通道溫升同時改變載子能量分布與界面態產生速率，且 HCI 造成的退化是不可逆的累積效應。要從本篇萃取「純 SHE 造成的飽和 Ion 下降」必須先扣除 HCI 退化，摘要層級無法判斷是否已解耦。
   5. 分類無 ta_sweep 陷阱，但溫度萃取有循環論證風險：本篇以「汲極電流」反推「通道溫度」，而 SHE 的效果又是透過「汲極電流下降」呈現；此校正關係的建立（不同閘／汲偏壓下的電流-溫度對應）若未以獨立的溫度源（如外部加熱台）標定，即存在循環性。摘要未說明校正細節，且未提供誤差棒或重複性資訊，使用者引用其 ΔT 數字時應先取得全文確認校正程序。

**6 可引用性**　B（只能引用定性結論）— 僅可引用定性與方法論結論（首次以 sub-1 ns、~500 ps 速度量測 14 nm FinFET 之 SHE；建立通道溫度與汲極電流之對應關係以萃取暫態與穩態通道溫度；即使在 GHz 隨機訊號下 SHE 對 HCI 退化仍有顯著影響），這些皆有 OpenAlex 重建之摘要逐字原文支撐。所有 ΔT、Rth、Ion% 與偏壓數值在付費牆內未取得，不得引用。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iedm.2017.8268520?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/iedm.2017.8268520
   - https://api.openalex.org/works/doi:10.1109/iedm.2017.8268520?select=abstract_inverted_index
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/iedm.2017.8268520/citations?fields=title,contexts&limit=40

**8 與原表差異**　與原表一致。原表記載之要點本次全部複驗成立：14 nm 節點商用 Si bulk FinFET、IEDM 全文付費牆內未取得、pulsed-vs-DC 的 ID 差異為圖層級、引文脈絡查無被引用的具體 %（本次再查 Semantic Scholar citation contexts，取回 5 則引文脈絡皆為定性描述，如 "ID increases significantly as the gate pulsewidth decreases, attributed to suppression of SHE by shorter pulsewidth, reaching saturation at 20 ns"，仍無本篇印出之 % 數字）、摘要層級稱任意工作條件下可萃取暫態與穩態通道溫度。本次新增原表未載之項目：完整標題補全、第一作者 Yiming Qu 與完整共同作者名單及機構（Zhejiang University 為主、Bing Chen 屬 Hunan University）、經 OpenAlex inverted index 重建之逐字摘要全文（Semantic Scholar 該欄已被出版者移除，此為新取得管道）、量測速度 ~500 ps 之明確數字，以及摘要末段「即使 GHz 隨機訊號下 SHE 對 HCI 仍有顯著影響」之逐字結論。

---

## 四04 — Investigation of Self-Heating Effect on Ballistic Transport Characterization for Si FinFETs Featuring Ultrafast Pulsed IV Technique

- **DOI／識別**：`10.1109/ted.2016.2646907`　**來源**：IEEE　**年**：2017（IEEE TED 64(3)，2017 年 3 月號；DOI 字串含 2016 係線上先行編號）
- **作者／單位**：Ran Cheng（第一作者），Zhejiang University, China；共同作者 Xiao Yu、Bing Chen、Yiming Qu、Jinghui Han、Rui Zhang（Zhejiang University）、Junfeng Li（Institute of Microelectronics, Chinese Academy of Sciences）、Yi Zhao（通訊，Zhejiang University & State Key Laboratory of Silicon Materials）
- **出處**：IEEE Transactions on Electron Devices，Volume 64, Issue 3, pp. 909-915

**1 元件**　Ultrascaled Si FinFETs（摘要原文即以 "ultrascaled Si FinFETs" 描述，未指名節點）。Lg、Hfin/Wfin、n/p 型別、鰭數與指數本次全部未取得（IEEE 付費牆；Semantic Scholar 標示 abstract 與 tldr 均被出版者 elided、openAccessPdf CLOSED；ieeexplore 頁面回傳空內容）。摘要來源為 OpenAlex 之 abstract_inverted_index 逐字重建。與 四01／四02／四03 同屬浙江大學趙毅團隊之 sub-ns 脈衝量測系列（四03 IEDM 2017 之共同作者 Ran Cheng、Xiao Yu、Yiming Qu 皆在列）。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　實驗量測（非 TCAD），以 ultrafast pulsed IV 對照傳統 DC 特性化。摘要原文："Traditional dc characterization technique is compared with ultrafast pulsed IV method." 提出脈衝量測作為正確萃取彈道傳輸的手段："Therefore, an ultrafast pulsed IV measurement technique is proposed for accurate ballistic transport characterization." 另處理串聯電阻之溫度相依性以避免熱效應污染萃取："since the series resistance (RSD) of FinFETs is temperature-dependent, a modified backscattering model is adopted to extract the ballistic transport without influence of the temperature-variant RSD." 並建立可外推之模型："A ballisticity scaling model was established to predict the ballistic transport parameters." 無求解器、熱邊界條件、thermode 位置或 SurfaceResistance（純量測 + 解析模型，不適用）。

**3 關鍵定量結果**　未取得具體數值（IEEE 付費牆）。摘要層級可引用之定性結論（逐字原文）："Due to severe self-heating effect introduced in process, ballistic parameters extracted using dc method would show essential discrepancies from those in real high-speed IC circuits." 以及外推結論 "It is found that very high ballistic transport could be achieved for sub-10-nm FinFETs technology nodes." 摘要中無任何 Ion 下降 %、Rth（K/W）、ΔT（K）、峰值晶格溫度或偏壓條件（VGS/VDS/TA）之數字。pulsed-vs-DC 之電流差異為圖層級（需自讀原圖），本次未能存取。

**4 TCAD 校準用途**　不可直接校準，理由：未取得任何 ΔT、Rth、Ion% 或偏壓數值，本篇亦無 thermode／SurfaceResistance 等模擬參數（純量測論文）。唯一有價值的間接指引是一項方法論警訊：本篇證實 SHE 會使 DC 法萃取的參數與真實高速電路情境「出現本質性差異」，並特別點出 series resistance（RSD）具溫度相依性。使用者的 TCAD deck 若要與文獻的實驗 I-V 比對，必須確認被比對的實驗數據是 DC 量測還是脈衝量測——拿 DC 實驗曲線去校準等溫（isothermal）模擬結果，會因為實驗曲線本身已含 SHE 而導致 thermode 被錯誤地調鬆（過絕熱）。此外，deck 中若把 S/D 串聯電阻設為溫度無關的常數，在電熱模式下會低估 SHE 對飽和電流的影響。

**5 批判**
   1. 無數值可判定，原因：IEEE TED 全文在付費牆內，Semantic Scholar 之 abstract 與 tldr 皆被出版者移除，本次僅能由 OpenAlex inverted index 重建摘要，其中不含 Ion 下降 %、ΔT 或 Rth，故無法與 bulk 3-12% / SOI 8-17% 判準帶或 0.10-0.20 %/K 交叉檢核比值做任何比對。
   2. 元件識別不足是本篇最大的引用障礙：摘要僅以 "ultrascaled Si FinFETs" 描述，未給節點、Lg、Hfin、Wfin 或鰭數。SHE 強度與彈道係數兩者都對 Lg 高度敏感（Lg 越短彈道性越高、但功率密度也越高），在未知 Lg 下無法判斷其結論適用於使用者的哪一段幾何空間。
   3. 糾纏因子最嚴重的一篇：本篇的目標量是 ballistic transport 參數（backscattering 係數、彈道係數），而非 SHE 本身；SHE 在此是被視為污染源而要被排除的因子。這代表本篇不會給出「SHE 造成 Ion 下降幾 %」的乾淨數字——它的結構性目的是把 SHE 從萃取中扣掉。把本篇當成 SHE 量化證據來引用是方向性的誤用。
   4. 模型外推的可信度受限："very high ballistic transport could be achieved for sub-10-nm FinFETs technology nodes" 是由 ballisticity scaling model 外推而得，非實測 sub-10 nm 元件。外推結論不應被引用為對 sub-10 nm 節點的實證。
   5. 分類無 ta_sweep 陷阱，但溫度相依 RSD 是隱藏變因：作者自承 RSD 具溫度相依性並為此改用 modified backscattering model，代表原始 pulsed-vs-DC 電流差中同時含有「通道遷移率下降」與「串聯電阻上升」兩個溫度機制。若未解耦就把整個電流差歸因於通道 SHE，會高估通道溫升。摘要層級未提供誤差棒、量測重複次數或跨晶片變異資訊。

**6 可引用性**　B（只能引用定性結論）— 僅可引用定性結論（因製程引入的嚴重 SHE，DC 法萃取之彈道參數與真實高速 IC 電路情境存在本質性差異，故提出 ultrafast pulsed IV 法；並以 ballisticity scaling model 外推 sub-10 nm FinFET 可達很高的彈道傳輸），皆有 OpenAlex 重建摘要之逐字原文支撐。所有數值在付費牆內未取得，不得引用；且本篇結構性地把 SHE 當作待排除的污染源，不適合作為 SHE 定量證據。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2016.2646907?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2016.2646907?fields=tldr,abstract,openAccessPdf,externalIds,publicationVenue,journal
   - https://api.openalex.org/works/doi:10.1109/ted.2016.2646907
   - https://api.openalex.org/works/doi:10.1109/ted.2016.2646907?select=abstract_inverted_index

**8 與原表差異**　與原表一致。原表記載之要點本次全部複驗成立：研究元件為 ultrascaled Si FinFETs 且 Lg 未於可及文本揭露、付費牆導致數值未取得、摘要僅定性稱 DC 法因嚴重 SHE 使彈道傳輸參數萃取出現 essential discrepancies、% 在圖層級、偏壓與 dT 均未取得。本次新增原表未載之項目：完整標題補全、第一作者 Ran Cheng 與完整共同作者名單及機構（Zhejiang University 為主、Junfeng Li 屬中科院微電子所、Yi Zhao 另掛 State Key Laboratory of Silicon Materials）、卷期頁碼（IEEE TED Vol. 64, Issue 3, pp. 909-915）、經 OpenAlex inverted index 重建之逐字摘要全文（Semantic Scholar 該欄已被出版者移除），以及原表未載之兩項方法細節：series resistance RSD 具溫度相依性、採用 modified backscattering model 排除溫度相依 RSD 之影響，並建立 ballisticity scaling model。年份備註（非 CORRECTION）：原表記 2017，與 IEEE TED 64(3) 2017 年 3 月號一致；DOI 字串中的 2016 為線上先行編號，Semantic Scholar 與 OpenAlex 亦均記 2017，原表無誤。

---

## 四05 — A Thermal-Aware Device Design Considerations for Nanoscale SOI and Bulk FinFETs

- **DOI／識別**：`10.1109/ted.2015.2502062`　**來源**：IEEE　**年**：2016（Crossref 記 published January 2016，TED 63(1)；OpenAlex 之 publication_year 顯示 2015 係線上先行日期）
- **作者／單位**：Ulayil Sajesh Kumar（第一作者），Department of Electrical Engineering, Indian Institute of Technology Bombay (IIT Bombay), Mumbai, India；共同作者 Valipe Ramgopal Rao（通訊，IIT Bombay, Department of Electrical Engineering）
- **出處**：IEEE Transactions on Electron Devices，Volume 63, Issue 1, pp. 280-287

**1 元件**　sub-22 nm 技術世代之 SOI 與 bulk Si FinFET（摘要原文："for sub-22-nm technologies"）。摘要明載其掃描變數包含 effective fin height（"bulk FinFETs will perform better than SOI FinFETs for small effective fin heights"）、body doping（"increased body doping in bulk FinFETs will increase self-heating effects"）與 channel length（"Channel length scaling in FinFETs"）。具體 Lg 值、Hfin/Wfin 數值、n/p 型別、鰭數與指數本次未取得（IEEE 付費牆；Semantic Scholar 標示 abstract 已被出版者 elided、openAccessPdf CLOSED；Crossref 無 abstract 欄；ieeexplore 頁面回傳空內容）。摘要來源為 OpenAlex 之 abstract_inverted_index 逐字重建。

**2 方法與 SHE 定義**　`Rth-extraction`　TCAD 電熱模擬，並以兩種熱參數萃取法交叉驗證。摘要原文："Thermal performance characteristics of fin-shaped FETs (FinFETs) are studied and analyzed in this paper for sub-22-nm technologies using the well-calibrated TCAD simulations." 萃取方法："In order to understand the isothermal characteristics of these devices because thermal effects, we use pulse rise-time well as ac conductance methods."（此句經 inverted index 重建，語序有還原瑕疵，語意為同時採用 pulse rise-time 法與 ac conductance 法）。作者明確指出 ac conductance 法對 FinFET 失效："We demonstrate that the method fails to accurately capture thermal time constants for FinFETs, as self-heating and gate resistance regions are indistinguishable from each other." 並確立 pulse rise-time 為可行路徑："A pulse rise-time method gives isothermal characteristics of these devices." 求解器名稱（Sentaurus 或其他）、熱邊界條件、thermode 位置與 SurfaceResistance 具體設定、是否啟用 hydrodynamic／BTE／聲子模型，本次均未取得（在付費牆內）。

**3 關鍵定量結果**　未取得具體數值（IEEE 付費牆；本次僅達重建摘要層級）。摘要中無 Ion 下降 %、Rth（K/W）、ΔT（K）、峰值晶格溫度之數字，亦未載明偏壓（VGS/VDS/TA）。可引用之定性結論（逐字原文）："bulk FinFETs have a relatively better thermal performance as compared with SOI FinFETs"；"only at high frequencies (>1 GHz), FinFETs show suppression of thermally induced degradation, which can be attributed to their higher surface-to-volume ratio"；"It is observed that bulk FinFETs will perform better than SOI FinFETs for small effective fin heights"；"we show increased body doping in bulk FinFETs will increase self-heating effects"。摘要末句經 inverted index 重建後語序破碎（提及 channel length scaling 與 drain current degradation with heating 之關係，並稱其為 sub-22 nm 之重要設計參數），語意方向可辨但不宜逐字引用，須取得全文原句確認。pulsed vs DC 之電流差為圖層級（需自讀原圖），本次未能存取。

**4 TCAD 校準用途**　間接可用，是本批中對 deck 設計思路最相關的一篇（同為 TCAD 電熱模擬、同為 Si FinFET、同時涵蓋 bulk 與 SOI），但無數值可直接搬用。可用之處：(1) 方法論——本篇明確指出 ac conductance 法在 FinFET 上因 self-heating 區與 gate resistance 區在頻域上無法區分而失效，pulse rise-time 法才能給出等溫特性；使用者若打算用 AC 小訊號輸出電導法從模擬中反推 Rth，本篇是必須引用的反例，改採脈衝上升時間法較穩健。(2) 幾何設計方向——bulk FinFET 熱性能優於 SOI、且在小的 effective fin height 下優勢更明顯；提高 body doping 會加重 SHE。使用者做 thermode／幾何敏感度掃描時可用這三條趨勢做方向性 sanity-check（若 deck 算出 SOI 比 bulk 更涼，即為熱邊界設定錯誤的強烈訊號）。(3) 頻率界限——>1 GHz 才觀察到熱致退化被抑制，可作為暫態模擬之頻率掃描起點。(4) 不可用於：Rth 絕對值、ΔT 或 Ion% 之數值校準，因摘要層級完全無數字，且單鰭 Rth 1-4 MK/W 之判準帶無法由本篇佐證。

**5 批判**
   1. 無數值可判定，原因：IEEE TED 全文在付費牆內，Semantic Scholar abstract 欄已被出版者移除、Crossref 無 abstract 欄，本次僅能由 OpenAlex inverted index 重建摘要，其中無任何 Ion 下降 %、Rth 或 ΔT 數字，故無法與 bulk 3-12% / SOI 8-17% 判準帶、0.10-0.20 %/K 比值或 single-fin Rth 1-4 MK/W 之判準帶做比對。
   2. 方法論警訊值得單獨引用：作者證實 ac conductance 法在 FinFET 上會失效（self-heating 與 gate resistance 的頻率響應區間無法分離）。這對使用者有直接影響——若打算用小訊號輸出電導的頻率相依性從 TCAD 反推熱時間常數與 Rth，本篇指出該路徑在 FinFET 幾何下有系統性風險，應改用脈衝上升時間法或直接讀取 thermode 熱流。
   3. bulk 優於 SOI 的結論須註明成立條件，不可無條件外推：摘要明載此優勢與 effective fin height 綁定（"for small effective fin heights"），且 bulk 的優勢會被 body doping 提高而侵蝕（"increased body doping in bulk FinFETs will increase self-heating effects"）。單一幾何或單一摻雜條件的結論不能外推成「bulk 永遠比 SOI 涼」。使用者的 deck 若為 bulk FinFET，這也意味著通道／基體摻雜是一個必須固定的糾纏變因。
   4. 分類無 ta_sweep 陷阱，但 method_type 有邊界模糊：本篇同時具 Rth-extraction（pulse rise-time 與 ac conductance 萃取熱時間常數與等溫特性）與 ET-vs-ISO（等溫 vs 含熱之 I-V 對照）兩種成分。本卡歸為 Rth-extraction 是因為摘要的敘事主軸在「如何正確取得等溫特性與熱時間常數」；引用時應說明其電流退化數字（若取得全文）究竟來自哪一組對照。
   5. 年份與資料庫記載不一致，引用時須用正式卷期：Crossref 記 IEEE TED Vol. 63, Issue 1, pp. 280-287, January 2016；OpenAlex 之 publication_year 顯示 2015（線上先行）、Semantic Scholar 記 2016。原表記 2016 正確。書目應寫 IEEE Trans. Electron Devices, vol. 63, no. 1, pp. 280-287, Jan. 2016。
   6. 缺誤差棒與可重現性資訊：純 TCAD 模擬且摘要僅稱 "well-calibrated"，未說明校準對象（實測數據來源、校準參數、殘差），亦無網格收斂或熱參數敏感度分析之描述。在無 Rth 絕對值與校準細節的情況下，本篇只能提供趨勢方向，不能提供量值。

**6 可引用性**　B（只能引用定性結論）— 僅可引用定性結論（bulk FinFET 熱性能優於 SOI FinFET、且在小 effective fin height 下更明顯；提高 body doping 會加重 SHE；僅在 >1 GHz 以上才觀察到熱致退化被抑制，歸因於較高的表面／體積比；ac conductance 法無法準確捕捉 FinFET 之熱時間常數，pulse rise-time 法可給出等溫特性），皆有 OpenAlex 重建摘要之逐字原文支撐。所有 Rth、ΔT、Ion% 數值在付費牆內未取得，不得引用。若後續人工取得全文並讀到 Rth 與電流退化 %，可升為 A——這是本批中最值得補查全文的一篇。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2015.2502062?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/ted.2015.2502062
   - https://api.openalex.org/works/doi:10.1109/ted.2015.2502062?select=abstract_inverted_index
   - https://api.crossref.org/works/10.1109/ted.2015.2502062
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ted.2015.2502062/citations?fields=title,contexts&limit=40

**8 與原表差異**　與原表一致。原表記載之要點本次全部複驗成立：sub-22 nm SOI 與 bulk Si FinFET、摘要無 %、以 pulse rise-time 法取得等溫特性（隱含 pulsed vs DC 電流差在圖層級）、全文未能存取、偏壓與 dT 未取得。本次新增原表未載之項目：完整標題補全、作者全名與機構（Ulayil Sajesh Kumar 與 Valipe Ramgopal Rao，均為 IIT Bombay 電機系）、卷期頁碼（IEEE TED Vol. 63, Issue 1, pp. 280-287, Jan. 2016，經 Crossref 與 OpenAlex 雙源確認）、經 OpenAlex inverted index 重建之逐字摘要全文，以及四項原表未載之定性結論：bulk 熱性能優於 SOI、ac conductance 法在 FinFET 上因 self-heating 與 gate resistance 區無法區分而失效、僅在 >1 GHz 以上熱致退化才被抑制（歸因於較高表面／體積比）、增加 body doping 會加重 SHE。另本次由 Semantic Scholar citation contexts 讀到一則第三方引用脈絡稱 "It is observed that for the small effective fin heights the bulk FinFETs offer better performance than the SOI FinFETs [6,7]"，與本篇摘要自述一致，可作為交叉佐證（但為第三方轉述，不作為數值來源）。年份備註（非 CORRECTION）：原表記 2016，Crossref 支持；OpenAlex 之 2015 為線上先行日期，原表無誤。

---

## 四06 — Hot carrier reliability characterization in consideration of self-heating in FinFET technology

- **DOI／識別**：`10.1109/IRPS.2016.7574505`　**來源**：IEEE　**年**：2016
- **作者／單位**：M. (Minjung) Jin 為第一作者；OpenAlex 原始單位字串為「System LSI division, Technology Reliability, Quality & Reliability Team, Yongin-City, Gyeonggi-Do, Korea」，其中共同作者 Lijie Zhang、Kab-Jin Nam 被 OpenAlex 對應到 Samsung (South Korea)。共 12 位作者（含 Sangwoo Pae、Haebum Lee）。
- **出處**：2016 IEEE International Reliability Physics Symposium (IRPS)

**1 元件**　未取得。可及文本（摘要＋metadata）僅稱「FinFET technology」，並區分 PFET / NFET。技術節點、bulk 或 SOI、Lg、Hfin/Wfin、鰭數、指數皆未載明。原表所記「14nm-class」本次無法從可及文本佐證。

**2 方法與 SHE 定義**　`pulsed-vs-DC`　純電性可靠度量測，非 TCAD 模擬。可及摘要指出比較 DC HCI stress 與 nanosecond pulsed waveform HCI stress，並以 Ring Oscillator（電路級 AC 條件）結果驗證所提出的「去耦 SHE 的經驗式 HCI lifetime model」。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、有無 hydrodynamic/BTE 等資訊：不適用（本篇非模擬論文）且全文未取得。

**3 關鍵定量結果**　無 Ion 下降百分比、無 Rth、無 ΔT、無峰值晶格溫度、無 VGS/VDS 數值。摘要層級逐字引用（原文印出，但為純定性）："A severity of hot carrier injection (HCI) in PFET becomes worse than NFET at elevated temperatures."；"This new observation is further found to be due to the coupled self-heating effects (SHE) during DC HCI stress (also a higher Ea in PFET HCI), rather than the negative bias temperature instability (NBTI) effect during HCI stress."；"a new empirical HCI lifetime model decoupled from the SHE is proposed, which is further verified by the Si data from nanosecond pulsed waveform HCI stress and Ring Oscillator stress results." 全文為 IEEE 付費牆，圖層級數字未取得。

**4 TCAD 校準用途**　不可直接校準，理由：可及文本完全沒有 Rth、ΔT、峰值晶格溫度、Ion 退化百分比或任何元件幾何，無法對應到 thermode SurfaceResistance 量級或 ΔT 判準。唯一可轉用的是「量測策略」層面的提示：ns 級 pulsed 波形可視為近似等溫（heat-free）基準，DC 則含 SHE；使用者若要用文獻做 ET-vs-ISO 對照，pulsed/DC 差值是實驗端的對應量。

**5 批判**
   1. 無數值可判定，原因：本次僅取得 OpenAlex 摘要（Semantic Scholar 的 abstract 欄位被出版者 elided），摘要內無任何 Ion%、ΔT、Rth 數字，故無法與判準帶（bulk 3–12%、SOI 8–17%、ΔIon%/ΔT 0.10–0.20 %/K）比較。
   2. 分類語意需注意：本篇的 pulsed-vs-DC 是為了抽出 HCI 壽命模型，不是為了量化飽和 Ion 的 SHE 退化；把它當成 ET-vs-ISO 的替代品會混淆「熱載子退化」與「自熱造成的瞬時電流下降」兩件事。
   3. 糾纏因子極重：HCI、NBTI、SHE 三者在 DC 應力下同時發生，論文的主要貢獻正是宣稱把 SHE 從 HCI 壽命中解耦；此解耦是否成立取決於未取得的全文細節（活化能 Ea 擬合、pulse 佔空比），摘要層級無法驗證。
   4. 可重現性資訊缺失：無元件數、無誤差棒、無晶圓/批次資訊，且作者為業界團隊（Samsung System LSI），製程細節通常不公開。

**6 可引用性**　C（僅可當背景引用）— 僅可當背景引用：可用來支持「DC 應力下 SHE 會與 HCI 耦合、PFET 在高溫下 HCI 反而比 NFET 嚴重」這類定性陳述，但沒有任何可引用的數值，且與使用者的飽和區 Ion 退化主題只是鄰接而非直擊。

**7 取得狀態**　摘要
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/irps.2016.7574505?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf
   - https://api.openalex.org/works/doi:10.1109/IRPS.2016.7574505

**8 與原表差異**　與原表一致：原表記「no Ion %；reliability-lifetime class metric only；bias/dT 未取得（全文付費）」，本次結果相同。補充一項需降級的記載：原表 orig 稱「Samsung production FinFET (14nm-class)」，本次可及文本（OpenAlex 摘要＋作者單位字串）只能確認作者隸屬 Samsung System LSI（韓國龍仁），全篇可及文字未出現任何節點數字，建議該欄改記為「節點未載明」。此為證據不足之降級，非數值衝突，故未標 CONFLICT。

---

## 四07 — A Reflection-Based Ultra-Fast Measurement Method for the Continuous Characterization of Self-Heating for Advanced MOSFETs

- **DOI／識別**：`10.3390/electronics14132634`　**來源**：非　**年**：2025
- **作者／單位**：Wei Liu（第一作者），College of Information Science and Electronic Engineering, Zhejiang University, Hangzhou 310027, China；通訊作者 Yi Zhao（Zhejiang University 兼 School of Integrated Circuits, East China Normal University, Shanghai）。
- **出處**：Electronics (MDPI), Volume 14, Issue 13, Article 2634

**1 元件**　全文層級確認：僅稱 "commercial-ready scaled transistors"、"short channel transistors"，為 RF 晶圓級量測而設計成 ground–signal–ground (GSG) 佈局；結論段稱 "advanced FinFET devices"。技術節點、bulk/SOI、Lg、Hfin/Wfin、鰭數、指數、n 或 p 通道：全文皆未載明（已逐頁掃過全文，內文出現的 14 nm / 28 nm / sub-10 nm 字樣全部只在參考文獻與引言的他人工作描述中，不是本篇 DUT）。

**2 方法與 SHE 定義**　`Rth-extraction`　純實驗量測（無 TCAD、無求解器、無 thermode/SurfaceResistance 概念）。設定：高頻 AWG 雙通道分別驅動 gate 與 drain，脈衝上升時間 tr = 200 ps；pick-off tee 內含 R1 = R2 = R3 = 16.7 Ω；傳輸線特性阻抗 Z0 = 50 Ω；1 m 傳輸線提供約 10 ns 延遲以分離入射波與反射波；gate pad 用 50 Ω 阻抗匹配 RF 探針，drain pad 刻意不匹配以產生反射；高頻寬 digital phosphor oscilloscope (DPO) 擷取。校正用 50 Ω 標準電阻與浮接傳輸線兩種端接分離入射/反射波形。以 Γ3 反推 channel resistance RC，再由 ID = VD/RC 得電流。熱阻由 ΔT[K] = Rth[K/W]·PD[W] 線性擬合取得，其中 PD = ID·VD。溫度計以 t=0 的 heat-free 電流對 chuck 溫度線性標定：Iheat-free = αTchuck + β。

**3 關鍵定量結果**　（1）熱時間常數 τth ≈ 17 ns —— 原文印出數字："And the τth value of the devices in Figure 4 is about 17 ns."（以 63.2% 電流退化為判準）。（2）熱阻 Rth ≈ 3.4 × 10^4 K/W —— 原文印出數字："The thermal resistance extracted from the experiment data is about 3.4 × 104 K/W, which is reliable compared with previous results of ultra-scaled MOSFETs"，Figure 5c 圖說亦印出 "Fitting yields Rth = 3.4 × 104 K/W."（3）偏壓 —— Figure 5a 圖說原文印出："under fixed bias conditions (VG = 700 mV; VD = 690 mV)"。（4）環境（chuck）溫度掃描範圍 223 K 至 373 K，原文印出："Figure 4 shows the drain current degradation versus the time at different chuck temperatures, ranging from 223 K to 373 K."（5）溫度計擬合參數原文印出：α = −0.0027 mA/K、β = 3.6 mA；穩態溫度取 t = 100 ns 之值。（6）Ion / ID 下降百分比：原文未印出任何百分比，僅圖層級（Figure 4 的 ID(t) 曲線），文字只到 "The drain current ID decreases rapidly at the first 50 ns once the device is on"（需自讀原圖）。（7）ΔT 絕對值：原文未印出，僅 Figure 5b/5c 圖層級。本次由原文印出的 α、β、Rth、偏壓自行推算（非原文印出，僅供 sanity-check）：Tchuck = 300 K 時 Iheat-free ≈ 3.6 − 0.0027×300 = 2.79 mA，PD ≈ 2.79 mA × 0.69 V ≈ 1.9 mW，ΔT ≈ 3.4×10^4 × 1.9×10^-3 ≈ 65 K。（8）另有一個 ~14% 的數字，但語意完全不同，原文印出："Previous comparative studies [26] showed that this method yields a slightly higher drain current (~14%) than commercial systems such as the B1500 due to reduced thermal stress under nanosecond pulses." 這是量測系統間差異，不是 SHE 造成的 Ion 退化。

**4 TCAD 校準用途**　高可用。（a）Rth = 3.4 × 10^4 K/W 正好落在判準帶的「多鰭多指 RF 結構約 34 kK/W」錨點上（GSG RF 佈局本質即多鰭多指），可直接拿來 sanity-check deck 中對應多鰭元件的等效熱阻；若使用者的 thermode SurfaceResistance 換算出的元件級 Rth 落在 MK/W 量級，代表模擬的是 single-fin 而非 RF 多指結構，兩者不可混比。（b）τth ≈ 17 ns 可校準暫態電熱模擬的熱容/熱時間常數，並定義「等溫（heat-free）基準」的量測窗上限——deck 若要重現「等溫」I-V，對應的是 t < 幾 ns 的狀態。（c）ΔT = Rth·PD 的線性關係可用來檢查 deck 在給定汲極功率下解出的 ΔT 是否合理；在 PD ≈ 1.9 mW（VD = 0.69 V）下，本文參數推得 ΔT ≈ 65 K 量級（此為本次推算值，非原文印出，僅作量級檢核）。（d）偏壓 VG = 700 mV / VD = 690 mV 幾乎等同使用者的 VDD ≈ 0.7 V 條件，偏壓對齊良好。（e）缺點：完全沒有幾何（Lg、Hfin、Wfin、鰭數），無法做幾何對齊，也無法把 Rth 歸一化成 per-fin 值。

**5 批判**
   1. 判準帶判定：Rth = 3.4 × 10^4 K/W 落在判準帶內，且精確命中「多鰭多指 RF 結構約 34 kK/W」這一錨點，原因是本篇 DUT 為 GSG RF 佈局的商用化短通道元件，散熱路徑寬、等效熱阻遠低於 single-fin 的 1–4 MK/W；至於「飽和 Ion 下降 7–11%」這一帶則無法判定，因為全文未印出任何 Ion 退化百分比（僅 Figure 4 圖層級）。
   2. 熱邊界/量測窗風險：t = 0 的 heat-free 電流是外插值，而 τth 只有 17 ns，200 ps 上升緣所涵蓋的窗口與熱時間常數僅差兩個數量級；若實際 τth 有更快的分量（近接面 ballistic 聲子），t = 0 外插會低估初始溫升，連帶低估 Rth。論文自己承認 "the DUT remains in a near-isothermal state during the early measurement window" 是一個假設而非量測結果。
   3. 糾纏因子與誤引陷阱：內文的 "~14%" 是本方法與 Keysight B1500 的量測系統差異，不是 SHE 造成的電流退化；這個數字若被誤引為「SHE 使 Ion 下降 14%」會直接跳出 7–11% 判準帶。引用時必須明確切割。
   4. 元件資訊缺失使外推受限：無節點、無 Lg/Hfin/Wfin/鰭數/指數、未說明 n 或 p 通道，Rth 無法歸一化到單鰭或單位閘寬，也無法判斷 3.4 × 10^4 K/W 對應幾根鰭；跨結構外推等於盲推。
   5. 統計與重複性薄弱：α、β 只說 "with a high R2 value" 卻未給 R2 數值；Figure 5c 的紅點（掃 chuck 溫度）與藍點（固定 273 K 掃 VD）混在同一條擬合線上，兩種取數路徑的系統誤差未分離；全篇無誤差棒、無元件數、無重複量測統計。
   6. 分類正確性：本篇同時做了 ta_sweep（chuck 223–373 K）與 SHE 量測，但 chuck 掃描是為了建立電流-溫度校正曲線（溫度計），不是把環境溫度效應當成 SHE，分類為 Rth-extraction 正確，未落入「ta_sweep 被誤當 SHE」的陷阱。

**6 可引用性**　A（可直接引用數字）— Rth = 3.4 × 10^4 K/W、τth ≈ 17 ns、VG = 700 mV / VD = 690 mV、chuck 223–373 K、α = −0.0027 mA/K、β = 3.6 mA 全為開放取用全文中原文印出的數字，可直接引用；但「Ion 下降百分比」與「ΔT 絕對值」屬圖層級，不可當作原文數字引用，需自讀 Figure 4 與 Figure 5b/5c。

**7 取得狀態**　全文
   - https://mdpi-res.com/d_attachment/electronics/electronics-14-02634/article_deploy/electronics-14-02634.pdf
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/electronics14132634?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf

**8 與原表差異**　與原表一致並補全。原表 orig 已載「Figure-level only: Fig. 4 shows continuous ID degradation vs time (first ~50 ns) at chuck temperatures 223-373 K; no step...」、「bias: VG = 700 mV, VD = 690 mV (Fig. 5a heat-free...)」、「dT: Real-time T(t) extracted via Iheat-free = ...」，本次全文取得後全部複驗成立。新增本次自全文取得的原文印出數字：Rth = 3.4 × 10^4 K/W、τth ≈ 17 ns、α = −0.0027 mA/K、β = 3.6 mA、pick-off tee R1=R2=R3=16.7 Ω、tr = 200 ps、穩態取樣點 t = 100 ns。原表 verdict「value_corrected」與本次結果相符，無衝突。

---

## 四08 — Experimental investigation of self heating effect (SHE) in multiple-fin SOI FinFETs

- **DOI／識別**：`10.1088/0268-1242/29/11/115021`　**來源**：非　**年**：2014
- **作者／單位**：Hai Jiang（第一作者），Institute of Microelectronics / Academy for Advanced Interdisciplinary Studies, Peking University, Beijing 100871, China；共同作者含 Nuo Xu（Dept. of EECS, University of California, Berkeley）、Xiaoyan Liu、Gang Du、Xing Zhang（皆 Peking University）。
- **出處**：Semiconductor Science and Technology (IOP Publishing), Volume 29, Number 11, Article 115021

**1 元件**　摘要層級確認：metal gate multiple-fin SOI FinFET，同時量測 n-channel 與 p-channel，涵蓋多組幾何參數（gate length、fin 數目、fin width 皆為變數）。以下幾何為原表既有記載、本次未能複驗（IOP 全文被 Radware bot 驗證阻擋）：Lg 90 nm–5 µm、Wfin 20–35 nm、Hfin 58 nm、2–50 根鰭。

**2 方法與 SHE 定義**　`Rth-extraction`　實驗量測，非 TCAD。摘要原文："the self-heating effect (SHE) on metal gate multiple-fin SOI FinFETs is studied by adopting the ac conductance technique to extract the thermal resistance and temperature rise in both n-channel and p-channel SOI FinFETs with various geometry parameters." 即 AC output conductance 法抽 Rth 與 ΔT。求解器、熱邊界條件、thermode 位置與 SurfaceResistance、hydrodynamic/BTE：不適用（純量測）；量測頻率範圍、儀器型號等細節本次未取得。

**3 關鍵定量結果**　飽和輸出電流退化（摘要原文印出）："It is shown that the SHE degrades by over 10% of the saturation output current in the n-channel and by over 7% in the p-channel." 幾何相依趨勢（摘要原文印出，皆為定性方向而無數值）："The extracted thermal resistances R th increase with the scaled down gate length, reducing the number of fin and shrinking the fin width."；"The temperature rise caused by the SHE increases with the scaled down gate length, increasing the number of fin and shrinking the fin width under the saturated operation condition."；"due to a larger power density in the n-channel SOI FinFETs under the same bias condition, the temperature in the n-channel FinFETs is higher than that in the p-channel FinFETs. Because the Si thermal conductivity decreases as the temperature increases, R th is larger in the n-channel FinFETs than in the p-channel FinFETs." Rth 與 ΔT 的具體數值：摘要未印出，屬圖層級（原表記載為「各幾何之 Rth/dT 於圖中給出」），本次未取得全文故未複驗。偏壓：摘要未載；原表記載為「飽和區：n-channel VGS=VDS=1.5 V；p-channel VGS=V…」，本次未複驗。峰值晶格溫度：未取得。

**4 TCAD 校準用途**　部分可用。（a）n-channel >10% / p-channel >7% 的飽和輸出電流退化，可作為 SOI FinFET 判準帶（8–17%）的實驗下界錨點，用來檢查 deck 若跑 SOI 版本、ET-vs-ISO 差值是否至少達到 10%（n）。（b）Rth 隨 Lg 縮短、鰭數減少、Wfin 變窄而上升的趨勢，可直接用來驗證 deck 的 thermode / SurfaceResistance 是否具備正確的幾何相依性——若使用者掃鰭數時 Rth 不隨鰭數減少而上升，代表熱邊界被設在離通道太遠或太導熱的位置，SHE 被抹平。（c）n 通道溫度高於 p 通道（功率密度較高）且 Rth(n) > Rth(p)（Si 熱導率隨溫上升而下降）這條因果鏈，可拿來檢查 deck 是否啟用了溫度相依的 Si 熱導率模型——若 deck 用固定 κ，就重現不出 Rth 的 n/p 不對稱。（d）不可直接設定 SurfaceResistance 數值，理由：本次未取得具體 Rth 數字（僅圖層級），且本篇為 SOI（BOX 主導熱阻），與使用者的 bulk FinFET 散熱路徑不同。

**5 批判**
   1. 判準帶判定：n-channel 「>10%」落在判準帶內（SOI 8–17%），p-channel 「>7%」略低於 SOI 帶下界但仍在 bulk 3–12% 帶內；原因合理——SOI 的 BOX 阻熱使退化高於 bulk，而 p 通道在相同偏壓下功率密度較低故退化較小，論文自己給出的物理解釋（power density 與 Si 熱導率的溫度相依）與判準帶方向一致。惟這兩個數字是不等式（"over"）而非點估計，做定量校準時只能當下界。
   2. 偏壓不可平移：原表記載本篇飽和量測在 VGS = VDS = 1.5 V，遠高於使用者的 VDD ≈ 0.7 V。SHE 造成的 ΔIon% 大致隨功耗超線性成長，1.5 V 下的 >10% 不能直接搬到 0.7 V；跨檢比值 ΔIon%/ΔT ≈ 0.10–0.20 %/K 也需要對應偏壓下的 ΔT 才能檢核，而本次無 ΔT 數值。
   3. 世代與結構外推風險高：90 nm 世代 metal gate SOI FinFET 與 sub-10 nm bulk FinFET 的散熱路徑本質不同（BOX 串聯熱阻 vs 基板直通），且 Hfin 58 nm、Wfin 20–35 nm 的長寬比與現代高鰭窄鰭不同；用本篇校準 bulk deck 的絕對 Rth 會系統性偏高。
   4. 量測語意陷阱：AC conductance 抽出的過溫是主動區的面積平均過溫，不是鰭內峰值溫度（同批的五04 正是在論證這一點）；若使用者拿本篇的 ΔT 去對 deck 的 peak lattice temperature，會低估峰值、進而把 thermode 調得過度絕熱。
   5. 統計與可及性：摘要層級無誤差棒、無元件數、無晶圓資訊；Rth 與 ΔT 全部只在圖中，需自讀原圖才有數值，而 IOP 全文本次被反爬阻擋，這是可及性限制而非論文缺陷。

**6 可引用性**　B（只能引用定性結論）— 「n-channel 飽和輸出電流退化 >10%、p-channel >7%」是摘要原文印出、可直接引用的定量下界；但除此之外的 Rth、ΔT、幾何、偏壓全部只在圖表或全文中，本次未取得無法複驗，故整體僅能引用定性結論與這組不等式，不宜當作可代入 deck 的點數值來源。

**7 取得狀態**　摘要
   - https://api.openalex.org/works/doi:10.1088/0268-1242/29/11/115021
   - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1088/0268-1242/29/11/115021?fields=title,abstract,year,authors,venue,externalIds,openAccessPdf

**8 與原表差異**　與原表一致：原表記「n-channel >10%、p-channel >7% 飽和電流劣化——IOP 全文確認」，本次以 OpenAlex 還原之摘要逐字複驗成立（"degrades by over 10% ... in the n-channel and by over 7% in the p-channel"），無衝突。存取層級差異需標明：原表為「IOP 全文確認」，本次 IOP 站台以 Radware/perfdrive bot 驗證阻擋，僅取得摘要，因此原表所載之幾何（Lg 90 nm–5 µm、Wfin 20–35 nm、Hfin 58 nm、2–50 鰭）與偏壓（n-channel VGS=VDS=1.5 V）本次未複驗，於本卡中已明確標示為「沿用原表記載、非本次查證所得」。另補正一項原表未載的書目資訊：本刊為 Semiconductor Science and Technology, IOP Publishing, Vol. 29, No. 11, 115021，第一作者 Hai Jiang 隸屬北京大學微電子研究院，共同作者 Nuo Xu 隸屬 UC Berkeley。

---
