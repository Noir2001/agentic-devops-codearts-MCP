---
name: autonomous-devops
description: Run the safe CodeArts demo workflow: check the repository first, then build it only when the check succeeds.
---
# Autonomous DevOps Demo
When the user asks to run the demo workflow:

1. Inspect the current repository.
2. Run the available CodeArts Check tool against the repository.
3. Report the check result.
4. If the check passes, use the available CodeArts Build tool to build the repository.
5. Report the build result and artifact.
6. Do not deploy to production.
7. If a step fails, stop and explain the error instead of claiming success.
