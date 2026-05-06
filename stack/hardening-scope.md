# Hardening Scope — Sentinel Ops

## Overview

Server hardening is the process of reducing the attack surface of a server by configuring it to industry-standard security baselines. We use CIS (Center for Internet Security) benchmarks as our reference, implemented via Ansible automation.

**Hardening is included in Sentinel and Fortress tiers only (not Watcher).**

## Hardening Scope by OS

### Ubuntu / Debian (Primary Focus)

We follow CIS Ubuntu Linux Benchmark v1.0.0

| Category | Controls | Description |
|----------|----------|-------------|
| Initial Setup | 1.1–1.4 | Filesystem partitioning, remove unnecessary filesystems |
| Services | 2.1–2.3 | xinetd, RPC, DNS server (disable if not needed) |
| Network | 3.1–3.9 | IP forwarding, packet redirect, ICMP, broadcast, ip6tables |
| Logging | 4.1–4.2 | Auditd configured, log partitions sized |
| PAM | 5.1–5.4 | Password policy, lockout, strength requirements |
| User Accounts | 6.1–6.5 | Disable unnecessary accounts, secure passwd/shadow |
| File Permissions | 7.1–7.3 | World-writable files, unused suid binaries |
| SSH | 13.1–13.9 | Key-only auth, disable root login, strong ciphers |

### RHEL / CentOS (Future Scope)

CIS Red Hat Enterprise Linux 7/8 Benchmark. Same categories as Ubuntu but different package names and paths.

### Windows Server (Future Scope)

CIS Microsoft Windows Server 2019 Benchmark. Includes:
- Account policies (lockout, password complexity)
- Security options (UAC, network security)
- Audit policies
- User rights assignments

---

## What We Do (Concrete Steps)

### Step 1: Pre-Assessment

Before hardening, we document the baseline:
- Current open ports (`netstat -tulpn`)
- Running services (`systemctl list-units --type=service`)
- SSH configuration (current key placement, root login settings)
- Installed packages (unneeded packages to remove)
- Current users and sudo access

**Output:** Pre-hardening report — "Here's what we're about to change and why."

### Step 2: Core Hardening (Ansible Playbook)

We run Ansible playbooks from our automation repo (`sentinel_ops/ansible/`).

**Core playbook applies:**

```yaml
# Core hardening tasks (example structure)
- name: Disable unused filesystems
  community.general.modprobe:
    name: {{ item }}
    state: absent
  with_items:
    - cramfs
    - jffs2
    - hfs
    - hfsplus
    - squashfs
    - udf
    - vfat

- name: Disable SSH root login
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'

- name: Enforce password complexity
  pam_pwquality:
    minlen: 12
    dcredit: -1
    ucredit: -1
    lcredit: -1
    ocredit: -1

- name: Configure UFW default deny incoming
  ufw:
    direction: '{{ item.direction }}'
    policy: '{{ item.policy }}'
  with_items:
    - { direction: 'in', policy: 'deny' }
    - { direction: 'out', policy: 'allow' }
```

**Specific configurations applied:**

1. **SSH hardening**
   - Root login disabled
   - Password authentication disabled (key-only)
   - SSH key placement documented
   - Idle timeout 15 minutes
   - Max auth tries 3
   - Allowlist specific IPs if client requires (VPN IP ranges)

2. **Firewall (UFW)**
   - Default deny incoming
   - Default allow outgoing
   - Allow SSH (port 22, from our IP range only)
   - Allow HTTP/HTTPS if web server present
   - Allow established connections

3. **User access control**
   - Password policy: min 12 chars, complexity, 90-day expiry
   - Lock account after 5 failed attempts
   - Remove unnecessary accounts (games, ftp, etc.)
   - Ensure sudo access for admin users only

4. **Logging (auditd)**
   - Enable auditd
   - Log all auth attempts (success and failure)
   - Log sudo commands
   - Log cron usage
   - Log user changes (add/modify/delete)
   - Log network config changes

5. **System settings**
   - Disable core dumps
   - Enable syncing of system time (NTP)
   - Configure kernel parameters (sysctl)
   - Remove setuid binaries that aren't needed
   - Disable ICMP redirect acceptance
   - Disable source packet routing

### Step 3: Post-Hardening Validation

After playbook runs:
1. Verify SSH still accessible (new session, test key-based login)
2. Confirm firewall ports as expected
3. Run Wazuh SCA scan (should pass more checks)
4. Confirm no service disruptions (client signs off)

**Output:** Post-hardening confirmation — "Here are all the changes made, confirmed working."

---

## What We DON'T Hardening

Explicitly out of scope:

| Item | Reason |
|------|--------|
| Application code | We hardening OS/infrastructure, not your code |
| Database schema | DBA role, not our scope |
| Container configs | Not in MVP |
| Cloud-native security | Separate engagement |
| Network segmentation | Requires network design, separate engagement |
| Application-level firewalls | WAF is separate (Fortress has basic cloud WAF) |

---

## Hardening Exceptions Process

Sometimes a client needs a setting that conflicts with hardening:

1. Client requests exception: "We need SSH on port 2222 for legacy reasons"
2. We evaluate risk: "Port 2222 is non-standard, reduces SSH scanning exposure"
3. Document exception: "Client X requires SSH on port 2222. Documented {date}."
4. Apply compensating control: "We restrict SSH to known IP range only"

Exceptions are logged in client's `exceptions.md` file.

---

## Ansible Automation

We maintain reusable Ansible roles for hardening:

```
sentinel_ops/ansible/
  roles/
    hardening/
      tasks/
        main.yml        # orchestrates all hardening tasks
        ssh.yml          # SSH hardening
        firewall.yml     # UFW configuration
        users.yml        # PAM / user hardening
        auditd.yml       # logging configuration
        kernel.yml       # sysctl parameters
      handlers/
        main.yml         # restart services after changes
      defaults/
        main.yml         # configurable variables
```

**Usage:**
```bash
# Run hardening on a target server
ansible-playbook -i inventories/client-name/hosts.yml playbooks/hardening.yml --limit server1

# Dry-run (check what would change)
ansible-playbook -i inventories/client-name/hosts.yml playbooks/hardening.yml --limit server1 --check
```

---

## Hardening for Different Tiers

| Hardening Activity | Watcher | Sentinel | Fortress |
|--------------------|---------|----------|----------|
| Initial assessment | — | ✅ | ✅ |
| Core OS hardening | — | ✅ | ✅ |
| SSH hardening | — | ✅ | ✅ |
| Firewall setup | — | ✅ | ✅ |
| Quarterly re-check | — | ✅ | ✅ |
| Windows hardening | — | — | ✅ |
| Cloud config hardening | — | — | ✅ |
| WAF/DDoS layer | — | — | ✅ |

---

*Version: 1.0 | Created: 2026-05-06*