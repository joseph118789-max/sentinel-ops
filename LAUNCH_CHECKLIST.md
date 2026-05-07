# Sentinel Ops — Launch Checklist

> One list. Follow top to bottom. Site goes live, then BrioHR goes out.

---

## 1. Fill placeholders in `site/index.html`

Replace:
- `[email]`
- `[whatsapp]`
- `[LinkedIn]`
- `[email@domain.com]`

Use:
- real contact email
- WhatsApp in international format, e.g. `60123456789`
- full LinkedIn profile URL

---

## 2. Point DNS

In Cloudflare:
- `A` record: `seeln.site` → `187.127.97.175`
- set to **DNS only** (proxied: false)
- optional: add `www` A record too

---

## 3. Copy files to server

```bash
ssh root@187.127.97.175
mkdir -p /var/www/sentinel-ops
cd /var/www/sentinel-ops
```

Copy into `/var/www/sentinel-ops`:
- `index.html`
- `docker-compose.yml`

From local:
```bash
scp site/index.html site/docker-compose.yml root@187.127.97.175:/var/www/sentinel-ops/
```

---

## 4. Check port and start container

```bash
ssh root@187.127.97.175
ss -ltnp | grep :8080
```

- If 8080 is free → use `8080:80` in docker-compose.yml
- If 8080 is busy → use `8092:80` in docker-compose.yml and update nginx `proxy_pass` accordingly

```bash
mkdir -p /var/www/sentinel-ops
cd /var/www/sentinel-ops
docker compose up -d
curl http://127.0.0.1:<port>   # verify container is serving before touching nginx
```

Expected: HTML of the landing page returns, container stays up.

---

## 5. Install nginx reverse proxy

Copy `deploy/nginx-sentinel-ops` to:
```
/etc/nginx/sites-available/sentinel-ops
```

Then:
```bash
ln -sf /etc/nginx/sites-available/sentinel-ops /etc/nginx/sites-enabled/sentinel-ops
nginx -t && systemctl reload nginx
```

---

## 6. Test HTTP

Open:
- `http://seeln.site`
- `http://www.seeln.site` (if www configured)

---

## 7. Enable SSL (after DNS propagates)

```bash
ssh root@187.127.97.175
apt install -y certbot python3-certbot-nginx
certbot --nginx -d seeln.site -d www.seeln.site
```

Or without www:
```bash
certbot --nginx -d seeln.site
```

---

## 8. Final live test

Check:
- site loads over HTTPS
- all links work (email, WhatsApp, LinkedIn)
- mobile layout looks correct
- contact details are accurate

---

## 9. Send BrioHR

Use short message + site link. No PDF on first touch.

Message:
> Hi [Name] — I'm building Sentinel Ops, lean managed cybersecurity for teams that need better monitoring, hardening, and security reporting without building a full SOC. Short overview: [seeln.site]. If it looks relevant, open to a quick conversation?

Log the send. Bring results back.

---

## Quick rollback

```bash
cd /var/www/sentinel-ops
docker compose down
```

---

*Stack ready. Outreach is the only remaining move.*