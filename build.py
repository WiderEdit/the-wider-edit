"""Build the bilingual, dependency-free personal blog. Run: python3 build.py."""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).parent
OUT = ROOT / 'docs'
BASE = '/the-wider-edit/'
ORIGIN = 'https://wideredit.github.io'
LAW = 'https://matsne.gov.ge/en/document/view/16198'

TEXT = {
 'ru': dict(label='Частный блог из Грузии', nav=['Бизнес','Отдых','Здоровье'], about='О блоге и авторе', skip='К содержанию', home='Главная',
 title='Свой бизнес.<br>Своя жизнь.<br><em>Свой взгляд.</em>', description='Как работать, отдыхать и заботиться о себе: личный опыт, полезные открытия и мнение с характером.',
 kicker='Личный опыт. Широкий взгляд.', caption='Иногда, чтобы увидеть больше, нужно сменить точку зрения.', sections='Три стороны одной жизни', sub='Не только дела. Не только отдых. Всё, из чего складывается жизнь.',
 intros=['О решениях, людях и обещаниях. Личный взгляд на маркетинг, технологии и жизнь собственного дела.', 'Поездки, отели, рестораны и маленькие открытия. О том, как переключаться и получать удовольствие от жизни.', 'О внимании к себе, самочувствии и привычках. Собственный опыт и вопросы, которые хочется изучить глубже.'],
 enter='В раздел', edition='Русская версия', ednote='Русская и немецкая версии — самостоятельные подборки. Некоторые тексты могут отличаться или выходить только на одном языке.',
 soon='Первые истории ещё впереди', soontext='Блог только начинается. Здесь появится самая новая публикация — из личного опыта, с собственной точкой зрения.',
 empty='Здесь скоро появятся первые публикации.', emptytext='Пока этот раздел открыт с чистого листа. Истории добавляются после подготовки и проверки.',
 quote='Интересное начинается там,<br>где перестаёшь смотреть по привычке.', qlabel='The Wider Edit · Chris West', back='Вернуться на главную', written='Chris West · личный блог',
 aboutintro='Опыт за плечами.<br><em>Любопытство впереди.</em>',
 bio=['Место рождения автора — территория бывшего Советского Союза. Ещё в детстве автор начал жить в Германии. За этим последовали 35 лет, собственный бизнес и немало опыта, который не получишь из учебников.',
 'Теперь дом автора — Грузия. Здесь можно жить, наслаждаться жизнью и продолжать замечать интересное вокруг. Бизнес остался в прошлом, но интерес к нему никуда не исчез: автор по-прежнему следит за тенденциями, наблюдает за решениями компаний и тем, как они относятся к своим клиентам.',
 'Автор много путешествует, занимается своим здоровьем и делится здесь впечатлениями, находками и мыслями. Иногда с юмором, иногда резко — как подсказывает собственный опыт.'],
 pseudo='Chris West — псевдоним автора. Право использовать псевдоним вместо настоящего имени или не указывать имя предусмотрено статьёй 17(1)(b) закона Грузии «Об авторском праве и смежных правах».', law='Текст закона на Matsne',
 principles='Как устроен блог', principletext='Здесь публикуются личные впечатления, наблюдения и мысли. Собственный опыт отделяется от внешних сведений, а мнение — от проверяемых фактов. Если текст опирается на внешний источник, рядом будет ссылка. На старте здесь нет рекламы, платных услуг, комментариев и форм обратной связи.'),
 'de': dict(label='Ein privater Blog aus Georgien', nav=['Business','Auszeit','Gesundheit'], about='Über den Blog und die Person dahinter', skip='Zum Inhalt', home='Startseite',
 title='Das eigene Business.<br>Das eigene Leben.<br><em>Der eigene Blick.</em>', description='Über Arbeit, Auszeiten und die Kunst, auf sich zu achten. Persönliche Erfahrungen, gute Entdeckungen und eine Meinung mit Ecken und Kanten.',
 kicker='Persönliche Erfahrungen. Neue Perspektiven.', caption='Manchmal sieht man mehr, wenn man den Blickwinkel verändert.', sections='Drei Seiten des Lebens', sub='Arbeit, die bewegt. Pausen, die guttun. Ein Leben, das zusammenpasst.',
 intros=['Über Entscheidungen, Menschen und große Versprechen. Ein persönlicher Blick auf Marketing, Technologie und das Leben mit einem eigenen Unternehmen.', 'Reisen, Hotels, Restaurants und kleine Entdeckungen. Über das Abschalten und die Freude daran, Neues zu erleben.', 'Über Wohlbefinden, Gewohnheiten und einen achtsamen Umgang mit sich selbst. Persönliche Erfahrungen und Fragen, die einen zweiten Blick verdienen.'],
 enter='Zum Bereich', edition='Deutsche Ausgabe', ednote='Die deutsche und die russische Ausgabe haben eine eigene Themenauswahl. Manche Texte unterscheiden sich oder erscheinen nur in einer Sprache.',
 soon='Die ersten Geschichten kommen noch', soontext='Dieser Blog steht am Anfang. Hier wird der neueste Beitrag erscheinen — persönlich erlebt und mit einem eigenen Standpunkt.',
 empty='Hier erscheinen bald die ersten Beiträge.', emptytext='Dieser Bereich beginnt mit einem unbeschriebenen Blatt. Beiträge werden nach Vorbereitung und Prüfung ergänzt.',
 quote='Spannend wird es dort,<br>wo der gewohnte Blick aufhört.', qlabel='The Wider Edit · Chris West', back='Zurück zur Startseite', written='Chris West · privater Blog',
 aboutintro='Erfahrung im Gepäck.<br><em>Neugier im Blick.</em>',
 bio=['Die Lebensgeschichte hinter Chris West beginnt auf dem Gebiet der ehemaligen Sowjetunion. Noch in der Kindheit führte der Weg nach Deutschland. Es folgten 35 Jahre, ein eigenes Unternehmen und reichlich Erfahrungen, die in keinem Lehrbuch stehen.',
 'Heute ist Georgien das Zuhause. Ein Ort, um das Leben zu genießen und aufmerksam zu bleiben für das, was um einen herum passiert. Das eigene Unternehmen gehört der Vergangenheit an. Das Interesse an Wirtschaft ist geblieben: an neuen Entwicklungen, an Entscheidungen von Unternehmen und daran, wie sie mit ihrer Kundschaft umgehen.',
 'Reisen, die eigene Gesundheit und die Freude an Entdeckungen prägen den Alltag. Daraus entstehen die Eindrücke, Gedanken und Geschichten dieses Blogs. Mal mit Humor, mal mit einer klaren Kante — so, wie es die persönliche Erfahrung nahelegt.'],
 pseudo='Chris West ist ein Pseudonym. Das Recht, ein Pseudonym anstelle des eigenen Namens zu verwenden oder auf eine Namensnennung zu verzichten, ist in Artikel 17 Absatz 1 Buchstabe b des georgischen Gesetzes über das Urheberrecht und verwandte Schutzrechte vorgesehen.', law='Gesetzestext auf Matsne',
 principles='Wie dieser Blog funktioniert', principletext='Hier geht es um persönliche Eindrücke, Beobachtungen und Gedanken. Eigene Erfahrungen werden von Angaben aus anderen Quellen unterschieden, Meinungen von überprüfbaren Tatsachen. Externe Informationen erhalten einen Quellenlink. Zum Start gibt es keine Werbung, kostenpflichtigen Leistungen, Kommentare oder Kontaktformulare.')
}
SLUGS = ['business','leisure','health']

