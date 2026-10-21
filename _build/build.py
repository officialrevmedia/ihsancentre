#!/usr/bin/env python3
"""Static site generator for ihsancentre.org.

Every page is rendered to plain HTML at build time, so search engines and
visitors get full content without running any JavaScript.
Run:  python3 _build/build.py   (from the repo root)
"""
import json, os, html, datetime
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.ihsancentre.org'
TODAY = datetime.date.today().isoformat()

ZEFFY_DONATE = 'https://www.zeffy.com/en-CA/donation-form/preserve-tradition-build-community-shape-hearts'
ZEFFY_EH = 'https://www.zeffy.com/en-CA/ticketing/enlightened-hearts-2026--27'
ZEFFY_OLIVE = 'https://www.zeffy.com/en-CA/ticketing/the-olive-tree-preschool-circle-and-story-time-fall--2026'
PATREON = 'https://www.patreon.com/mysticmedicine'
FORM_ACTION = 'https://formsubmit.co/info@ihsancentre.org'
WA_COMMUNITY = 'https://chat.whatsapp.com/L8RwZr6FlDSI9dMjtM22IJ'
WA_BOOKCLUB = 'https://chat.whatsapp.com/EBidf6kg3Ij0rKZvZDzTsq'
INSTAGRAM = 'https://www.instagram.com/alihsancentre/'
CHARITY_NO = '763444353RR0001'

ADDRESS = {"@type": "PostalAddress", "streetAddress": "487 Shaver Road", "addressLocality": "Ancaster",
           "addressRegion": "ON", "addressCountry": "CA"}
PLACE = {"@type": "Place", "name": "Al-Ihsan Learning Centre", "address": ADDRESS}

e = html.escape

# ---------------------------------------------------------------- images
def img(name, alt, sizes='100vw', cls='', eager=False, small=True):
    """<img> with explicit width/height (no layout shift) and a 600w variant."""
    p = os.path.join(ROOT, 'assets/img', name + '.webp')
    w, h = Image.open(p).size
    sm = os.path.join(ROOT, 'assets/img', name + '-600.webp')
    srcset = ''
    if small and os.path.exists(sm):
        srcset = f' srcset="/assets/img/{name}-600.webp {Image.open(sm).size[0]}w, /assets/img/{name}.webp {w}w" sizes="{sizes}"'
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img src="/assets/img/{name}.webp"{srcset} width="{w}" height="{h}" alt="{e(alt)}"{c}{load}>'

STAR = '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M9 1l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" fill="#B08A4F"/></svg>'

# ---------------------------------------------------------------- forms
def field(name, label, kind='text', required=False, options=None, full=False, placeholder='', rows=4):
    req = ' required' if required else ''
    star = ' <span aria-hidden="true">*</span>' if required else ''
    cls = 'field full' if full or kind == 'textarea' else 'field'
    fid = 'f-' + name.lower().replace(' ', '-')
    ph = f' placeholder="{e(placeholder)}"' if placeholder else ''
    if kind == 'textarea':
        ctrl = f'<textarea id="{fid}" name="{e(name)}" rows="{rows}"{req}{ph}></textarea>'
    elif kind == 'select':
        opts = '<option value="">Choose one</option>' + ''.join(f'<option>{e(o)}</option>' for o in options)
        ctrl = f'<select id="{fid}" name="{e(name)}"{req}>{opts}</select>'
    else:
        auto = {'email': ' autocomplete="email"', 'tel': ' autocomplete="tel"'}.get(kind, '')
        if name == 'Name': auto = ' autocomplete="name"'
        ctrl = f'<input id="{fid}" type="{kind}" name="{e(name)}"{auto}{req}{ph}>'
    return f'<div class="{cls}"><label for="{fid}">{e(label)}{star}</label>{ctrl}</div>'

def form(subject, fields, button, next_path='/thank-you/', fid='form', note=''):
    n = f'<p class="form-note">{note}</p>' if note else ''
    return f'''<form class="form" id="{fid}" action="{FORM_ACTION}" method="POST">
  <input type="hidden" name="_subject" value="{e(subject)}">
  <input type="hidden" name="_next" value="{SITE}{next_path}">
  <input type="hidden" name="_template" value="table">
  <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form-grid">{''.join(fields)}</div>
  {n}<button class="btn btn-gold" type="submit">{e(button)}</button>
</form>'''

CONTACT_FIELDS = [field('Name', 'Your name', required=True), field('Email', 'Email', 'email', required=True),
                  field('Phone', 'Phone (optional)', 'tel')]

# ---------------------------------------------------------------- shared blocks
NAV = [('/programs/', 'Programs'), ('/events/', 'Events'), ('/rentals/', 'Rentals'),
       ('/about/', 'About'), ('/volunteer/', 'Volunteer'), ('/contact/', 'Contact')]

