# Wazuh Scope — Sentinel Ops

## Overview

Wazuh is our core monitoring platform. It provides agent-based security monitoring, log analysis, vulnerability detection, and threat response. We use the open-source version (not the paid SIEM cloud) — deployed on our infrastructure for MVP.

## What We Deploy (Per Client)

### Agent Onboarding

1. **Install Wazuh agent** on in-scope servers (Ubuntu, Debian, RHEL, CentOS, Windows Server)
2. **Register agent** with our Wazuh Manager (TLS, pre-shared key)
3. **Configure agent** for the client's environment (IP ranges, hostname, groups)
4. **Verify connectivity** — agent shows as active in Wazuh dashboard

**Agent Installation Methods:**
```bash
# Ubuntu/Debian (Wazuh repo)
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add -
echo "deb https://packages.wazuh.com/4.x/apt/ stable main" > /etc/apt/sources.list.d/wazuh.list
apt update && apt install wazuh-agent

# Windows: download MSI from our Wazuh manager, install via remote (PSExec/WinRM)
```

---

## What Wazuh Monitors

### System Calls and Logs

| Event Type | Source | Alert Level |
|------------|--------|-------------|
| SSH login (success/fail) | auth.log, secure | High |
| Sudo usage | auth.log | High |
| New user/group created | auth.log | Medium |
| Cron job changes | cron.log | Medium |
| Package install/remove | dpkg.log, yum.log | Low |
| Service start/stop/enable | systemd | Medium |
| File integrity changes | Wazuh FIM (OSSEC HIDS) | High |
| Network connections | netstat / SS output | Medium |
| Port scan detected | Wazuh rules | High |
| Malware indicators | Wazuh rootcheck | Critical |

### Vulnerability Detection

- ** CVE scanning** — Wazuh agent periodically checks installed packages against CVE database (requires internet access from agent)
- Scan interval: daily by default
- We review CVE findings weekly, prioritize by exploit availability

### Configuration Assessment

- CIS benchmark checks (via Wazuh SCA — Security Configuration Assessment)
- Enabled for Ubuntu, Debian, CentOS/RHEL
- Runs on agent registration, then weekly
- Results go into Elasticsearch, surfaced in reports

### Cloud Security (if applicable)

If client uses AWS, Azure, or GCP:
- Wazuh Cloud Trail / CloudWatch logs → our manager
- Requires AWS credentials (read-only) or cloud log export
- We detect: unauthorized API calls, insecure S3 buckets, IAM policy changes

---

## Rules and Decoders (Custom)

We maintain custom rules to reduce false positives and highlight real threats:

### High-Priority Rules (immediate alert)

```yaml
# SSH brute force detected
- id: 100101
  level: 12
  description: "SSH brute force attack detected"
  rule:
    - id: 5716
      if_group: authentication_failed
    - match: "sshd"
  timeframe: 20
  condition: matches > 10
  action: send email + PagerDuty

# Malware file detected
- id: 100102
  level: 15
  description: "Malware signature detected on server"
  rule:
    - id: 503
      if_group: malware_detected

# Privilege escalation (sudo)
- id: 100103
  level: 10
  description: "Unauthorized privilege escalation attempt"
  rule:
    - id: 54003
      if_group: sudo
```

### Medium-Priority Rules (daily review)

```yaml
# New cron job from unknown user
- id: 100201
  level: 7
  description: "New cron job created by non-root user"
  
# New SSH key added
- id: 100202
  level: 9
  description: "SSH authorized_keys modified"

# Configuration file changed
- id: 100203
  level: 8
  description: "Critical config file modified"
  match: "/etc/passwd|/etc/shadow|/etc/sudoers"
```

---

## Agent Groups

We group clients by tier for management:

| Group | Purpose | Monitoring Level |
|-------|---------|-----------------|
| `sentinel-watcher` | Watcher tier clients | Basic (logs + CVE) |
| `sentinel-sentinel` | Sentinel tier clients | Full (SCA + rules) |
| `sentinel-fortress` | Fortress tier clients | Full + 24/7 rules |
| `client-{name}` | Per-client isolation | Client-specific |

Example: Agent group assignment in `/var/ossec/etc/ossec.conf`:
```xml
<group>client-acme,sentinel-sentinel</group>
```

---

## What We DON'T Monitor

Explicitly out of scope for Wazuh agent:

- Application-level logs (unless forwarded to syslog)
- Database query logs (MySQL, PostgreSQL — unless they output to syslog)
- Container-level events (Docker/Kubernetes — requires separate collector)
- Network traffic analysis (full packet capture — requires different tooling)
- Mobile devices / BYOD

---

## Agent Troubleshooting

**Agent not connecting:**
1. Check agent service: `systemctl status wazuh-agent`
2. Check connectivity: `telnet our-manager-ip 1514`
3. Check enrollment: `/var/ossec/logs/ossec.log` for enrollment errors
4. Re-register: `/var/ossec/bin/agent-auth -m our-manager-ip -p 1515`

**High CPU usage:**
- Default agent uses minimal resources (~1-2%)
- If high, check: FIM scanning too many directories, CVE scan running
- Solution: adjust scanning intervals, exclude large directories

---

## Upgrade Path

Wazuh agents auto-upgrade from the manager:
- We push agent package from manager
- Client agent accepts upgrade automatically (configurable)
- Manager can force upgrade via API

We trigger upgrades during low-traffic windows with client notice.

---

## Storage and Retention

| Data | Location | Retention | Rotation |
|------|----------|----------|---------|
| Agent logs (raw) | Wazuh manager | 30 days | Automatic |
| Elasticsearch (alerts) | Elasticsearch | 90 days | Automatic |
| Reports (PDF) | Local / emailed | Indefinite | Manual |
| Kibana dashboards | Kibana | N/A | Config |

After 90 days, Elasticsearch indices are deleted. We keep PDF reports for client record.

---

*Version: 1.0 | Created: 2026-05-06*