# Pilot Review Call Script — Sentinel Ops

> Use at Day 30 of every pilot. Controls the end-of-pilot conversation: recap value, present findings, and drive conversion to MRR.

**Time:** 45–60 minutes  
**Who:** Prospect (technical contact + decision-maker if available)  
**Goal:** Convince them the pilot was worth RM 2,000 and that continuing is the obvious next step.

---

## Before the Call

- [ ] Final report sent 24 hours before call (PDF or well-formatted markdown)
- [ ] Operations log complete (all hardening changes, alerts, tuning notes)
- [ ] Before/after risk score calculated
- [ ] 3 conversion path options prepared with pricing
- [ ] Join 3 min early — share screen ready with terminal/dashboard open
- [ ] Timer set for 60 min hard stop

**Pre-call WhatsApp:**

> "Hi [name], looking forward to tomorrow's review call. The final report is sent — it summarises everything we found and did over 30 days. We'll walk through it together and I'll share the options for continuing. See you at [time]."

---

## Call Opening (5 min)

**Say:**

> "Thanks for making time today. Over the past 30 days, we've deployed monitoring across [N] servers, applied hardening, and run continuous triage. This call has three parts: what we found, what we changed, and what we recommend for the next step. We'll finish with a decision — no pressure, just clarity."

**Then — quick poll:**

> "Before we start — have you had a chance to look at the report I sent?"

_If yes: dive in. If no: "No problem, we'll walk through it together."_

---

## Part 1: What We Monitored (5 min)

**Show screen:** Agent list in terminal (`agent_control -lc`)

> "Here are the [N] servers we covered. Every one has a Wazuh agent running, feeding alerts back to our manager 24/7. This is what continuous monitoring looks like."

**Say:**

> "For the past 30 days, we captured [N] total alerts. [X] were classified as noise and tuned out. [Y] were confirmed events. Zero were critical incidents — which for a small company is actually a good sign."

**Show screen:** Alert summary from manager logs

> "Here's what was firing most: [top 3 alert types]. Most of this is expected system noise — we tuned it so you're not buried in alerts. What you're left with is signal, not noise."

---

## Part 2: What We Found (10 min)

**Say:**

> "Let me walk you through the findings — starting with the most important."

### 2A: Critical/High Findings
**If any confirmed threats detected:**

> "On [date], we detected [threat description]. This [was resolved / is being monitored]. This is exactly the type of thing that would have been invisible without monitoring in place."

**If no confirmed threats:**

> "The good news: we didn't find any active compromise. Your environment is clean. But we did find configuration weaknesses that could have allowed an attack to succeed."

### 2B: CIS Configuration Findings
**Say:**

> "We ran a CIS benchmark scan — it's a security configuration standard used by companies going through compliance audits. Here's what we found before hardening:"

| Finding | Severity | Before | After |
|---------|----------|--------|-------|
| SSH root login | HIGH | Enabled | Disabled |
| Password auth | HIGH | Enabled | Key-only |
| Firewall | HIGH | Inactive | Active (default deny) |
| Unused filesystems | MEDIUM | Loaded | Disabled |
| Audit logging | MEDIUM | Off | On |

> "These are configuration-level risks — not vulnerabilities — but they're the most common way attackers get in. We fixed all of them."

### 2C: Compliance Posture (if PDPA applies)
**Say:**

> "Since you're subject to PDPA, I also want to note: we now have audit-grade logging active on all servers. If you get audited, you can show that you have continuous monitoring, event logging, and a managed security team. That's a stronger position than just having a firewall."

---

## Part 3: What Changed — Before vs After (5 min)

**Say:**

> "Let me show you the before and after clearly."

**Show screen:** Terminal diff — SSH config before (from ops log) vs after

> "Before: [values]. After: [values]. This is the difference between a server that an attacker can guess their way into, and one they can't."

**Risk score slide:**

> "We use a risk score from 0 to 100. Before the pilot, your score was [X] — [MEDIUM/HIGH]. Today, after hardening and 30 days of monitoring, it's [Y]. That's a [Z]% reduction. The pilot reduced your risk measurably."

---

## Part 4: What Stays Open (3 min)

**Say:**

> "I want to be straight with you about what still needs attention. We're not done — we're never done. Here are the remaining items on your plate:"

> 1. **[Open item 1]** — severity, why it matters, recommended fix
> 2. **[Open item 2]** — same format

