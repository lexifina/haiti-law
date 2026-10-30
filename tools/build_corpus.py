import json,hashlib,re
from parse import units,paras
def key(k):
    a=k.split('.'); return 'art-%03d'%int(a[0])+''.join('-%02d'%int(x) for x in a[1:])
def label(k): return 'Art. '+k
def U(k,ps,head=None):
    return {'label':label(k) if head is None else head,'kind':'art' if head is None else 'preamble','text':'# '+('Article '+k if head is None else head)+'\n'+''.join(p+'\n' for p in ps)}
pre87,a87=units('src/ht1987.htm','plain')
_,anew=units('src/ht2011.htm','new')
v1={'preambule':U('', paras(pre87,True),'Préambule')}
for k,b,m in a87: v1[key(k)]=U(k,paras(b))
v1_by={k:b for k,b,m in a87}
v2={};
pre11,_x=units('src/ht2011.htm','new')
v2['preambule']=U('',paras(pre11,True),'Préambule')
if v2['preambule']['text']!=v1['preambule']['text']: print('PREAMBLE DIFF')
for k,b,m in anew:
    ps=paras(b)
    if not ps: continue
    if k in v1_by and not m: ps=paras(v1_by[k])
    v2[key(k)]=U(k,ps)
changes={}
for k,u in v2.items():
    if v1.get(k)!=u: changes[k]=u
for k in v1:
    if k not in v2: changes[k]=None
print(len(v1),len(v2),len(changes),'removed',[k for k,v in changes.items() if v is None])
sha=lambda p:hashlib.sha256(open(p,'rb').read()).hexdigest()
H='https://mjp.univ-perp.fr/constit/'
credits={k:['amendement-2011'] for k in changes}
corpus={
 'country':{'code':'HT','name':'Haiti','slug':'haiti','lang':'fr','tz':'America/Port-au-Prince','future_branch':'future',
  'publisher':{'name':'Digithèque MJP, Université de Perpignan (copie de tiers)','email':'mjp@univ-perp.invalid'},
  'default_in_force_rule':{'text':'Constitution du 29 mars 1987, art. 298: elle entre en vigueur dès sa publication au Moniteur.','source':H+'ht1987.htm'},
  'licence_note':'Third-party copy: the bytes come from the Digithèque of Jean-Pierre Maury (mjp.univ-perp.fr). Haiti copyright Decree of 12 October 2005, art. 5: official legislative texts are not protected.'},
 'sources':[{'name':'Digithèque de matériaux juridiques et politiques (MJP), Université de Perpignan: Haïti, Constitution 1987','url':H+'ht1987.htm','retrieved':'2026-10-30','licence':'Third-party copy of an official text; see LICENSE (Haiti copyright Decree of 2005, art. 5).','notes':'Original 1987 text, from the brochure Constitution de la République d\'Haïti, 29 mars 1987.'},
  {'name':'Digithèque MJP: Haïti, Constitution 1987 amendée (Moniteur extraordinaire du 19 juin 2012)','url':H+'ht2011.htm','retrieved':'2026-10-30','licence':'As above.','notes':'Marked version: struck-through words repealed, underlined words new.'}],
 'laws':{
  'constitution-1987':{'label':'Constitution du 29 mars 1987','title':'Constitution de la République d\'Haïti','kind':'referendum','enacted':'1987-03-10','published':'1987-03-29','url':H+'ht1987.htm','temporary_until':None,'restores':None,'note':None},
  'amendement-2011':{'label':'Loi constitutionnelle portant amendement de la Constitution de 1987 (2011)','title':'Amendement de la Constitution de 1987, texte corrigé publié au Moniteur du 19 juin 2012','kind':'law','enacted':'2011-05-09','published':'2012-06-19','url':H+'ht2011.htm','temporary_until':None,'restores':None,'note':None}},
 'acts':[{'slug':'constitution','short':'CONST','title':'Constitution de la République d\'Haïti (1987)','url':H+'ht2011.htm','first_law':'constitution-1987','earlier_laws':[],
   'versions':[{'from':'1987-03-29','source_url':H+'ht1987.htm','sha256':sha('src/ht1987.htm'),'units':v1,'credits':{}},
    {'from':'2012-06-19','source_url':H+'ht2011.htm','sha256':sha('src/ht2011.htm'),'changes':changes,'credits':credits,'note':'Text as amended, from the marked page: struck words dropped, underlined words kept.'}]}],
 'applies':[],
 'decisions':[
  'The text is a third-party copy from the MJP digital library (Université de Perpignan); the national copyright act (Decree of 12 October 2005, art. 5 para. 1) excludes official legislative texts from protection. Titles, chapters and sections headings of the Constitution are left out; each article is a unit.',
  'The 1987 version is the original text from the host page ht1987.htm, dated 1987-03-29 (ratification by referendum; in force on publication in Le Moniteur, art. 298).',
  'The amended version is dated 2012-06-19, the Moniteur extraordinaire that published the corrected text of the 2011 constitutional amendment (the first, flawed publication of 13 May 2011 is not used). It is read from the host page ht2011.htm, which marks repealed words with strike-through and new words with underline: struck words are dropped and underlined words kept.',
  'Articles the host page leaves unmarked keep the 1987 text taken from ht1987.htm, so that small differences between the host\'s two pages (for example silent spelling corrections) are not credited to the amendment. Articles the 2011 page leaves wholly struck were removed.',
  'The host notes that the 2012 text leaves articles 63, 68, 78, 90.1, 92, 92.1, 92.3, 95, 218, 264 and 267.2 as in 1987 (mandate lengths of 4 years); the page\'s own text is followed.',
  'The host page is itself unofficial; the official source is Le Moniteur, which is not online. Check against Le Moniteur for anything that matters.'],
 'ai_use':['none']}
json.dump(corpus,open('corpus.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
