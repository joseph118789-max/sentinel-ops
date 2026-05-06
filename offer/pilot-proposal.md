# 30-Day Pilot Proposal — Sentinel Ops

## What Is This Pilot?

A structured, risk-controlled way for your business to experience Sentinel Ops managed security without a long-term commitment. We deploy a lean security stack, find real vulnerabilities, apply hardening, and deliver a clear management report at the end — so you can see exactly what you'd get from a full engagement.

**Duration:** 30 days from sign-off  
**Investment:** RM 2,000 (one-time, non-recurring)  
**Scope:** 3–5 key servers or endpoints  
**Outcome:** A clear decision point — proceed with ongoing service or walk away with actionable findings

---

## Why This Pilot Exists

Most security vendors ask you to sign 12-month contracts before you've seen any value. That's backwards. You shouldn't commit to something you haven't tested.

The pilot exists so you can:
- See real findings from your actual infrastructure (not a generic sample report)
- Experience our communication style and responsiveness
- Understand what hardening actually looks like on your servers
- Get a management-ready report you can use for internal decision-making
- Make an informed decision about ongoing security operations

---

## Pilot Timeline

### Week 1: Baseline Assessment (Days 1–7)

**Deliverable:** Initial Security Assessment Report

Activities:
- Remote access setup (we guide you through this, no site visit needed)
- Initial vulnerability scan of all in-scope servers/endpoints
- Basic configuration review (no deep penetration testing)
- Establish monitoring baseline (install Wazuh agent or configure existing tools)

Output:
- Asset inventory (what we're monitoring)
- Vulnerability inventory (what we found, prioritized by risk)
- Baseline risk score

---

### Week 2: Initial Hardening (Days 7–14)

**Deliverable:** Hardening Applied + Confirmation Report

Activities:
- Apply CIS-based server hardening via Ansible ( OS-level configurations, not application code)
- Configure/update monitoring rules based on baseline
- Set up alerting thresholds (we tune out noise)
- Document any high-risk findings that need immediate attention

Output:
- Hardening applied confirmation (which servers, what was changed)
- List of findings that need client action (not our job to fix your application code)
- Updated risk score post-harden

---

### Weeks 3–4: Active Monitoring + Alert Triage (Days 14–37)

**Deliverable:** Real-time monitoring with human triage

Activities:
- Continuous monitoring of in-scope assets
- Daily/weekly alert review (we filter out false positives, escalate real threats)
- WhatsApp/Email support channel (response within 4 hours during business hours)
- Any critical findings get immediate notification with remediation guidance

Output:
- Alert log summary (what we saw, what we dismissed, why)
- Any security incidents detected and resolved (or contained)
- Running risk score through the monitoring period

---

### Day 30: Pilot Wrap-Up Report

**Deliverable:** Management-Ready Pilot Report

Contents:
- Executive summary (1 page, for management/board)
- What we found and remediated
- Risk reduction achieved (baseline score vs. end-of-pilot score)
- What remains open (and what it would take to fix)
- Recommendation for ongoing Sentinel Ops service tier
- Clear pricing for ongoing monitoring

This report is designed to be shown to your management or used for internal budget discussions. It should answer: "Did Sentinel Ops find things we didn't know about, and did they fix or contain them?"

---

## Pilot Decision Points

At day 30, you have three paths:

**Option A — Continue with Sentinel Ops**  
Move to Watcher, Sentinel, or Fortress tier. First month fee credited (up to RM 3,500) toward your first month of ongoing service.

**Option B — Standalone improvements**  
You take the pilot report and findings. We can provide limited consulting to help you implement our recommendations (billed at RM 400/hour).

**Option C — No further engagement**  
You have our findings and hardening. No further obligation. We wish you well.

---

## What's Included in the RM 2,000 Pilot

- All monitoring and alerting during 30 days
- Initial vulnerability scan + re-scan after hardening
- Remote hardening of in-scope servers (we do the work)
- Alert triage and human review (not just automated alerts)
- Weekly written summary (every Friday)
- Pilot wrap-up report (day 30)
- Email/chat support (business hours Mon–Fri 9am–6pm)
- Up to 3 hours of your team's time (for access, interviews, approvals)

---

## What's NOT Included in the Pilot

- Physical on-site visit (can be arranged as add-on at RM 800/visit)
- Application-layer penetration testing
- Legal/regulatory representation
- SLA for incidents outside business hours (available in Sentinel tier and above)
- Fixing client-side application vulnerabilities (we hardening OS/infrastructure, not your code)
- 24/7 on-call support (available in Fortress tier)

---

## Prerequisites / What We Need From You

To make this pilot work, we need:

1. **A technical contact** — someone who can provide SSH/sudo access to in-scope servers, approve firewall changes, and answer questions about the environment
2. **Remote access window** — allow us to connect remotely (VPN or direct SSH) during onboarding (we'll schedule with you)
3. **Honest environment context** — tell us about any known issues, past incidents, or sensitive systems. We can't protect what we don't know about.
4. **Decisive stakeholder** — someone who can make decisions on remediation (we can't fix everything remotely without approval)

Without these, the pilot scope may need to be reduced.

---

## Risk and Limitations

- **We cannot guarantee breach prevention.** No one can. What we can do is reduce risk, surface findings early, and respond fast.
- **Hardening may cause service interruptions.** We'll test in a safe window and coordinate with your team, but some changes can affect running services. We'll warn you before high-impact changes.
- **We rely on the information you provide.** If you hide a system or misconfigure something intentionally, our scope won't cover it.

---

## Ready to Start?

If you'd like to proceed with the pilot:
1. We agree on scope (which servers, how many)
2. You sign a simple SoW (statement of work) for the pilot
3. We invoice RM 2,000 (payable within 7 days)
4. We start within 5 business days of payment confirmation

Contact us at [agent@openclaw.ai] to get started.

---

*Version: 1.0 | Created: 2026-05-06*