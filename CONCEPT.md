# The Wider Edit

Private, noncommercial personal blog from Georgia. Public author identity: **Chris West / Крис Вест**, a pseudonym. Do not add real author identity to source, metadata, structured data, or bylines.

## Launch

- Forest green, paper white, graphite. Desktop and mobile.
- Separate Russian and German editions. Browser language selects German when German; otherwise Russian. Explicit RU/DE links always visible. No stored language preference.
- Equal main areas: Business, Leisure, Health. No public subcategories at launch.
- No advertising, sponsored placements, affiliate remuneration, commercial calls to action, payments, contact forms, comments, subscriptions, advertising trackers, or external widgets. GoatCounter is used for pageview counts without cookies; see Datenschutz.
- Local images and system fonts; the only external script is the configured GoatCounter pageview counter. GitHub Pages still processes visitor IP addresses for security; disclose this without claiming zero personal-data processing.
- About page in the footer, pseudonymous approved biography. Impressum in German and Georgian. Datenschutz in German.
- Copyright Act Article 17(1)(b) supports use of a pseudonym; it does not establish a blanket exemption from operator-disclosure requirements. Legal applicability depends on actual circumstances.

## Publishing later

No fictional launch articles. Personal observations and substantive original writing, preserving author voice; separate fact, sourced information, and opinion. Manual review before publication.

Homepage: one most recent article once an approved article exists. Section pages: six newest items, then older pages; year/month archive only inside sections. Publication and substantive update dates on articles. Contextual internal links and related articles. External links open a new tab; internal links use the current tab. Add Article schema only to real articles; hreflang only for actual equivalents. No search at launch.

Octopus, the blog, any future routing bot, and specialists remain independent resources. No Octopus features, account collection, or service funnel are part of this launch. Reassess legal and privacy notices before any commercial or technical expansion.

## Page creation and publication quality

Required reusable layout and interaction rules are maintained in [SITE_QUALITY.md](SITE_QUALITY.md). Read that document before creating or changing pages.

The homepage places one latest approved story immediately after the introduction and Chris West signature, followed by the topic sections. The former decorative study image is omitted. A bright “Новая статья” / “Neuer Beitrag” link scrolls to the story's text preview; a separate prominent reading button opens the full article in the current tab. On mobile the reading button spans the card width.

Reserve image geometry before loading, prevent blank layout gaps and text shifts, preserve the bottom-right AI stamp on generated images, and version changed CSS. Verify the published result after deployment using the browser checks and limitations documented in SITE_QUALITY.md. Reuse these design principles on new resources, adapting their own routes, branding and test configuration.

## Build and host

Run `python3 build.py`, then `python3 validate.py`. In GitHub Settings → Pages, select Deploy from a branch → main → /docs. The canonical base is `https://wideredit.github.io/the-wider-edit/`. No dependencies or server required. Generated HTML is tracked so the deployed content remains inspectable.

The project `robots.txt` is within the repository subpath. A crawler only uses a robots file at the origin root; no crawler restrictions are claimed from this file. Sitemap can be submitted by its full URL after launch.
