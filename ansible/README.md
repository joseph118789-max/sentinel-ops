# Sentinel Ops — Ansible Playbooks

## Overview

These playbooks deploy and manage the Sentinel Ops managed security stack.

```
ansible/
├── playbooks/
│   ├── wazuh-manager.yml      # Deploy Wazuh manager on our infrastructure
│   ├── wazuh-agent.yml         # Deploy Wazuh agent on client servers
│   ├── hardening.yml           # Apply CIS hardening to servers
│   └── demo-setup.yml          # Set up demo environment (3 VMs)
├── roles/
│   ├── wazuh-manager/          # Wazuh server role
│   ├── wazuh-agent/            # Wazuh client agent role
│   └── hardening/              # CIS hardening role
├── inventories/
│   ├── demo/                   # Demo environment hosts
│   └── clients/                # Per-client inventories
└── ansible.cfg
```

---

## Quick Start

```bash
# Deploy Wazuh Manager (our server)
ansible-playbook playbooks/wazuh-manager.yml -i inventories/demo/hosts.yml

# Deploy Wazuh Agent to client servers
ansible-playbook playbooks/wazuh-agent.yml -i inventories/clients/acme/hosts.yml --limit web-01

# Apply hardening to a server
ansible-playbook playbooks/hardening.yml -i inventories/clients/acme/hosts.yml --limit db-01
```

---

## Inventory Structure

```yaml
# inventories/demo/hosts.yml
all:
  vars:
    ansible_user: sentinel
    ansible_python_interpreter: /usr/bin/python3
    wazuh_manager_ip: 10.0.1.50
    sentinel_ops_team: agent@openclaw.ai
  children:
    wazuh_managers:
      hosts:
        wazuh-01:
          ansible_host: 10.0.1.50
          os: ubuntu 22.04
    demo_servers:
      hosts:
        web-01:
          ansible_host: 10.0.2.10
          os: ubuntu 22.04
          server_role: web
          client: demo
        db-01:
          ansible_host: 10.0.2.11
          os: ubuntu 22.04
          server_role: database
          client: demo
        mail-01:
          ansible_host: 10.0.2.12
          os: debian 11
          server_role: mail
          client: demo
```

---

*Version: 1.0 | Created: 2026-05-06*