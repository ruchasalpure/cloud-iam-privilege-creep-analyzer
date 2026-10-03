# Duties and Responsibilities for Cloud IAM Privilege Creep Analyzer Agent

## Dual-Control Architecture
Maker:
policy-graph-reducer

Checker:
blast-radius-checker

## Operational Workflow
1. The Maker (policy-graph-reducer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (blast-radius-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
