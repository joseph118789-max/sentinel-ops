# demo-weak-01 Findings — CIS Benchmark Scan

**Agent:** demo-weak-01 (Docker container, Debian bookworm-slim)  
**Scan:** CIS Benchmark for Amazon Linux 2023 Benchmark v1.0.0  
**Scan ID:** 593819762

## CIS Benchmark Failures Detected

| # | Finding | CIS Ref | Severity |
|---|---------|---------|----------|
| 1 | /tmp is not a separate partition | 1.1.2.1 | MEDIUM |
| 2 | squashfs filesystem not disabled | 1.1.1.1 | MEDIUM |
| 3 | freevxfs filesystem not disabled | 1.1.1.2 | MEDIUM |
| 4 | udf filesystem not disabled | 1.1.1.3 | MEDIUM |
| 5 | /tmp without noexec option | 1.1.2.3 | HIGH |
| 6 | /tmp without nosuid option | 1.1.2.4 | HIGH |
| 7 | /tmp without nodev option | 1.1.2.2 | MEDIUM |

## Weak SSH Configuration

Container SSH config (intentionally weak):
- `PermitRootLogin yes`
- `PasswordAuthentication yes`
- `PermitEmptyPasswords yes`
- `MaxAuthTries 10`

These were used as demo triggers but would also fail CIS checks.

## Total Alerts (as of demo)

- demo-web-01: ~25 alerts (system events, Docker errors)
- demo-weak-01: ~195 alerts (CIS failures, SSH auth events, systemd)

## Remediation Path

All CIS findings can be remediated using Sentinel Ops hardening playbook:
1. Create separate /tmp partition with noexec,nosuid,nodev options
2. Disable unused filesystems (squashfs, freevxfs, udf)
3. SSH hardening (root login disabled, key-only auth)
4. Firewall (default deny)
5. Auditd logging enabled

