# Hardening After State — demo-web-01

## SSH Configuration (AFTER)

| Setting | Before | After | Status |
|---------|--------|-------|--------|
| PermitRootLogin | # (default = prohibit-password) | no | ✅ Fixed |
| PasswordAuthentication | # (default = yes) | no | ✅ Fixed |
| MaxAuthTries | # (default = 6) | 3 | ✅ Fixed |
| ClientAliveInterval | # (0 = disabled) | 900 (15 min) | ✅ Fixed |
| ClientAliveCountMax | # (default = 3) | 3 | ✅ Configured |

## Commands Applied

```bash
# Applied via Sentinel Ops hardening playbook (manual execution):
sed -i 's/^#*PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/^#*MaxAuthTries.*/MaxAuthTries 3/' /etc/ssh/sshd_config
sed -i 's/^#*ClientAliveInterval.*/ClientAliveInterval 900/' /etc/ssh/sshd_config
sed -i 's/^#*ClientAliveCountMax.*/ClientAliveCountMax 3/' /etc/ssh/sshd_config
systemctl restart sshd
```

## Backup

Original SSH config backed up to: `/tmp/sshd_config.backup`

## Rollback Command

```bash
cp /tmp/sshd_config.backup /etc/ssh/sshd_config && systemctl restart sshd
```

