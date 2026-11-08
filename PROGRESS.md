# 📍 VanguardAI — Flight Recorder & Engineering State Anchor

> **Zero-Context Resumption Protocol:** When starting a new chat, the AI Assistant reads this file and the active Git branch to instantly resume exactly where we left off, with zero explanation needed.

---

## 🎯 Current Mission Cockpit

| Attribute | Current Value | Description |
| :--- | :--- | :--- |
| **Active Milestone** | **Milestone 1: Core Foundation & Strict Contracts** | Initial setup, config validation, domain schemas, resilient AI gateway |
| **Active Step** | **Step 1: Workspace Packaging & Type-Safe Config** | `pyproject.toml` + `src/vanguard/config.py` |
| **Active Phase** | **Phase 0: Options Brief & GitHub Issue Setup** | Evaluating architecture options, creating Issue #1, and branching |
| **Git Branch** | `main` (Pending `feat/issue-1-config-foundation`) | Feature branch for Step 1 |
| **GitHub Issue** | `#1` (Pending creation) | Tracking issue with 6-phase task checklist |
| **State Status** | 🟡 Ready for Phase 0 Kickoff | Awaiting options decision and issue creation |

---

## ⏭️ Immediate Next Action (Cold-Start Pointer)
1. Present the **Engineering Options Menu** for Step 1 (`pydantic-settings` vs. `dynaconf` vs. `hydra` + packaging with `uv`).
2. Run `gh auth login` (if not already logged in) and create GitHub Issue #1.
3. Check out branch `feat/issue-1-config-foundation` to begin Phase 0.

---

## 📝 Key Architectural Decisions & Log
| Timestamp | Step / Component | Decision Made | Rationale |
| :--- | :--- | :--- | :--- |
| 2026-11-08 | System / Mentor | Implemented Dual-Sync Session Protocol (`PROGRESS.md` + GitHub Issues/Milestones) | Solves chat context loss; allows instant cold resumption in new chats while displaying live progress on GitHub. |

---

## 🗺️ Progressive Milestone Roadmap & GitHub Progress

### 🌱 Milestone 1: Core Foundation, Strict Contracts & Resilient AI Gateway
*GitHub Milestone: `Milestone 1: Core Foundation`*

- [ ] **Step 1: Workspace Packaging & Type-Safe Config**
  - **Path:** `pyproject.toml`, `src/vanguard/config.py`
  - **Issue:** `#1` | **PR:** `—`
  - **Checklist:** `[ ] Phase 0` | `[ ] Phase A` | `[ ] Phase B` | `[ ] Phase C` | `[ ] Phase D` | `[ ] Phase E`
  - **Status:** 🟡 Up Next
- [ ] **Step 2: Strict Domain & Adversarial Critic Schemas**
  - **Path:** `src/vanguard/schemas/domain.py`
  - **Status:** ⏳ Queued
- [ ] **Step 3: Multi-Provider LiteLLM Gateway with Retries & Budget Guards**
  - **Path:** `src/vanguard/llm/gateway.py`
  - **Status:** ⏳ Queued

### 🔎 Milestone 2: Hybrid Vector Memory (`pgvector`) & Sub-10ms Typst PDF Server
*GitHub Milestone: `Milestone 2: Memory & PDF Engine`*

- [ ] **Step 4: Async SQLAlchemy 2.0 Engine & `pgvector` HNSW ORM Models** (`src/vanguard/db/session.py`, `models.py`)
- [ ] **Step 5: Hybrid Vector + Keyword Search Repository** (`src/vanguard/db/repository.py`)
- [ ] **Step 6: FastMCP Typst PDF Compiler Server** (`src/vanguard/mcp/pdf_server.py`)

### 🤖 Milestone 3: Adversarial LangGraph & Self-Healing Browser Engine
*GitHub Milestone: `Milestone 3: Agentic Graphs & Browser`*

- [ ] **Step 7: Adversarial Resume Subgraph (Tailor ⇄ ATS Critic)** (`src/vanguard/agents/resume_subgraph.py`)
- [ ] **Step 8: Self-Healing Playwright + Vision Set-of-Marks MCP Server** (`src/vanguard/mcp/browser_server.py`)
- [ ] **Step 9: Master Orchestrator Graph with Postgres Checkpointing & HITL Interrupt** (`src/vanguard/agents/master_graph.py`)

### 🌐 Milestone 4: Distributed Scale, Streaming API, Evals & CI/CD
*GitHub Milestone: `Milestone 4: Production Scale & CI/CD`*

- [ ] **Step 10: Redis Portal-Selector Cache & Rate Limiter** (`src/vanguard/cache/redis_client.py`)
- [ ] **Step 11: FastAPI Async Server with SSE Live Streaming** (`src/vanguard/api/main.py`)
- [ ] **Step 12: Langfuse Tracing & Pytest LLM-as-a-Judge Eval Gate** (`tests/evals/test_hallucination_gate.py`)
- [ ] **Step 13: Production Docker Compose & GitHub Actions CI Pipeline** (`Dockerfile`, `.github/workflows/ci.yml`)
