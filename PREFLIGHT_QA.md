# Sentinel Ops — Live Preflight QA Checklist

> Run this right before sending BrioHR. Every box must be YES before you send.

---

## Content
- [ ] `index.html` placeholders all replaced
- [ ] email address is correct
- [ ] WhatsApp number is correct
- [ ] LinkedIn URL is correct
- [ ] no `[placeholder]` text remains anywhere on page
- [ ] spelling / company name looks clean

## Container
- [ ] `docker compose up -d` completed without errors
- [ ] `docker ps` shows the landing page container running
- [ ] `curl http://127.0.0.1:8080` returns the page HTML
- [ ] page loads locally from server on port 8080

## Nginx
- [ ] nginx site file copied to `/etc/nginx/sites-available/sentinel-ops`
- [ ] symlink exists in `/etc/nginx/sites-enabled/`
- [ ] `nginx -t` passes
- [ ] `systemctl reload nginx` succeeds
- [ ] `http://seeln.site` loads the landing page

## DNS
- [ ] `seeln.site` resolves to `187.127.97.175`
- [ ] Cloudflare is set to **DNS only** (proxied: false)
- [ ] if using `www`, `www.seeln.site` also resolves correctly

## SSL
- [ ] certbot completed successfully
- [ ] `https://seeln.site` loads without certificate warning
- [ ] if using `www`, `https://www.seeln.site` also works
- [ ] HTTP redirects cleanly to HTTPS

## Links / Actions
- [ ] email link opens correct email address
- [ ] WhatsApp link opens correct number
- [ ] LinkedIn link opens correct profile
- [ ] no broken buttons or dead links

## Visual Check
- [ ] hero section looks normal on desktop
- [ ] page looks normal on mobile
- [ ] no overlapping text
- [ ] no missing images / icons
- [ ] page loads fast enough

## Final Go / No-Go
- [ ] site opens on mobile network, not just server / local cache
- [ ] Joseph would be comfortable sending this to a prospect right now

---

**Go rule:** Every box YES → send BrioHR. Any box NO → fix first, then send.

---

*Preflight clean = send. Preflight dirty = fix first.*