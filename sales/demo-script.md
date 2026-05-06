# Demo Script — Sentinel Ops

## Purpose
A demo should accomplish two things: (1) show the prospect we know what we're doing, and (2) show them what they would get — in concrete, visual terms. Don't demo features, demo outcomes.

The demo is not the product walkthrough — it's a story about what we solve and how.

---

## Demo Flow (Total: 15–20 minutes)

### Part 1: Context Setting (3 min)

**"Let me show you what Sentinel Ops looks like from a client's perspective — not the technical stack, but what you'd actually see and receive."**

Start by setting context about what problem we solve, not what tools we use.

> "Most businesses we talk to have this common situation: they have IT infrastructure — servers, maybe some cloud — and they know they should be doing more security, but they're not sure what exactly, or they have tools that generate alerts they don't understand, or they've been burned before and want to do better."

> "What we do is: we take security monitoring, hardening, and ongoing management, and we package it as a managed service so you don't have to build it yourself. We show up every week with a clear picture of where you stand, and we handle the noise so you can focus on what matters."

**Transition:** "Here's what that looks like in practice..."

---

### Part 2: Vulnerability Scan Findings (5 min)

Walk through a real example of what we'd find.

> "Let's say we start with an initial scan of your infrastructure. Here's what we typically find in the first week — and this is from actual clients, not made up."

Show the kind of findings we'd surface:
- Open ports on servers that shouldn't be exposed
- Outdated software with known CVEs
- SSH configurations that are exploitable
- Missing security patches
- Overly permissive firewall rules

**Key message:** "These aren't theoretical — these are real findings from real servers. The question is: do you want to know about them, or do you want your attackers to find them first?"

If possible, show a sanitized sample report (even a screenshot of a scan tool output works).

---

### Part 3: Hardening Applied (5 min)

Show what we do about the findings.

> "After the initial scan, we apply hardening. Here's what that means: we take industry-standard CIS benchmarks and apply them to your servers — things like disabling unnecessary services, locking down SSH, setting up proper logging, configuring audit rules."

Show the before/after of a hardened server:
- Before: exposed ports, weak configs
- After: locked down, monitored, logged

> "This isn't just about being secure — it's about knowing what's happening on your servers at any given time. After hardening, if something changes, we see it."

---

### Part 4: Ongoing Monitoring (5 min)

Show what continuous monitoring looks like.

> "The scan and hardening is the one-time work. What keeps you safe day-to-day is monitoring. Here's what that looks like."

Show examples of:
- Alert triage: "We receive hundreds of potential alerts. We filter out the noise and escalate the real threats — with clear action steps."
- Weekly digest: "Every Friday, your team gets a summary of what happened this week — findings, what's been resolved, what's still open."
- Monthly report: "Every month, you get a management-ready report that shows your risk score trend — are you getting safer or not?"

If you have a sample dashboard, show it. If not, describe it:
- Risk score (visual, trended)
- Findings by severity
- Remediated vs. open items
- Compliance status (PDPA controls)

---

### Part 5: The Pilot (3 min)

Close with the pilot offer.

> "Here's how we'd start. We do a 30-day pilot. We scan, harden, monitor, and at the end of 30 days we give you a management report. You see real findings, real risk reduction, and then you decide — do you want to continue or not."

> "The pilot costs RM 2,000, all-inclusive. We handle everything — remote access, tools, monitoring, reporting. You just give us access and approve changes. And at the end, you get a clear view of where your security posture stands and what it would take to maintain it."

---

## Demo Tips

**Do:**
- Customize to what matters to them. If they're healthcare, show PDPA compliance angle. If they're e-commerce, show PCI angle.
- Show findings, not features. "We found this open port on your server" beats "our platform uses advanced threat detection."
- Use their company name if you know it. "In your case, based on what you've told me, we'd start by looking at..."
- Be honest about limitations. If you can't show something, say so.
- Pause and check for questions. "Does that make sense so far?"

**Don't:**
- Go deep on technical architecture. They don't care about Wazuh vs. Elastic stack.
- Demo things that don't map to their problem.
- Rush. If they have questions, answer them. The demo is a conversation, not a presentation.
- Over-promise. Don't say "we catch everything" — we don't.

---

## Demo Setup Checklist

Before demo:
- [ ] Know their industry and size
- [ ] Know their pain point (incident, compliance, fear)
- [ ] Have sanitized sample outputs ready (scan report, weekly digest, monthly report)
- [ ] Know the pricing tier you'd propose
- [ ] Have a clear close: "Would a 30-day pilot make sense for your team?"
- [ ] Log in to any tools ahead of time — don't fumble during the call

---

## Post-Demo Follow-Up

After the demo, send within 24 hours:
1. Thank you message
2. Summary of what we discussed
3. Relevant findings for their situation
4. Pilot proposal (if qualified)
5. Next steps (schedule a follow-up call, send proposal document, etc.)

---

*Version: 1.0 | Created: 2026-05-06*