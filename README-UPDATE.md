# Ihsan Centre Website Update (August 2026)

## What changed
1. New modern design: deep navy, cream, and bronze gold palette drawn from the 2026-27 campaign flyers, arch-shaped image frames, Fraunces display type, scroll reveals, sticky nav.
2. Enlightened Hearts 2026-27 is now the main feature: registration pill, flyer, program highlights, dates (Sundays, Sept 13, 2026 to June 13, 2027), fees ($100/month or $900/year, sibling rates, subsidized seats), and multiple register CTAs.
3. Age-appropriate learning revamped to the new five-level structure: Fig Tree (4 to 5), Grape Tree Levels 1 and 2 (6 to 9), Pomegranate Tree (9 to 11), Date Palm Tree (12 to 16). The Olive Tree is now its own Friday preschool program.
4. New section: The Olive Tree Preschool Circle and Story Time (ages 0 to 4, Fridays 9:30 to 10:30 AM, Sept 18 to Nov 27, 2026, ten classes, no class Oct 9, parent supported), with flyer and register link.
5. New featured event: The Light We Follow with Shaykh Jamal al-Zahabi, Sunday Aug 23, 2026, 2:00 to 5:00 PM, doors 1:45 PM, plus a site-wide announcement bar.
6. New Volunteer With Us section routing to info@ihsancentre.org.
7. All STEM Summer Camp content removed (hero stat, nav item, camp section, meta tags).
8. All teacher names removed.
9. All contact, question, and form actions route to info@ihsancentre.org.
10. Registration links added throughout (17 Zeffy CTAs across nav, hero, sections, footer, and a sticky mobile bar).

## SEO
- Updated title, description, keywords, Open Graph, Twitter cards, geo tags, canonical.
- JSON-LD structured data: EducationalOrganization, Course (Enlightened Hearts), and two Events (The Light We Follow, The Olive Tree fall session). Eligible for Google event and course rich results.
- sitemap.xml and robots.txt included.

## Mobile
Fully responsive: collapsible menu, stacked layouts, sticky bottom Register bar on phones, safe-area padding, reduced-motion support, keyboard focus styles.

## Deploying to GitHub Pages
1. Replace index.html at the repo root with this one.
2. Copy the three new files in assets/ into your existing assets/ folder:
   - enlightened-hearts-2026-flyer.jpg
   - olive-tree-fall-2026-flyer.jpg
   - olive-tree-storytime.jpg
3. Add sitemap.xml and robots.txt to the repo root.
4. Keep the existing assets folder (logo.png, about.jpg, hero-bg.jpg, hub-*.jpg, enlightened-hearts.jpg are still referenced). You can delete camp.jpg and the tree-*.jpg images if you want to slim the repo; nothing references them anymore.
5. Commit and push. GitHub Pages will publish automatically.

## After the Aug 23 event
Remove the announcement bar (the div with class "announce" near the top of body) and, if you like, swap the featured event section for the next Mawlid.

## Note
The Light We Follow PDF poster did not come through in the upload, so the event uses a styled card instead. If you want the poster embedded or downloadable, add the PDF to assets/ as the-light-we-follow-poster.pdf and add a link button in the event-ctas div.
