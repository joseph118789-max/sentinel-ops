# Sentinel Ops Demo Environment

## Current Status

**Stack:** ✅ Running  
**Manager:** ✅ Active (Wazuh 4.9.0, API on port 55000)  
**Indexer:** ✅ Active (cluster green, port 9200)  
**Dashboard:** 🔧 In progress (SSL cert issues)  
**Agent demo-web-01:** ✅ Enrolled and sending alerts

## Services Running

| Service | Port | URL | Status |
|---------|------|-----|--------|
| Wazuh Manager | 55000 | https://localhost:55000 | ✅ Running |
| Wazuh Indexer | 9200 | http://localhost:9200 | ✅ Running |
| Wazuh Dashboard | 5601 | http://localhost:5601 | 🔧 SSL issue |

## Demo Stack Commands

```bash
# Check all services
docker ps | grep wazuh

# Restart manager
docker compose -f demo/wazuh-docker/docker-compose.yml restart wazuh.manager

# View manager logs
docker compose -f demo/wazuh-docker/docker-compose.yml logs -f wazuh.manager

# Check agent status
docker exec wazuh-docker-wazuh.manager-1 agent_control -lc

# View alerts
docker exec wazuh-docker-wazuh.manager-1 tail -f /var/ossec/logs/alerts/alerts.log

# Trigger SSH brute force (for demo)
for i in $(seq 1 10); do sshpass -p wrong ssh -o StrictHostKeyChecking=no wrong@localhost 2>/dev/null || true; done
```

## Agent Enrollment

**Agent:** `demo-web-01` (ID: 001)
```bash
# On the agent machine:
# 1. Install Wazuh agent
apt-get install wazuh-agent=4.9.0-1

# 2. Configure manager IP
sed -i 's/MANAGER_IP/192.168.1.239/' /var/ossec/etc/ossec.conf

# 3. Enroll with manager
/var/ossec/bin/agent-auth -m 192.168.1.239 -p 1515 -A "demo-host-name"

# 4. Start agent
systemctl enable wazuh-agent && systemctl start wazuh-agent
```

## Demo Flow

### 1. Show Agent Enrollment
```bash
docker exec wazuh-docker-wazuh.manager-1 agent_control -lc
```
Should show: `demo-web-01` as "Active"

### 2. Trigger SSH Brute Force
```bash
# From any machine with agent:
for i in $(seq 1 15); do sshpass -p wrong ssh wronguser@AGENT_IP 2>/dev/null || true; done
```
Check alerts: `docker exec wazuh-docker-wazuh.manager-1 tail /var/ossec/logs/alerts/alerts.log | grep 5710`

### 3. Show SCA Findings
```bash
# Trigger SCA scan on agent
docker exec wazuh-docker-wazuh.manager-1 agent_control -r -u 001
# Wait 60s, check alerts for "sca" or "cis"
```

### 4. Show Hardening Impact
- Before: `grep PermitRootLogin /etc/ssh/sshd_config` → commented
- After: `grep PermitRootLogin /etc/ssh/sshd_config` → `PermitRootLogin no`

## Demo Findings (Pre-Recorded)

From the live demo run on 2026-05-06:

| Finding | Rule | Severity | Agent |
|---------|-------|----------|-------|
| SSH brute force attempt | 5710 | HIGH | demo-web-01 |
| PAM login failed | 5503 | MEDIUM | demo-web-01 |
| Systemd service failure | 40704 | LOW | demo-web-01 |
| Docker DNS error | 86003 | LOW | demo-web-01 |

## Artifacts

- `demo-artifacts/findings-report.md` — Demo findings with descriptions and recommended actions
- `demo-artifacts/hardening-before.md` — Before hardening state
- `demo-artifacts/hardening-after.md` — After hardening state

## Pending Fixes

1. **Dashboard SSL** — Wazuh dashboard connects to indexer over SSL but indexer has SSL disabled. Need to either:
   - Enable SSL on indexer with proper certs
   - Or configure dashboard to use HTTP for indexer connection

2. **Agent ID** — demo-web-01 enrolled as ID 001. Manager shows 0 agents via API (indexer sync issue) but CLI shows agent as Active.

3. **Second Demo Agent** — Need to add `demo-weak-01` as intentionally misconfigured host for hardening contrast demo.

## Architecture

```
Internet
    │
┌─────────────────────────────────────────┐
│   openclaw01 (192.168.1.239)             │
│                                          │
│  ┌──────────────────────────────────┐    │
│  │  Docker: wazuh-docker           │    │
│  │                                  │    │
│  │  wazuh.manager (port 55000)     │    │
│  │  wazuh.indexer (port 9200)      │    │
│  │  wazuh.dashboard (port 5601)     │    │
│  │  Ports: 1514/udp, 1515/tcp      │    │
│  └──────────────────────────────────┘    │
│                                          │
│  ┌─────────────────────────────┐        │
│  │  Local: wazuh-agent (host)  │        │
│  │  demo-web-01 (agent ID 001)  │        │
│  │  Connected to manager         │        │
│  └─────────────────────────────┘        │
└─────────────────────────────────────────┘
```

*Demo environment ready — update: 2026-05-06*