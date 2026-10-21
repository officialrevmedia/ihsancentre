# ihsancentre.org

Static site for Al-Ihsan Learning Centre, served by GitHub Pages at www.ihsancentre.org.

- Pages are pre-rendered HTML (no client-side rendering).
- Edit content in `_build/pages.py`, styles in `_build/site.css`, then run `python3 _build/build.py && python3 _build/pages.py` from the repo root (needs Python 3 and Pillow). This regenerates every page, `sitemap.xml` and `robots.txt`.
- Images live in `assets/img/` as WebP, with `-600` variants for phones.
- Forms post to FormSubmit (formsubmit.co) and arrive at info@ihsancentre.org.
