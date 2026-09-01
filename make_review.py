# -*- coding: utf-8 -*-
"""
從 _cards.json（87 張八欄深度卡）+ _worklist.json + _top10.json 產出：
  1) cards/*.md            — 依章節分檔的 Markdown 卡片
  2) 87papers_review.html  — 單頁 artifact（總覽 + 篩選 + 可展開卡片）
設計語彙：實驗室量測儀器 — 冷石墨中性 + 溫升橙 accent，方角、密集、等寬數字。
"""
import json, os, html, re, io, sys
from collections import Counter, OrderedDict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
BASE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(BASE, *a)

cards = json.load(open(P('_cards.json'), encoding='utf-8'))
wl = {w['id']: w for w in json.load(open(P('_worklist.json'), encoding='utf-8'))}
top10 = json.load(open(P('_top10.json'), encoding='utf-8')) if os.path.exists(P('_top10.json')) else []

SEC = OrderedDict([
    ('二', ('ET-vs-ISO｜矽 FinFET', '模擬中 SHE 的正確定義：同一 deck 開／關晶格加熱之差', 16)),
    ('三', ('ET-vs-ISO｜nanosheet / GAA', '相鄰技術，趨勢對照用', 14)),
    ('四', ('量測 pulsed-vs-DC / TRE', '實體元件的 SHE 定義：DC 與脈衝 I-V 之差', 8)),
    ('五', ('熱阻 Rth / ΔT', 'thermode SurfaceResistance 的校準標的', 45)),
    ('七', ('ta_sweep（非 SHE）', '改的是環境溫度，不可當 SHE 劣化基準引用', 4)),
])
SECFILE = {'二': '02_ET_vs_ISO_FinFET', '三': '03_ET_vs_ISO_NS_GAA', '四': '04_measurement',
           '五': '05_Rth_dT', '七': '07_ta_sweep'}
ACCESS_RANK = {'全文': 3, '摘要': 2, '僅metadata': 1, '未取得': 0}
CITE_TEXT = {'A': '可直接引用數字', 'B': '只能引用定性結論', 'C': '僅可當背景引用', 'D': '不建議引用'}

# 差異標記偵測：agent 常寫「無 CONFLICT」「非 CORRECTION」，須先剔除否定語境
NEG = re.compile(r'(無|非|不標|未標|無需標|不構成|未構成|不算|無需)\s*(CONFLICT|CORRECTION)', re.I)


def detect_flag(t):
    s = NEG.sub('', t)
    hard = re.search(r'[\[（(【⚠]\s*(CONFLICT|CORRECTION)', s, re.I)
    if hard:
        return hard.group(1).upper()
    m = re.search(r'\b(CONFLICT|CORRECTION)\b', s, re.I)
    return m.group(1).upper() if m else ''


def g(c, k, d='未取得'):
    v = c.get(k)
    return d if v is None or (isinstance(v, str) and not v.strip()) else v


def norm(c):
    i = c.get('id', '')
    w = wl.get(i, {})
    c = dict(c)
    c['ch'] = i[0] if i else '?'
    c['idx'] = int(i[1:]) if i[1:].isdigit() else 0
    c['ieee'] = w.get('ieee', '')
    c['orig_verdict'] = w.get('verdict', '')
    c['critique'] = c.get('critique') or []
    if isinstance(c['critique'], str):
        c['critique'] = [c['critique']]
    c['sources'] = c.get('sources') or []
    if isinstance(c['sources'], str):
        c['sources'] = [c['sources']]
    for k in ('title_full', 'authors', 'venue', 'year', 'device', 'method_type', 'method_detail',
              'results', 'tcad_use', 'citability', 'citability_reason', 'access_level', 'diff_note'):
        c[k] = g(c, k)
    m = re.search(r'(19|20)\d{2}', str(c['year']))
    c['yr'] = int(m.group()) if m else 0
    c['flag'] = detect_flag(c['diff_note'])
    return c


cards = [norm(c) for c in cards]
cards.sort(key=lambda c: (list(SEC).index(c['ch']) if c['ch'] in SEC else 9, c['idx']))
BYID = {c['id']: c for c in cards}

