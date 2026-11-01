# GK / GS Online Mock Test — VS Code se edit, link apne aap update

Ek baar setup karne ke baad: **VS Code mein change → Commit → Sync** karte hi aapka live link ~1 minute mein update ho jayega. Har baar dobara upload nahi karna.

## Folder kya hai
| File / Folder | Kya hai |
|---|---|
| `index.html` | Page ka structure (header, home, exam, result) |
| `css/style.css` | Design, rang, dark mode, print/PDF styling |
| `js/app.js` | Exam logic, music/sound, certificate, report, topics ke study tips (`TP`) |
| `js/data.js` | Saare questions (ek question = ek line) |
| `sw.js`, `manifest.webmanifest`, `icons/` | Offline + "Install App" |
| `tools/` | (Optional) Python se questions dobara banane ke liye |
| `.github/workflows/pages.yml` | Auto-deploy ka setup (ise na chhedein) |

## Ek baar ka setup (15 minute)
1. **VS Code** (code.visualstudio.com) aur **Git** (git-scm.com) install karein. GitHub par free account banayein (github.com).
2. VS Code mein **File → Open Folder** se ye folder kholein.
3. Left bar mein **Source Control** (branch icon) → **Initialize Repository** → message likhein `first version` → **Commit**.
4. **Publish Branch / Publish to GitHub** dabayein → naam: `gk-mock-test` → **Public repository** chunein → sab files select rakhein.
5. GitHub par apne repo mein jayein: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
6. **Actions** tab mein "Deploy website to GitHub Pages" hara ✔ hone tak 1–2 minute rukein.
7. Aapka link: `https://<aapka-username>.github.io/gk-mock-test/` ✅

## Roz ka kaam (har change ke baad)
1. File edit karein → **Ctrl+S**.
2. **Source Control** → message likhein (jaise `new questions added`) → **Commit** → **Sync Changes** (push).
3. 1 minute baad wahi link update. Browser mein **Ctrl+Shift+R** (phone par reload) karein.

Local preview (push se pehle dekhne ke liye): extension **Live Server** install karein → `index.html` par right-click → **Open with Live Server**.

## Kya kahan badlein
- **Question/option/answer badalna:** `js/data.js` mein us line ko edit karein. `a` = sahi option ka number (0=A, 1=B, 2=C, 3=D).
- **Naya set jodna:** `js/data.js` mein naya `[ ... ],` block jodein (har set mein 100 questions). Bihar Police jaise alag timer wale sets ke liye `NG` ke baad rakhein.
- **Rang/design:** `css/style.css` ke upar `:root{--navy:...;--or:...}` variables.
- **Study tips / topics:** `js/app.js` mein `TP` list.
- **Exam time:** `js/app.js` mein `TL=()=>cur>=NG?7200:3600` (seconds).
- **Python se questions dobara banana (optional):** `tools/data1.py` / `tools/data2.py` edit karke `python tools/make_data.py` chalayein — ye `js/data.js` badal dega.

## Dusra option: Netlify / Cloudflare Pages (GitHub se connect)
Netlify → *Add new site → Import from Git* → apna repo chunein → Build command khali, Publish directory `.` → Deploy. Iske baad bhi har `git push` par site apne aap update hogi. (Is case mein GitHub Pages wala step 5 zaroori nahi.) Custom domain wahin Domain settings se.

## Dikkat aaye to
- Actions mein laal ✘: us par click karke error padhein; sabse aam wajah — Settings → Pages mein Source "GitHub Actions" nahi chuna.
- Purana version dikh raha: Ctrl+Shift+R; installed app ko band karke dobara kholein.
- Ye sirf practice material hai; CSBC/RRB/SSC se koi sambandh nahi.
