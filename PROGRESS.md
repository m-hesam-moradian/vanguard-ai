# 📍 veritasnet — Flight Recorder & Engineering State Anchor

> **Zero-Context Resumption Protocol:** When starting a new chat, the AI Assistant reads this file and the active Git branch to instantly resume exactly where we left off, with zero explanation needed.

---

## 🎯 Current Mission Cockpit

| Attribute | Current Value | Description |
| :--- | :--- | :--- |
| **Active Milestone** | **Milestone 1: Core Foundation, Packaging & Config** | Workspace packaging, type-safe settings, domain schemas, spot-check verifier |
| **Active Step** | **Step 2: Environment Overrides, Range Validation & Secrets** | `src/veritasnet/config.py` (SecretStr, Port ranges, .env loading) |
| **Active Phase** | **Phase 0: Options Brief & GitHub Issue Setup** | Ready to kick off Step 2 |
| **Git Branch** | `main` | Clean on main |
| **GitHub Issue** | `#1` (Closed via PR #4) | Issue #1 complete |
| **State Status** | 🟢 Step 1 Complete & Merged ➔ Ready for Step 2 | Next: Port range validation & SecretStr |

---

## ⏭️ Immediate Next Action (Cold-Start Pointer)
1. Branch out for Step 2 (`feat/issue-2-config-validation-secrets`).
2. Add port range constraints (`ge=1024, le=65535`) and secret masking (`SecretStr`).
3. Add TDD red tests for invalid ports, missing secrets, and `.env` loading.

---

## 📝 Key Architectural Decisions & Log
| Timestamp | Step / Component | Decision Made | Rationale |
| :--- | :--- | :--- | :--- |
| 2026-11-08 | System / Mentor | Implemented Dual-Sync Session Protocol (`PROGRESS.md` + GitHub Issues/Milestones) | Solves chat context loss; allows instant cold resumption in new chats while displaying live progress on GitHub. |
| 2026-11-10 | Architecture / Spec | Aligned to VeritasNet Decentralized PoTW & 2026 MLOps Standards | Comprehensive enterprise MLOps platform (Triton, vLLM, MLflow v3, Airflow 3.1, pgvector, LangGraph). |
| 2026-11-14 | Step 1 / Config | Standardized on `pyproject.toml` (PEP 518/621) + `pydantic-settings` v2 | Guarantees immutable, type-safe settings with zero global side-effects. |

---

## 🗺️ Progressive Milestone Roadmap & GitHub Progress

### 🌱 Milestone 1: Core Foundation, Verifiable Contracts & PoTW Engine
*GitHub Milestone: `Milestone 1: Core Foundation`*

- [x] **Step 1: Workspace Packaging & Type-Safe Config**
  - **Path:** `pyproject.toml`, `src/veritasnet/config.py`
  - **Issue:** `#1` (Closed) | **PR:** `#4` (Merged)
  - **Checklist:** `[x] Phase 0` | `[x] Phase A` | `[x] Phase B` | `[x] Phase C` | `[x] Phase D` | `[x] Phase E`
  - **Status:** 🟢 **DONE**
- [ ] **Step 2: Strict Pydantic v2 Schemas for Task Manifests & Merkle Proofs**
  - **Path:** `src/veritasnet/schemas/domain.py`
  - **Issue:** `#2` | **PR:** `—`
  - **Checklist:** `[ ] Phase 0` | `[ ] Phase A` | `[ ] Phase B` | `[ ] Phase C` | `[ ] Phase D` | `[ ] Phase E`
  - **Status:** 🟡 Up Next
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
