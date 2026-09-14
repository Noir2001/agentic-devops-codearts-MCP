## MCP Implementation Repository

This project is implemented and maintained in the following GitHub repository:
**[agentic-devops-codearts-MCP](https://github.com/Noir2001/agentic-devops-codearts-MCP)**
The repository contains the MCP-based implementation used to connect CodeArts Agent with DevOps tools and demonstrate an Agentic DevOps workflow.
The MCP layer provides the tool connectivity required for the Agent to interact with external DevOps capabilities.
The overall mechanism is:


```text
User Request
     |
     v
CodeArts Agent
     |
     v
Agent Skill
     |
     v
MCP Server
     |
     +-------------------+
     |                   |
     v                   v
CodeArts Check      CodeArts Build
     |                   |
     v                   v
Check Result         Build Result
     |                   |
     +---------+---------+
               |
               v
          Final Report

# Agentic DevOps Demo
A simple Proof of Concept (PoC) for testing autonomous DevOps with Huawei CodeArts Agent.

## Project Goal
This project demonstrates how CodeArts Agent can orchestrate DevOps tasks using CodeArts tools.
The initial workflow is:
```text
CodeArts Agent
      |
      v
CodeArts Check
      |
      v
Check Result
      |
      v
CodeArts Build
      |
      v
Build + Tests
      |
      v
Final Result



#Tasks

Task 1 - Code Check
___________________
The Agent checks the entire repository for code quality issues and bugs.
Prompt:
Check the entire current repository for bugs and code quality issues. Use the available CodeArts Check tool and report the result. Do not modify the code.
Expected result:
Code Check: PASS
No blocking issues found.

Task 2 - Build
______________
After the code check passes, the Agent builds the repository.
Prompt:
Build the entire current repository using the available CodeArts Build tool. Run the tests and report the build result and generated artifact.
Expected result:
Build: SUCCESS

Tests:
3 passed
Artifact:
agentic-devops-demo.tar.gz



#Autonomous Workflow Test
After Task 1 and Task 2 work separately, test both tasks with one request.
Use this prompt:
Check the entire repository. If the check passes, build the repository and report the result of every step. Do not deploy to production.
User Request
     |
     v
CodeArts Agent
     |
     v
Inspect Repository
     |
     v
CodeArts Check
     |
     +---- FAIL ----> Stop and Report
     |
    PASS
     |
     v
CodeArts Build
     |
     +---- FAIL ----> Stop and Report

     |
   SUCCESS
     |
     v
Final Report

Automated Tests
The project contains three tests:
test_add
test_calculate_total
test_health
Expected local test result:
3 passed


