# Statement of Work — Sentinel Ops 30-Day Security Pilot

## Parties

**Service Provider:** Sentinel Ops (agent@openclaw.ai)  
**Client:** {Client Legal Name} ("Client")  
**Date:** {YYYY-MM-DD}  
**SOW Reference:** SO-{YYYY}-{###}

---

## 1. Purpose

This Statement of Work ("SOW") defines the scope, deliverables, and terms for a 30-day managed security pilot conducted by Sentinel Ops for the Client. The pilot is designed to demonstrate the value of Sentinel Ops' managed security services before any ongoing commitment.

---

## 2. Scope

### In-Scope Servers / Endpoints
The pilot covers the following assets:

| Asset Name | IP / Hostname | OS | Role |
|------------|---------------|----|------|
| {server-01} | {x.x.x.x} | Ubuntu 22.04 | {web server} |
| {server-02} | {x.x.x.x} | Ubuntu 20.04 | {database} |
| {server-03} | {x.x.x.x} | Debian 11 | {application} |
| *(add as needed)* | | | |

Maximum scope: **5 servers/endpoints** (additional scope requires separate agreement).

### Excluded
- Physical infrastructure / on-premise hardware not listed above
- Cloud infrastructure beyond listed endpoints (unless separately agreed)
- Application-layer penetration testing
- Third-party vendor systems not owned by Client

---

## 3. Pilot Timeline

| Phase | Days | Activities |
|-------|------|------------|
| **Phase 1: Baseline** | Day 1–7 | Access setup, vulnerability scan, configuration audit |
| **Phase 2: Hardening** | Day 7–14 | CIS baseline hardening applied to in-scope servers |
| **Phase 3: Monitoring** | Day 14–37 | Continuous Wazuh monitoring + human alert triage |
| **Phase 4: Report** | Day 30 | Pilot wrap-up management report delivered |

**Total Duration:** 30 days from pilot sign-off  
**Start Date:** {Start Date}  
**End Date:** {End Date}

---

## 4. Deliverables

### 4.1 Baseline Assessment Report
- Vulnerability scan results (CVE findings, prioritized by severity)
- Configuration gaps (CIS benchmark failures)
- Asset inventory (what we're monitoring)
- Baseline risk score

### 4.2 Hardening Confirmation
- CIS-based OS hardening applied to all in-scope servers
- Before/after comparison (what changed)
- List of any items requiring client action (application-level issues, etc.)

### 4.3 Continuous Monitoring
- Wazuh agent deployed and active on all in-scope servers
- Alert triage: human review of high/medium severity alerts
- Weekly written summary (every Friday during pilot)
- Critical alerts escalated to client WhatsApp/SMS immediately

### 4.4 Pilot Wrap-Up Report (Day 30)
- Executive summary (1 page, suitable for management/board)
- What was found and remediated
- Risk score trajectory (baseline vs. end-of-pilot)
- Open items and recommended next steps
- Proposal for ongoing Sentinel Ops service (if applicable)

---

## 5. Client Responsibilities

For Sentinel Ops to deliver effectively, the Client must:

1. **Provide a technical contact** — someone who can grant SSH/sudo access and approve configuration changes
2. **Maintain remote access** — keep VPN or direct SSH access active throughout the pilot period
3. **Act on critical findings** — if Sentinel Ops escalates a critical vulnerability, Client must acknowledge and act within 48 hours
4. **Inform of changes** — notify Sentinel Ops of any new systems, network changes, or applications added during the pilot
5. **Pay the pilot fee** — per Section 7 below

---

## 6. Change Process

If the Client requests scope changes (additional servers, expanded monitoring, etc.) during the pilot:
1. Sentinel Ops provides a scope change request (SCR) with impact on timeline and cost
2. Client approves SCR in writing (email acceptable)
3. Additional cost billed as per agreed rate

---

## 7. Fees and Payment

**Pilot Fee:** RM 2,000 (two thousand Malaysian Ringgit), one-time, non-recurring

**Payment Terms:**
- Invoice issued on SOW signing
- Payment due within 7 days of invoice date
- Pilot begins within 5 business days of payment confirmation

**NOT included in pilot fee:**
- Additional servers beyond 5 (RM 400/server if added)
- On-site visits (available at RM 800/visit within Klang Valley)
- Application-layer penetration testing
- Regulatory representation

---

## 8. Ongoing Service (Post-Pilot)

At the end of the pilot, the Client has the following options:

| Option | Details | Monthly Fee |
|--------|---------|-------------|
| **Continue — Sentinel** | Full monitoring, hardening, alert triage | RM 3,500/month |
| **Continue — Watcher** | Monthly scan + digest report | RM 1,500/month |
| **Standalone** | Client takes findings and remediates independently | N/A |
| **No continuation** | No further obligation | N/A |

**Pilot-to-MRR credit:** If Client continues to Sentinel or Fortress tier, first month fee credited (up to RM 3,500) toward month 1 of ongoing service.

---

## 9. Confidentiality

Sentinel Ops agrees to keep all Client information confidential, including:
- Infrastructure details, network architecture, server configurations
- Security findings and vulnerability information
- Business operations and data

Sentinel Ops will not disclose Client information to any third party without written consent, except as required by law.

---

## 10. Limitation of Liability

Sentinel Ops' liability under this SOW is limited to direct damages and shall not exceed the total pilot fee paid under this agreement. Sentinel Ops is not liable for:
- Indirect, consequential, or punitive damages
- Loss of data or business interruption
- Client's failure to act on critical findings within reasonable time
- Third-party actions or negligence

Sentinel Ops does not guarantee breach prevention. The goal is risk reduction and visibility.

---

## 11. Term and Termination

**Pilot Term:** 30 days from sign-off date  
**Termination:** Either party may terminate with 5 business days written notice  
**Effect of Termination:** Upon termination, Client retains all deliverables produced during the pilot. Unused portion of pilot fee refunded pro-rata.

---

## 12. Acceptance

By signing below (or responding to this email with approval), the Client agrees to the terms of this SOW.

| | |
|---|---|
| **Client:** | **{Client Name}** |
| **Name:** | |
| **Title:** | |
| **Date:** | |
| **Signature:** | |

| | |
|---|---|
| **Sentinel Ops:** | **Sentinel Ops** |
| **Name:** | OpenClaw Agent |
| **Date:** | {Date} |
| **Signature:** | agent@openclaw.ai |

---

*Version: 1.0 | Created: 2026-05-06*  
*SOW Reference: SO-{YYYY}-{###}*