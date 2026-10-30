import re,html,json,hashlib
def segs(path):
    t=open(path,encoding='utf8',errors='replace').read()
    t=t[t.find('Le Peuple Ha'):]
    out=[];st=0;un=0;h=0
    for m in re.finditer(r'<(/?)([a-zA-Z0-9]+)[^>]*>|([^<]+)',t):
        if m.group(3) is not None:
            out.append(('T',html.unescape(m.group(3)).replace('\xa0',' '),st>0,un>0,h>0)); continue
        close,tag=m.group(1)=='/',m.group(2).lower()
        if tag in('strike','s','del'): st+=-1 if close else 1; st=max(st,0)
        elif tag=='u': un+=-1 if close else 1; un=max(un,0)
        elif tag in('h3','h4'): h+=-1 if close else 1; h=max(h,0); out.append(('B',))
        elif tag in('br','p','blockquote','center','hr','table','tr','td'): out.append(('B',))
    return out
def render(path,mode):
    # mode 'orig': keep unmarked+strike (drop u); 'new': keep unmarked+u (drop strike); 'plain': keep all
    lines=[];cur=''
    for s in segs(path):
        if s[0]=='B':
            lines.append(cur);cur='';continue
        _,x,st,un,h=s
        if mode=='orig' and un: continue
        if mode=='new' and st: continue
        if h and x.strip(): cur+=('' if not cur else ' ')+x.strip() if False else x
        else: cur+=x
    lines.append(cur)
    return lines
ART=re.compile(r'^\s*Article\s+(premier|\d+(?:\.\d+)?)\.?\s*(\(nouveau\))?\s*$',re.I)
def units(path,mode):
    # headings are h-lines; get via segs flag: rebuild with heading marks
    items=[];cur='';curh=False;mk=False
    for s in segs(path):
        if s[0]=='B':
            items.append((curh,cur,mk));cur='';curh=False;mk=False;continue
        _,x,st,un,h=s
        if (st or un) and x.strip(): mk=True
        if mode=='orig' and un: continue
        if mode=='new' and st: continue
        cur+=x; curh=curh or h
    items.append((curh,cur,mk))
    arts=[];pre=[];key=None;body=[];phase='pre';marked=False
    for h,x,mk in items:
        s=re.sub(r'\s+',' ',x).strip()
        if not s:
            if mk and key: marked=True
            continue
        m=ART.match(s)
        if m or (mk and not s and False):
            if key: arts.append((key,body,marked))
            k=m.group(1).lower(); key='1' if k=='premier' else k; body=[]; phase='art'; marked=bool(m.group(2)); continue
        if phase=='pre':
            if h and s.startswith('Titre'): phase='skip'; continue
            pre.append(x); continue
        if phase=='skip': continue
        if h and re.match(r'^(Titre|Chapitre|Section|Sous-section|Dispositions)',s): continue
        if mk: marked=True
        body.append(x)
    if key: arts.append((key,body,marked))
    return pre,arts
def paras(chunks,pre=False):
    out=[]
    for c in chunks:
        c=re.sub(r'\n(?=\s*(?:[a-z]\)|\d+\)|\d+[.-]\s))','\n\n',c)
        for p in re.split(r'\n\s*\n',c):
            p=re.sub(r'\s+',' ',p).strip()
            if not p: continue
            if re.fullmatch(r'[.;,:]+',p):
                if out: out[-1]+=p
                continue
            if pre: out+=re.split(r'(?<=[.;]) (?=Pour )',p)
            else: out.append(p)
    return out
if __name__=='__main__':
    import sys
    for path,mode in (('src/ht1987.htm','plain'),('src/ht2011.htm','orig'),('src/ht2011.htm','new')):
        pre,arts=units(path,mode); print(path,mode,len(arts),[a[0] for a in arts][:6],[a[0] for a in arts][-3:])
        print(sum(1 for a in arts if not paras(a[1])),'empty')