# ---------------------------------------------------------------- Markdown
os.makedirs(P('cards'), exist_ok=True)
for ch, (name, sub, n) in SEC.items():
    sel = [c for c in cards if c['ch'] == ch]
    L = ['# 第%s章 · %s' % (ch, name), '', '_%s_' % sub, '',
         '原表 %d 篇｜本檔 %d 篇｜取得層級：%s' % (
             n, len(sel), '、'.join('%s %d' % kv for kv in Counter(x['access_level'] for x in sel).most_common())), '']
    for c in sel:
        L += ['## %s — %s' % (c['id'], c['title_full']), '',
              '- **DOI／識別**：`%s`　**來源**：%s　**年**：%s' % (c['doi'], c['ieee'], c['year']),
              '- **作者／單位**：%s' % c['authors'],
              '- **出處**：%s' % c['venue'], '',
              '**1 元件**　%s' % c['device'], '',
              '**2 方法與 SHE 定義**　`%s`　%s' % (c['method_type'], c['method_detail']), '',
              '**3 關鍵定量結果**　%s' % c['results'], '',
              '**4 TCAD 校準用途**　%s' % c['tcad_use'], '',
              '**5 批判**'] + ['   %d. %s' % (i + 1, x) for i, x in enumerate(c['critique'])] + ['',
              '**6 可引用性**　%s（%s）— %s' % (c['citability'], CITE_TEXT.get(c['citability'], ''), c['citability_reason']), '',
              '**7 取得狀態**　%s' % c['access_level']] + \
             (['   - %s' % u for u in c['sources']] if c['sources'] else ['   - （無）']) + ['',
              '**8 與原表差異**　%s' % c['diff_note'], '', '---', '']
    open(P('cards', SECFILE[ch] + '.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('cards/*.md 已產出')

# ---------------------------------------------------------------- 統計
e = html.escape
cnt_ch = Counter(c['ch'] for c in cards)
cnt_cite = Counter(c['citability'] for c in cards)
cnt_acc = Counter(c['access_level'] for c in cards)
cnt_meth = Counter(c['method_type'] for c in cards)
n_ieee = sum(1 for c in cards if c['ieee'] == 'IEEE')
n_src = sum(len(c['sources']) for c in cards)
flags = [c for c in cards if c['flag']]
yrs = [c['yr'] for c in cards if c['yr']]


def bars(counter, order, labels=None, total=None):
    tot = total or (max(counter.values()) if counter else 1)
    out = []
    for k in order:
        v = counter.get(k, 0)
        lab = (labels or {}).get(k, k)
        out.append('<div class="brow"><span class="bk">%s</span><span class="btrack">'
                   '<span class="bfill s-%s" style="width:%.1f%%"></span></span>'
                   '<span class="bv">%d</span></div>' % (e(str(lab)), e(str(k)), v / tot * 100, v))
    return ''.join(out)


def card_html(c, ord_i):
    acc = ACCESS_RANK.get(c['access_level'], 0)
    dots = ''.join('<i class="%s"></i>' % ('on' if k < acc else '') for k in range(3))
    src = ''.join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (e(u), e(u))
                  for u in c['sources']) or '<li class="mut">（本次未取得任何可讀來源）</li>'
    crit = ''.join('<li>%s</li>' % e(x) for x in c['critique'])
    fl = '<b class="fl">%s</b>' % c['flag'] if c['flag'] else ''
    res_short = c['results'][:165] + ('…' if len(c['results']) > 165 else '')
    q = (c['title_full'] + ' ' + c['device'] + ' ' + c['results'] + ' ' + c['doi'] + ' ' + c['venue']).lower()
    return ('<article class="row" data-id="%s" data-ord="%d" data-ch="%s" data-cite="%s" data-acc="%s" '
            'data-meth="%s" data-src="%s" data-yr="%d" data-flag="%s" data-q="%s">'
            '<button class="hd" aria-expanded="false">'
            '<span class="id">%s</span><span class="hdmain">'
            '<span class="ti">%s</span>'
            '<span class="meta">%s · %s · %s</span>'
            '<span class="res">%s</span></span>'
            '<span class="hdside">%s<span class="cite c%s" title="%s">%s</span>'
            '<span class="acc" title="取得層級：%s">%s</span></span></button>'
            '<div class="bd"><dl>'
            '<dt><b>1</b>元件</dt><dd>%s</dd>'
            '<dt><b>2</b>方法與 SHE 定義</dt><dd><span class="tag">%s</span>%s</dd>'
            '<dt><b>3</b>關鍵定量結果</dt><dd class="q">%s</dd>'
            '<dt><b>4</b>TCAD 校準用途</dt><dd class="hi">%s</dd>'
            '<dt><b>5</b>批判</dt><dd><ol class="crit">%s</ol></dd>'
            '<dt><b>6</b>可引用性</dt><dd><span class="cite c%s">%s</span> %s — %s</dd>'
            '<dt><b>7</b>取得狀態</dt><dd>%s<ul class="src">%s</ul></dd>'
            '<dt><b>8</b>與原表差異</dt><dd class="%s">%s</dd>'
            '<dt><b>0</b>識別</dt><dd class="mut">%s｜原表狀態 <span class="mono">%s</span></dd>'
            '</dl></div></article>') % (
        e(c['id']), ord_i, c['ch'], e(c['citability']), e(c['access_level']), e(c['method_type']),
        'IEEE' if c['ieee'] == 'IEEE' else 'NONIEEE', c['yr'], c['flag'], e(q),
        e(c['id']), e(c['title_full']), e(c['doi']), e(c['venue'][:56]),
        str(c['yr']) if c['yr'] else e(c['year'][:12]), e(res_short),
        fl, e(c['citability']), e(CITE_TEXT.get(c['citability'], '')), e(c['citability']),
        e(c['access_level']), dots,
        e(c['device']), e(c['method_type']), e(c['method_detail']), e(c['results']), e(c['tcad_use']), crit,
        e(c['citability']), e(c['citability']), e(CITE_TEXT.get(c['citability'], '')), e(c['citability_reason']),
        e(c['access_level']), src,
        'diff' if c['flag'] else '', e(c['diff_note']),
        e(c['authors'][:190]), e(c['orig_verdict']))


CSS = open(P('_style.css'), encoding='utf-8').read()
JS = open(P('_app.js'), encoding='utf-8').read()

# ---- 章別 chips
ch_chips = ''.join('<button class="chip" data-k="ch" data-v="%s" aria-pressed="false">%s <i>%d</i></button>'
                   % (k, SEC[k][0], cnt_ch.get(k, 0)) for k in SEC)
cite_chips = ''.join('<button class="chip" data-k="cite" data-v="%s" aria-pressed="false">%s %s <i>%d</i></button>'
                     % (k, k, CITE_TEXT[k], cnt_cite.get(k, 0)) for k in 'ABCD' if cnt_cite.get(k))
acc_chips = ''.join('<button class="chip" data-k="acc" data-v="%s" aria-pressed="false">%s <i>%d</i></button>'
                    % (k, k, cnt_acc.get(k, 0)) for k in ['全文', '摘要', '僅metadata', '未取得'] if cnt_acc.get(k))
meth_chips = ''.join('<button class="chip" data-k="meth" data-v="%s" aria-pressed="false">%s <i>%d</i></button>'
                     % (k, k, v) for k, v in cnt_meth.most_common())
misc_chips = ('<button class="chip" data-k="src" data-v="IEEE" aria-pressed="false">IEEE <i>%d</i></button>'
              '<button class="chip" data-k="src" data-v="NONIEEE" aria-pressed="false">非 IEEE <i>%d</i></button>'
              '<button class="chip" data-k="flag" data-v="CORRECTION" aria-pressed="false">CORRECTION <i>%d</i></button>'
              '<button class="chip" data-k="flag" data-v="CONFLICT" aria-pressed="false">CONFLICT <i>%d</i></button>'
              ) % (n_ieee, len(cards) - n_ieee,
                   sum(1 for c in flags if c['flag'] == 'CORRECTION'),
                   sum(1 for c in flags if c['flag'] == 'CONFLICT'))

top_html = ''.join(
    '<div class="titem"><span class="num">%02d</span><div class="tbody">'
    '<strong><a href="#" data-goto="%s">%s</a></strong>'
    '<span class="tmeta">%s · %s · %s · 取得層級 %s</span><p>%s</p></div></div>'
    % (i + 1, e(t['id']), e(BYID[t['id']]['title_full']), e(t['id']), e(BYID[t['id']]['doi']),
       e(BYID[t['id']]['year'][:12]), e(BYID[t['id']]['access_level']), e(t['why']))
    for i, t in enumerate(top10) if t['id'] in BYID)

flag_html = ''.join(
    '<div class="fitem %s"><b>%s</b><span class="fid">%s · %s</span>'
    '<p><a href="#" data-goto="%s">%s</a></p><p>%s</p></div>'
    % (c['flag'].lower(), c['flag'], e(c['id']), e(c['doi']), e(c['id']), e(c['title_full'][:88]),
       e(re.sub(r'\s+', ' ', c['diff_note'])[:330] + '…'))
    for c in flags)

rows_html = ''.join(card_html(c, i) for i, c in enumerate(cards))

SPEC_ROWS = [
    ('標準矽 FinFET 飽和 Ion 下降', '~7–11 %', 'VDD≈0.7 V、TA=300 K、電熱 vs 等溫；判準帶 bulk 3–12 %、SOI 8–17 %'),
    ('交叉檢核比值', 'ΔIon% ÷ ΔT ≈ 0.10–0.20 %/K', '兩端都要對得上才算自洽'),
    ('過強訊號', '飽和 Ion 差 &gt; 20 %', '排除 DMG／junctionless 特例後 → 查 thermode 是否過絕熱'),
    ('過弱訊號', '飽和 Ion 差 &lt; 1 %', 'SHE 被邊界條件抹掉 → 查 thermode 是否貼太近通道'),
    ('single-fin 熱阻', 'Rth ≈ 1–4 MK/W', '單鰭元件級'),
    ('多鰭多指 RF 結構熱阻', 'Rth ≈ 34 kK/W', '與單鰭相差近百倍，最常搞錯的量級'),
    ('核心錨點 · 14 nm', 'n 7.26 % / p 8.91 % @VDS=0.7 V', '見 二09（全文可取得）'),
    ('核心錨點 · 3 nm', 'n 10.6 % / p 21.6 % @VG=VD=0.7 V', '見 二08；p 值含機械應力糾纏，非硬上限'),
]
spec_html = ''.join('<div><dt>%s</dt><dd>%s <em>%s</em></dd></div>' % r for r in SPEC_ROWS)

HTML = """<meta charset="utf-8">
<title>FinFET 自熱效應文獻庫</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=Noto+Serif+TC:wght@400;500;700&display=swap">
<style>__CSS__</style>

<header class="mast"><div class="wrap">
 <p class="eyebrow">TCAD 校準用文獻卡片庫</p>
 <h1>FinFET 自熱效應文獻庫</h1>
 <p class="lede">矽 FinFET 自熱對飽和區汲極電流的影響，__N__ 篇逐篇上網查證的深度卡。每篇八欄：元件、方法與 SHE 定義、關鍵定量結果、TCAD 校準用途、批判、可引用性分級、取得來源、與原目錄的差異。每一個數字都標了來源與取得層級；讀不到的就寫「未取得」，沒有一句是推測。</p>
 <div class="hstat">
  <div><b>__N__</b><span>篇深度卡</span></div>
  <div><b>__FULL__</b><span>取得全文</span></div>
  <div><b>__A__</b><span>可直接引用數字</span></div>
  <div><b>__FLAG__</b><span>修正／衝突</span></div>
  <div><b>__SRC__</b><span>查證來源 URL</span></div>
  <div><b>__YR__</b><span>年份跨度</span></div>
 </div>
</div></header>

<section><div class="wrap">
 <h2>判準帶</h2>
 <p class="sub">沿用原目錄第一章，逐字不動。每張卡的批判第 1 點都據此判定落在帶內或帶外。</p>
 <div class="spec">__SPEC__</div>
</div></section>

<section><div class="wrap">
 <h2>必讀 Top 10</h2>
 <p class="sub">依「對你的 TCAD deck 的校準價值」排序，編號即優先序。點標題直接跳到該卡並展開。另有 13 篇同為 A 級，用下方 <em>可引用性 A</em> 篩選查看。</p>
 <div class="top">__TOP__</div>
</div></section>

<section><div class="wrap">
 <h2>本次查證的修正與衝突（__FLAG__ 筆）</h2>
 <p class="sub">CORRECTION＝確認原目錄有誤或不完整並附證據；CONFLICT＝查到的值與原目錄不同，兩說並列不覆蓋，需自行讀原文判定。這是本次逐篇重查最有價值的產出。</p>
 __FLAGS__
</div></section>

<div class="filters"><div class="wrap">
 <div class="frow"><span class="flab">章別</span>__CHCHIPS__</div>
 <div class="frow"><span class="flab">可引用</span>__CITECHIPS__<span class="fsep"></span>__ACCCHIPS__</div>
 <div class="frow"><span class="flab">方法</span>__METHCHIPS__<span class="fsep"></span>__MISCCHIPS__</div>
 <div class="frow"><span class="flab">搜尋</span>
  <input id="q" type="search" placeholder="標題、元件、數字、DOI、期刊…">
  <select id="sort" class="chip"><option value="ord">依章節排序</option><option value="yr">依年份（新→舊）</option><option value="cite">依可引用性</option></select>
  <button class="chip" id="toggleAll">全部展開</button>
  <button class="chip" id="reset">清除篩選</button>
  <span class="count" id="cnt">__N__ / __N__ 篇</span>
 </div>
</div></div>

<main id="list" class="wrap">__ROWS__</main>

<footer><div class="wrap">
 <p>來源目錄：<span class="mono">FinFET_SHE_saturation_Ion_121papers (3).pdf</span>（121 篇）。本頁涵蓋第二、三、四、五、七章共 __N__ 篇；第六章「可靠度／其他指標」34 篇依指示排除。</p>
 <p>取得鏈：Semantic Scholar API → OpenAlex → openAccessPdf／arXiv → doi.org 出版者頁 → WebSearch。取得層級以卡片右側三格指示器表示（實心格數＝全文／摘要／僅 metadata）。</p>
 <p>標「僅圖層級」的數字表示原文有曲線但未印出單一百分比，引用前務必自讀原圖。</p>
</div></footer>
<script>__JS__</script>
"""

out = (HTML.replace('__CSS__', CSS).replace('__JS__', JS)
       .replace('__SPEC__', spec_html).replace('__TOP__', top_html)
       .replace('__FLAGS__', flag_html).replace('__ROWS__', rows_html)
       .replace('__CHCHIPS__', ch_chips).replace('__CITECHIPS__', cite_chips)
       .replace('__ACCCHIPS__', acc_chips).replace('__METHCHIPS__', meth_chips)
       .replace('__MISCCHIPS__', misc_chips)
       .replace('__FULL__', str(cnt_acc.get('全文', 0))).replace('__A__', str(cnt_cite.get('A', 0)))
       .replace('__FLAG__', str(len(flags))).replace('__SRC__', str(n_src))
       .replace('__YR__', '%d–%d' % (min(yrs), max(yrs)))
       .replace('__N__', str(len(cards))))

open(P('87papers_review.html'), 'w', encoding='utf-8').write(out)
print('87papers_review.html 已產出 %.0f KB' % (len(out) / 1024))

# ---- 片段預覽：全頁 596KB / 14885px 超過截圖工具負荷，切片供視覺檢查用
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@500;600;700'
         '&family=Noto+Serif+TC:wght@400;500;700&display=swap">')


def frag(name, body, js=''):
    open(P('_frag_%s.html' % name), 'w', encoding='utf-8').write(
        '<meta charset="utf-8"><title>frag %s</title>%s<style>%s</style>%s%s'
        % (name, FONTS, CSS, body, ('<script>%s</script>' % js) if js else ''))


frag('top', '<section><div class="wrap"><h2>必讀 Top 10</h2>'
            '<p class="sub">依「對你的 TCAD deck 的校準價值」排序，編號即優先序。</p>'
            '<div class="top">%s</div></div></section>' % ''.join(re.findall(r'<div class="titem">.*?</div></div>', top_html)[:3]))
frag('flag', '<section><div class="wrap"><h2>本次查證的修正與衝突（%d 筆）</h2>'
             '<p class="sub">CORRECTION＝確認原目錄有誤並附證據；CONFLICT＝查到的值與原目錄不同，兩說並列。</p>%s</div></section>'
     % (len(flags), ''.join(sorted(re.findall(r'<div class="fitem[^"]*">.*?</p></div>', flag_html),
                                    key=lambda x: 0 if 'conflict' in x[:40] else 1)[:4])))
sel_rows = [c for c in cards if c['id'] in ('二09', '二16', '三12', '五18', '七04')]
frag('rows', '<div class="filters"><div class="wrap">'
             '<div class="frow"><span class="flab">章別</span>%s</div>'
             '<div class="frow"><span class="flab">可引用</span>%s<span class="fsep"></span>%s</div>'
             '<div class="frow"><span class="flab">搜尋</span>'
             '<input id="q" type="search" placeholder="標題、元件、數字、DOI、期刊…">'
             '<select id="sort" class="chip"><option value="ord">依章節排序</option></select>'
             '<button class="chip" id="toggleAll">全部展開</button>'
             '<button class="chip" id="reset">清除篩選</button>'
             '<span class="count" id="cnt">5 / 5 篇</span></div></div></div>'
             '<main id="list" class="wrap">%s</main>'
     % (ch_chips, cite_chips, acc_chips, ''.join(card_html(c, i) for i, c in enumerate(sel_rows))), JS)
print('片段預覽 _frag_top / _frag_flag / _frag_rows 已產出')
print('章別', dict(cnt_ch), '| 取得', dict(cnt_acc), '| 可引用', dict(cnt_cite), '| 標記', len(flags))
