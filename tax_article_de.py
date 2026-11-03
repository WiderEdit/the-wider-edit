"""German personal essay."""
import json
from html import escape
TITLE='Ein Auto kaufen und ein Jahr lang „kostenlos“ fahren – wie soll das gehen?'
DESC='Wie ich beim finanzierten Autokauf die Vorsteuer für die ersten Raten einplante.'
SLUG='autokauf-finanzierung-vorsteuer'
PATH=f'de/stories/{SLUG}/'
DATE='2026-11-03'
IMAGE='assets/avto-nds-de-ai.webp'
ALT='Dunkelgrünes Auto. Ein Auto kaufen und ein Jahr lang „kostenlos“ fahren.'
BODY="""Als ich in Deutschland ein Unternehmen hatte, stellte ich mir gegen Jahresende immer dieselbe Frage: Wie viel Umsatzsteuer muss ich noch ans Finanzamt überweisen – und welche Anschaffungen stehen ohnehin an?

Wenn der Betrieb sowieso ein anderes Auto braucht, warum bis Januar warten? Bei einem Kauf im Dezember konnte die Vorsteuerverrechnung dafür sorgen, dass genug Geld für die ersten zwölf Raten im Budget blieb. Genau das fand ich interessant.

<h2>Eine Rechnung fürs ganze Auto. Gezahlt wird in Raten.</h2>

Beim finanzierten Autokauf bekam ich vom Händler eine Rechnung über den gesamten Kaufpreis. Die ging in die Buchhaltung, obwohl ich zu diesem Zeitpunkt erst die erste Rate gezahlt hatte. Die Vorsteuer aus der Rechnung konnte ich bei meinem Kauf in voller Höhe geltend machen.

Und jetzt kommt die Rechnung, die mir daran gefiel. Nehmen wir an, auf den Kauf entfallen <strong>4.000 Euro abziehbare Vorsteuer</strong>, und die Monatsrate beträgt <strong>330 Euro</strong>. Zwölf Raten machen <strong>3.960 Euro</strong>. Damit reicht der Betrag rechnerisch für ein ganzes Jahr Autoraten.

Ergab sich eine Erstattung, kam Geld aufs Konto. Wurde die Vorsteuer mit meiner Umsatzsteuerschuld verrechnet, musste ich weniger ans Finanzamt überweisen. Für meine Planung war entscheidend, was am Ende auf dem Konto blieb: <strong>Dieses Geld konnte ich für die Raten einplanen.</strong>

<h2>„Kostenlos“? Die Anführungszeichen bleiben.</h2>

Das Auto hat mir natürlich niemand geschenkt. Der Kredit lief weiter, und Versicherung und Sprit musste ich auch bezahlen. Aber mir gefiel der Gedanke: Das Auto war schon für den Betrieb im Einsatz, und für die ersten zwölf Raten war das Geld eingeplant.

Beim Geschäftshandy war es dasselbe in kleinerem Maßstab: <strong>2.000 Euro Kaufpreis, eine Rechnung über den Gesamtbetrag, zwei Jahre Raten.</strong> In meiner Buchhaltung wurde die Vorsteuer anhand der vollständigen Rechnung berücksichtigt. Ich musste sie nicht Monat für Monat aus den Raten zusammensammeln.

Das war meine Strategie zum Jahresende: erst schauen, was der Betrieb sowieso braucht, und dann rechnen, wann die Anschaffung am besten ins Budget passt.

Und wenn ohnehin ein anderes Auto anstand, war das für mich eine runde Sache: Der Betrieb hatte ein neues Auto, ich hatte mir etwas gegönnt, und ans Finanzamt ging dank des Vorsteuerabzugs erst mal weniger Geld. So macht eine Anschaffung zum Jahresende gleich dreimal Freude."""
def card(site, preview=False):
 attr=' id="new-story-preview" tabindex="-1" class="story-preview"' if preview else ''
 href=site.url(PATH)
 return f'<article class="story-card"><a class="story-image" style="display:block;position:relative;width:100%;height:0;padding-bottom:100%;overflow:hidden" href="{href}" tabindex="-1" aria-hidden="true"><img style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain" src="{site.url(IMAGE)}" width="1254" height="1254" alt="" loading="lazy"></a><div{attr}><p class="eyebrow">Business</p><h2><a href="{href}">{escape(TITLE)}</a></h2><p>{escape(DESC)}</p><a class="textlink" href="{href}">Artikel lesen ↗</a></div></article>'

def render(site):
 body=''.join(p if p.startswith('<h2>') else f'<p>{p}</p>' for p in BODY.split('\n\n'))
 content=f'<div class="wrap"><article class="story"><header class="story-head"><p class="eyebrow"><a href="{site.url("de/business/")}">Business</a></p><h1>{escape(TITLE)}</h1><p class="story-meta">Chris West · <time datetime="{DATE}">3. November 2026</time> · Aktualisiert: <time datetime="{DATE}">3. November 2026</time></p></header><figure class="story-photo beauty-photo"><img src="{site.url(IMAGE)}" width="1254" height="1254" alt="{escape(ALT,quote=True)}" fetchpriority="high"><figcaption>KI-generierte Illustration.</figcaption></figure><div class="prose story-prose">{body}<p><em>Das ist meine persönliche Erfahrung aus meiner Zeit in Deutschland. Die Beträge sind Rechenbeispiele. Die gesetzliche Grundlage für den Vorsteuerabzug steht in <a href="https://www.gesetze-im-internet.de/ustg_1980/__15.html" target="_blank" rel="noopener noreferrer">§ 15 UStG</a>.</em></p></div></article></div>'
 page=site.shell('de',TITLE,DESC,content,PATH,active='business')
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':TITLE,'description':DESC,'inLanguage':'de','datePublished':DATE,'dateModified':DATE,'author':{'@type':'Person','name':'Chris West'},'mainEntityOfPage':site.ORIGIN+site.url(PATH),'articleSection':'Business','image':site.ORIGIN+site.url(IMAGE)}
 page=page.replace('property="og:type" content="website"','property="og:type" content="article"').replace('</head>','<meta property="og:image" content="'+site.ORIGIN+site.url(IMAGE)+'"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head>')
 site.write(PATH+'index.html',page)
