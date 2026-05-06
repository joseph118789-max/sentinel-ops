# Onboarding Checklist — Sentinel Ops

## Purpose

This checklist ensures every client gets the same structured onboarding experience. It should be followed for every new client, regardless of tier.

**Goal:** Client is fully onboarded and monitoring within 5 business days of sign-off.

---

## Pre-Onboarding (Before Day 1)

### Sales Hand-off
- [ ] Pilot/contract signed and invoice sent
- [ ] Payment confirmed (or first payment confirmed in escrow)
- [ ] Client info collected (company, contact, technical contact, SLA contacts)
- [ ] Client GitHub organization access granted (if using our tools)
- [ ] Slack/WhatsApp group created with client team + Sentinel Ops team

### Internal Setup
- [ ] Client added to Sentinel Ops CRM (spreadsheet or Notion for MVP)
- [ ] Client folder created: `sentinel_ops/clients/{client-name}/`
- [ ] Client's on-call rotation configured (email, PagerDuty)
- [ ] Client-specific alert rules reviewed and configured
- [ ] Client's known IP ranges whitelisted in Wazuh (office, VPN)
- [ ] Client's SSH key or VPN access details for remote access

---

## Day 1: Kickoff Call (30 min)

**Attendees:** Client technical contact + Sentinel Ops team

**Agenda:**
1. Confirm scope (which servers, how many endpoints)
2. Walk through onboarding plan (this checklist)
3. Confirm remote access method (direct SSH / VPN / jump host)
4. Assign technical lead on client side (who approves changes)
5. Schedule weekly check-ins (30 min, same time each week)
6. Set up communication channel (WhatsApp group for alerts + ops)

**Output:** Kickoff confirmation email sent to all attendees

---

## Day 1–2: Access Setup

### For client servers:
- [ ] Receive SSH credentials / VPN access from client
- [ ] Verify connectivity: can SSH to all in-scope servers
- [ ] Test sudo access (we need root/sudo for hardening and monitoring)
- [ ] Confirm firewall allows outbound to our Wazuh manager (ports 1514, 1515)
- [ ] Record server inventory:

| Server Name | IP | OS | Role | Access Method | Sudo User |
|-------------|----|----|----|---------------|-----------|
| web-01 | x.x.x.x | Ubuntu 22.04 | Web server | SSH key | deploy |
| db-01 | x.x.x.x | Ubuntu 20.04 | Database | SSH key | dbadmin |
| ... | | | | | |

- [ ] Store access credentials in client's `secrets.md` (encrypted, not in plain text)

### For our Wazuh manager:
- [ ] Confirm Wazuh manager is running and accessible
- [ ] Generate enrollment packages for each OS type (Linux, Windows)
- [ ] Prepare agent installation instructions per OS

---

## Day 2–3: Agent Deployment

### Linux servers (Ubuntu/Debian/RHEL/CentOS):
```bash
# Run on each Linux server (we execute this via SSH)
curl -s https://our-wazuh-manager/packages.wazuh.com/4.x/apt/ | bash
apt update && apt install wazuh-agent
# Register with manager
/var/ossec/bin/agent-auth -m WAZUH-MANAGER-IP -p 1515
# Configure agent
cat > /var/ossec/etc/ossec.conf << 'EOF'
<client>
  <server>
    <address>WAZUH-MANAGER-IP</address>
    <port>1514</port>
    <protocol>udp</protocol>
  </server>
</client>
EOF
systemctl enable wazuh-agent
systemctl start wazuh-agent
```

- [ ] Verify agent is active and connected: `systemctl status wazuh-agent`
- [ ] Verify agent appears in Wazuh dashboard: check agent list
- [ ] Verify agent is receiving logs: check Wazuh dashboard → agents → {client} → status

### Windows servers:
- [ ] Download Wazuh agent MSI from our manager portal
- [ ] Deploy via PSExec or remote PowerShell
- [ ] Register with manager (same as Linux)
- [ ] Verify connectivity

### Post-deployment check:
- [ ] All in-scope servers show "Active" in Wazuh
- [ ] No agent enrollment errors in Wazuh manager logs
- [ ] Test alert: SSH a wrong password to trigger auth failure alert → verify we receive it

---

## Day 3–4: Baseline Scan

- [ ] Run initial vulnerability scan on all in-scope servers (Wazuh CVE scan)
- [ ] Run CIS benchmark scan (SCA — Security Configuration Assessment)
- [ ] Capture baseline: open ports, running services, current risk score
- [ ] Document baseline in `clients/{client-name}/baseline-YYYY-MM-DD.md`

**Baseline report includes:**
- Number of critical/high vulnerabilities found
- Servers with most risk (ranked)
- Configuration issues (CIS failures)
- Recommended priority order for hardening

---

## Day 4–5: Hardening (Sentinel/Fortress only)

- [ ] Schedule maintenance window with client (1–2 hours)
- [ ] Apply hardening via Ansible (run with --check first, then for real)
- [ ] During hardening: monitor for service interruptions
- [ ] After hardening: verify services still running, test SSH access
- [ ] Run post-hardening scan to confirm improvements
- [ ] Get client sign-off: "Hardening applied, no issues"

**If issues arise during hardening:**
- Roll back using Ansible `state=present` revert or snapshots
- Document issue and resolution in `clients/{client-name}/incidents.md`

---

## Day 5: Go-Live

### Before go-live:
- [ ] All agents active and reporting
- [ ] Alert rules configured and tested
- [ ] Client notification channel confirmed (WhatsApp number correct)
- [ ] PagerDuty escalation configured (for Fortress tier)
- [ ] Client has our contact info for urgent issues

### Go-live checklist:
- [ ] Send welcome email to client:

```
SUBJECT: Sentinel Ops is now monitoring {client_name}

Hi {client_contact},

You're now live with Sentinel Ops. Here's what you need to know:

What we monitoring:
- {N} servers/endpoints
- All running services, auth events, CVE updates

What to expect:
- Weekly digest every Friday (email)
- Monthly management report (end of month)
- Immediate alerts for critical/high severity issues via WhatsApp

Your dashboard: https://kibana.oursentinelops.com (credentials sent separately)

If you have any questions, reply here or WhatsApp us.

— Sentinel Ops Team
```

- [ ] Set up weekly recurring call (same time, every week for first month)
- [ ] Add to Sentinel Ops client calendar (notion/spreadsheet)
- [ ] Hand off to ongoing monitoring team (us)

---

## Ongoing (First 30 Days)

- [ ] Monitor for any agent disconnection
- [ ] Review first week's alerts — tune false positives
- [ ] Verify weekly digest is being sent
- [ ] Address any client questions
- [ ] At day 30: deliver pilot report (for pilot clients) or monthly report (for ongoing)

---

## Client Folder Structure

```
sentinel_ops/clients/{client-name}/
  baseline-YYYY-MM-DD.md
  inventory.md
  exceptions.md          # hardening exceptions granted
  incidents.md           # any incidents during onboarding
  tuning-log.md          # alert rule tuning notes
  weekly-reports/        # saved copies of weekly digests
  monthly-reports/       # saved copies of monthly reports
  secrets.md             # access credentials (encrypted)
  onboarding-checklist.md  # this file, signed off
```

---

## Onboarding Metrics (Track for Review)

| Metric | Target |
|--------|--------|
| Time to go-live | ≤ 5 business days |
| Agent coverage | 100% of in-scope servers |
| Alert false positive rate | < 30% (tune down over time) |
| Client satisfaction | > 7/10 by day 30 |
| First alert confirmed real | < 48h after go-live (validate system works) |

---

*Version: 1.0 | Created: 2026-05-06*