def write(path, content):
 p = OUT / path
 p.parent.mkdir(parents=True, exist_ok=True)
 p.write_text(content, encoding='utf-8')

def url(path=''):
 return BASE + path

def shell(lang, title, desc, body, path, active='', alternate=None, noindex=False):
 t = TEXT[lang]
 other = 'de' if lang=='ru' else 'ru'
 nav=''.join(f'<a href="{url(lang+"/"+s+"/")}"'+(' aria-current="page"' if active==s else '')+f'>{t["nav"][i]}</a>' for i,s in enumerate(SLUGS))
 alts = ''
 if alternate:
  alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{ORIGIN}{url(p)}">' for l,p in alternate.items())
 schema = {'@context':'https://schema.org','@type':'WebPage','name':title,'url':ORIGIN+url(path),'inLanguage':lang,'isPartOf':{'@type':'WebSite','name':'The Wider Edit','url':ORIGIN+BASE}}
 return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)} · The Wider Edit</title><meta name="description" content="{escape(desc,quote=True)}"><meta name="theme-color" content="#153e34"><link rel="canonical" href="{ORIGIN}{url(path)}">{alts}<meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN}{url(path)}"><meta property="og:site_name" content="The Wider Edit"><link rel="icon" href="{url('assets/mark.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{url('assets/site.css')}">{'<meta name="robots" content="noindex,follow">' if noindex else ''}<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><a class="skip" href="#main">{t['skip']}</a><header class="header"><div class="wrap top"><a class="brand" href="{url(lang+'/')}" aria-label="The Wider Edit — {t['home']}">The Wider Edit<span class="brand-dot">.</span></a><div class="edition"><span>{t['label']}</span><div class="languages" aria-label="Language"><a href="{url('ru/')}" lang="ru" {'aria-current="true"' if lang=='ru' else ''}>RU</a><span>/</span><a href="{url('de/')}" lang="de" {'aria-current="true"' if lang=='de' else ''}>DE</a></div></div></div><div class="wrap navrow"><nav aria-label="{'Разделы' if lang=='ru' else 'Themen'}">{nav}</nav><span class="navnote">A PERSONAL POINT OF VIEW</span></div></header>
<main id="main">{body}</main><footer><div class="wrap footer-main"><a class="footer-brand" href="{url(lang+'/')}">The Wider Edit.</a><p>{t['written']}</p><nav aria-label="{'Информация' if lang=='ru' else 'Information'}"><a href="{url(lang+'/about/')}">{t['about']}</a><a href="{url('impressum/')}" lang="de">Impressum</a><a href="{url('datenschutz/')}" lang="de">Datenschutz</a></nav></div><div class="wrap footer-bottom"><span>© 2026 The Wider Edit</span><span>GEORGIA · A WIDER POINT OF VIEW</span></div></footer></body></html>'''

def home(lang):
 t=TEXT[lang]
 cards=''.join(f'<section class="topic"><span class="number">0{i+1}</span><h3>{t["nav"][i]}</h3><p>{t["intros"][i]}</p><a class="textlink" href="{url(lang+"/"+s+"/")}">{t["enter"]}<span aria-hidden="true">↗</span></a></section>' for i,s in enumerate(SLUGS))
 body=f'''<div class="wrap"><section class="hero"><div class="hero-copy"><p class="eyebrow">{t['kicker']}</p><h1>{t['title']}</h1><p class="lead">{t['description']}</p><div class="signature"><span class="signature-line"></span>Chris West</div></div><figure class="hero-art"><img src="{url('assets/landscape.svg')}" width="780" height="860" alt="{'Иллюстрация: горы, деревья и терраса с видом на долину' if lang=='ru' else 'Illustration: Berge, Bäume und eine Terrasse mit Blick ins Tal'}"><figcaption>{t['caption']}</figcaption></figure></section>
<section class="section-intro"><span class="eyebrow">THE EDIT / 01—03</span><div><h2>{t['sections']}</h2><p>{t['sub']}</p></div></section><div class="topics">{cards}</div>
<section class="coming"><div><span class="eyebrow">{'Новая публикация' if lang=='ru' else 'Der nächste Beitrag'}</span><h2>{t['soon']}</h2></div><p>{t['soontext']}</p></section></div>
<aside class="quote"><div class="wrap"><p>{t['quote']}</p><span>{t['qlabel']}</span></div></aside><div class="wrap edition-note"><strong>{t['edition']}</strong><p>{t['ednote']}</p></div>'''
 path=lang+'/'
 write(path+'index.html',shell(lang,'The Wider Edit — '+t['kicker'],t['description'],body,path,alternate={'ru':'ru/','de':'de/','x-default':''}))

def section(lang,i):
 t=TEXT[lang]; s=SLUGS[i]; path=f'{lang}/{s}/'
 body=f'''<div class="wrap"><div class="breadcrumb"><a href="{url(lang+'/')}">{t['home']}</a><span>/</span>{t['nav'][i]}</div><section class="page-hero"><span class="eyebrow">THE EDIT / 0{i+1}</span><h1>{t['nav'][i]}<span class="olive-dot">.</span></h1><p class="lead">{t['intros'][i]}</p></section><section class="empty"><span class="empty-symbol" aria-hidden="true">✳</span><h2>{t['empty']}</h2><p>{t['emptytext']}</p><a class="textlink" href="{url(lang+'/')}">{t['back']}<span aria-hidden="true">←</span></a></section><div class="edition-note"><strong>{t['edition']}</strong><p>{t['ednote']}</p></div></div>'''
 write(path+'index.html',shell(lang,t['nav'][i],t['intros'][i],body,path,active=s,noindex=True))

def about(lang):
 t=TEXT[lang]; path=f'{lang}/about/'
 body=f'''<div class="wrap"><div class="breadcrumb"><a href="{url(lang+'/')}">{t['home']}</a><span>/</span>{t['about']}</div><section class="about-layout"><div class="about-heading"><span class="eyebrow">CHRIS WEST / THE WIDER EDIT</span><h1>{t['aboutintro']}</h1><div class="monogram" aria-hidden="true">CW<span>GEORGIA</span></div></div><div class="prose about-copy">{''.join('<p>'+p+'</p>' for p in t['bio'])}<h2>{t['principles']}</h2><p>{t['principletext']}</p><aside class="legal-note"><p>{t['pseudo']}</p><a class="textlink" href="{LAW}" target="_blank" rel="noopener noreferrer">{t['law']} <span aria-hidden="true">↗</span></a></aside></div></section></div>'''
 write(path+'index.html',shell(lang,t['about'],t['bio'][0],body,path,alternate={'ru':'ru/about/','de':'de/about/'}))

def legal():
 imprint='''<section lang="de"><span class="eyebrow">DEUTSCH</span><h2>Über dieses Angebot</h2><p>The Wider Edit ist ein privater, nichtkommerzieller Blog aus Georgien. Hier erscheinen persönliche Erfahrungen, Beobachtungen und Gedanken unter dem Pseudonym Chris West.</p><p>Der Blog enthält keine Werbung, bietet keine kostenpflichtigen Leistungen an und erhält keine Vergütung für die gesetzten Links.</p><h2>Veröffentlichung unter Pseudonym</h2><p>Die Verwendung eines Pseudonyms anstelle des eigenen Namens sowie der Verzicht auf eine Namensnennung sind in Artikel 17 Absatz 1 Buchstabe b des georgischen Gesetzes über das Urheberrecht und verwandte Schutzrechte vorgesehen.</p><p><a href="https://matsne.gov.ge/en/document/view/16198" target="_blank" rel="noopener noreferrer">Gesetzestext auf dem offiziellen georgischen Gesetzesportal Matsne ↗</a></p></section>
<section lang="ka" class="georgian"><span class="eyebrow">ქართული</span><h2>სამართლებრივი ინფორმაცია</h2><p>The Wider Edit არის საქართველოდან წარმოებული პირადი, არაკომერციული ბლოგი. აქ Chris West-ის ფსევდონიმით ქვეყნდება პირადი გამოცდილება, დაკვირვებები და მოსაზრებები.</p><p>ბლოგი არ შეიცავს რეკლამას, არ სთავაზობს ფასიან მომსახურებას და არ იღებს ანაზღაურებას განთავსებული ბმულებისთვის.</p><h2>ფსევდონიმით გამოქვეყნება</h2><p>საკუთარი სახელის ნაცვლად ფსევდონიმის გამოყენების, აგრეთვე სახელის მითითებაზე უარის თქმის უფლება გათვალისწინებულია საქართველოს კანონის „საავტორო და მომიჯნავე უფლებების შესახებ“ მე-17 მუხლის პირველი პუნქტის „ბ“ ქვეპუნქტით.</p><p><a href="https://matsne.gov.ge/ka/document/view/16198" target="_blank" rel="noopener noreferrer">კანონის ტექსტი საქართველოს საკანონმდებლო მაცნეზე ↗</a></p></section>'''
 privacy='''<p class="intro-text">Diese Website ist ein privater Blog. Sie verwendet keine Analyse- oder Werbedienste und bietet keine Registrierung, Kommentarfunktion oder Kontaktformulare an.</p>
<h2>1. Technische Bereitstellung durch GitHub Pages</h2><p>Der Blog wird über GitHub Pages bereitgestellt. Beim Besuch einer GitHub-Pages-Website wird die IP-Adresse des Besuchs laut GitHub aus Sicherheitsgründen protokolliert und gespeichert. Dies gilt auch ohne Anmeldung bei GitHub. Die Bereitstellung erfolgt somit nicht ohne technische Verarbeitung personenbezogener Daten.</p><p>Weitere Informationen über die Verarbeitung durch GitHub, die Speicherdauer, internationale Übermittlungen und die dort beschriebenen Datenschutzrechte finden Sie in den Informationen des Hostinganbieters:</p><ul><li><a href="https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection" target="_blank" rel="noopener noreferrer">GitHub Pages: Data collection ↗</a></li><li><a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener noreferrer">GitHub General Privacy Statement ↗</a></li></ul><p>Der Blog führt keine eigene Besucherdatenbank und verwendet keine eigenen Zugriffsprotokolle zur Auswertung des Besuchsverhaltens.</p>
<h2>2. Keine Analyse, Werbung oder Profilbildung</h2><p>Es werden keine Analyse-Pixel, Werbenetzwerke, Sitzungsaufzeichnungen oder Verfahren zur Erstellung von Nutzungsprofilen eingesetzt. Der Blog setzt keine eigenen Cookies und speichert keine Besuchsdaten im lokalen Browserspeicher.</p>
<h2>3. Bilder, Schriften und Sprache</h2><p>Die Website verwendet Systemschriften und lokal bereitgestellte Grafiken. Es sind keine externen Schriftendienste, Karten, Video-Player oder Social-Media-Widgets eingebettet.</p><p>Auf der Einstiegsseite wird die vom Browser bereitgestellte Sprache ausschließlich im Browser ausgewertet: Deutsch führt zur deutschen Ausgabe, andere Sprachen zur russischen Ausgabe. Es wird dafür kein Sprachprofil gespeichert und kein gesonderter Sprachdienst aufgerufen. Über RU und DE können Sie die Ausgabe wechseln.</p>
<h2>4. Links zu anderen Websites</h2><p>Externe Links werden erst aufgerufen, wenn Sie darauf klicken, und öffnen sich in einem neuen Tab. Auf der Zielseite gelten die Datenschutzinformationen des jeweiligen Anbieters. Der Blog erhält keine Vergütung für diese Links.</p>
<h2>5. Änderungen</h2><p>Diese Informationen beschreiben die gegenwärtige technische Gestaltung. Werden später weitere Funktionen eingeführt, werden die Hinweise entsprechend angepasst.</p><p class="legal-date">Stand: 23. Oktober 2026</p>'''
 for path,title,content,desc in [('impressum/','Impressum',imprint,'Informationen zum privaten Blog The Wider Edit, auf Deutsch und Georgisch.'),('datenschutz/','Datenschutz',privacy,'Hinweise zur technischen Datenverarbeitung beim Besuch von The Wider Edit.')]:
  body=f'<div class="wrap legal-wrap"><span class="eyebrow">THE WIDER EDIT / INFORMATION</span><h1>{title}</h1><div class="prose">{content}</div></div>'
  write(path+'index.html',shell('de',title,desc,body,path))

if __name__ == '__main__':
 for l in TEXT:
  home(l); about(l)
  for i in range(3): section(l,i)
 legal()
 write('index.html','''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>The Wider Edit — RU / DE</title><meta name="description" content="The Wider Edit — личный блог Chris West из Грузии. Ein privater Blog von Chris West aus Georgien."><link rel="canonical" href="https://wideredit.github.io/the-wider-edit/"><link rel="alternate" hreflang="ru" href="https://wideredit.github.io/the-wider-edit/ru/"><link rel="alternate" hreflang="de" href="https://wideredit.github.io/the-wider-edit/de/"><link rel="alternate" hreflang="x-default" href="https://wideredit.github.io/the-wider-edit/"><link rel="stylesheet" href="assets/site.css"><script src="assets/language.js" defer></script></head><body><main class="wrap language-page"><p class="eyebrow">A PERSONAL POINT OF VIEW</p><h1>The Wider Edit.</h1><p>Chris West · Georgia</p><nav aria-label="Language"><a href="ru/" lang="ru">Читать по-русски ↗</a><a href="de/" lang="de">Auf Deutsch lesen ↗</a></nav></main></body></html>''')
 write('assets/language.js',"'use strict';\nconst language=(navigator.language||'ru').toLowerCase().startsWith('de')?'de':'ru';\nlocation.replace(new URL(language+'/',location.href).href);\n")
 write('404.html',shell('ru','Страница не найдена','Эта страница недоступна.',f'<div class="wrap page-hero"><span class="eyebrow">404</span><h1>Здесь чистый лист.</h1><p class="lead">Страница не найдена или больше недоступна.</p><a class="textlink" href="{url("ru/")}">На главную ↗</a></div>','404.html',noindex=True))
 write('.nojekyll','')
 paths=['','ru/','de/','ru/about/','de/about/','impressum/','datenschutz/']
 write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+ORIGIN+url(p)+'</loc></url>' for p in paths)+'</urlset>')
 write('robots.txt','User-agent: *\nAllow: /\nSitemap: '+ORIGIN+url('sitemap.xml')+'\n')
 print('Built', len(list(OUT.rglob('*.html'))), 'HTML pages')
