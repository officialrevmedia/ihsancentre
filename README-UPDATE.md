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


## Round 2 changes (this package)
1. Logo fixed: the header and footer now use an inline SVG logo mark, so the logo always renders regardless of the assets folder. The favicon is also inline SVG now. Your existing assets/logo.png is still referenced only in the structured data for Google.
2. Hero photo replaced with the learning circle photo of the Centre (assets/hero-gathering.jpg).
3. The Light We Follow now has a real poster (assets/light-we-follow-poster.jpg, also sized for Instagram at 1080x1350). It replaces the placeholder graphic in the featured event card and opens full size on tap. Feel free to use the same file for WhatsApp and Instagram promotion.
4. New "Life at Ihsan Centre" photo gallery (11 photos) between the About section and Gatherings.
5. New "Previous events" section with six past event posters: Raising an Ethical Human Being (Jul 2026), Why Islam is True (May to Jun 2026), Isra wal Mi'raj (Jan 2026), The Maghazi (Fall 2025), Milad-un-Nabi (Sept 2025), and Reflect Renew Reconnect (Jun 2025).
6. Footer links added for the gallery and previous events.

## Files to copy into your repo for this round
All of assets/ in this zip (18 new gallery and poster images plus the 3 from round 1), plus index.html at the root.


## Round 3 changes (this package)
1. Real logo installed. The header uses the full AL-IHSAN LEARNING CENTRE lockup (assets/logo.png), the footer uses a reversed version tuned for the dark navy background (assets/logo-light.png), and the favicon plus iOS home screen icon use the star medallion on its own (assets/logo-mark.png, assets/apple-touch-icon.png). The white background was removed from all of them, so they are transparent PNGs and sit cleanly on any colour.
2. Four images the old site relied on (about.jpg, hub-gathering.jpg, hub-khidma.jpg, hub-youth.jpg) were rebuilt from your uploaded photos, so this package is now fully self-contained. Nothing depends on files already on the server.
3. Removed three duplicate photos that appeared in both the hub cards and the gallery, and added a course session photo, so every photo on the site now appears exactly once.

## Verified before packaging
- 28 of 28 image references resolve to real, valid image files. No broken links, no orphan files.
- All 28 img tags have descriptive alt text.
- HTML tag structure validated, no unclosed tags.
- No em dashes anywhere in the file.

## Upload instructions (important)
Unzip this package on your computer FIRST, then in GitHub use Add file, Upload files and drag in index.html, sitemap.xml, robots.txt and the whole assets folder together in one go. Uploading files individually is what corrupted index.html last time. Confirm index.html sits at the repo root and opens as readable HTML on GitHub before you check the live site.


## Round 4 changes (this package)
1. The Light We Follow now uses your correct poster (the Green Dome design with Shaykh Jamal al-Zahabi's photo), on the left side of the featured event card.
2. Removed the Traversing the Cosmos: Isra wal Mi'raj event from Previous events, and deleted its image file.
3. Reflect, Renew, Reconnect is no longer cropped. That poster is a wide banner, and it was being forced into a tall 4:5 card frame. It now spans two columns and displays complete. On phones it drops back to one column, still uncropped.
4. Added the Family Festival poster (Islamic New Year 1447, Ancaster Fairgrounds) to Previous events.
5. Added the community fundraiser photo to the gallery.

Previous events now reads, newest first: Raising an Ethical Human Being, Why Islam is True, The Maghazi, Milad-un-Nabi, Family Festival, Reflect Renew Reconnect.

Note: the Family Festival poster and the Reflect Renew Reconnect banner are both for the same June 29, 2025 event. Both are currently shown as separate cards. If you would rather show only one, delete whichever article block you do not want from the past-grid section.


## Round 5 changes (this package)

### 1. Four levels, not five
Every reference to "five levels" is now "four levels":
- Hero stat block: 5 Levels is now 4 Levels
- Section heading: "Four levels, rooted in tradition"
- Button: "Explore the Four Levels"
- Course structured data for Google: "across four age-based levels"
- The Grape Tree card previously read "Two levels (ages 6 to 7 and 8 to 9)", which
  contradicted a four-level count. It now reads "Two age groups (6 to 7 and 8 to 9)",
  so the age split is still shown but the total stays at four.

The four level cards are unchanged: The Fig Tree (4 to 5), The Grape Tree (6 to 9),
The Pomegranate Tree (9 to 11), The Date Palm Tree (12 to 16).

The flyer artwork has also been corrected. The navy band near the bottom of
assets/enlightened-hearts-2026-flyer.jpg read "Five Levels, Rooted in Tradition" and now reads
"Four Levels, Rooted in Tradition". The flyer is set in Fraunces, so the original typeface was
used for the replacement word, matched on weight, optical size and letter-spacing against the
surrounding text. "Levels, Rooted in Tradition" is untouched original artwork, nudged 9 pixels
right to make room for the wider word. Nothing else on the flyer changed, and the registration
QR code still resolves to the correct Zeffy link.

The filename is unchanged, so the flyer also updates automatically wherever it is used as the
link preview image for Facebook, WhatsApp and X. If you re-export the flyer from your own
design file later, just save over the same path and filename.

The four tree columns at the bottom of the flyer are unchanged, including the Grape Tree's
"Level 1: Ages 6 to 7 / Level 2: Ages 8 to 9" split. That now matches the "two age groups"
wording on the website.

### 2. The Light We Follow is finished
- The featured event section has been removed from the top of the page.
- The event now appears as the newest card in Previous events, dated August 23, 2026,
  reusing the same poster. That card uses a new "tall" style so the 2:3 poster shows
  complete instead of being cropped into the 4:5 card frame.
- The event's Google structured data block has been deleted, so the site no longer
  advertises a past event as upcoming.
- The Zeffy ticket link for the event has been removed from the footer.
- The Open Graph description no longer mentions the event.
- The old #events anchor still works. It now lands on the Gatherings and Programs
  section, so the Events nav link and any existing shared links keep working.

### 3. Registration push
- The announcement bar is now a continuous scrolling bar with three messages:
  Enlightened Hearts registration, the four levels and fees, and The Olive Tree.
  It pauses when you hover or tab into it, and collapses to a single static line for
  visitors who have reduced motion turned on.
- The main hero button now goes straight to the Zeffy registration form instead of
  scrolling down the page. The second button goes to the program details.
- A highlighted note was added under the Enlightened Hearts heading: classes begin
  September 13, 2026, register now, with the info@ihsancentre.org address for questions.

### Verified before packaging
- 29 of 29 image references resolve to real files. No broken links, no orphan files.
- Flyer edit confined to the heading area, background matched to the surrounding navy,
  and the QR code re-tested and still decoding to the Zeffy registration page.
- All 27 img tags have descriptive alt text.
- All three JSON-LD blocks parse as valid JSON.
- Every internal #anchor link resolves to an element that exists.
- HTML tag structure balanced, no unclosed tags. No em dashes anywhere.
- Rendered and checked at desktop and mobile widths, and with reduced motion enabled.

### Upload instructions
Unzip this package on your computer FIRST, then in GitHub use Add file, Upload files and
drag in index.html, sitemap.xml, robots.txt and the whole assets folder together in one go.
Uploading files one at a time is what corrupted index.html previously. Confirm index.html
sits at the repo root and opens as readable HTML on GitHub before checking the live site.
