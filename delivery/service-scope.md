# Service Scope — Sentinel Ops

## Overview

Sentinel Ops is a managed security operations service. We provide ongoing security monitoring, vulnerability management, server hardening, and alert triage — wrapped in clear reporting and a named team that owns security outcomes for your business.

This document defines what is included in each service tier, what's explicitly excluded, and how we work operationally.

---

## Core Services by Tier

### Watcher (RM 1,500/month)

**Scope:**
- Monthly vulnerability scan (up to 10 servers/endpoints)
- Monthly digest report (findings, risk trends, remediation priorities)
- Email/chat support (business hours Mon–Fri 9am–6pm, response within 4 hours)
- Read-only access to findings dashboard
- 1x remote remediation session per quarter (up to 2 hours)

**Excluded:**
- Continuous monitoring / real-time alerting
- Incident response
- Server hardening
- Compliance mapping
- After-hours support

---

### Sentinel (RM 3,500/month)

**Scope:**
- **Continuous monitoring** — up to 20 servers/endpoints with Wazuh-based agent or configuration
- **Alert triage** — human review of alerts, escalation of real threats with clear action steps
- **Monthly vulnerability scan** — unlimited ports, all critical/common CVEs
- **Server hardening** — CIS-based Ansible hardening on all monitored servers (initial on-boarding + quarterly review)
- **Monthly management report** — risk score, findings, remediation progress, compliance status
- **PDPA gap mapping (light)** — control mapping to PDPA requirements, gap inventory
- **Email/chat support** — response within 4 hours during business hours
- **Incident response** — remote support, up to 4 hours/month included (escalates to on-site at cost)
- **Quarterly review call** — strategy alignment with IT lead/manager

**Excluded:**
- 24/7 on-call (available in Fortress)
- On-site visits (add-on: RM 800/visit within Klang Valley)
- Physical security services
- Application-layer penetration testing (we can arrange via partner, separate cost)
- Legal or regulatory representation

---

### Fortress (RM 7,500/month)

**Scope:**
Everything in Sentinel, plus:
- **24/7 alerting** — on-call rotation, defined escalation path
- **SOC-style weekly digest** — more detailed than Sentinel (C-level summary, threat intelligence)
- **Compliance reporting** — PDPA full mapping + audit prep documentation (preparation for audit, not representation)
- **Quarterly on-site security review** — 2-hour visit, hardening audit, remediation plan
- **Unlimited incident response hours** (remote, capped at 8h/month — additional at RM 400/hr)
- **WAF/DDoS basic protection** — cloud layer (separate if dedicated hardware)
- **Priority support** — response within 1 hour, any time including weekends

---

## What We Deliver (Per Client, Per Month)

| Deliverable | Watcher | Sentinel | Fortress |
|-------------|---------|----------|----------|
| Vulnerability scan | Monthly | Monthly | Weekly |
| Risk report | Monthly digest | Monthly full | Weekly + Monthly |
| Alert monitoring | — | Continuous | 24/7 |
| Alert triage | — | ✅ | ✅ |
| Hardening | — | ✅ | ✅ |
| Incident response (remote) | — | 4h/month | 8h/month |
| PDPA gap mapping | — | Light | Full |
| On-site visit | — | — | Quarterly |
| Support SLA | Business hours | Business hours | 24/7 |

---

## Hardening Scope

Our server hardening follows CIS (Center for Internet Security) benchmarks. We apply hardening to:

**Included:**
- OS-level configurations (Ubuntu, Debian, RHEL, CentOS, Windows Server)
- SSH hardening (key-based auth, disabled root login, idle timeout)
- Firewall configuration (UFW/firewalld, only necessary ports)
- Logging and audit configuration (auditd, rsyslog/syslog)
- User access controls (sudo, password policies, inactive account removal)
- Package/service least-exposure (remove unnecessary services)
- Kernel parameters (sysctl hardening)
- Time synchronization (NTP)
- Disk encryption recommendation (not implementation — client decides)

**NOT Included:**
- Application-layer hardening (your code, your app config)
- Database query-level hardening (we harden the DB server config, not the schema)
- Network segmentation design (we can recommend, not implement without engagement)
- Cloud-specific security (we do baseline, but cloud-native security requires separate scope)

---

## Monitoring Scope

We monitor via Wazuh (open source SIEM) on client infrastructure. Scope:

**Included:**
- System logs (auth, syslog, application errors)
- File integrity monitoring (critical files)
- Network connection logs
- Process execution monitoring
- SSH/login anomaly detection
- Port scan detection
- Software inventory (what's running on what)

**NOT Included:**
- Application-level logs (unless they feed into syslog)
- Custom application performance monitoring
- Network flow analysis (netflow, sflow) — available in Fortress tier
- Database query monitoring (available as separate add-on)

---

## Alert Triage

Our alert triage process:
1. Alerts come in from monitored assets → Wazuh → our triage queue
2. Tier 1 analyst reviews (noise filtering, false positive dismissal)
3. Real threats escalate to client with: severity, affected asset, likely impact, recommended action
4. Critical alerts get immediate notification (SMS/WhatsApp) + call if Fortress tier
5. Weekly alert summary shows: alerts dismissed, alerts actioned, threats contained

**Alert SLA:**
- Watcher: not included
- Sentinel: business hours triage (Mon–Fri 9am–6pm), critical alerts escalated
- Fortress: 24/7 triage, critical alerts within 15 minutes

---

## Exclusions (Explicit)

The following are explicitly OUT of scope for Sentinel Ops unless separately contracted:

- **Physical security** — guard services, CCTV, physical access control systems
- **Application security testing** — penetration testing of web apps, mobile apps (we can arrange via partner)
- **Legal and regulatory representation** — we don't represent you in regulatory proceedings
- **Insurance** — we don't provide cyber insurance; we can recommend brokers
- **Business continuity / disaster recovery** — we help with security but not BC/DR planning (separate service)
- **Compliance certification** — we help you prepare, but certification is issued by the certification body
- **Fixing client-side application vulnerabilities** — we harden OS and infrastructure; your application code is yours to fix
- **Social engineering / phishing testing** — available as separate engagement
- **Cloud infrastructure automation** — we can recommend architecture, not implement without separate IaC engagement

---

## Client Responsibilities

For us to deliver effectively, the client must:

1. **Provide a technical contact** — someone who can grant us access and approve changes
2. **Maintain remote access** — keep VPN or SSH access active for our monitoring
3. **Act on critical findings** — if we escalate a critical vulnerability, client must act within reasonable time
4. **Inform us of changes** — new servers, network changes, applications — we need to know to keep monitoring current
5. **Pay on time** — service continues as long as invoices are paid

If a client repeatedly ignores our recommendations and a breach occurs as a result, we document our recommendations and their decisions. We cannot protect against client decisions to not act.

---

## Escalation Path

| Severity | Definition | Response |
|----------|------------|----------|
| Critical | Active breach, ransomware in progress, data exfiltration | Immediate WhatsApp + call, 15-min response |
| High | Vulnerability with active exploit, serious misconfiguration | Within 1 hour (business hours), 4 hours (after hours) |
| Medium | Vulnerable but not actively exploited, significant finding | Within 4 hours (business hours) |
| Low | Informational finding, hardening recommendation | Next business day, in weekly report |

---

## Service Review

Quarterly service review (included in Sentinel and Fortress):
- Walk through the quarter's findings and trends
- Review risk score trajectory
- Adjust monitoring scope if client added infrastructure
- Discuss upcoming changes (new systems, regulatory deadlines)
- Confirm continued scope and any adjustments

---

*Version: 1.0 | Created: 2026-05-06*