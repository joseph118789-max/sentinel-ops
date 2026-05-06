# Hardening Before State — demo-web-01

## SSH Configuration (Before)

| Setting | Current Value | Default Risk |
|---------|-------------|-------------|
| PermitRootLogin | #PermitRootLogin (commented = default = prohibit-password) | MEDIUM |
| PasswordAuthentication | #PasswordAuthentication (commented = default = yes) | HIGH |
| MaxAuthTries | #MaxAuthTries (commented = default = 6) | MEDIUM |
| ClientAliveInterval | #ClientAliveInterval (commented = 0 = disabled) | MEDIUM |
| Protocol | not set (default = SSH 2) | LOW |

**Issues identified:**
1. Root login via password potentially allowed (default SSH behavior)
2. Password authentication enabled (vulnerable to brute force)
3. No idle timeout (unattended sessions stay open)
4. Max auth tries not explicitly limited

## Firewall

- UFW: not installed
- SSH port 22: open to all (0.0.0.0/0)
- No firewall rules restricting access

## Audit/Syslog

- auditd: NOT installed
- No centralized logging of auth events
- No file integrity monitoring configured

## System

- Kernel params: default (ICMP redirects enabled, source routing enabled)
- Core dumps: enabled
- Unused filesystems: loaded (cramfs, jffs2, vfat, etc.)

