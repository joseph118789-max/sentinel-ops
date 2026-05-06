# PDPA + RMIT Mapping (Lite) — Sentinel Ops

## Purpose

This is a lightweight PDPA (Personal Data Protection Act 2010, Malaysia) compliance mapping document for SMEs. It maps security controls to PDPA requirements, helping clients understand how Sentinel Ops helps with compliance.

**This is not legal advice.** For formal compliance, consult a PDPA-qualified lawyer. This document is a practical security control mapping.

---

## What Is PDPA?

The Personal Data Protection Act 2010 (PDPA) governs how Malaysian businesses collect, process, and protect personal data. It applies to:
- Any business that processes personal data of Malaysian individuals
- Data users (organizations that control the processing)
- Data processors (organizations that process on behalf of data users)

**7 Principles of PDPA:**
1. General Principle — lawful, fair, and transparent processing
2. Purpose Principle — collected for specific, legitimate purposes
3. Disclosure Principle — not disclosed beyond what was stated
4. Retention Principle — not kept longer than necessary
5. Data Integrity Principle — accurate and complete
6. Access Principle — individuals can access their data
7. Correction Principle — individuals can correct inaccurate data

---

## How Sentinel Ops Maps to PDPA Requirements

| PDPA Principle | Security Control | How We Help |
|----------------|-----------------|-------------|
| **General Principle** | Access controls, logging, audit trails | We enforce key-based auth, disable root, track who's accessing systems |
| **Purpose Principle** | Data classification, access restrictions | We help identify where personal data lives, restrict access |
| **Disclosure Principle** | Network segmentation, monitoring | We detect unauthorized data access or exfiltration attempts |
| **Retention Principle** | Log retention, data lifecycle | We help define and enforce retention policies via log management |
| **Data Integrity** | File integrity monitoring, alerts | Wazuh FIM detects unauthorized file changes (critical for data integrity) |
| **Access Principle** | Authentication logging | Full audit trail of who accessed what and when |
| **Correction Principle** | Data inventory | We help identify where personal data is stored (pre-requisite for correction) |

---

## PDPA Requirements and Our Coverage

### 1. Security Measures (Section 9)

PDPA requires: "Appropriate security measures to prevent unauthorized access, loss, or disclosure."

| Requirement | Our Coverage | Evidence |
|-------------|-------------|-----------|
| **Access control** | SSH hardening, key-only auth, firewall, sudo controls | Weekly alert report shows failed auth attempts |
| **Encryption** | Recommend disk encryption, TLS for data in transit | Onboarding checklist includes encryption review |
| **Monitoring** | Continuous Wazuh monitoring, alert triage | Monthly report shows monitoring coverage |
| **Incident response** | Alert triage, escalation, remediation support | Incident log in client folder |
| **Audit trail** | Full logging via auditd + Wazuh | Available for audit requests |

**What we do NOT cover:**
- Application-level encryption (client's responsibility)
- Physical security of servers (client's responsibility)
- Network segmentation beyond server hardening

---

### 2. Retention and Disposal (Section 9)

PDPA requires: "Not keep personal data longer than necessary."

| Requirement | Our Coverage | Evidence |
|-------------|-------------|-----------|
| **Data lifecycle** | We help identify where personal data is stored | Client inventory includes data locations |
| **Secure disposal** | We help ensure secure deletion processes | Logged in incidents file |
| **Log retention** | 90-day Elasticsearch retention (configurable) | Retention policy documented |

**Limitation:** We do not manage the client's database or application data retention directly — this is an application/infrastructure decision.

---

### 3. Data Subject Rights

PDPA gives individuals the right to:
- Access their personal data
- Correct inaccurate data

| Requirement | Our Coverage | Evidence |
|-------------|-------------|-----------|
| **Data inventory** | Help identify where personal data is stored | Server inventory in client folder |
| **Access logging** | Full audit trail of who accessed what | Available via Elasticsearch queries |
| **Data location** | Help identify personal data systems | Discovery questions during onboarding |

---

### 4. Notification of Breach (Section 10)

PDPA requires notification to PDPA authority within 72 hours of a breach.

| Requirement | Our Coverage | Evidence |
|-------------|-------------|-----------|
| **Detection** | Wazuh detects anomalies, file integrity changes | Critical alerts within 15 min |
| **Investigation** | Alert triage + investigation support | We help determine scope of breach |
| **Documentation** | Incident log with timeline | Available for compliance audit |

**Limitation:** We do not notify PDPA on behalf of client — client must file. We provide the evidence and investigation support.

---

## RMIT (Rangka MatrixIndustri IT) Mapping

RMIT is a Malaysian government framework for IT industry maturity. Sentinel Ops maps to RMIT domains:

| RMIT Domain | RMIT Controls | Our Coverage |
|-------------|----------------|---------------|
| **GR01 — Governance** | Security policies, risk management | We provide security recommendations and risk reports |
| **GR02 — Human Capital** | Security training, awareness | Basic security hygiene guidance in reports |
| **GR03 — Technology** | Secure infrastructure | Server hardening, monitoring |
| **GR04 — Process** | Incident management, change management | Alert triage, incident response |
| **GR05 — Data** | Data protection, access control | File integrity monitoring, access logging |

---

## PDPA Compliance Quick Checklist

For a client to assess their PDPA compliance, we use this as a starting point:

- [ ] Do you have a data protection policy?
- [ ] Do you know where all personal data is stored?
- [ ] Is access to personal data restricted (least privilege)?
- [ ] Are authentication logs tracked and retained?
- [ ] Are there procedures for data subject access requests?
- [ ] Is personal data encrypted at rest and in transit?
- [ ] Do you have an incident response plan?
- [ ] Is there a process for reporting breaches to PDPA?
- [ ] Are third parties (vendors) compliant?

Sentinel Ops helps with the technical controls (logging, access, hardening, monitoring). The policy and process side is the client's responsibility (or their legal advisor).

---

## What Clients Get

When a client asks about PDPA compliance, we deliver:

1. **PDPA-lite gap assessment** (Sentinel tier and above)
   - Identify where personal data likely resides
   - Review current access controls
   - Identify high-risk areas
   - Gap report: what needs to be fixed

2. **Monitoring alignment**
   - Ensure logging covers personal data systems
   - Alert rules tuned for personal data access anomalies

3. **Evidence package** (for audit, if needed)
   - Access logs for the period
   - Configuration audit (hardening status)
   - Incident log
   - Monthly reports as evidence of ongoing management

---

## What We DON'T Do (Legal Disclaimer)

- **We are not a law firm.** This document is practical security guidance, not legal advice.
- **PDPA compliance is the client's responsibility** — we support the technical controls.
- **We don't guarantee PDPA compliance** — compliance depends on the client's full operations, not just server hardening.
- **For formal compliance certification**, client should engage a PDPA consultant or legal firm.

---

## Recommended Next Steps (for Client)

If client wants to move toward full PDPA compliance:

1. **Engage a PDPA consultant** (legal firm specializing in data protection)
2. **Conduct a formal data mapping exercise** (data inventory across all systems)
3. **Implement a DPO (Data Protection Officer)** if required
4. **Document all data processing activities** (RMIT / ISO 27001 approach)
5. **Consider ISO 27001 certification** if the client handles sensitive personal data at scale

Sentinel Ops can help with steps 2–5 (technical controls only).

---

*Version: 1.0 | Created: 2026-05-06*  
*Disclaimer: This document is for guidance only and does not constitute legal advice. Consult a qualified lawyer for formal PDPA compliance.*