# Deployment Guide

This site is a static HTML/CSS/JS bundle. It can be deployed anywhere that serves static files. Below are recipes for the most common targets, with **GitHub Pages** as the default.

---

## Option 1 — GitHub Pages (recommended, free)

The repo includes a workflow at `.github/workflows/deploy.yml` that auto-deploys on every push to `main`.

### One-time setup

1. **Create the repo on GitHub** and push this code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-org>/ihsan-centre-website.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repo → **Settings → Pages**
   - Under **Build and deployment**, set **Source** to **GitHub Actions**

3. **Wait for the first deploy**
   - Go to the **Actions** tab → watch the "Deploy to GitHub Pages" workflow run
   - When it completes, your site will be live at `https://<your-org>.github.io/<repo>/`

### Custom domain (`ihsancentre.org`)

1. The `CNAME` file in this repo already contains `ihsancentre.org` — that tells GitHub Pages which domain to serve.

2. **At your DNS provider** (Cloudflare, GoDaddy, Namecheap, etc.), add these records:

   For an **apex domain** (`ihsancentre.org`):
   ```
   Type    Name    Value
   A       @       185.199.108.153
   A       @       185.199.109.153
   A       @       185.199.110.153
   A       @       185.199.111.153
   AAAA    @       2606:50c0:8000::153
   AAAA    @       2606:50c0:8001::153
   AAAA    @       2606:50c0:8002::153
   AAAA    @       2606:50c0:8003::153
   ```

   For the `www` subdomain:
   ```
   Type    Name    Value
   CNAME   www     <your-org>.github.io.
   ```

3. **Back on GitHub** → Settings → Pages → enter `ihsancentre.org` in the Custom domain field, save, then tick **Enforce HTTPS** once the certificate provisions (usually 5–30 min).

### Updating the site

Just commit and push:
```bash
git add .
git commit -m "Update hero copy"
git push
```
The workflow re-runs automatically. New version is live in ~1 minute.

---

## Option 2 — Netlify (drag-and-drop or git)

### Drag-and-drop (no git needed)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the entire project folder onto the page
3. Done — you'll get a `*.netlify.app` URL immediately

### Git-based (auto-deploy)
1. Push this repo to GitHub
2. Netlify → **Add new site → Import from Git** → pick your repo
3. **Build command:** *(leave blank)*
4. **Publish directory:** `.` (the root)
5. Deploy

**Custom domain:** Netlify → Domain management → Add custom domain → follow their DNS instructions.

---

## Option 3 — Cloudflare Pages

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**
2. Pick the repo
3. **Framework preset:** None
4. **Build command:** *(leave blank)*
5. **Build output directory:** `/` (root)
6. Deploy

**Custom domain** is configured under the project's **Custom domains** tab. If your DNS is already on Cloudflare, it's a one-click setup.

---

## Option 4 — Vercel

1. [vercel.com/new](https://vercel.com/new) → import the GitHub repo
2. **Framework preset:** Other
3. **Build command:** *(leave blank)*
4. **Output directory:** `.`
5. Deploy

---

## Option 5 — Any static host / your own server

Just upload the contents of this folder (all files at the root, plus `assets/`) to your web root. Make sure:

- `index.html` is at the document root
- `assets/` is at the same level as `index.html`
- The server serves `.html`, `.jpg`, `.png`, `.xml`, and `.txt` with correct MIME types (every modern web server does this by default)

### Recommended server config

**Nginx:**
```nginx
server {
    listen 80;
    listen [::]:80;
    server_name ihsancentre.org www.ihsancentre.org;
    return 301 https://ihsancentre.org$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name ihsancentre.org;

    root /var/www/ihsan-centre;
    index index.html;

    # Cache assets aggressively
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Don't cache HTML
    location ~ \.html$ {
        expires -1;
        add_header Cache-Control "no-cache, must-revalidate";
    }

    error_page 404 /404.html;

    # Security headers
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
}
```

**Apache** (`.htaccess`):
```apache
# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# 404
ErrorDocument 404 /404.html

# Cache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType application/javascript "access plus 7 days"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
```

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Custom domain shows "Improperly configured" | DNS propagation takes 10–60 min. Re-check in an hour. |
| HTTPS button greyed out on GitHub Pages | Wait for the cert to provision (up to 24h, usually <30 min). |
| Images broken on GitHub Pages | Make sure paths use `assets/foo.jpg` (relative), not `/assets/foo.jpg` (absolute) — relative paths already used in `index.html`. |
| Site shows the old version | Hard-refresh (`Cmd/Ctrl + Shift + R`) or clear CDN cache. |
| Sitemap not picked up by Google | Submit `https://ihsancentre.org/sitemap.xml` in [Google Search Console](https://search.google.com/search-console). |

---

## Post-deploy checklist

- [ ] Site loads at `https://ihsancentre.org`
- [ ] `https://www.ihsancentre.org` redirects to the apex
- [ ] HTTPS is enforced (no insecure-content warnings)
- [ ] Mobile layout looks correct (test on a real phone)
- [ ] Donation button (Zeffy) opens in a new tab and works
- [ ] WhatsApp floating button opens the community chat
- [ ] Instagram link works
- [ ] Map shows the correct location
- [ ] Submit sitemap to [Google Search Console](https://search.google.com/search-console) and [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [ ] (Optional) Add Google Analytics / Plausible snippet before `</head>`
