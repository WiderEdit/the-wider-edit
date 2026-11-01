"""Approved personal salon-equipment story, Russian and German editions."""
import json
from html import escape
from pathlib import Path
import re

def inline(text):
 return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escape(text))

SLUG = 'ultraschall-kosmetikgeraete-preis-marketing'
DATE = '2026-11-01'


def image(lang):
 return f'assets/ultraschall-kosmetikgeraete-{lang}-ai.webp'

def path(lang):
 return f'{lang}/stories/{SLUG}/'

def load():
 return json.loads((Path(__file__).parent/'equipment.json').read_text())

def card(lang, site, preview_id=None):
 a=load()[lang]; href=site.url(path(lang))
 attr=f' id="{preview_id}" tabindex="-1" class="story-preview"' if preview_id else ''
 return f'<article class="story-card"><a class="story-image" style="display:block;position:relative;width:100%;height:0;padding-bottom:100%;overflow:hidden" href="{href}" tabindex="-1" aria-hidden="true"><img style="position:absolute;inset:0;display:block;width:100%;height:100%;object-fit:contain" src="{site.url(image(lang))}" width="1254" height="1254" alt="" loading="lazy"></a><div{attr}><p class="eyebrow">{site.TEXT[lang]["nav"][0]}</p><h2><a href="{href}">{escape(a["title"])}</a></h2><p>{escape(a["desc"])}</p><a class="textlink" href="{href}">{"Читать статью" if lang=="ru" else "Den Beitrag lesen"} ↗</a></div></article>'

def render(lang, site):
 a=load()[lang]; other='de' if lang=='ru' else 'ru'
 date='1 ноября 2026' if lang=='ru' else '1. November 2026'
 body=''.join('<h2>'+escape(b['h'])+'</h2>' if 'h' in b else '<p>'+inline(b['p'])+'</p>' for b in a['body'])
 content=f'<div class="wrap"><article class="story"><header class="story-head"><p class="eyebrow"><a href="{site.url(lang+"/business/")}">{site.TEXT[lang]["nav"][0]}</a></p><h1>{escape(a["title"])}</h1><p class="lead">{escape(a["desc"])}</p><p class="story-meta">Chris West · <time datetime="{DATE}">{date}</time> · {"Обновлено" if lang=="ru" else "Aktualisiert"}: <time datetime="{DATE}">{date}</time></p></header><figure class="story-photo beauty-photo"><img src="{site.url(image(lang))}" width="1254" height="1254" alt="{escape(a["alt"],quote=True)}" fetchpriority="high"><figcaption>{escape(a["caption"])}</figcaption></figure><div class="prose story-prose">{body}<p><em>{escape(a["note"])}</em></p><p class="story-meta">Chris West</p></div><aside class="story-note prose"><p><a href="{site.url(path(other))}" lang="{other}">{"Читать на немецком" if lang=="ru" else "Auf Russisch lesen"}</a></p><p><a href="{site.url(lang+"/business/")}">{"Другие статьи о бизнесе" if lang=="ru" else "Weitere Beiträge über Business"}</a></p></aside></article></div>'
 page=site.shell(lang,a['title'],a['desc'],content,path(lang),active='business',alternate={l:path(l) for l in ('ru','de')})
 for l in ('ru','de'):
  page=page.replace('href="'+site.url(l+'/')+'" lang="'+l+'"','href="'+site.url(path(l))+'" lang="'+l+'"')
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':a['title'],'description':a['desc'],'inLanguage':lang,'datePublished':DATE,'dateModified':DATE,'author':{'@type':'Person','name':'Chris West'},'mainEntityOfPage':site.ORIGIN+site.url(path(lang)),'image':site.ORIGIN+site.url(image(lang)),'articleSection':site.TEXT[lang]['nav'][0]}
 page=page.replace('property="og:type" content="website"','property="og:type" content="article"')
 page=page.replace('</head>','<meta property="og:image" content="'+site.ORIGIN+site.url(image(lang))+'"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head>')
 site.write(path(lang)+'index.html',page)
