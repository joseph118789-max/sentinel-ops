# Sentinel Ops — 30-Day Pilot Execution Plan

## Purpose
This pilot is designed to prove value fast on a limited scope. It is not a full security transformation project.

The pilot exists to:
- deploy monitoring quickly
- identify meaningful risks
- improve baseline security hygiene
- produce a management-friendly output
- convert into a recurring managed service if value is proven

## Pilot Scope Principles
Keep scope narrow and controlled:
- 3 to 10 Linux servers
- one environment, team, or business unit
- one primary customer point of contact
- one agreed escalation path
- no full-company rollout during pilot
- no custom engineering unless explicitly approved

## Commercial Guardrails
- Pilot duration: 30 days
- Pilot fee: RM 2,000 to RM 5,000 depending on scope
- Asset count must be agreed before kickoff
- Additional scope requires repricing or deferral to post-pilot phase
- Pilot is not a 24/7 SOC, full IR retainer, or full compliance engagement

## Week 0 — Pre-Start and Kickoff Preparation
### Objective
Remove onboarding friction before technical work begins.

### Internal Actions
- confirm signed SOW
- confirm in-scope assets
- confirm supported OS versions
- confirm access method and deployment responsibilities
- define escalation channel
- define customer technical contact and fallback contact
- schedule kickoff call

### Customer Inputs Required
- asset list
- server IPs/hostnames
- environment notes
- access method or agent installation support
- known security concerns or audit pressure

### Deliverables
- pilot scope confirmation
- onboarding checklist
- kickoff agenda
- implementation schedule

### Success Condition
Pilot can start without missing access, missing asset data, or unclear ownership.

## Week 1 — Deployment and Baseline Visibility
### Objective
Get the monitoring layer live quickly and establish a baseline.

### Actions
- run kickoff call
- validate host list
- deploy Wazuh agents
- verify enrollment and connectivity
- group or label assets if needed
- validate alert routing
- capture baseline host posture

### Deliverables
- live monitored host list
- go-live confirmation
- baseline onboarding summary
- first-pass visibility notes

### Customer Experience Goal
The customer should feel onboarding was smooth and non-chaotic.

### Warning
Do not over-tune detections in Week 1. Live visibility first, tuning second.

## Week 2 — Alert Triage and Risk Identification
### Objective
Separate noise from signal and surface meaningful issues quickly.

### Actions
- review early alerts
- suppress obvious false-noise items where justified
- identify top risks
- classify issues by category:
  - auth/access
  - configuration weakness
  - vulnerability/patching
  - exposed service
  - monitoring/logging gap
- prepare interim notes for customer

### Deliverables
- interim findings summary
- prioritized findings list
- recommended next actions

### Customer Experience Goal
The customer should feel they are already learning useful things from the pilot.

### Warning
Do not try to engineer a perfect detection program. This is a proof-of-value phase.

## Week 3 — Hardening and Improvement Work
### Objective
Demonstrate visible, practical security improvement.

### Actions
- review approved hardening scope
- run safe hardening tasks on selected systems
- document before/after state
- identify which actions were completed vs pending approval
- note unresolved risks requiring customer action

### Deliverables
- hardening change log
- before/after evidence
- remediation tracker

### Customer Experience Goal
The customer should feel Sentinel Ops improves security posture, not just observes it.

### Warning
Do not make risky production changes without explicit approval.

## Week 4 — Reporting, Review, and Conversion
### Objective
Summarize value clearly and make the path to ongoing service obvious.

### Actions
- prepare final monthly/pilot report
- summarize monitored assets
- summarize alerts reviewed
- summarize top findings and business impact
- summarize hardening changes made
- summarize open risks and recommended next actions
- include compliance-readiness observations where relevant
- run pilot review call
- recommend next service tier

### Deliverables
- pilot summary report
- review meeting
- commercial recommendation for continuation

### Customer Experience Goal
The customer should feel continuing the service is the logical next step.

## Pilot Success Criteria
Pilot is considered successful if at least 4 of the following are true:
- monitored hosts deployed successfully
- meaningful security findings identified
- noisy alerts reduced to manageable level
- hardening improvements completed on agreed systems
- customer receives management-friendly reporting
- customer understands ongoing risks and next steps
- customer sees clear value in continued monitoring

## Common Pilot Risks
- scope expands beyond agreed host count
- unsupported or messy environments consume too much time
- customer expects unlimited remediation
- customer assumes 24/7 coverage
- technical contact is unresponsive
- custom requests derail repeatability

## Guardrail Responses
If scope expands:
- pause and re-scope
- document change
- propose post-pilot expansion

If customer asks for unsupported work:
- acknowledge the need
- separate from pilot scope
- quote later if strategically useful

## Conversion Trigger
At the end of the pilot, ask one direct question:
"Do you want to stop here with the findings and improvements delivered, or continue into a managed monthly service so visibility, hardening, and reporting remain active?"

## Internal Weekly Rhythm
- Monday: review alerts and open items
- Tuesday: analyze findings and draft recommendations
- Wednesday: hardening/remediation work
- Thursday: reporting and customer follow-up
- Friday: commercial review, pipeline, and conversion prep

## Final Principle
The pilot should feel structured, fast, and useful. If it starts feeling like a custom consulting swamp, tighten the scope immediately.
