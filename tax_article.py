"""Russian-only personal essay."""
import json
from html import escape
TITLE='Как купить машину и год ездить на ней «бесплатно»? Мой опыт в Германии'
DESC='Как зачёт входного НДС помогал мне планировать платежи за машину в рассрочку.'
SLUG='avto-v-rassrochku-nds-germaniya'
PATH=f'ru/stories/{SLUG}/'
DATE='2026-11-03'
IMAGE='assets/avto-nds-ru-ai.webp'
ALT='Тёмно-зелёный автомобиль. Как купить машину и год ездить на ней «бесплатно»?'
BODY="""Как купить машину и год ездить на ней «бесплатно»? Когда у меня был бизнес в Германии, к концу года у меня всегда возникал один и тот же вопрос: сколько предстоит перечислить в Finanzamt и что для бизнеса всё равно пора купить?

Если машину уже пора менять, зачем откладывать покупку до января? Иногда декабрьская покупка позволяла оставить в бюджете деньги почти на год платежей. Вот как это выглядело у меня.

Машину я обычно оформляю в кредит — тогда, в Германии, схема была такой: дилер выставлял <strong>счёт на всю стоимость автомобиля</strong>, а выплаты шли по графику. В бухгалтерию попадал полный счёт, хотя к тому моменту проходил только первый платёж. Входной НДС по покупке у меня целиком шёл в зачёт.

А теперь самое интересное. Допустим, в счёте за машину <strong>4 000 € НДС</strong>, а ежемесячный платёж — <strong>330 €</strong>. Двенадцать платежей — <strong>3 960 €</strong>. То есть суммы зачтённого НДС хватает на целый год платежей.

Если получался возврат, деньги приходили на счёт. Если НДС шёл в зачёт, в Finanzamt уходило меньше. Для моего бюджета результат был один: <strong>эти деньги можно было направить на выплаты за машину</strong>.

Вот что я имею в виду под «бесплатно». Машина, конечно, не подарок. Кредит остаётся, страховку и бензин тоже никто не отменял. Но мне нравилась эта арифметика: машина уже работает на бизнес, а деньги на первые двенадцать платежей есть.

С рабочим телефоном у меня была та же история, только суммы скромнее. Телефон за 2 000 €, счёт на всю покупку, выплаты на два года. В бухгалтерии НДС учитывался по полному счёту, а не по кусочкам с каждого платежа.

Для меня это и было стратегией на конец года: посмотреть, <strong>что бизнесу всё равно нужно</strong>, и посчитать, когда покупка лучше впишется в бюджет. Если машина нужна — считаю. Если не нужна — пусть стоит у дилера. Покупать машину только потому, что жалко перечислять НДС, — слишком дорогой способ себя порадовать."""
def card(site, preview=False):
 attr=' id="new-story-preview" tabindex="-1" class="story-preview"' if preview else ''
 href=site.url(PATH)
 return f'<article class="story-card"><a class="story-image" style="display:block;position:relative;width:100%;height:0;padding-bottom:100%;overflow:hidden" href="{href}" tabindex="-1" aria-hidden="true"><img style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain" src="{site.url(IMAGE)}" width="1254" height="1254" alt="" loading="lazy"></a><div{attr}><p class="eyebrow">Бизнес</p><h2><a href="{href}">{escape(TITLE)}</a></h2><p>{escape(DESC)}</p><a class="textlink" href="{href}">Читать статью ↗</a></div></article>'

def render(site):
 body=''.join(f'<p>{p}</p>' for p in BODY.split('\n\n'))
 content=f'<div class="wrap"><article class="story"><header class="story-head"><p class="eyebrow"><a href="{site.url("ru/business/")}">Бизнес</a></p><h1>{escape(TITLE)}</h1><p class="story-meta">Chris West · <time datetime="{DATE}">3 ноября 2026</time> · Обновлено: <time datetime="{DATE}">3 ноября 2026</time></p></header><figure class="story-photo beauty-photo"><img src="{site.url(IMAGE)}" width="1254" height="1254" alt="{escape(ALT,quote=True)}" fetchpriority="high"><figcaption>Иллюстрация создана с помощью ИИ.</figcaption></figure><div class="prose story-prose">{body}<p><em>Это мой личный опыт времён жизни в Германии. Суммы приведены для примера. Правовая основа вычета входного НДС — <a href="https://www.gesetze-im-internet.de/ustg_1980/__15.html" target="_blank" rel="noopener noreferrer">§ 15 UStG</a>.</em></p></div></article></div>'
 page=site.shell('ru',TITLE,DESC,content,PATH,active='business')
 schema={'@context':'https://schema.org','@type':'BlogPosting','headline':TITLE,'description':DESC,'inLanguage':'ru','datePublished':DATE,'dateModified':DATE,'author':{'@type':'Person','name':'Chris West'},'mainEntityOfPage':site.ORIGIN+site.url(PATH),'articleSection':'Бизнес','image':site.ORIGIN+site.url(IMAGE)}
 page=page.replace('property="og:type" content="website"','property="og:type" content="article"').replace('</head>','<meta property="og:image" content="'+site.ORIGIN+site.url(IMAGE)+'"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script></head>')
 site.write(PATH+'index.html',page)
