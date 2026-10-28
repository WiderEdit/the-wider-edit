"""Check generated pages, internal links and launch privacy boundaries."""
from pathlib import Path
from html.parser import HTMLParser
import json
from urllib.parse import urlparse

root=Path(__file__).parent/'docs'
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.tags=[]; self.h1=0; self.scripts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); self.tags.append((tag,a))
  if tag=='h1': self.h1+=1

pages=list(root.rglob('*.html'))
for f in pages:
 p=Page(); text=f.read_text(); p.feed(text)
 assert p.h1==1,(f,'expected one h1')
 assert '<html lang=' in text
 assert 'name="description"' in text
 assert 'rel="canonical"' in text
 for tag,a in p.tags:
  assert tag not in ('form','iframe'),(f,tag)
  for attr in ('href','src'):
   link=a.get(attr,'')
   if link.startswith('/the-wider-edit/'):
    target=root/urlparse(link).path.removeprefix('/the-wider-edit/')
    if urlparse(link).path.endswith('/'): target=target/'index.html'
    assert target.is_file(),(f,link)
   if tag=='a' and urlparse(link).scheme in ('http','https'):
    assert a.get('target')=='_blank',(f,link)
    assert 'noopener' in a.get('rel','')
  if tag in ('script','img','link') and a.get('src',a.get('href','')).startswith('http'):
   assert (tag=='link' and a.get('rel') in ('canonical','alternate')) or (tag=='script' and a.get('src')=='https://gc.zgo.at/count.js' and a.get('data-goatcounter')=='https://the-wider-edit.goatcounter.com/count'),(f,'unexpected external dependency')
 assert 'localStorage' not in text and 'sessionStorage' not in text
 assert 'Anna' not in text and 'Trocka' not in text
print(f'PASS: {len(pages)} pages; headings, metadata, local links, external-link safety, privacy boundaries.')
print('Public payload:',sum(f.stat().st_size for f in root.rglob('*') if f.is_file()),'bytes')
