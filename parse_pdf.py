# -*- coding: utf-8 -*-
"""
階段 1：從來源 PDF 解析出 87 筆工作清單。

  FinFET_SHE_saturation_Ion_121papers (3).pdf
    -> _121papers_fulltext.txt   PDF 全文（UTF-8；PDF 內中文用一般方式讀會亂碼，必須經 PyMuPDF）
    -> _sections.json            第二/三/四/五/七章的原始文字（第六章依指示排除）
    -> _worklist.json            87 筆結構化條目
    -> _items.json               餵給查證 agent 的精簡版
    -> WORKLIST.md               人可讀的對數表

用法：python parse_pdf.py        （需要 PyMuPDF：pip install pymupdf）

三個 PDF 解析陷阱（本檔已處理，重跑請勿移除）：
  1. 硬換行會切斷 DOI，例如 "10.1109/ted.2020.29978" + 換行 + "48"
  2. 五35 的識別碼是 IEEE Xplore URL 而非 DOI（該文確實沒有註冊 DOI）
  3. 查證狀態欄也會被換行切開，例如 "value_corr" + 換行 + "ected"
"""
import io, os, re, sys, json, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
BASE = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(BASE, *a)
PDF = 'FinFET_SHE_saturation_Ion_121papers (3).pdf'

# 章別 -> (標題關鍵字, 分類名, 原表篇數)
HEADS = [('二、電熱', '二', 'ET-vs-ISO｜矽 FinFET', 16),
         ('三、電熱', '三', 'ET-vs-ISO｜nanosheet/GAA', 14),
         ('四、量測', '四', '量測 pulsed-vs-DC / TRE', 8),
         ('五、熱阻', '五', '熱阻 Rth / ΔT', 45),
         ('六、可靠度', '六', '可靠度／其他指標（排除）', 34),
         ('七、環境溫度', '七', 'ta_sweep（非 SHE）', 4)]
KEEP = ['二', '三', '四', '五', '七']          # 第六章依指示完全排除

ANCHOR = re.compile(r'\(\s*(IEEE|非)\s*,\s*(.{2,200}?)\)\s*DOI:\s*', re.S)
VERD = re.compile(r'(confirmed|CONFIRMED|plausible_\s*unveri\w*|reclassifie\s*d\w*|value_corr\s*\w*)')
DOI_OK = re.compile(r'^(10\.\d{4,9}/\S+|https?://arxiv\.org/abs/\S+|https?://\S+/\d+)$')


def extract_text():
    """PDF -> UTF-8 純文字。已存在則沿用。"""
    if os.path.exists(P('_121papers_fulltext.txt')):
        return open(P('_121papers_fulltext.txt'), encoding='utf-8').read()
    import fitz                                   # PyMuPDF
    doc = fitz.open(P(PDF))
    t = ''.join(page.get_text() for page in doc)
    open(P('_121papers_fulltext.txt'), 'w', encoding='utf-8').write(t)
    print('抽取 %d 頁，%d 字元' % (doc.page_count, len(t)))
    return t


def split_sections(t):
    """去掉重複頁首與表頭後，依章切段。"""
    t = re.sub(r'FinFET SHE 飽和區 Ion 下降 % 文獻目錄（121 篇）\n第 \d+ 頁\n', '', t)
    t = re.sub(r'論文 / IEEE / 年 / DOI\n元件\n[^\n]*\n[^\n]*\n查證\n', '', t)
    pos = [t.find(h[0]) for h in HEADS] + [t.find('資料來源：')]
    assert all(p > 0 for p in pos), '章節標題定位失敗，PDF 版本可能不同'
    return {h[1]: t[pos[i]:pos[i + 1]] for i, h in enumerate(HEADS)}


def grab_doi(txt):
    """抓 DOI 並合併被硬換行切斷的續行（陷阱 1、2）。"""
    lines = txt.split('\n')
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    doi, j = lines[i].strip(), i + 1
    while j < len(lines):
        n = lines[j].strip()
        # 續行條件：無空白、無中文、僅 DOI 合法字元，且看起來是被切斷的尾段
        if (n and ' ' not in n and not re.search(r'[一-鿿]', n)
                and re.fullmatch(r'[0-9A-Za-z./\-_()]+', n)
                and (n.isdigit() or ('.' in n and '/' not in n) or re.match(r'^[a-z]+\d', n))):
            doi += n
            j += 1
        else:
            break
    # 仍不成格式 -> 再放寬接一行（處理五35 的 IEEE Xplore URL）
    if not DOI_OK.match(doi) and j < len(lines):
        n = lines[j].strip()
        if (n and ' ' not in n and not re.search(r'[一-鿿]', n)
                and re.fullmatch(r'[0-9A-Za-z./\-_()]+', n)):
            doi += n
            j += 1
    return doi, '\n'.join(lines[j:])


