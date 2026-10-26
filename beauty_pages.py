"""Render the approved bilingual personal beauty-business story."""
import json
from html import escape
from pathlib import Path

SLUG='faltenfrei-im-schlaf-professional-cosmetics'
DATE='2026-10-26'

def path(lang):
 return f'{lang}/stories/{SLUG}/'

def load():
 return json.loads((Path(__file__).parent/'beauty.json').read_text())

def card(lang, site):
 a=load()[lang]; href=site.url(path(lang))
 return f'<article class="story-card"><a class="story-image beauty-thumb" style="display:block;position:relative;width:100%;height:0;padding-bottom:100%;overflow:hidden" href="{href}" tabindex="-1" aria-hidden="true"><img style="position:absolute;inset:0;display:block;width:100%;height:100%;object-fit:contain" src="{site.url("assets/beauty-professional-ai.webp")}" width="1254" height="1254" alt="" loading="lazy"></a><div><p class="eyebrow">{site.TEXT[lang]["nav"][0]}</p><h2><a href="{href}">{escape(a["title"])}</a></h2><p>{escape(a["desc"])}</p><a class="textlink" href="{href}">{"Читать историю" if lang=="ru" else "Den Beitrag lesen"} ↗</a></div></article>'

def render(lang, site):
 a=load()[lang]; other='de' if lang=='ru' else 'ru'; date='26 октября 2026' if lang=='ru' else '26. Oktober 2026'
 paragraphs=''.join(p if p.startswith('<h2>') else '<p>'+p+'</p>' for p in a['body'])
 old=site.ARTICLES[lang]
 content=f'''<div class="wrap"><article class="story"><header class="story-head"><p class="eyebrow"><a href="{site.url(lang+'/business/')}">{site.TEXT[lang]['nav'][0]}</a></p><h1>{escape(a['title'])}</h1><p class="lead">{escape(a['desc'])}</p><p class="story-meta">Chris West · <time datetime="{DATE}">{date}</time> · {a['updated']}: <time datetime="{DATE}">{date}</time></p></header><figure class="story-photo beauty-photo"><img src="{site.url('assets/beauty-professional-ai.webp')}" width="1254" height="1254" alt="{escape(a['imageAlt'],quote=True)}" fetchpriority="high"><figcaption>{escape(a['imageCaption'])}</figcaption></figure><div class="prose story-prose">{paragraphs}<p class="story-meta">Chris West</p></div><aside class="story-note prose"><h2>{a['related']}</h2><p><a href="{site.url(site.article_path(lang))}">{escape(old['title'])}</a></p><p><a href="{site.url(path(other))}" lang="{other}">{'Читать эту статью на немецком' if lang=='ru' else 'Diesen Beitrag auf Russisch lesen'}</a></p></aside></article></div>'''
 page=site.shell(lang,a['title'],a['desc'],content,path(lang),active='business',alternate={l:path(l) for l in ('ru','de')})
 page=page.replace('property="og:type" content="website"','property="og:type" content="article"')
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':a['title'],'description':a['desc'],'inLanguage':lang,'datePublished':DATE,'dateModified':DATE,'author':{'@type':'Person','name':'Chris West'},'mainEntityOfPage':site.ORIGIN+site.url(path(lang)),'image':site.ORIGIN+site.url('assets/beauty-professional-ai.webp'),'articleSection':site.TEXT[lang]['nav'][0]}
 page=page.replace('</head>','<meta property="og:image" content="'+site.ORIGIN+site.url('assets/beauty-professional-ai.webp')+'"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head>')
 site.write(path(lang)+'index.html',page)
