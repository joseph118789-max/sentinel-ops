# Architecture MVP — Sentinel Ops

## Design Principle

Every architectural choice must answer one question: **does this help close or deliver the first 3 paying customers?**

If not, it waits.

We build a lean, demonstrable stack that shows real value in 30 days — not a platform that could scale to 300 clients someday.

---

## Core Stack (MVP Scope)

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Environment                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│  │ Ubuntu   │  │ Debian   │  │ Win Srv  │  ← Servers/endpoints│
│  │ Wazuh    │  │ Wazuh    │  │ Wazuh    │    (3–20 in scope) │
│  │ Agent    │  │ Agent    │  │ Agent    │                     │
└──────┬───────┴──────┬───────┴──────┬───────┘                     │
       │              │              │                             │
       └──────────────┼──────────────┘                             │
                      │  (encrypted, port 1514/udp + 1515/tcp)     │
                     ▼                                              │
┌─────────────────────────────────────────────────────────────┐
│                   Wazuh Manager Server                        │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────────┐   │
│   │ Rules/      │   │ Agent       │   │ Alerts          │   │
│   │ Decoders    │   │ enrollment  │   │ Pipeline        │   │
│   │ (custom)    │   │ (authd)     │   │ → JSON output   │   │
│   └─────────────┘   └─────────────┘   └────────┬────────┘   │
│                                                 │             │
│                    ┌────────────────────────────┘             │
│                    ▼                                          │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │           Elasticsearch (single-node MVP)                │ │
│   │  - Index: wazuh-alerts-4.x-*                           │ │
│   │  - Retention: 90 days (configurable)                   │ │
│   │  - Read-only access for dashboards                     │ │
│   └─────────────────────────────────────────────────────────┘ │
│                    │                                           │
│                    ▼                                           │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │           Kibana (single-node, localhost-only)         │ │
│   │  - Dashboards: Security, Compliance, Agents           │ │
│   │  - Read-only view for client-facing demos              │ │
│   │  - Not exposed externally in MVP (SSH tunnel for now)  │ │
│   └─────────────────────────────────────────────────────────┘ │
│                                                              │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │           Alert Triage Layer (Sentinel Ops Team)        │ │
│   │  - Wazuh email/PagerDuty webhook → our inbox           │ │
│   │  - Manual review → WhatsApp to client                   │ │
│   │  - We own the escalation path                           │ │
│   └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## Where It Runs

**Option A: Our infrastructure (recommended for MVP pilots)**
- Single VPS/cloud instance (we manage)
- Wazuh Manager + Elasticsearch + Kibana (co-located)
- Client agents connect outbound to our manager (port 1514/1515)
- We handle patching, backups, monitoring of the stack itself

**Option B: Client infrastructure**
- Wazuh Manager installed on client's network (VM or bare metal)
- We get remote access (VPN or SSH jump)
- More complex onboarding, better for clients with strict data residency

**Option C: Hybrid (future)**
- Wazuh manager on client side
- Elasticsearch in our cloud (for aggregation and reporting)
- Not in MVP — adds complexity without clear revenue benefit yet

---

## Network Requirements

**From client servers to our Wazuh Manager:**
- Outbound UDP 1514 (agent to manager, encrypted)
- Outbound TCP 1515 (agent enrollment and file desync)
- Outbound TCP 443 (agent registration and upgrade, wazuh.com)

**For our management interface:**
- SSH access to Wazuh manager (for us only)
- Kibana accessible via SSH tunnel (localhost:5601) — NOT public

**For client demo access:**
- Read-only Kibana dashboard via password-protected link
- Or weekly PDF report (no portal needed for Watcher tier)

---

## Data Flow

```
1. Agent installs on client server
   → registers with Wazuh Manager (TCP 1515)
   → receives rules, configs

2. Agent collects logs and security events
   → sends to Wazuh Manager (UDP 1514, encrypted)

3. Wazuh Manager processes with rules/decoders
   → generates alert if rule matches
   → alert stored in Elasticsearch

4. Alert rule triggers notification
   → email to Sentinel Ops team
   → or webhook to PagerDuty/Slack

5. Sentinel Ops team triages
   → real threat → WhatsApp client within SLA
   → false positive → rule tuned, logged

6. Monthly: automated report
   → from Kibana/Elasticsearch queries
   → formatted in monthly report template
   → sent to client
```

---

## What's NOT in MVP

These are in the roadmap but not in MVP:

| Feature | Why Not MVP |
|---------|-------------|
| Multi-tenant isolation | Not needed until 5+ clients |
| Kubernetes agent | Single server onboards easier |
| Windows agent (full) | Linux-first MVP |
| Custom threat intel feed | Basic rules sufficient for now |
| API for client self-service | Reports and WhatsApp are enough |
| Mobile app | Not needed for B2B service |
| Full SIEM correlation | Basic rule matching sufficient |
| Distributed Elasticsearch | Single node handles MVP easily |

---

## Technology Versions (MVP)

| Component | Version | Notes |
|-----------|---------|-------|
| Wazuh Manager | 4.9.x | Current stable, easy agent onboarding |
| Wazuh Agent | 4.9.x | Matches manager |
| Elasticsearch | 8.x (via Wazuh bundle) | Single node, not exposed |
| Kibana | 8.x (via Wazuh bundle) | Same, localhost-only |
| OS (our server) | Ubuntu 22.04 LTS | We manage this |
| OS (client) | Ubuntu 18.04+, Debian 10+, RHEL 8+, Windows Srv 2019+ | Agent supported |

---

## Scalability Path (When to Build What)

**3–5 clients:**
- Single Wazuh manager handles up to ~50 agents
- One Elasticsearch node, fine
- No changes needed

**5–10 clients:**
- Separate indices per client (wazuh-alerts-{client})
- Add more disk/RAM to Elasticsearch
- One manager still ok, monitor performance

**10+ clients:**
- Consider separate Wazuh manager per client (their infra)
- Or dedicated manager with more RAM (16GB+)
- Evaluate managed Elasticsearch (Elastic Cloud) vs. self-hosted

---

## Security of Our Stack

Our management server is itself a target, so we harden it:
- Wazuh manager on Ubuntu 22.04, CIS-hardened
- SSH key-only, no password auth
- UFW firewall, only allow our IP
- Elasticsearch not publicly accessible
- Kibana bound to localhost, accessed via SSH tunnel
- Rotate passwords and API keys quarterly

---

*Version: 1.0 | Created: 2026-05-06*