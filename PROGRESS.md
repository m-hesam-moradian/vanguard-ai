# 📍 veritasnet — Flight Recorder & Engineering State Anchor

> **Zero-Context Resumption Protocol:** When starting a new chat, the AI Assistant reads this file and the active Git branch to instantly resume exactly where we left off, with zero explanation needed.

---

## 🎯 Current Mission Cockpit

| Attribute | Current Value | Description |
| :--- | :--- | :--- |
| **Active Milestone** | **Milestone 1: Core Foundation, Packaging & Config** | Workspace packaging, type-safe settings, domain schemas, spot-check verifier |
| **Active Step** | **Step 1: Workspace Packaging & Type-Safe Config** | `pyproject.toml` + `src/veritasnet/config.py` |
| **Active Phase** | **Phase D: Verification Gate & Chaos Lab** | Answering architectural questions and running the 30-second break-it test |
| **Git Branch** | `feat/issue-1-config-foundation` | Feature branch for Step 1 |
| **GitHub Issue** | `#1` | [Issue #1](https://github.com/m-hesam-moradian/veritasnet/issues/1) linked to Milestone 1 |
| **State Status** | 🟢 Green Phase Verified ➔ Phase D Active | Verification & chaos experiment |

---

## ⏭️ Immediate Next Action (Cold-Start Pointer)
1. Present the **Engineering Options Menu** for Step 1 (`pydantic-settings` vs. `dynaconf` vs. `hydra` + packaging with `uv`).
2. Run `gh issue create` to create GitHub Issue #1.
3. Check out branch `feat/issue-1-config-foundation` to begin Phase 0.

---

## 📝 Key Architectural Decisions & Log
| Timestamp | Step / Component | Decision Made | Rationale |
| :--- | :--- | :--- | :--- |
| 2026-11-08 | System / Mentor | Implemented Dual-Sync Session Protocol (`PROGRESS.md` + GitHub Issues/Milestones) | Solves chat context loss; allows instant cold resumption in new chats while displaying live progress on GitHub. |
| 2026-11-10 | Architecture / Spec | Aligned to veritasnet Decentralized PoTW & 2026 MLOps Standards | Comprehensive enterprise MLOps platform (Triton, vLLM, MLflow v3, Airflow 3.1, pgvector, LangGraph). |

---

## 🗺️ Progressive Milestone Roadmap & GitHub Progress

### 🌱 Milestone 1: Core Foundation, Verifiable Contracts & PoTW Engine
*GitHub Milestone: `Milestone 1: Core Foundation`*

- [ ] **Step 1: Workspace Packaging & Type-Safe Config**
  - **Path:** `pyproject.toml`, `src/veritasnet/config.py`
  - **Issue:** `#1` | **PR:** `—`
  - **Checklist:** `[x] Phase 0` | `[x] Phase A` | `[ ] Phase B` | `[ ] Phase C` | `[ ] Phase D` | `[ ] Phase E`
  - **Status:** 🟡 In Progress (Branch: `feat/issue-1-config-foundation`)
- [ ] **Step 2: Strict Pydantic v2 Schemas for Task Manifests & Merkle Proofs**
  - **Path:** `src/veritasnet/schemas/domain.py`
  - **Issue:** `#2` | **PR:** `—`
  - **Checklist:** `[ ] Phase 0` | `[ ] Phase A` | `[ ] Phase B` | `[ ] Phase C` | `[ ] Phase D` | `[ ] Phase E`
  - **Status:** ⏳ Queued
- [ ] **Step 3: Cryptographic Merkle Tree & Verde Single-Step PoTW Verifier**
  - **Path:** `src/veritasnet/potw/verifier.py`
  - **Issue:** `#3` | **PR:** `—`
  - **Checklist:** `[ ] Phase 0` | `[ ] Phase A` | `[ ] Phase B` | `[ ] Phase C` | `[ ] Phase D` | `[ ] Phase E`
  - **Status:** ⏳ Queued

### ⛏️ Milestone 2: Deterministic Mining, Byzantine Defense & Economic Ledger
*GitHub Milestone: `Milestone 2: Training & Consensus`*

- [ ] **Step 4: Deterministic PyTorch + LoRA Miner Training Node** (`src/veritasnet/training/miner.py`)
- [ ] **Step 5: Byzantine Defense Engine (Multi-Krum + Cosine Guard)** (`src/veritasnet/training/aggregator.py`)
- [ ] **Step 6: Economic Consensus, Staking Vault & Slashing Ledger** (`src/veritasnet/ledger/consensus.py`)

### 🗄️ Milestone 3: Storage Sovereignty & Agentic Governance
*GitHub Milestone: `Milestone 3: Sovereignty & Agents`*

- [ ] **Step 7: PostgreSQL 16 + pgvector & MLflow v3 S3 Registry Client** (`src/veritasnet/db/registry.py`)
- [ ] **Step 8: FastMCP Tool Server & LangGraph Autonomous Audit Orchestrator** (`src/veritasnet/agents/audit_graph.py`)

### 🚀 Milestone 4: High-Concurrency Serving, Airflow & Production Deployment
*GitHub Milestone: `Milestone 4: Serving & Infrastructure`*

- [ ] **Step 9: High-Concurrency FastAPI ASGI Gateway & Triton/vLLM Client** (`src/veritasnet/api/main.py`)
- [ ] **Step 10: Apache Airflow 3.1 Retraining Micro-DAG, Langfuse Tracing & Docker Cluster** (`docker-compose.yml`)