**Then:**

> "These are things we can continue handling for you if you continue. The pilot proved we can do the work. The question is whether you want ongoing coverage."

---

## Part 5: The Recommendation (10 min)

**Say:**

> "Based on what we've seen over 30 days, here's what I recommend for your situation."

**Present the tier that fits their profile:**

> "[Tier name] — RM [price]/month. Here's what you get: [list key items]. Here's why it fits: [their specific security driver, compliance need, or scale reason]."

**If their budget concern is the main pushback:**

> "If [Watcher tier] is the right fit at RM 1,500/month — that's the starting point. We can expand from there as your environment grows. You don't have to commit to the full suite today."

---

## Part 6: The 3 Paths (5 min)

**Say:**

> "At this point, you have three options. I want to lay them all out clearly so you can make the best decision for your business."

### Option A: Continue — Managed Service (your recommendation)

> "**Continue with Sentinel Ops.** Stay on the Guardian or Watcher tier — whatever fits your scope. We keep monitoring, we keep hardening current, and you have a team looking after your security full-time. Price is RM [X]/month."
>
> **This fits you because:** [reason tailored to their situation]

### Option B: Expand Scope

> "**Expand the pilot.** More servers, more coverage, or longer monitoring before converting. This makes sense if you want to prove value across more of your environment before committing long-term."
>
> **This fits you because:** [reason — e.g., they mentioned more servers]

### Option C: Stop After Pilot

> "**Stop here.** The pilot did what it was supposed to — you have a baseline scan, hardening, and a clear picture of where you stand. No hard feelings. You can always come back in 3 months when you're ready."
>
> **This fits you because:** [if applicable — e.g., they're in between decisions]

---

## Part 7: The Close (5 min)

**Say:**

> "I want to give you time to think, but I also want to be direct. Based on everything we've shown you — the CIS findings, the hardening, the monitoring coverage — do you want to continue with Sentinel Ops?"

**If yes:**

> "Great. Here's what happens next: I'll send the contract today. Once it's signed, we continue monitoring from tomorrow — no gap, no lapse. [Start date] is Day 1 of your managed service."

> Then: send contract within 2 hours, WhatsApp follow-up same day

**If not yet:**

> "What do you need to feel ready? Is it the price, the scope, something else?"

> Handle objection (see below). If still not ready, give 48-hour close.

**If no:**

> "I understand. Can I ask what changed your mind — was it the findings, the price, something else? I want to make sure we're building the right thing."

> Listen. Don't argue. Take notes. Keep the door warm.

---

## Objection Handling During the Close

**"The price is too high"**
> "I hear you. What we're actually charging for is the human time — the triage, the hardening, the reporting. If you hired someone part-time to do this, you'd pay RM 3,000–5,000/month easily. We're offering that at a fraction of the cost because we've built the process. What budget did you have in mind?"

**"We need to think about it"**
> "Of course. What specifically do you need to think through? If it's the scope, let's walk through it again. If it's budget, we can look at a smaller tier. If it's something else, tell me."

**"We want to show the board first"**
> "Makes sense. What do they need to see? I can give you a one-page executive summary, or a full PDF report they can take. What format works best?"

**"We'll come back in a few months"**
> "No problem. I'll put you in the calendar for a 3-month check-in. If anything changes before then — a security incident, an audit, anything — reach out immediately. We're always here."

---

## Post-Call Actions (within 2 hours)

**If converting:**
- [ ] Send signed contract template
- [ ] Confirm start date, send welcome message
- [ ] Add to operations calendar: Day 1 of managed service
- [ ] Schedule onboarding call within 48 hours

**If not converting:**
- [ ] Send warm WhatsApp message: "Thanks for the honest conversation today. The pilot was worth it either way — you now know where you stand. Our door is open whenever."
- [ ] Add to 3-month follow-up list
- [ ] Log outcome in CRM

---

## Quick Reference: What to Have Ready Before This Call

- [ ] Final report (sent 24h before)
- [ ] Operations log (hardening changes, alert summary)
- [ ] Before/after risk score
- [ ] Alert count: total / critical / high / medium / low / false positive
- [ ] CIS findings count before and after hardening
- [ ] 3 conversion path options with pricing
- [ ] Recommended tier and why
- [ ] Any remaining open risks that need attention

---

*Version: 1.0 | Created: 2026-05-06 | Owner: Sentinel Ops*
