# JBA Website — Project Skill Reference

## Overview
Personal portfolio site for Jennifer BA. Static HTML/CSS/JS site hosted on GitHub Pages.

- **Live URL:** https://jenniferba-lei.github.io (GitHub user site)
- **Repo:** https://github.com/JenniferBa-Lei/JenniferBa-Lei.github.io
- **Local path:** `/Users/jenniferba/Documents/AI_Agents/JBA Website/`
- **Preview server:** Python http.server on port 7701

---

## GitHub Deployment

### Important: Token Security
- GitHub secret scanning auto-revokes tokens pasted in AI chats (Anthropic is a partner)
- Always store the token in `~/.gh_token` and reference it as `$(cat ~/.gh_token)`
- Never paste the raw token value in any chat or commit message

### Push Changes to GitHub
```bash
cd "/Users/jenniferba/Documents/AI_Agents/JBA Website"
git add .
git commit -m "your message"
git push https://$(cat ~/.gh_token)@github.com/JenniferBa-Lei/JenniferBa-Lei.github.io.git main
```

### First-time setup (if remote not set)
```bash
git init
git remote add origin https://$(cat ~/.gh_token)@github.com/JenniferBa-Lei/JenniferBa-Lei.github.io.git
git branch -M main
git push -u origin main
```

### GitHub Pages CDN Cache
- After pushing, live site may take 2-5 minutes to update
- Use incognito window (Cmd+Shift+N) to bypass browser cache
- Or DevTools → Network tab → check "Disable cache" → reload

---

## Site Structure

### Files
- `index.html` — single-page site with all sections
- `style.css` — all styles
- `script.js` — navbar scroll, reveal animations, contact form handler
- `watermark.py` — Python script to apply watermarks to artwork images
- `images/watercolor/` — watermarked watercolor painting JPEGs (14 files)
- `images/logo/` — watermarked logo PNGs (8 files)

### Nav Structure
```
About | Portfolio (dropdown: Software / Arts / Logos) | Resume | Contact
```

### Sections (in order)
1. `#hero` — hero with tagline "Software Engineer · Painter · Designer"
2. `#about` — about + interests
3. `#projects` — software portfolio cards (section-alt bg)
   - `#arts` — watercolor paintings subsection
   - `#logos` — logo designs subsection
4. `#opportunities` — Resume / skills section
5. `#contact` — contact section (section-alt bg)

---

## Contact Form (Formspree)
Form submissions go to **JenniferBA2022@gmail.com** via Formspree.

- **Formspree endpoint:** `https://formspree.io/f/xlgakryj`
- Wired in `script.js` via `fetch` (no `action` attribute needed on the `<form>` tag)
- Free tier: 50 submissions/month
- To change the destination email: update the email in Formspree dashboard at formspree.io

**Email on page:** `JenniferBA2022@gmail.com`
**GitHub:** `github.com/JenniferBa-Lei`
**LinkedIn:** `linkedin.com/in/jennifer-ba-lei`

---

## Artwork: Watermarks

### Script: `watermark.py`
Run from the JBA Website folder:
```bash
cd "/Users/jenniferba/Documents/AI_Agents/JBA Website"
python3 watermark.py
```

### Watermark settings (current)
- Text: `JBA`
- Opacity: 50 (out of 255) — subtle
- Grid: 3 columns × 2 rows = 6 watermarks per painting
- Logos: 2 columns × 2 rows = 4 watermarks
- Rotation: -35 degrees
- Font size: ~4.5% of image width

### Source folders (originals — never committed to repo)
- Paintings: `/Users/jenniferba/Documents/My Art Portfolios/Watercolor/`
- Logos: `/Users/jenniferba/Documents/My Art Portfolios/Logo/` (files only, not subfolders)

### Output folders (committed to repo)
- Paintings: `images/watercolor/` (JPEG)
- Logos: `images/logo/` (PNG, preserves transparency)

### Adding new artwork
1. Add the original file to the source folder
2. Add an entry to `WATERCOLOR_MAP` or `LOGO_MAP` in `watermark.py`
3. Run `python3 watermark.py`
4. Add an `<article class="art-card">` block in `index.html` (Arts or Logos subsection)
5. Push to GitHub

---

## Arts Section Layout
- Paintings and logos are displayed as cards using `.art-card` class
- Grid: `projects-grid` (auto-fill, minmax 280px)
- Painting cards use `object-fit: cover` (`.art-card-img`)
- Logo cards use `object-fit: contain` with padding (`.art-card-img--logo`)
- Subsection headers (Arts, Logos) use `.subsection-title` class with border-top separator

---

## Watercolor Paintings (14 total)
| File | Title | Dimensions |
|------|-------|-----------|
| rose.jpg | Rose | 12×15 in |
| whiterose.jpg | White Rose | 12×15 in |
| tulip.jpg | Tulip | 12×15 in |
| waterlily.jpg | Water Lily | 12×15 in |
| sunflowers.jpg | Sunflowers | 12×15 in |
| yellowflower.jpg | Yellow Flower | 12×15 in |
| wildflowers.jpg | Wild Flowers | 7.5×9 in |
| hydrangea.jpg | Hydrangea | 12×15 in |
| lily.jpg | Lily | 12×15 in |
| cat.jpg | Cat | 7.5×11 in |
| tiger.jpg | Tiger | 7.5×11 in |
| goldenfish.jpg | Golden Fish | 7.5×11 in |
| lele.jpg | LeLe | 7.5×11 in |
| ic.jpg | IC | 9×12 in |

## Logo Designs (8 total)
| File | Title | Tags |
|------|-------|------|
| nacbc-red.png | NACBC Logo | Logo · Red |
| nacbc-glow-red.png | NACBC Logo with Glow | Logo · Red |
| nacbc-glow-white.png | NACBC Logo with Glow | Logo · White |
| nub7-v2.png | NuB7 Logo | Logo · v2 |
| nub7-v3.png | NuB7 Logo | Logo · v3 |
| nub7-v4.png | NuB7 Logo | Logo · v4 |
| red-green-white.png | RED Logo | Logo · Green/White |
| red-red-white.png | RED Logo | Logo · Red/White |

---

## Local Preview
```bash
cd "/Users/jenniferba/Documents/AI_Agents/JBA Website"
python3 -m http.server 7701
# Open: http://localhost:7701
```

Or use the Claude Code preview server (configured in Investment_Monitor_Tool/.claude/launch.json as "jba-website" on port 7701).
