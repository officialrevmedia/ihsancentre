# Al-Ihsan Learning Centre — Website

Official website for **Al-Ihsan Learning Centre** (Ihsan Centre), a registered Canadian charity offering Islamic weekend education, Qur'an circles, community gatherings, and service initiatives in Ancaster, Ontario.

🌐 **Live site:** [ihsancentre.org](https://ihsancentre.org)

> *Preserve Tradition. Build Community. Enlighten Hearts.*

---

## 📦 What's in this repo

This is a **static, single-page website** — no build step, no framework. Just HTML, CSS, and a tiny bit of vanilla JavaScript. That makes it cheap, fast, and trivial to host anywhere.

```
.
├── index.html              # The full site (HTML + inline CSS/JS)
├── 404.html                # Friendly fallback page
├── robots.txt              # Search engine crawler rules
├── sitemap.xml             # Sitemap for SEO
├── CNAME                   # Custom domain for GitHub Pages
├── .nojekyll               # Tell GitHub Pages to skip Jekyll processing
├── assets/                 # Images (logo, hero, programs, etc.)
│   ├── logo.png
│   ├── hero-bg.jpg
│   ├── about.jpg
│   ├── camp.jpg
│   ├── enlightened-hearts.jpg
│   ├── support-bg.jpg
│   ├── hub-gathering.jpg
│   ├── hub-khidma.jpg
│   ├── hub-youth.jpg
│   ├── tree-olive.jpg
│   ├── tree-fig.jpg
│   ├── tree-grape.jpg
│   ├── tree-pomegranate.jpg
│   └── tree-date.jpg
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions → GitHub Pages
├── DEPLOY.md               # Step-by-step deployment guide
├── LICENSE                 # MIT licence (code only)
├── .gitignore
└── README.md
```

---

## ✨ Features

- **Fully responsive** — mobile, tablet, desktop, with a slide-in mobile menu
- **SEO ready** — meta tags, Open Graph, Twitter Cards, canonical URL, JSON-LD structured data (Organization, Event, Course), `robots.txt`, and `sitemap.xml`
- **Accessible** — skip link, ARIA labels, focus states, semantic HTML, `prefers-reduced-motion` support
- **Fast** — no framework, no bundler, real `<img>` files with `loading="lazy"`, system-font fallbacks
- **Brand-consistent** — navy/copper/cream palette, Cormorant Garamond + DM Sans + Amiri typography

---

## 🛠️ Local development

No tooling required. Just clone and open the file:

```bash
git clone https://github.com/<your-org>/ihsan-centre-website.git
cd ihsan-centre-website
```

Then either:

```bash
# Option A — open directly in your browser
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows

# Option B — run a tiny static server (recommended for testing relative paths)
python3 -m http.server 8000
# then visit http://localhost:8000

# Option C — Node
npx serve .
```

---

## 🚀 Deployment

The repo ships with a GitHub Actions workflow that automatically deploys to **GitHub Pages** on every push to `main`.

See **[DEPLOY.md](./DEPLOY.md)** for step-by-step instructions, including:

- GitHub Pages setup
- Custom domain (`ihsancentre.org`) configuration
- DNS records you'll need at your registrar
- Alternative deploy targets (Netlify, Cloudflare Pages, Vercel)

Quick version:

1. Push this repo to GitHub.
2. **Settings → Pages** → Source: *GitHub Actions*.
3. Add `ihsancentre.org` as the custom domain.
4. Point your DNS at GitHub Pages (see `DEPLOY.md`).

---

## ✏️ Editing content

All content lives in **`index.html`**. Common edits:

| What | Where to look in `index.html` |
|---|---|
| Hero headline | `<section class="hero">` → `<h1>` |
| About copy | `<section class="about">` → `<p class="about-body">` |
| Class group teachers / descriptions | `<section class="programs">` → each `<article class="program">` |
| Events (Circle of Light, Mawlid, etc.) | `<section class="events">` → each `<article class="event">` |
| Summer camp dates / price | `<section class="camp">` → `.camp-meta` and `.camp-price` |
| Contact details | `<section class="contact">` → `.contact-list` |
| Footer links / charity number | `<footer class="footer">` |
| Brand colours / fonts | `:root { --navy: ...; --copper: ...; }` near the top of `<style>` |

To replace an image, drop a new file with the same name into `assets/` (or update the `src` in `index.html`).

---

## 🔍 SEO & analytics

- `sitemap.xml` and `robots.txt` are at the root.
- Update the `<lastmod>` date in `sitemap.xml` whenever the homepage content changes meaningfully.
- To add Google Analytics / Plausible / etc., paste the snippet just before `</head>` in `index.html`.

---

## 📝 Licence

The **code** in this repository is released under the [MIT Licence](./LICENSE).

The **content** (text, images, logos, the Al-Ihsan Learning Centre name and brand) is © Al-Ihsan Learning Centre and all rights are reserved. Please do not reuse the brand assets without permission.

---

## 🤝 Contact

- 📍 487 Shaver Road, Hamilton, ON
- ✉️ [info@ihsancentre.org](mailto:info@ihsancentre.org)
- 📞 [905-869-8993](tel:9058698993)
- 📷 [@alihsancentre](https://www.instagram.com/alihsancentre/)
- 💬 [WhatsApp Community](https://chat.whatsapp.com/L8RwZr6FlDSI9dMjtM22IJ)

Registered Canadian Charity · **763444353RR0001**