def first_title(pre):
    """該章第一筆的標題：切掉章節標題與前言。"""
    p = re.sub(r'\s+', ' ', pre).strip()
    for sep in ['。', '）']:
        if sep in p:
            return p.rsplit(sep, 1)[-1].strip()
    return p


def parse(secs):
    wl = []
    for _, ch, sec, n in HEADS:
        if ch not in KEEP:
            continue
        seg = secs[ch]
        ms = list(ANCHOR.finditer(seg))
        assert len(ms) == n, '第%s章解析出 %d 筆，原表為 %d 筆' % (ch, len(ms), n)
        recs = []
        for i, m in enumerate(ms):
            nxt = ms[i + 1].start() if i + 1 < len(ms) else len(seg)
            doi, rest = grab_doi(seg[m.end():nxt])
            vs = list(VERD.finditer(rest))          # 取最後一個＝欄位值（內文也會出現 confirmed）
            if vs:
                body, verd, tail = rest[:vs[-1].start()], vs[-1].group(), rest[vs[-1].end():]
            else:
                body, verd, tail = rest, '?', ''
            recs.append((doi, m.group(1), re.sub(r'\s+', ' ', m.group(2)).strip(),
                         re.sub(r'\s+', ' ', body).strip(), re.sub(r'\s+', '', verd),
                         re.sub(r'\s+', ' ', tail).strip(), m.start()))
        for i, r in enumerate(recs):
            wl.append(dict(id='%s%02d' % (ch, i + 1), ch=ch, sec=sec, idx=i + 1, doi=r[0],
                           ieee=r[1], year=r[2], verdict=r[4], body=r[3],
                           title=first_title(seg[:r[6]]) if i == 0 else recs[i - 1][5]))
    return wl


def verify(wl):
    ok = True
    got = collections.Counter(w['ch'] for w in wl)
    for _, ch, _, n in HEADS:
        if ch in KEEP and got[ch] != n:
            print('!! 第%s章 %d != %d' % (ch, got[ch], n)); ok = False
    dup = [k for k, v in collections.Counter(w['doi'] for w in wl).items() if v > 1]
    bad = [w['id'] for w in wl if not DOI_OK.match(w['doi'])]
    resid = [w['id'] for w in wl if re.match(r'^(ected|ed|fied|veri|d)\b', w['title'])]
    for label, arr in (('重複 DOI', dup), ('DOI 格式異常', bad), ('標題殘留查證狀態', resid)):
        if arr:
            print('!! %s：%s' % (label, arr)); ok = False
    print('合計 %d 筆｜%s｜%s' % (len(wl), dict(got),
                                  dict(collections.Counter(w['verdict'] for w in wl))))
    return ok


if __name__ == '__main__':
    secs = split_sections(extract_text())
    json.dump(secs, open(P('_sections.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    wl = parse(secs)
    if not verify(wl):
        sys.exit('解析未通過驗證，請先排除上列問題再繼續')

    json.dump(wl, open(P('_worklist.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    items = [{k: w[k] for k in ('id', 'doi', 'ieee', 'year', 'title', 'verdict')} |
             {'orig': w['body'][:420]} for w in wl]
    json.dump(items, open(P('_items.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

    md = ['# WORKLIST — 87 篇逐篇深度介紹工作清單', '',
          '來源：`%s`｜排除第六章（可靠度／其他指標 34 篇）' % PDF, '',
          '篇數對數：二 16 + 三 14 + 四 8 + 五 45 + 七 4 = **87**（實際解析 %d 筆，DOI 全唯一）' % len(wl), '',
          '| # | 章 | 分類 | DOI／識別 | 來源 | 年 | 原表查證 | PDF 內截斷標題 |',
          '|---|---|---|---|---|---|---|---|']
    md += ['| %s | %s | %s | `%s` | %s | %s | %s | %s |'
           % (w['id'], w['ch'], w['sec'], w['doi'], w['ieee'], w['year'][:24], w['verdict'], w['title'][:80])
           for w in wl]
    open(P('WORKLIST.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print('已產出 _sections.json / _worklist.json / _items.json / WORKLIST.md')
