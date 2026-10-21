#!/usr/bin/env python3
"""Page content for ihsancentre.org. Run from repo root: python3 _build/pages.py"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

HM_DONATE = ZEFFY_DONATE + '?utm_source=healthmarkers'
# Replace with the Winter Warmth Drive Zeffy campaign link once it is created:
ZEFFY_WINTER = 'https://www.zeffy.com/en-CA/donation-form/winter-warmth-drive-3?utm_source=website'
HOME = ('/', 'Home'); PROG = ('/programs/', 'Programs')
ORG = {"@context": "https://schema.org", "@type": ["EducationalOrganization", "NGO"], "@id": SITE + "/#org",
       "name": "Al-Ihsan Learning Centre", "alternateName": "Ihsan Centre", "url": SITE + "/",
       "logo": SITE + "/assets/img/logo.webp", "email": "info@ihsancentre.org", "telephone": "+1-905-869-8993",
       "address": ADDRESS, "sameAs": [INSTAGRAM], "slogan": "Preserve Tradition. Build Community. Enlighten Hearts.",
       "nonprofitStatus": "Nonprofit501c3" if False else None}
ORG.pop("nonprofitStatus")

def ev(name, start, end, desc, url, offer_url=None, free=True):
    d = {"@context": "https://schema.org", "@type": "Event", "name": name, "startDate": start, "endDate": end,
         "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
         "eventStatus": "https://schema.org/EventScheduled", "location": PLACE, "description": desc,
         "organizer": {"@type": "Organization", "name": "Al-Ihsan Learning Centre", "url": SITE + "/"},
         "image": [SITE + "/assets/og/home.jpg"], "url": SITE + url}
    if offer_url or free:
        d["offers"] = {"@type": "Offer", "url": offer_url or SITE + url, "price": "0", "priceCurrency": "CAD",
                       "availability": "https://schema.org/InStock"}
    return d

def sec(inner, cls='bg-cream', id=''):
    i = f' id="{id}"' if id else ''
    return f'<section class="{cls}"{i}><div class="container">{inner}</div></section>'

def ticks(items):
    return '<ul class="ticks">' + ''.join(f'<li>{STAR}<span>{x}</span></li>' for x in items) + '</ul>'

def facts(items):
    return '<div class="facts">' + ''.join(f'<div class="fact"><span>{k}</span><strong>{v}</strong></div>' for k, v in items) + '</div>'

def simple_hero(eyebrow, h1, lead, btns=''):
    return f'''<section class="page-hero"><div class="container"><p class="eyebrow light">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p>{btns}</div></section>'''

# ================================================================ HOME
PROGRAM_CARDS = [
    ('/enlightened-hearts/', 'Sundays · Ages 4 to 16', 'Enlightened Hearts', "Our weekend school. Qur'an, Aqidah, Seerah, Adab and Islamic arts across four age-based levels."),
    ('/olive-tree/', 'Fridays · Ages 0 to 4', 'The Olive Tree', 'A preschool circle of stories and song. A parent or guardian joins each class.'),
    ('/markers-of-health/', 'Every other Thursday · Free', 'Markers of Health', 'One health marker per session with Dr. Rehan Zaidi, ND, explained through holistic and Prophetic medicine.'),
    ('/book-club/', 'Every other month · Fridays', 'Book Club', 'Read a book together, then meet at the Centre to talk it through over coffee. New readers welcome.'),
    ('/guys-night/', 'Friday evenings', 'Guys Night', 'Games, good food and brotherhood. Brothers old and new, food and drinks provided.'),
    ('/family-night/', 'Monthly · Launching soon', 'Family Night', 'One evening a month for the whole family: dinner, a short talk, and activities for the kids.'),
    ('/hifz/', 'Launching 2027', 'Hifz Program', "A dedicated path for children to memorize the Qur'an, taught with traditional method and care."),
]
def program_cards(exclude=None):
    return '<div class="cards">' + ''.join(
        f'<article class="card"><p class="tag">{t}</p><h3><a href="{u}" style="text-decoration:none">{n}</a></h3><p>{d}</p><a class="more" href="{u}">Learn more<span class="sr"> about {n}</span></a></article>'
        for u, t, n, d in PROGRAM_CARDS if u != exclude) + '</div>'

home = f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <p class="eyebrow light">Al-Ihsan Learning Centre · Ancaster, Ontario</p>
    <h1>Preserve tradition. Build community. <em>Enlighten hearts.</em></h1>
    <p class="lead">A community learning centre on Shaver Road in Ancaster. We run a weekend Islamic school for children, a preschool circle, programs for adults and families, and gatherings throughout the year. Most of it is free, and all of it is kept running by donors.</p>
    <div class="btns"><a class="btn btn-gold" href="/donate/">Donate to the Centre</a><a class="btn btn-outline-light" href="/programs/">See our programs</a></div>
  </div>
  <div class="arch">{img('hero-gathering', 'Families and children gathered in a learning circle at Al-Ihsan Learning Centre', '(max-width:980px) 90vw, 440px', eager=True)}</div>
</div></section>
{sec(f"""<div class="center"><p class="eyebrow">What happens here</p><h2 class="section-title">Programs for <em>every age</em></h2>
<p class="lead">From toddlers to grandparents. Pick a program to see times, details and how to sign up.</p></div>
{program_cards()}<p class="center" style="margin-top:30px"><a class="btn btn-outline" href="/programs/">All programs and gatherings</a></p>""", 'bg-cream', 'enlightened-hearts')}
{give_band()}
{sec(f"""<div class="split"><div class="arch">{img('gallery-nikkah', 'The Centre decorated for a nikkah ceremony', '(max-width:980px) 90vw, 540px', small=True)}</div>
<div><p class="eyebrow">Rent the Centre</p><h2 class="section-title">Host your nikkah, dinner or celebration <em>with us</em></h2>
<p class="lead">The Centre is open to the community for nikkahs, engagements, dinners, aqiqahs, iftars and family gatherings. Rates are kept affordable, the space is handled with care, and we work with decorators for backdrops, flowers and table styling. Every booking helps fund our programs.</p>
<div class="btns"><a class="btn btn-navy" href="/rentals/">Rental details and enquiries</a></div></div></div>""", 'bg-white', 'rentals')}
{sec(f"""<p class="eyebrow">Coming up</p><h2 class="section-title">Upcoming at <em>the Centre</em></h2>
<div class="upcoming">
<div class="up"><div class="date"><b>22</b><span>Oct · Thu</span></div><div><h3>Markers of Health, Matters of the Heart</h3><p>7:30 to 8:30 PM with Dr. Rehan Zaidi, ND · In person and live online · Free</p></div><a class="btn btn-sm btn-outline" href="/markers-of-health/">Details</a></div>
<div class="up"><div class="date"><b>23</b><span>Oct · Fri</span></div><div><h3>Book Club: The AI Mirror</h3><p>7:00 to 8:30 PM · Conversation and coffee · New joiners welcome</p></div><a class="btn btn-sm btn-outline" href="/book-club/">Sign up</a></div>
<div class="up"><div class="date"><b>1</b><span>Nov · Sun</span></div><div><h3>Winter Warmth Drive drop-off begins</h3><p>Sundays to Dec 6, 10 AM to 1 PM · Coats, socks, toques and essentials</p></div><a class="btn btn-sm btn-outline" href="/winter-drive/">Details</a></div>
<div class="up"><div class="date"><b>Sun</b><span>Weekly</span></div><div><h3>Enlightened Hearts weekend school</h3><p>10:00 AM to 1:00 PM · Ages 4 to 16 · Late registration still open</p></div><a class="btn btn-sm btn-outline" href="/enlightened-hearts/">Details</a></div>
</div><p style="margin-top:22px"><a href="/events/">See all events and past gatherings</a></p>""", 'bg-cream', 'events')}
{sec(f"""<div class="split"><div><p class="eyebrow">Who we are</p><h2 class="section-title">A learning centre <em>run by its community</em></h2>
<p class="lead">Al-Ihsan Learning Centre teaches traditional Islamic knowledge to children and adults, and serves families in Ancaster, Hamilton and beyond through food drives, iftars, emergency aid and support for new Muslims. We are a registered Canadian charity ({CHARITY_NO}).</p>
<div class="btns"><a class="btn btn-outline" href="/about/">About the Centre</a><a class="btn btn-outline" href="/volunteer/">Volunteer</a></div></div>
<div class="arch">{img('about', "A child learning the Qur'an at Al-Ihsan Learning Centre", '(max-width:980px) 90vw, 540px')}</div></div>""", 'bg-white', 'about')}
'''
page('/', 'Al-Ihsan Learning Centre | Islamic School and Community Centre in Ancaster, ON',
     'Islamic weekend school, preschool circle, adult and family programs, and event rentals in Ancaster, Ontario. A registered charity serving Hamilton families.',
     home, preload='<link rel="preload" as="image" href="/assets/img/hero-gathering.webp" imagesrcset="/assets/img/hero-gathering-600.webp 480w, /assets/img/hero-gathering.webp 800w" imagesizes="(max-width:980px) 90vw, 440px" fetchpriority="high">\n', ld=[ORG, {"@context": "https://schema.org", "@type": "WebSite", "name": "Al-Ihsan Learning Centre", "url": SITE + "/"}])

# ================================================================ PROGRAMS HUB
gather = [
    ('Weekly', 'Circle of Light', "A weekly circle of Qur'an recitation and dhikr, open to everyone.", '/contact/?subject=Circle%20of%20Light'),
    ('Monthly · Selected Sundays', 'In Praise of the Beloved ﷺ', 'A monthly Mawlid with poetry, nasheed, stories and reflection on the Prophet ﷺ.', '/contact/?subject=Mawlid%20schedule'),
]
prog_body = simple_hero('Programs', 'Programs and <em>gatherings</em>', 'Weekend school, preschool, adult learning, social evenings and gatherings. Everything runs at 487 Shaver Road, Ancaster unless noted.') + \
    sec('<h2 class="section-title">Our programs</h2>' + program_cards(), 'bg-cream') + \
    sec('<h2 class="section-title">Regular gatherings</h2><div class="cards">' + ''.join(
        f'<article class="card"><p class="tag">{t}</p><h3>{n}</h3><p>{d}</p><a class="more" href="{u}">Ask for the schedule</a></article>' for t, n, d, u in gather) + '</div>', 'bg-white') + \
    give_band('Keep these programs free and open.', 'Enlightened Hearts subsidizes seats for families who need them, and most adult and family programs cost nothing to attend. Donations cover the difference.')
page('/programs/', 'Programs | Al-Ihsan Learning Centre, Ancaster',
     'Every program at Al-Ihsan in Ancaster: weekend school, preschool, Markers of Health, Book Club, Guys Night, Family Night, Hifz 2027 and Mawlid.',
     prog_body, trail=[HOME, PROG])

# ================================================================ ENLIGHTENED HEARTS
eh_faq = [
    ('What ages is Enlightened Hearts for?', 'Children and youth aged 4 to 16, grouped into four levels: The Fig Tree (4 to 5), The Grape Tree (6 to 9), The Pomegranate Tree (9 to 11) and The Date Palm Tree (12 to 16).'),
    ('When are classes?', 'Sundays from 10:00 AM to 1:00 PM, September 13, 2026 to June 13, 2027.'),
    ('How much does it cost?', '$100 per month or $900 for the year. Sibling rates are available, and free and subsidized seats are offered so that no family is turned away because of cost.'),
    ('Can we still register mid-year?', f'Yes. Register online through <a href="{ZEFFY_EH}">our registration form</a>, or email info@ihsancentre.org and we will help you find the right level.'),
]
eh = simple_hero('Our flagship program · Sundays', 'Enlightened Hearts <em>2026-27</em>',
    "A weekend Islamic school for ages 4 to 16. Children learn about Allah, the Prophet ﷺ, the Qur'an and good character through stories, discussion, memorization and Islamic arts.",
    f'<div class="btns"><a class="btn btn-gold" href="{ZEFFY_EH}" rel="noopener">Register your child</a><a class="btn btn-outline-light" href="/donate/">Sponsor a seat</a></div>') + \
    sec(f'''<div class="split top"><div class="flyer"><a href="/assets/img/enlightened-hearts-2026-flyer.webp">{img('enlightened-hearts-2026-flyer', 'Enlightened Hearts 2026-27 flyer: Sundays 10 AM to 1 PM, September 13, 2026 to June 13, 2027, ages 4 to 16, 487 Shaver Road, Ancaster', '(max-width:980px) 90vw, 560px')}</a></div>
    <div><h2 class="section-title">What children learn</h2>{ticks(["Aqidah, Seerah, Adab and Qur'an memorization", "Readings from the Al-Ghazali Children's Series and Shamaail literature", 'Islamic visual arts and nasheed', 'Inquiry-based projects and mentorship for older students', 'Small classes with teachers who know each child by name'])}
    {facts([('Sundays', 'Sept 13, 2026 to June 13, 2027'), ('Time', '10:00 AM to 1:00 PM'), ('Ages', '4 to 16'), ('Fees', '$100/month or $900/year')])}
    <div class="note">Sibling rates are available, and no family is turned away because of cost. If fees are a barrier, email <a href="mailto:info@ihsancentre.org">info@ihsancentre.org</a> in confidence.</div>
    <a class="btn btn-gold" href="{ZEFFY_EH}" rel="noopener">Register for 2026-27</a></div></div>''') + \
    sec(f'''<div class="center"><h2 class="section-title">Four levels, <em>rooted in tradition</em></h2><p class="lead">Each level is named after a tree mentioned in the Qur'an.</p></div>
    <div class="levels">{''.join(f'<article class="level"><span class="ages">{a}</span><h3>{n}</h3><p>{d}</p></article>' for a, n, d in [('Ages 4 to 5', 'The Fig Tree', 'Stories, songs, memorization, daily duas and a love for Allah and His Messenger ﷺ.'), ('Ages 6 to 9', 'The Grape Tree', 'Two age groups (6 to 7 and 8 to 9): Seerah, Shamaail, character, memorization, poetry and Al-Ghazali readings.'), ('Ages 9 to 11', 'The Pomegranate Tree', 'Aqidah, Shamaail, Adab, inquiry-based learning, memorization and poetry.'), ('Ages 12 to 16', 'The Date Palm Tree', 'Aqidah, Seerah, character, Fiqh, critical reasoning and principled engagement.')])}</div>
    <p class="center" style="margin-top:26px">Children under 4? See <a href="/olive-tree/">The Olive Tree preschool circle</a>.</p>''', 'bg-white') + \
    sec('<h2 class="section-title">Questions parents ask</h2>' + faq_block(eh_faq)) + \
    give_band('Sponsor a child\'s seat.', '$100 covers one child for a month. $900 covers a full year. Sponsored seats go to families who could not otherwise attend, and stay anonymous.')
page('/enlightened-hearts/', 'Enlightened Hearts 2026-27 | Weekend Islamic School in Ancaster',
     'Weekend Islamic school for ages 4 to 16 in Ancaster. Sundays 10 AM to 1 PM, Sept 2026 to June 2027. Four levels, $100/month, subsidized seats available.',
     eh, trail=[HOME, PROG, ('/enlightened-hearts/', 'Enlightened Hearts')], og='enlightened-hearts',
     ld=[faq_ld(eh_faq), {"@context": "https://schema.org", "@type": "Course", "name": "Enlightened Hearts 2026-27",
         "description": "Weekend Islamic education for ages 4 to 16 across four age-based levels.",
         "provider": {"@id": SITE + "/#org", "@type": "EducationalOrganization", "name": "Al-Ihsan Learning Centre"},
         "offers": {"@type": "Offer", "url": ZEFFY_EH, "price": "900", "priceCurrency": "CAD", "category": "Paid"},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Onsite", "startDate": "2026-09-13", "endDate": "2027-06-13",
                               "courseSchedule": {"@type": "Schedule", "byDay": "https://schema.org/Sunday", "startTime": "10:00", "endTime": "13:00", "repeatFrequency": "P1W"}, "location": PLACE}}])

# ================================================================ OLIVE TREE
ot_faq = [('Who is The Olive Tree for?', 'Children aged 0 to 4, with a parent or guardian who stays and takes part in each class.'),
          ('When is the fall session?', 'Fridays from 9:30 to 10:30 AM, September 18 to November 27, 2026. Ten classes, with no class on October 9.'),
          ('How do we register?', f'Register online through <a href="{ZEFFY_OLIVE}">the fall session form</a>. To hear about the winter session, sign up for email updates on our <a href="/contact/#newsletter">contact page</a>.')]
ot = simple_hero('Preschool · Fridays', 'The Olive Tree: <em>Preschool Circle and Story Time</em>',
    'A class for our youngest learners, ages 0 to 4, built around stories, songs, crafts and movement. A parent or guardian joins their child each week.',
    f'<div class="btns"><a class="btn btn-olive" href="{ZEFFY_OLIVE}" rel="noopener">Register for fall 2026</a></div>') + \
    sec(f'''<div class="split"><div class="arch">{img('olive-tree-storytime', 'A mother reading a picture book with her young child at The Olive Tree', '(max-width:980px) 90vw, 540px')}</div>
    <div><h2 class="section-title">Faith through the five senses</h2><p class="lead">Teachers use stories, song, hands-on crafts and play to help little ones grow a connection to Allah and His Prophet ﷺ.</p>
    {facts([('Fridays', '9:30 to 10:30 AM'), ('Fall session', 'Sept 18 to Nov 27, 2026'), ('Classes', 'Ten (no class Oct 9)'), ('Ages', '0 to 4, with a parent')])}
    <a class="btn btn-olive" href="{ZEFFY_OLIVE}" rel="noopener">Register</a></div></div>''', 'bg-olive') + \
    sec(f'<div class="flyer" style="max-width:860px;margin:0 auto">{img("olive-tree-fall-2026-flyer", "The Olive Tree fall 2026 flyer: ages 0 to 4, Fridays 9:30 to 10:30 AM, September 18 to November 27, 2026", "(max-width:900px) 92vw, 860px")}</div>', 'bg-white') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(ot_faq)) + give_band()
page('/olive-tree/', 'The Olive Tree Preschool Circle (Ages 0 to 4) | Al-Ihsan, Ancaster',
     'Preschool circle and story time for ages 0 to 4 in Ancaster. Fridays 9:30 to 10:30 AM, Sept 18 to Nov 27, 2026. A parent joins each class.',
     ot, trail=[HOME, PROG, ('/olive-tree/', 'The Olive Tree')], og='olive-tree', ld=[faq_ld(ot_faq)])

# ================================================================ MARKERS OF HEALTH
mh_faq = [('Is it free?', 'Yes. Markers of Health is free to attend in person and online. Donations help keep it that way.'),
          ('How do I watch online?', f'Sessions are streamed live and recorded on <a href="{PATREON}">Dr. Rehan\'s Patreon page</a>, where you can also register.'),
          ('Do I need a medical background?', 'No. Each session explains one marker in plain language, with time for questions at the end.'),
          ('Is this medical advice?', 'No. Sessions are educational. Speak with your own doctor about your results and any changes to your care.')]
dates = ['Thursday, October 22', 'Thursday, November 5', 'Thursday, November 19', 'Thursday, December 3']
mh = f'''<section class="page-hero has-photo"><div class="ph-img">{img('markers-header', 'Dr. Rehan Zaidi pointing to inflammation markers on a whiteboard at Al-Ihsan Learning Centre', '100vw', eager=True)}</div>
<div class="container"><div><p class="eyebrow light">Every other Thursday · Free</p><h1>Markers of Health, <em>Matters of the Heart</em></h1>
<p class="lead">A bi-weekly wellness program with Dr. Rehan Zaidi, ND. Each session takes one health marker and explains what it measures, what it says about your health, and practical steps from holistic and Prophetic medicine.</p>
<div class="btns"><a class="btn btn-gold" href="{PATREON}" rel="noopener">Register on Patreon</a><a class="btn btn-outline-light" href="{HM_DONATE}" rel="noopener">Donate</a></div></div></div></section>''' + \
    sec(f'''<div class="split top"><div><h2 class="section-title">What each session covers</h2>{ticks(['What the marker is and what it measures', 'What it tells us about our health', 'Practical steps from holistic and Prophetic medicine', 'Open Q&amp;A with Dr. Rehan'])}
    {facts([('When', 'Every other Thursday'), ('Time', '7:30 to 8:30 PM'), ('Where', '487 Shaver Road, Ancaster'), ('Online', 'Streamed live')])}
    <h3 style="font-size:22px;margin:26px 0 10px">Upcoming sessions</h3><ul class="ticks">{''.join(f'<li>{STAR}<span>{d}, 7:30 PM</span></li>' for d in dates)}</ul>
    <p class="small" style="color:var(--muted)">Dates can shift around holidays. Patreon always has the current schedule.</p></div>
    <div class="flyer">{img('markers-poster', 'Markers of Health, Matters of the Heart poster with Dr. Rehan Zaidi, ND, every other Thursday 7:30 to 8:30 PM, with QR codes to register and donate', '(max-width:980px) 90vw, 540px')}</div></div>''') + \
    sec(f'''<div class="split"><div><p class="eyebrow">Your host</p><h2 class="section-title">Dr. Rehan Zaidi, ND</h2><p class="lead">A naturopathic doctor and the founder of Mystic Medicine, Dr. Rehan has practised traditional and integrative medicine for 22 years in Canada, Jordan and Malaysia.</p>
    <div class="btns"><a class="btn btn-outline" href="https://mysticmedicine.com/authors/dr-rehan-ali-zaidi/" rel="noopener">Read his full bio</a></div></div>
    <div>{form('Markers of Health: session reminders', CONTACT_FIELDS[:2], 'Send me session reminders', '/thank-you/', 'mh-form', 'We will email you before each session. Unsubscribe any time.')}</div></div>''', 'bg-white') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(mh_faq)) + \
    f'''<section class="give-band"><div class="container give-inner"><div><p class="eyebrow light">Keep it free</p><h2 class="section-title light">Help keep Markers of Health free for everyone.</h2><p class="lead light">The program costs nothing to attend. Donations cover the space, equipment and live stream.</p></div>
    <div class="give-amounts"><a class="amt" href="{HM_DONATE}" rel="noopener"><strong>$25</strong><span>Covers one session's stream</span></a><a class="amt" href="{HM_DONATE}" rel="noopener"><strong>$100</strong><span>Sponsors an evening at the Centre</span></a><a class="btn btn-gold" href="{HM_DONATE}" rel="noopener">Donate any amount</a></div></div></section>'''
mh_ld = [faq_ld(mh_faq), ev('Markers of Health, Matters of the Heart', '2026-10-22T19:30:00-04:00', '2026-10-22T20:30:00-04:00',
      'Free wellness session with Dr. Rehan Zaidi, ND on one health marker, in person and streamed live.', '/markers-of-health/', PATREON)]
mh_ld[1]["eventAttendanceMode"] = "https://schema.org/MixedEventAttendanceMode"
mh_ld[1]["location"] = [PLACE, {"@type": "VirtualLocation", "url": PATREON}]
mh_ld[1]["image"] = [SITE + "/assets/og/markers-of-health.jpg"]
mh_ld[1]["performer"] = {"@type": "Person", "name": "Dr. Rehan Zaidi, ND"}
page('/markers-of-health/', 'Markers of Health, Matters of the Heart | Free Wellness Program, Ancaster',
     'Free bi-weekly wellness talks with Dr. Rehan Zaidi, ND in Ancaster. Every other Thursday, 7:30 to 8:30 PM, in person and streamed live.',
     mh, preload='<link rel="preload" as="image" href="/assets/img/markers-header-600.webp" media="(max-width:600px)">\n', trail=[HOME, PROG, ('/markers-of-health/', 'Markers of Health')], og='markers-of-health', ld=mh_ld)

# ================================================================ BOOK CLUB
bc_faq = [('Do I need to have finished the book?', 'No. Come anyway. Plenty of people arrive halfway through and still join the conversation.'),
          ('How often do you meet?', 'Roughly every two months on a Friday evening, 7:00 to 8:30 PM, at the Centre. Dates are shared in the book club WhatsApp group.'),
          ('Where can I buy the book?', 'Most major bookstores carry our picks. Members have also found them at Epic Books on Ottawa Street in Hamilton, and we try to support independent and local sellers where we can.'),
          ('Who can join?', 'Any adult who enjoys reading and talking about ideas. New joiners are always welcome.')]
bc_fields = CONTACT_FIELDS + [field('How did you hear about us', 'How did you hear about the book club?', 'select', options=['Flyer or QR code', 'Instagram', 'WhatsApp', 'A friend', 'At the Centre', 'Other'])]
bc = simple_hero('Book Club · Every other month', 'Al-Ihsan <em>Book Club</em>',
    'We pick a book, read it over a couple of months, then meet at the Centre to talk it through. Come join in for conversation and coffee. New joiners are welcome.',
    '<div class="btns"><a class="btn btn-gold" href="#join">Join the book club</a></div>') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">Next meetup</h2>
    {facts([('Date', 'Friday, October 23'), ('Time', '7:00 to 8:30 PM'), ('Reading', 'The AI Mirror by Shannon Vallor'), ('Where', '487 Shaver Road, Ancaster')])}
    <h2 class="section-title" style="margin-top:34px">Our 2026 reads</h2>
    <div class="cards" style="margin-top:16px">
      <article class="card"><p class="tag">Read in June</p><h3>One Day, Everyone Will Have Always Been Against This</h3><p>Omar El Akkad</p></article>
      <article class="card"><p class="tag">Read in August</p><h3>Yesteryear</h3><p>Caro Claire Burke</p></article>
      <article class="card"><p class="tag">Reading now</p><h3>The AI Mirror</h3><p>Shannon Vallor</p></article>
    </div></div>
    <div class="flyer">{img('book-club-flyer', 'Al-Ihsan Book Club flyer listing the 2026 reads, every other month on Fridays 7 to 8:30 PM, with a QR code to join', '(max-width:980px) 90vw, 540px')}</div></div>''') + \
    sec(f'''<div class="split top"><div><p class="eyebrow">Join us</p><h2 class="section-title">Sign up for the book club</h2><p class="lead">Leave your details and we will send you the link to the book club WhatsApp group, where we share the next pick, meetup dates and reading reflections.</p>
    {ticks(['Free to join', 'Conversation and coffee at every meetup', 'No need to have finished the book'])}</div>
    <div>{form('Book Club sign-up', bc_fields, 'Join the book club', '/book-club/welcome/', 'join')}</div></div>''', 'bg-white', 'join') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(bc_faq)) + give_band()
page('/book-club/', 'Al-Ihsan Book Club | Monthly Reading Group in Ancaster and Hamilton',
     'Join the Al-Ihsan Book Club in Ancaster. We meet every other month on Fridays, 7 to 8:30 PM, for conversation and coffee. New joiners welcome.',
     bc, trail=[HOME, PROG, ('/book-club/', 'Book Club')], og='book-club',
     ld=[faq_ld(bc_faq), ev('Al-Ihsan Book Club: The AI Mirror', '2026-10-23T19:00:00-04:00', '2026-10-23T20:30:00-04:00',
         'Book club meetup discussing The AI Mirror by Shannon Vallor. Conversation and coffee. New joiners welcome.', '/book-club/')])

page('/book-club/welcome/', 'Welcome to the Book Club | Al-Ihsan Learning Centre',
     'Thank you for joining the Al-Ihsan Book Club.',
     simple_hero('You are in', 'Welcome to the <em>book club</em>', 'Thank you for signing up. Tap below to join the book club WhatsApp group, where we share the next pick and meetup dates.',
                 f'<div class="btns"><a class="btn btn-gold" href="{WA_BOOKCLUB}" rel="noopener">Join the WhatsApp group</a><a class="btn btn-outline-light" href="/book-club/">Back to the book club</a></div>'),
     noindex=True)

# ================================================================ GUYS NIGHT
gn_faq = [('Who is Guys Night for?', 'Brothers of all ages, whether you have been coming to the Centre for years or have never been before.'), ('Is there a cost?', 'No. Food and drinks are provided. Donations and sponsors cover the cost of each night.'), ('How do I find out about the next one?', 'Sign up on this page and we will email you the next date. It is also shared in our WhatsApp community.')]
gn = simple_hero('Guys Night · Friday evenings', 'Guys <em>Night</em>', 'Games. Good food. Brotherhood. An evening at the Centre for brothers old and new, with food and drinks provided.',
                 '<div class="btns"><a class="btn btn-gold" href="#signup">RSVP for the next one</a></div>') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">What to expect</h2>{ticks(['Games and friendly competition', 'Food and drinks provided', 'Good conversation and new friends', 'Open to brothers old and new'])}
    {facts([('When', 'Friday evenings'), ('Time', '7:30 to 10:00 PM'), ('Where', 'Al-Ihsan Learning Centre'), ('Cost', 'Free')])}
    <p class="lead">RSVP below so we know how much food to order. We will email you each new date.</p></div>
    <div id="signup">{form('Guys Night RSVP', CONTACT_FIELDS + [field('Guests', 'Bringing anyone? How many', 'number')], 'RSVP and send me dates', '/thank-you/', 'gn-form')}</div></div>''') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(gn_faq), 'bg-white') + \
    give_band('Sponsor a Guys Night.', 'Food, games and the space for an evening are covered by donors. Sponsoring a night is a simple way to keep it going.')
page('/guys-night/', 'Guys Night | Games, Food and Brotherhood at Al-Ihsan, Ancaster',
     'Guys Night at Al-Ihsan Learning Centre in Ancaster: games, good food and brotherhood for brothers old and new. Friday evenings, food and drinks provided. RSVP online.',
     gn, trail=[HOME, PROG, ('/guys-night/', 'Guys Night')], ld=[faq_ld(gn_faq)])

# ================================================================ WINTER WARMTH DRIVE
wd_faq = [('When and where can I drop off items?', 'Sundays from November 1 to December 6, 10 AM to 1 PM, at Al-Ihsan Learning Centre, 487 Shaver Road, Ancaster, by the Musalla.'),
          ('What should I bring?', 'New warm socks, toques, mittens, scarves, hand warmers, nut-free granola bars, toothbrushes, toothpaste and lip balm. Winter coats in kids and adult sizes are also welcome, new or clean and gently used.'),
          ('Who receives the kits?', 'Our students pack the kits, and they are delivered to people in need across Ancaster and Hamilton on Sunday, December 13.'),
          ("Can I give money instead?", f'Yes. <a href="{ZEFFY_WINTER}">Give online</a> and we will use it to fill any gaps in the kits, such as coats and sizes we are short on.')]
wd_pledge = CONTACT_FIELDS + [field('Helping how', 'How would you like to help?', 'select', options=['Dropping off items', 'Donating winter coats', 'Volunteering to pack kits', 'Helping with delivery on Dec 13', 'More than one of these']),
             field('Items', 'What are you planning to bring?', 'textarea', rows=3, placeholder='e.g. 10 pairs of socks, 2 kids coats (size 8)')]
wd = simple_hero('Enlightened Hearts community service project', 'Winter <em>Warmth</em> Drive',
    'Our students are collecting winter essentials and packing warmth kits for people in need across Ancaster and Hamilton. Drop off items on Sundays, or give online and we will buy what is missing.',
    f'<div class="btns"><a class="btn btn-gold" href="{ZEFFY_WINTER}" rel="noopener">Give online</a><a class="btn btn-outline-light" href="#pledge">Pledge items or volunteer</a></div>') + \
    sec(f'''<div class="split top"><div>
    {facts([('Drop-off', 'Sundays, Nov 1 to Dec 6'), ('Time', '10 AM to 1 PM'), ('Where', '487 Shaver Road, by the Musalla'), ('Delivered', 'Sunday, Dec 13')])}
    <h2 class="section-title" style="margin-top:28px">New essentials</h2>{ticks(['Warm socks', 'Toques, mittens and scarves', 'Hand warmers', 'Nut-free granola bars', 'Toothbrushes, toothpaste and lip balm'])}
    <h2 class="section-title" style="margin-top:20px">Also welcome</h2>{ticks(['Winter coats, kids and adult sizes, new or clean and gently used'])}
    <p class="lead" style="margin-top:18px;font-style:italic">"The best of people are those who bring the most benefit to others." (Prophet Muhammad, peace be upon him, reported by al-Tabarani)</p></div>
    <div class="flyer">{img('winter-drive-poster', 'Winter Warmth Drive poster: Sundays November 1 to December 6, 10 AM to 1 PM, drop off at 487 Shaver Road, Ancaster, kits delivered December 13', '(max-width:980px) 90vw, 540px')}</div></div>''') + \
    f'''<section class="give-band"><div class="container give-inner"><div><p class="eyebrow light">Don't have items to give?</p><h2 class="section-title light">Donate and we will purchase kits on your behalf.</h2><p class="lead light">Online gifts buy the coats, sizes and items we run short on, so every kit goes out complete.</p></div>
    <div class="give-amounts"><a class="amt" href="{ZEFFY_WINTER}" rel="noopener"><strong>$25</strong><span>Socks, mittens and a toque for one kit</span></a><a class="amt" href="{ZEFFY_WINTER}" rel="noopener"><strong>$50</strong><span>A complete warmth kit</span></a><a class="amt" href="{ZEFFY_WINTER}" rel="noopener"><strong>$100</strong><span>A new winter coat</span></a><a class="btn btn-gold" href="{ZEFFY_WINTER}" rel="noopener">Give any amount</a></div></div></section>''' + \
    sec(f'''<div class="split top"><div><p class="eyebrow">Pledge</p><h2 class="section-title">Tell us how you will help</h2><p class="lead">Let us know what you plan to bring, or sign up to pack and deliver kits. It helps us see what is still needed.</p></div>
    <div>{form('Winter Warmth Drive pledge', wd_pledge, 'Send my pledge', '/thank-you/', 'pledge')}</div></div>''', 'bg-white', 'pledge') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(wd_faq))
page('/winter-drive/', 'Winter Warmth Drive | Donate Winter Essentials in Ancaster and Hamilton',
     'Al-Ihsan Winter Warmth Drive: drop off socks, toques, mittens, coats and essentials Sundays Nov 1 to Dec 6 in Ancaster, or give online. Kits delivered Dec 13.',
     wd, trail=[HOME, ('/winter-drive/', 'Winter Warmth Drive')], og='winter-drive',
     ld=[faq_ld(wd_faq), ev('Winter Warmth Drive drop-off', '2026-11-01T10:00:00-05:00', '2026-12-06T13:00:00-05:00',
         'Drop off winter essentials for warmth kits for people in need across Ancaster and Hamilton. Sundays 10 AM to 1 PM.', '/winter-drive/')])

# ================================================================ FAMILY NIGHT
fn = simple_hero('Family Night · Launching soon', 'Family <em>Night</em>', 'One evening a month for the whole family. Dinner together, a short talk for the parents, and activities for the kids.',
                 '<div class="btns"><a class="btn btn-gold" href="#signup">Tell me when it starts</a></div>') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">An evening for everyone</h2>{ticks(['A shared community dinner', 'A short, practical talk for parents', 'Crafts, stories and games for children', 'A chance for families to get to know each other'])}
    <p class="lead">Family Night is launching this season. Add your family to the list and we will email you the first date.</p></div>
    <div id="signup">{form('Family Night: interest', CONTACT_FIELDS + [field('Children', 'Number and ages of children', placeholder='e.g. 2 children, ages 5 and 9')], 'Add our family to the list', '/thank-you/', 'fn-form')}</div></div>''') + \
    give_band('Sponsor a Family Night.', 'A sponsor covers dinner and activities for an evening, so every family can come regardless of cost.')
page('/family-night/', 'Family Night | Monthly Family Evenings at Al-Ihsan, Ancaster',
     'Monthly Family Night at Al-Ihsan in Ancaster: dinner, a short talk for parents and activities for kids. Launching soon. Sign up for the first date.',
     fn, trail=[HOME, PROG, ('/family-night/', 'Family Night')])

# ================================================================ HIFZ 2027
hz_faq = [('When does the Hifz program start?', 'The program launches in 2027. Families on the interest list will hear first about dates, levels and how to apply.'),
          ('Is there a cost to join the interest list?', 'No. Adding your child to the list is free and does not commit you to anything.'),
          ('How can I help the program launch?', 'Donations toward the Hifz program cover teachers, materials and classroom space for the first cohort. You can give through our <a href="/donate/">donation page</a>.')]
hz = simple_hero('Upcoming · 2027', 'Hifz <em>Program 2027</em>', "A dedicated path for children to memorize the Qur'an, taught with traditional method and care.",
                 '<div class="btns"><a class="btn btn-gold" href="#interest">Join the interest list</a><a class="btn btn-outline-light" href="/donate/">Help us launch it</a></div>') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">What we are building</h2><p class="lead">Many families in our community have asked for a serious, caring place for their children to memorize the Qur'an. The Hifz program will give students steady daily progress, careful revision, and teachers who track each child's memorization closely.</p>
    {ticks(['Traditional memorization and revision methods', 'Small groups and individual attention', 'Built alongside Enlightened Hearts, so character and understanding grow with memorization'])}</div>
    <div id="interest">{form('Hifz Program 2027: interest list', CONTACT_FIELDS + [field('Child age', "Child's age", 'number'), field("Current memorization", 'How much has your child memorized so far?', placeholder='e.g. Juz Amma'), field('Notes', 'Anything else we should know', 'textarea', rows=3)], 'Join the interest list', '/thank-you/', 'hifz-form')}</div></div>''') + \
    sec('<h2 class="section-title">Questions</h2>' + faq_block(hz_faq), 'bg-white') + \
    give_band('Help launch the Hifz program.', 'Your gift goes toward teachers, Qur\'ans and classroom space for the first students in 2027.')
page('/hifz/', 'Hifz Program 2027 | Qur\'an Memorization for Children, Ancaster',
     "A Hifz program launching in 2027 in Ancaster for children to memorize the Qur'an with traditional method and care. Join the interest list.",
     hz, trail=[HOME, PROG, ('/hifz/', 'Hifz Program 2027')], ld=[faq_ld(hz_faq)])

# ================================================================ DONATE
dn_faq = [('Is Al-Ihsan Learning Centre a registered charity?', f'Yes. We are a registered Canadian charity, registration number {CHARITY_NO}. You can confirm this on the <a href="https://www.canada.ca/en/revenue-agency/services/charities-giving.html">Canada Revenue Agency charities listing</a>.'),
          ('Will I get a tax receipt?', 'Yes. Official tax receipts are issued for eligible donations made through our donation form.'),
          ('Can I give monthly?', 'Yes. Choose the monthly option on the donation form. Monthly gifts let us plan teacher pay and subsidized seats for the whole year.'),
          ('Can my business sponsor a program?', 'Yes. Fill in the sponsorship form on this page and we will send you our sponsorship package with recognition options.')]
funds = [('Enlightened Hearts seats', '$100 sponsors one child for a month, and $900 for the full year. Sponsored seats go to families who could not otherwise attend.'),
         ('Hifz Program 2027', "Teachers, Qur'ans and classroom space for our first cohort of students."),
         ('Winter Warmth Drive', 'Warmth kits of coats, socks, toques and essentials for people in need across Ancaster and Hamilton. <a href="/winter-drive/">See the drive</a>.'),
         ('Caring for the Centre', 'Roof repairs, winterizing and upkeep of the building every program depends on.'),
         ('Ramadan 2027', 'Community iftars and our Ramadan fundraising night.'),
         ('Free community programs', 'Markers of Health, Book Club, Guys Night, Family Night and our Mawlid gatherings.')]
spon_fields = [field('Name', 'Your name', required=True), field('Business or organization', 'Business or organization'), field('Email', 'Email', 'email', required=True), field('Phone', 'Phone', 'tel'),
               field('Interest', 'I am interested in', 'select', options=['Sponsoring a program', 'Sponsoring an event or iftar', 'Founding Pillar (major gift)', 'Matching a campaign', 'Not sure yet']),
               field('Message', 'Anything you would like us to know', 'textarea', rows=3)]
dn = simple_hero('Donate', 'Help keep the Centre <em>open to everyone</em>',
    'Our weekend school, preschool, adult programs and community gatherings run on donations. Most of them are free, and no family is turned away from Enlightened Hearts because of cost. Your gift is what makes that possible.',
    f'<div class="btns"><a class="btn btn-gold" href="{ZEFFY_DONATE}" rel="noopener">Donate now</a><a class="btn btn-outline-light" href="#sponsor">Sponsor as a business</a></div>') + \
    give_band('Choose an amount.', 'Every amount helps. Monthly gifts help the most because they let us plan the year ahead.') + \
    sec(f'''<div class="center"><p class="eyebrow">Where your gift goes</p><h2 class="section-title">What you are <em>funding</em></h2></div>
    <div class="cards">{''.join(f'<article class="card"><h3>{n}</h3><p>{d}</p><a class="more" href="{ZEFFY_DONATE}" rel="noopener">Give to this</a></article>' for n, d in funds)}</div>''') + \
    sec(f'''<div class="split top"><div><p class="eyebrow">Businesses and major donors</p><h2 class="section-title">Sponsor the Centre</h2>
    <p class="lead">Businesses and families can sponsor a program, an event or a Ramadan iftar, with recognition at the Centre, on our website and across our community channels. Our highest level of partnership is the <strong>Founding Pillar</strong>, for gifts of $50,000 or more toward a larger permanent home and the programs it will hold.</p>
    <div class="tiers"><div class="tier feature"><h3>Founding Pillar</h3><div class="price">$50,000+</div><p>Lasting recognition and a direct hand in building the Centre's future.</p></div>
    <div class="tier"><h3>Program and event sponsors</h3><p style="margin-top:8px">Sponsor a program, a Family Night, a Guys Night or an iftar. We will send the full package with all levels.</p></div></div></div>
    <div>{form('Sponsorship enquiry', spon_fields, 'Send me the sponsorship package', '/thank-you/', 'sponsor')}</div></div>''', 'bg-white', 'sponsor') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">Questions about giving</h2>{faq_block(dn_faq)}</div>
    <div><h2 class="section-title">Other ways to help</h2>{ticks(['<a href="/volunteer/">Volunteer</a> your time on Sundays or at events', '<a href="/rentals/">Book the Centre</a> for your event. Rental income supports our programs', 'Share our programs with friends and family'])}</div></div>''')
page('/donate/', 'Donate | Support Al-Ihsan Learning Centre, a Registered Charity',
     "Support Al-Ihsan Learning Centre, a registered charity in Ancaster. Sponsor a child's seat, help launch Hifz 2027, or sponsor as a business.",
     dn, trail=[HOME, ('/donate/', 'Donate')], og='donate', ld=[faq_ld(dn_faq)])

# ================================================================ RENTALS
rt_faq = [('What kinds of events can I host?', 'Nikkahs, engagements, walimas and dinners, aqiqahs, iftars, birthdays and family celebrations, as well as community meetings, workshops and classes.'),
          ('Can you help with decorations?', 'Yes. We work with decorators who can provide backdrops, flowers, stage and table styling. Tell us what you have in mind on the enquiry form and we will connect you.'),
          ('How much does it cost?', 'We keep our rates affordable for the community. Pricing depends on the type of event, how long you need the space and the setup. Send an enquiry and we will reply with a quote.'),
          ('How far ahead should I book?', 'As early as you can. Weekends and Ramadan evenings fill up first.'),
          ('Are there any house rules?', 'The Centre is an Islamic space, so events follow Islamic etiquette, including no alcohol. We ask every guest to treat the space with care.')]
rt_fields = [field('Name', 'Your name', required=True), field('Email', 'Email', 'email', required=True), field('Phone', 'Phone', 'tel', required=True),
             field('Event type', 'Type of event', 'select', required=True, options=['Nikkah', 'Engagement', 'Walima or dinner', 'Aqiqah', 'Iftar', 'Birthday or family celebration', 'Community meeting or workshop', 'Other']),
             field('Preferred date', 'Preferred date', 'date', required=True), field('Alternate date', 'Alternate date', 'date'),
             field('Time', 'Start and end time', placeholder='e.g. 5 PM to 10 PM'), field('Guests', 'Expected number of guests', 'number'),
             field('Decor', 'Would you like help with decor?', 'select', options=['Yes, connect me with a decorator', 'No, we have our own', 'Not sure yet']),
             field('Details', 'Tell us about your event', 'textarea', rows=4)]
rt = simple_hero('Rent the Centre', 'Host your event at <em>Al-Ihsan</em>',
    'Our space is open to the community for nikkahs, engagements, dinners and family gatherings. Rates are affordable, the space is handled with care, and every booking supports the programs that run here.',
    '<div class="btns"><a class="btn btn-gold" href="#enquire">Check availability</a></div>') + \
    sec(f'''<div class="split"><div class="arch">{img('gallery-nikkah', 'The Centre decorated with a floral backdrop for a nikkah ceremony', '(max-width:980px) 90vw, 540px')}</div>
    <div><h2 class="section-title">Events we host</h2>{ticks(['Nikkahs and engagements', 'Walimas, dinners and family celebrations', 'Aqiqahs and birthdays', 'Community and family iftars', 'Meetings, workshops and classes'])}
    <h2 class="section-title" style="margin-top:30px">Decor made easy</h2><p class="lead">We work with decorators for backdrops, flowers, stage and table styling, so you can plan your event in one place.</p></div></div>''') + \
    sec(f'''<div class="split top"><div><p class="eyebrow">Book your date</p><h2 class="section-title">Rental enquiry</h2><p class="lead">Tell us about your event and we will reply with availability and a quote, usually within a few days.</p>
    {ticks(['Affordable community rates', 'A clean, welcoming space handled with care', 'Decorators for backdrops and flowers', 'Rental income supports our programs'])}</div>
    <div>{form('Rental enquiry', rt_fields, 'Send my enquiry', '/thank-you/', 'enquire')}</div></div>''', 'bg-white', 'enquire') + \
    sec('<h2 class="section-title">Rental questions</h2>' + faq_block(rt_faq))
page('/rentals/', 'Event Space Rental in Ancaster | Nikkahs, Dinners and Celebrations | Al-Ihsan',
     'Rent Al-Ihsan in Ancaster for nikkahs, engagements, dinners, aqiqahs and iftars. Affordable rates, and decorators for backdrops and flowers.',
     rt, trail=[HOME, ('/rentals/', 'Rentals')], og='rentals', ld=[faq_ld(rt_faq)])

# ================================================================ EVENTS
past = [('light-we-follow-poster', 'The Light We Follow ﷺ', 'With Shaykh Jamal al-Zahabi · August 23, 2026', True),
        ('past-talal-ahdab', 'Raising an Ethical Human Being', 'Evening lecture with Shaykh Talal Ahdab · July 17, 2026', False),
        ('past-why-islam-is-true', 'Why Islam is True', 'Eight-session course · May to June 2026', False),
        ('past-maghazi', 'The Maghazi: A Family Seerah Program', 'Five-week program · Fall 2025', False),
        ('past-mawlid', 'Milad-un-Nabi: The Prophetic Way', 'Mawlid gathering · September 12, 2025', False),
        ('past-family-festival', 'Family Festival: Renew, Reflect, Reconnect', 'Islamic New Year 1447 · June 29, 2025', True)]
evp = simple_hero('Events', 'Events at <em>the Centre</em>', 'What is coming up, and a look back at the gatherings our community has shared.') + \
    sec(f'''<h2 class="section-title">Coming up</h2><div class="upcoming">
<div class="up"><div class="date"><b>22</b><span>Oct · Thu</span></div><div><h3>Markers of Health, Matters of the Heart</h3><p>7:30 to 8:30 PM · Dr. Rehan Zaidi, ND · Free, in person and live</p></div><a class="btn btn-sm btn-outline" href="/markers-of-health/">Details</a></div>
<div class="up"><div class="date"><b>23</b><span>Oct · Fri</span></div><div><h3>Book Club: The AI Mirror</h3><p>7:00 to 8:30 PM · Conversation and coffee · New joiners welcome</p></div><a class="btn btn-sm btn-outline" href="/book-club/">Sign up</a></div>
<div class="up"><div class="date"><b>5</b><span>Nov · Thu</span></div><div><h3>Markers of Health</h3><p>7:30 to 8:30 PM · Free</p></div><a class="btn btn-sm btn-outline" href="/markers-of-health/">Details</a></div>
<div class="up"><div class="date"><b>1</b><span>Nov · Sun</span></div><div><h3>Winter Warmth Drive drop-off begins</h3><p>Sundays to Dec 6, 10 AM to 1 PM · Coats, socks, toques and essentials</p></div><a class="btn btn-sm btn-outline" href="/winter-drive/">Details</a></div>
<div class="up"><div class="date"><b>Fri</b><span>To Nov 27</span></div><div><h3>The Olive Tree Preschool Circle</h3><p>Fridays 9:30 to 10:30 AM · Ages 0 to 4</p></div><a class="btn btn-sm btn-outline" href="/olive-tree/">Details</a></div>
</div><p style="margin-top:20px">Want event news by email? <a href="/contact/#newsletter">Sign up for updates</a>.</p>''') + \
    sec('<h2 class="section-title">Past events</h2><div class="past">' + ''.join(
        f'<article{" class=contain" if c else ""}>{img(n, "Poster for " + t, "(max-width:600px) 90vw, 280px")}<div><h3>{t}</h3><p>{d}</p></div></article>' for n, t, d, c in past) + '</div>', 'bg-white') + give_band()
page('/events/', 'Events | Al-Ihsan Learning Centre, Ancaster',
     'Upcoming events at Al-Ihsan Learning Centre in Ancaster, including Markers of Health and the Book Club, plus past lectures and gatherings.',
     evp, trail=[HOME, ('/events/', 'Events')])

# ================================================================ ABOUT
gal = [('gallery-circle-story', 'Children gathered for storytime in a learning circle', 'Storytime circle'),
       ('gallery-arts', 'Children painting with watercolours during Islamic arts', 'Islamic arts'),
       ('gallery-storytime-paint', 'A teacher reading a storybook while children paint', 'Stories and crafts'),
       ('gallery-youth-project', 'Youth presenting a research project on the journey of Malcolm X', 'Youth projects'),
       ('gallery-ipad-circle', 'A small group learning together around a tablet', 'Small group learning'),
       ('gallery-fundraiser', 'Families seated at a community fundraiser dinner', 'Community fundraiser'),
       ('gallery-lecture', 'An adult course session in progress at the Centre', 'Courses for adults'),
       ('gallery-media', 'Recording an Islamic lesson at the Centre', 'Lessons and media'),
       ('gallery-signage', 'The Centre interior with the illuminated Al-Ihsan logo', 'Our home in Ancaster')]
ab = simple_hero('About us', 'About <em>Al-Ihsan Learning Centre</em>', 'A community learning centre in Ancaster, teaching traditional Islamic knowledge and serving local families.') + \
    sec(f'''<div class="split"><div class="prose"><h2 class="section-title">Who we are</h2>
    <p>Al-Ihsan Learning Centre (Ihsan Centre) runs classes, gatherings and community support from our home at 487 Shaver Road in Ancaster. Our name comes from ihsan, excellence in worship and in how we treat people, and that is the standard we try to hold ourselves to.</p>
    <p>On Sundays the building fills with children in Enlightened Hearts. During the week we host a preschool circle, adult programs, a book club, brothers' evenings and our monthly Mawlid. Throughout the year we run food drives, iftars, emergency aid and support for new Muslims and newcomer families.</p>
    <p>We are a registered Canadian charity ({CHARITY_NO}), run largely by volunteers and funded by our community.</p></div>
    <div class="arch">{img('about', "A child learning the Qur'an at the Centre", '(max-width:980px) 90vw, 540px')}</div></div>''') + \
    sec('<h2 class="section-title">What we care about</h2><div class="cards">' + ''.join(
        f'<article class="card media">{img(i, a, "(max-width:600px) 92vw, 380px")}<div class="cb"><h3>{t}</h3><p>{d}</p></div></article>' for i, a, t, d in [
            ('hub-gathering', 'Families gathered at a community event at the Centre', 'A place to gather', 'Potlucks, celebrations and evenings that bring families together.'),
            ('hub-khidma', 'Volunteers preparing food donations', 'Serving others', 'Food drives, Ramadan iftars, emergency aid and support for new Muslims.'),
            ('hub-youth', 'Children and youth at the Centre', 'Children and youth', 'A safe, joyful place to make friends and grow in faith and confidence.')]) + '</div>', 'bg-white') + \
    sec('<h2 class="section-title">Life at the Centre</h2><div class="gallery">' + ''.join(
        f'<figure>{img(n, a, "(max-width:600px) 46vw, 370px")}<figcaption>{c}</figcaption></figure>' for n, a, c in gal) + '</div>') + give_band()
page('/about/', 'About Al-Ihsan Learning Centre | Ancaster Islamic Community Centre',
     'Al-Ihsan Learning Centre is a registered charity in Ancaster teaching traditional Islamic knowledge and supporting local families.',
     ab, trail=[HOME, ('/about/', 'About')])

# ================================================================ VOLUNTEER
vol_fields = CONTACT_FIELDS + [field('Interest', 'I would like to help with', 'select', options=['Sunday classroom support', 'Events and setup', 'Food drives and iftars', 'Media, design or admin', 'Anywhere I am needed']),
                               field('Availability', 'Availability', placeholder='e.g. Sunday mornings'), field('Message', 'Anything else', 'textarea', rows=3)]
vo = simple_hero('Volunteer', 'Volunteer <em>with us</em>', 'The Centre runs on volunteers. Whatever your skills and schedule, there is a way to help.') + \
    sec(f'''<div class="split top"><div><h2 class="section-title">Ways to help</h2>{ticks(['Help in the classroom on Sunday mornings', 'Set up and host events and Mawlid gatherings', 'Support food drives, iftars and the winter drive', 'Share skills in media, design, admin or outreach'])}
    <div class="note">High school students: volunteer hours can count toward your community service requirement.</div></div>
    <div>{form('Volunteer sign-up', vol_fields, 'Sign me up', '/thank-you/', 'vol-form')}</div></div>''') + give_band()
page('/volunteer/', 'Volunteer | Al-Ihsan Learning Centre, Ancaster',
     'Volunteer at Al-Ihsan in Ancaster: Sunday classrooms, events, food drives, iftars, media and admin. High school service hours available.',
     vo, trail=[HOME, ('/volunteer/', 'Volunteer')])

# ================================================================ CONTACT
ct_fields = CONTACT_FIELDS + [field('Subject', 'Subject', 'select', options=['General question', 'Enlightened Hearts', 'The Olive Tree', 'Markers of Health', 'Book Club', 'Circle of Light', 'Mawlid schedule', 'Rentals', 'Donations and sponsorship', 'Other']),
                              field('Message', 'Message', 'textarea', required=True)]
ct = simple_hero('Contact', 'Visit or <em>get in touch</em>', 'Send us a message, call, or come by the Centre. We usually reply within a few days.') + \
    sec(f'''<div class="split top"><div>
    <div class="contact-cards">
      <div class="ccard"><span>Address</span><strong>487 Shaver Road, Ancaster, ON</strong></div>
      <div class="ccard"><span>Email</span><a href="mailto:info@ihsancentre.org">info@ihsancentre.org</a></div>
      <div class="ccard"><span>Phone</span><a href="tel:+19058698993">905-869-8993</a></div>
      <div class="ccard"><span>Instagram</span><a href="{INSTAGRAM}" rel="noopener">@alihsancentre</a></div>
      <div class="ccard"><span>WhatsApp</span><a href="{WA_COMMUNITY}" rel="noopener">Join our community</a></div>
      <div class="ccard"><span>Directions</span><a href="https://www.google.com/maps/search/?api=1&amp;query=487+Shaver+Road+Ancaster+ON" rel="noopener">Open in Google Maps</a></div>
    </div>
    <div class="map"><iframe src="https://www.google.com/maps?q=487+Shaver+Road,+Ancaster,+ON&amp;output=embed" title="Map of Al-Ihsan Learning Centre, 487 Shaver Road, Ancaster" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>
    <div>{form('Website message', ct_fields, 'Send message', '/thank-you/', 'contact-form')}</div></div>''') + \
    sec(f'''<div class="split"><div><p class="eyebrow">Email updates</p><h2 class="section-title">Hear about programs first</h2><p class="lead">A short monthly email with new programs, events and ways to help.</p></div>
    <div>{form('Newsletter sign-up', CONTACT_FIELDS[:2], 'Subscribe', '/thank-you/', 'newsletter-form')}</div></div>''', 'bg-white', 'newsletter')
page('/contact/', 'Contact Al-Ihsan Learning Centre | 487 Shaver Road, Ancaster',
     'Contact Al-Ihsan Learning Centre, 487 Shaver Road, Ancaster. Email info@ihsancentre.org or call 905-869-8993, or sign up for email updates.',
     ct, trail=[HOME, ('/contact/', 'Contact')],
     ld=[dict(ORG, **{"@type": "Place", "@id": SITE + "/#place", "geo": {"@type": "GeoCoordinates", "latitude": 43.2125, "longitude": -79.9846}})] if False else None)

# ================================================================ UTILITY PAGES
page('/thank-you/', 'Thank You | Al-Ihsan Learning Centre', 'Thank you for getting in touch with Al-Ihsan Learning Centre.',
     simple_hero('Received', 'Thank you, <em>we got it</em>', 'Your message has reached our team. We will reply by email within a few days.',
                 '<div class="btns"><a class="btn btn-gold" href="/">Back to home</a><a class="btn btn-outline-light" href="/donate/">Support the Centre</a></div>'), noindex=True)
page('/404.html', 'Page Not Found | Al-Ihsan Learning Centre', 'This page could not be found.',
     simple_hero('404', 'We could not find <em>that page</em>', 'It may have moved when we updated the website. These links should get you where you need to go.') +
     sec(program_cards() + '<div class="btns" style="justify-content:center"><a class="btn btn-gold" href="/">Home</a><a class="btn btn-outline" href="/donate/">Donate</a><a class="btn btn-outline" href="/rentals/">Rentals</a><a class="btn btn-outline" href="/contact/">Contact</a></div>'),
     noindex=True)

# ================================================================ sitemap + robots
urls = [p for p, ni in PAGES if not ni]
pri = {'/': '1.0', '/donate/': '0.9', '/enlightened-hearts/': '0.9', '/programs/': '0.8', '/rentals/': '0.8'}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pri.get(u, "0.7")}</priority></url>\n' for u in urls) + '</urlset>\n'
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
print('built', len(PAGES), 'pages;', len(urls), 'in sitemap')
