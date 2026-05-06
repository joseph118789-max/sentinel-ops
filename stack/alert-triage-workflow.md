# Alert Triage Workflow — Sentinel Ops

## Overview

Alert triage is where we deliver real value. Wazuh generates alerts; we filter out the noise and escalate only real threats with clear action steps. This document describes how alerts flow from detection to client notification.

**Our value: we do the filtering so clients don't have to.**

---

## Alert Flow Architecture

```
Wazuh Agent (client server)
    ↓ logs / events
Wazuh Manager (our server)
    ↓ rule match → alert
Elasticsearch index (wazuh-alerts-4.x)
    ↓ scheduled query
Sentinel Ops Inbox (email + PagerDuty)
    ↓ human review (triage)
Real Threat → Client WhatsApp/SMS (within SLA)
False Positive → Rule tuned, logged
Informational → Weekly report summary
```

---

## Alert Severity Levels

| Level | Wazuh Level | Definition | Response SLA |
|-------|------------|------------|-------------|
| **Critical** | 15–16 | Active breach, ransomware, data exfiltration | 15 min, any time |
| **High** | 12–14 | Exploitable vulnerability, successful intrusion | 1 hour (biz hours), 4 hours (after hours) |
| **Medium** | 7–11 | Anomaly detected, potential compromise | Next business day |
| **Low** | 1–6 | Informational, false positive likely | In weekly report |

---

## Triage Process (Detailed)

### Step 1: Alert Ingestion

- Alerts from all agents → Elasticsearch
- All agents indexed in `wazuh-alerts-4.x-*`
- We query via Kibana or directly via Elasticsearch API

**Triage Query (run every 30 minutes during business hours):**
```
severity >= 10 AND @timestamp > now-30m
```

**Critical Query (run every 5 minutes, 24/7):**
```
severity >= 15 AND @timestamp > now-5m
```

### Step 2: Initial Review (Triage Analyst)

For each alert:

1. **Context check** — Which client? Which server? What time?
2. **Likelihood check** — Is this a real threat or likely false positive?
3. **Impact check** — If real, what's the blast radius? Data? Systems?
4. **Action check** — What needs to happen right now?

**False positive indicators:**
- Known IT staff activity (our auth, known IPs)
- Scheduled tasks that generate alerts
- Expected changes that were not communicated
- Previous tuning confirmed working

**Real threat indicators:**
- Source IP from unexpected location (not VPN, not known office)
- Authentication from unusual time (3am, weekend)
- Escalating failures (brute force → successful login)
- File integrity change on critical system file
- Malware signature hit

### Step 3: Escalation Decision

After review, each alert gets classified as:

| Classification | Meaning | Action |
|---------------|---------|--------|
| **FALSE_POSITIVE** | Not a real threat | Tune rule, log reason, done |
| **CONFIRMED_THREAT** | Real security event | Escalate to client immediately |
| **SUSPICIOUS** | Needs more info | Investigate further, then decide |
| **UP_FOR_DEBATE** | Could go either way | Document, include in weekly report |

### Step 4: Client Notification (for Confirmed Threats)

**For High/Critical alerts:**
```
[CRITICAL/SECURITY ALERT] {client_name} — {server_name}

What: {description of the threat}
Where: {server IP/name}
When: {timestamp}
Impact: {what could happen if not acted on}
Recommended Action:
1. {step 1}
2. {step 2}
3. {step 3}

We are monitoring. Reply ASAP if you need immediate assistance.
— Sentinel Ops
```

**SLA Response:**
- Critical: Send WhatsApp + SMS simultaneously, call within 15 min
- High: WhatsApp, response within SLA window
- Medium: Email + WhatsApp, next business day

### Step 5: Resolution Documentation

After client acknowledges and acts:
1. Log: "Alert {ID} confirmed, client notified at {time}, client action taken"
2. If needed: open ticket in our tracking (simple markdown file per client for MVP)
3. Update rule if false positive: document why it fired, why it was dismissed

---

## Triage Schedule

| Time | Activity |
|------|----------|
| Every 5 min (24/7) | Critical alert query — if hit → immediate escalation |
| Every 30 min (business hours) | High/Medium alert review |
| Daily (Mon–Fri, end of day) | End-of-day triage summary — what's open, what's new |
| Weekly (Friday) | Weekly alert report for clients (automated) |

---

## Alert Sources We Watch

These are the primary Wazuh rules that generate real alerts in our environment:

### Authentication
- SSH brute force (multiple failed logins)
- Successful SSH login from new IP
- Sudo command executed (for Sentinel+ tier)
- Login outside business hours
- Login from country outside Malaysia (if known IT travels)

### File Integrity
- Critical system file modified (/etc/passwd, /etc/shadow, /etc/sudoers)
- SSH authorized_keys changed
- Cron job added by non-root
- New SUID binary added
- Unexpected kernel module loaded

### Network
- Port scan detected from client server (server is scanning others)
- Unusual outbound connection (callback to unknown IP)
- DNS query to known malicious domain
- Large data transfer outside business hours

### Malware
- Rootkit check triggered (rootcheck positive)
- Malware signature hit (ClamAV via Wazuh)
- Suspicious process running (heuristic)

### Configuration
- Wazuh SCA check failed (CIS benchmark)
- Security setting changed (firewall off, SELinux disabled)
- Unpatched CVE (critical/high severity)

---

## Triage Team Setup

For MVP, triage is done by:
- **Primary:** Sentinel Ops agent (us)
- **Secondary:** Rotating on-call for after hours

We use:
- **Email inbox** for alert aggregation (wazuh-alerts@openclaw.ai)
- **PagerDuty** for critical escalation (automated routing)
- **WhatsApp** for client notification (direct, fast)
- **Kibana** for ad-hoc investigation
- **Simple CRM/ticket** for tracking (spreadsheet or Notion for MVP)

**If more than 3 concurrent clients:** evaluate Opsgenie or Freshservice vs. manual triage.

---

## Tuning Process (Reducing False Positives)

Over time we tune rules so the ratio improves:

1. **Log false positive** → figure out which rule fired
2. **Determine why** → expected activity that we didn't know about
3. **Fix** → modify Wazuh rule to be more specific, OR add client IP to whitelist
4. **Document** → write in client's `tuning-log.md`: "Rule X suppressed for client Y because [reason]"

Example tuning:
```xml
<!-- Added to /var/ossec/etc/rules/local_rules.xml -->
<rule id="100101" level="0">
  <if_sid>5716</if_sid>
  <match>Accepted publickey</match>
  <source_ip>192.168.1.100</source_ip>
  <description>SSH from known IT workstation - suppress"</description>
</rule>
```

We review tuning quarterly per client.

---

## Weekly Alert Report (Automated)

Every Friday, we generate a weekly alert summary for each client:

```
SECURITY DIGEST — {client_name} — Week of {date}

SUMMARY
- Total alerts: {N}
- Critical: {N}
- High: {N}
- Medium: {N}
- False positives dismissed: {N}
- Confirmed threats: {N}

TOP FINDINGS
1. {finding} — {status/action}
2. ...

OPEN ITEMS
- {item} — {severity} — {since date}
- ...

LOOKING AHEAD
- Planned maintenance window: {date}
- Upcoming patch cycle: {date}
- Any changes to notify us about?

Stay safe,
Sentinel Ops
```

---

*Version: 1.0 | Created: 2026-05-06*