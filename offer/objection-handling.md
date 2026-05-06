# Objection Handling — Sentinel Ops

## Philosophy
Objections are not rejections — they're questions that haven't been answered to satisfaction yet. Most security objections fall into a few categories: price, need, trust, and urgency. When someone pushes back, we're usually dealing with one of these.

The key is to **acknowledge the concern, add information, then pivot to the real issue**.

---

## Price Objections

### "It's too expensive for our size"
> "I understand. Most SMEs we work with feel the same initially. What we find is that the real cost isn't the service — it's the cost of not knowing. One breach, one ransomware incident, one PDPA penalty — those cost multiples of what we're charging. We've seen it. What's driving this concern specifically — budget pressure right now, or doubt about the value?"

**Then:** Offer the Watcher tier or pilot as a lower-commitment entry point.

---

### "We already have an IT vendor / internal IT team"
> "That's great — most of our clients do. We're not replacing your IT vendor. We're adding security expertise on top. Your IT team handles infrastructure and availability; we handle security posture, hardening, monitoring, and compliance. They're complementary. The question is: does your current IT team have dedicated security training, or are they also doing everything else? Because our job is to be the security layer your IT vendor doesn't have time to be."

---

### "Can we do a smaller scope to reduce price?"
> "Absolutely. The Watcher tier starts at RM 1,500/month, which covers monitoring, monthly scans, and reports for up to 10 endpoints. If that's still tight, the 30-day pilot at RM 2,000 is a one-time cost that gives you real findings and a security baseline to work from — no ongoing commitment."

---

### "We need to get approval from [boss/board/investor]"
> "Totally normal. A good approach: ask what concerns are most likely to come up in that conversation. We can tailor what we give you — executive summary, ROI framing, risk reduction numbers. Most decision-makers respond to: 1) what we found, 2) what it would cost if we didn't fix it, and 3) what it costs to fix it with us vs. doing nothing. Would it help if I prepared a one-page summary you could share with [whoever needs to approve]?"

---

## Need Objections

### "We haven't had any security incidents"
> "That's genuinely good news — and also the best time to set up proper monitoring. Because when an incident happens and you don't have monitoring, you don't know the blast radius. The companies we see struggle most are ones who thought they were fine until a vendor or regulator told them otherwise. The goal isn't to react to incidents — it's to catch them early or prevent them entirely. Would you rather know or not know?"

---

### "We're too small to be a target"
> "I hear this a lot. The reality: most automated attacks don't discriminate by size. They're scanning all day for open ports, weak SSH, outdated software. You don't need to be a big bank to get hit — you just need to have data worth encrypting or a server worth using for pivoting. And for Malaysian SMEs specifically, we see a lot of ransomware cases that started because someone left SSH exposed or didn't patch a known CVE. Small targets get hit because they're easy. The question is whether you're easier to compromise than your neighbors."

---

### "We use cloud / someone else handles security"
> "Cloud providers (AWS, Azure, Google Cloud) have a shared responsibility model — they secure the infrastructure, you secure your data and access. If you're using SaaS like Microsoft 365, Google Workspace — those are secure at the platform level but you're responsible for your own configurations, MFA, data handling. A lot of cloud breaches come from misconfiguration, not cloud provider failure. We can review your cloud setup and tell you if you're exposed. That's actually a quick deliverable — we can do a basic cloud security review in a day."

---

## Trust Objections

### "How do we know you'll do what you say?"
> "Fair question. Here's what we can do: we can give you access to our monitoring dashboard from day one — you can see what we're seeing. We send weekly written reports, not just verbal updates. And the pilot structure is designed exactly for this — if we don't deliver, you don't continue. We're not asking you to trust us blindly. We're asking for 30 days to prove ourselves."

---

### "We can't give external people access to our servers"
> "Completely understood. Remote access doesn't mean open-ended. We can work with your IT team to set up access that: 1) is logged and audited, 2) is only used when needed with your approval, 3) can be revoked immediately at any time. We also sign an NDA as standard practice. If you have specific security policies about remote access, we can work within those constraints."

---

### "We already had a security company scan us and nothing happened"
> "One-time scans are useful but they give you a snapshot, not ongoing protection. The problem with a one-time scan is: day 2, you're already accumulating new vulnerabilities — software updates, config changes, new services. We do continuous monitoring, not point-in-time snapshots. We catch things as they happen, not 6 months later when the next annual scan comes around."

---

## Urgency Objections

### "We'll think about it and get back to you"
> "Completely fine. The only thing I'd ask: is there something specific you're waiting for? Sometimes people delay because they want to compare options, sometimes it's budget timing, sometimes it's internal readiness. If you can tell me what the timing depends on, I might be able to help unblock it. For context, our onboarding typically takes 5 business days from sign-off — so even if you decide in a month, we can get started quickly. But if you want to start before [event/audit/regulation deadline], we'd need to start earlier."

---

### "This isn't a priority right now"
> "Understood. Is there a time when this would become a priority? For example, if you're going through a compliance audit, if you're acquiring another company, if you're bringing on a new enterprise client who'll do security due diligence — those tend to make it urgent fast. I'd rather start before the pressure hits. But I respect that you know your business better than I do."

---

## Competitive / Alternative Objections

### "We talked to [other MSSP] and they quoted us lower"
> "I'd be curious what the scope is — because sometimes the comparison isn't apples-to-apples. Some MSSPs charge per endpoint with minimum 100 endpoints, or they charge for the SIEM platform separately, or they have annual minimums. If you share what they quoted, I can tell you what's included and what's not. We price for SMEs starting from 3 servers — we don't require enterprise minimums."

---

### "We can just use [consumer antivirus / free tool]"
> "For personal devices, that's probably fine. For business servers and production infrastructure, consumer tools weren't designed for that threat model. They don't do network monitoring, server hardening, compliance mapping, or incident response. If a server gets compromised and you need to know how they got in, consumer tools won't show you that. The question isn't whether you have protection — it's whether you have visibility."

---

## Closing Lines

When you sense a prospect is softening:
- "So if we can show you a real finding in your first week — something your current setup would miss — does that help you make a decision?"
- "What would make you feel confident enough to move forward?"
- "Would it help if we started with a pilot on just 2 servers, just to prove it works before committing to more?"

---

*Version: 1.0 | Created: 2026-05-06*