def header(path):
    links = ''.join(f'<li><a href="{u}"{" aria-current=page" if path.startswith(u) else ""}>{t}</a></li>' for u, t in NAV)
    return f'''<a href="#main" class="skip-link">Skip to main content</a>
<div class="topbar"><div class="container">Enlightened Hearts 2026-27 is in session. <a href="/donate/">Sponsor a child's seat</a> and help keep our programs open to every family.</div></div>
<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="/" aria-label="Al-Ihsan Learning Centre home"><img src="/assets/img/logo.webp" alt="Al-Ihsan Learning Centre" width="600" height="157" class="brand-logo"></a>
    <nav aria-label="Main navigation"><ul class="nav-links" id="navLinks">{links}</ul></nav>
    <div class="nav-cta">
      <a class="btn btn-gold btn-sm" href="/donate/">Donate</a>
      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

def crumbs(trail):
    """trail: list of (url, name); last item is the current page."""
    items = ''.join(
        (f'<li><a href="{u}">{e(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{e(n)}</li>')
        for i, (u, n) in enumerate(trail))
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="container"><ol>{items}</ol></div></nav>'

def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (u, n) in enumerate(trail)]}

def faq_block(faqs):
    items = ''.join(f'<details class="faq"><summary>{e(q)}</summary><div><p>{a}</p></div></details>' for q, a in faqs)
    return f'<div class="faqs">{items}</div>'

def faq_ld(faqs):
    import re
    strip = lambda s: re.sub('<[^>]+>', '', s)
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}

def give_band(headline='Every program here is kept open by donors.',
              body='Most of what happens at the Centre is free or subsidized, and no family is turned away because of cost. Your gift pays for teachers, materials, utilities and the upkeep of the building.'):
    return f'''<section class="give-band" aria-labelledby="give-h">
  <div class="container give-inner">
    <div>
      <p class="eyebrow light">Support the Centre</p>
      <h2 id="give-h" class="section-title light">{headline}</h2>
      <p class="lead light">{body}</p>
    </div>
    <div class="give-amounts">
      <a class="amt" href="{ZEFFY_DONATE}" rel="noopener"><strong>$50</strong><span>Books and materials for a class</span></a>
      <a class="amt" href="{ZEFFY_DONATE}" rel="noopener"><strong>$100</strong><span>One child's month of Enlightened Hearts</span></a>
      <a class="amt" href="{ZEFFY_DONATE}" rel="noopener"><strong>$900</strong><span>A full year's seat for one child</span></a>
      <a class="btn btn-gold" href="/donate/">See all ways to give</a>
    </div>
  </div>
</section>'''

FOOTER = f'''<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="/assets/img/logo-light.webp" alt="Al-Ihsan Learning Centre" width="600" height="157" loading="lazy">
        <p>Preserve Tradition. Build Community. Enlighten Hearts.</p>
        <p class="small">487 Shaver Road, Ancaster, ON<br><a href="mailto:info@ihsancentre.org">info@ihsancentre.org</a> · <a href="tel:+19058698993">905-869-8993</a></p>
      </div>
      <div><h2 class="fh">Programs</h2><ul>
        <li><a href="/enlightened-hearts/">Enlightened Hearts</a></li>
        <li><a href="/olive-tree/">The Olive Tree Preschool Circle</a></li>
        <li><a href="/markers-of-health/">Markers of Health</a></li>
        <li><a href="/book-club/">Book Club</a></li>
        <li><a href="/brothers-night/">Brothers Night</a></li>
        <li><a href="/family-night/">Family Night</a></li>
        <li><a href="/hifz/">Hifz Program 2027</a></li>
      </ul></div>
      <div><h2 class="fh">Centre</h2><ul>
        <li><a href="/donate/">Donate</a></li>
        <li><a href="/rentals/">Rent the Centre</a></li>
        <li><a href="/events/">Events</a></li>
        <li><a href="/about/">About us</a></li>
        <li><a href="/volunteer/">Volunteer</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul></div>
      <div><h2 class="fh">Stay connected</h2><ul>
        <li><a href="{INSTAGRAM}" rel="noopener">Instagram @alihsancentre</a></li>
        <li><a href="{WA_COMMUNITY}" rel="noopener">WhatsApp community</a></li>
        <li><a href="/contact/#newsletter">Email updates</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>© {datetime.date.today().year} Al-Ihsan Learning Centre</p>
      <p>Registered Canadian charity {CHARITY_NO}</p>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>'''

CSS = open(os.path.join(ROOT, '_build/site.css')).read()

def page(path, title, desc, body, trail=None, ld=None, og='home', noindex=False, h1_in_body=True, preload=''):
    """Render a full page. `trail` gives breadcrumbs; `ld` is a list of JSON-LD dicts."""
    ld = list(ld or [])
    if trail:
        ld.append(crumbs_ld(trail))
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large'
    canon = SITE + path
    doc = f'''<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#16324A">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{preload}<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/albert-sans-400.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Al-Ihsan Learning Centre">
<meta property="og:locale" content="en_CA">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/assets/og/{og}.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
{ld_html}
</head>
<body>
{header(path)}
{crumbs(trail) if trail else ''}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>'''
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if path != '/404.html' else os.path.join(ROOT, '404.html')
    if path == '/':
        out = os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)
    PAGES.append((path, noindex))

PAGES = []
