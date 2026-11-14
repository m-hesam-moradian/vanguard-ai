# ⚡ veritasnet

> **Decentralized Proof-of-Training-Work (PoTW) & Enterprise MLOps Infrastructure**  
> A Production-Grade Decentralized Training, Byzantine-Resilient Federated Learning, and High-Throughput Model Serving Platform built on **2026 MLOps Architectural Standards**.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-e92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x%2BPEFT-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-ASGI_Concur-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![NVIDIA Triton](https://img.shields.io/badge/Serving-Triton_%2B_vLLM-76b900?logo=nvidia&logoColor=white)](https://github.com/triton-inference-server/server)
[![MLflow](https://img.shields.io/badge/Registry-MLflow_v3-0194e2?logo=mlflow&logoColor=white)](https://mlflow.org/)
[![LangGraph](https://img.shields.io/badge/Agents-LangGraph-000000?logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![FastMCP](https://img.shields.io/badge/Tools-FastMCP-6366f1)](https://github.com/jlowin/fastmcp)
[![PostgreSQL](https://img.shields.io/badge/Storage-PostgreSQL_16_%2B_pgvector-336791?logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Apache Airflow](https://img.shields.io/badge/Orchestration-Airflow_3.1-017cee?logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
[![CI Gate](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/m-hesam-moradian/veritasnet/actions)
[![Progress](https://img.shields.io/badge/Roadmap-Milestone_1_%7C_Step_1-orange)](#-live-engineering-progress-tracker)

---

## 🏛️ System Architecture

```mermaid
flowchart TB
    subgraph Ingestion["🌊 1. Streaming Feature & Data Pipeline Layer"]
        KAFKA["Apache Kafka Event Bus<br/>(Live Telemetry & Training Shards)"]
        SPARK["Apache Spark Batch ETL<br/>(Shard Tokenization & Normalization)"]
        CASS[("Apache Cassandra<br/>Low-Latency Online Feature Store")]
        AIRFLOW["Apache Airflow 3.1 Micro-DAGs<br/>(Asset-Aligned Retraining Scheduler)"]
    end

    subgraph ControlPlane["⚡ 2. I/O-Bound Control Plane & Agentic Orchestrator"]
        FASTAPI["FastAPI + Uvicorn Multi-Worker ASGI<br/>(Pydantic v2 Validation & SSE Streams)"]
        LANGGRAPH["LangGraph Cyclic Orchestrator<br/>(Autonomous Round Triage & Audit Agent)"]
        MCP["FastMCP Tool Server<br/>(GitHub MCP, Sandbox Verifier, Ledger RPC)"]
    end

    subgraph Miners["⛏️ 3. Decentralized Untrusted GPU Miner Swarm"]
        M1["Miner Node A (Honest)<br/>PyTorch + LoRA/PEFT + Deterministic Seed"]
        M2["Miner Node B (Honest)<br/>Ollama / Open-Weight Local Fine-Tuning"]
        M3["Miner Node C (Byzantine Attacker)<br/>Poisoned Gradients / Lazy Noise"]
    end

    subgraph PoTW["🛡️ 4. Probabilistic Proof-of-Training-Work (PoTW) & Byzantine Engine"]
        MERKLE["1. Merkle Trajectory Commitment<br/>SHA-256 Hash Chain of State Checkpoints"]
        SPOT["2. Verde Single-Step Spot-Checker<br/>Re-computes 1 Random Step (t ➡️ t+1)"]
        KRUM["3. Multi-Krum & Cosine Distance Guard<br/>Rejects Outlying Adversarial Gradients"]
        HOLDOUT["4. Golden Holdout Loss Evaluator<br/>Verifies ΔLoss < 0 on Secret Test Split"]
        LEDGER["5. Staking & Slashing Consensus Engine<br/>(Yuma / Shapley Weight Scoring)"]
    end

    subgraph Storage["🗄️ 5. Unified Data & Sovereignty Registry Layer"]
        PG[("PostgreSQL 16 + pgvector + PostgresML<br/>Control Plane, HNSW Vectors & In-DB ML")]
        MLFLOW["MLflow v3 Model Registry<br/>(Unity Catalog RBAC + OTel Autologging)"]
        S3[("Customer-Owned S3 / MinIO Bucket<br/>Full Artifact & Checkpoint Sovereignty")]
    end

    subgraph Serving["🚀 6. Compute-Bound GPU Inference & LLMOps Observability"]
        TRITON["NVIDIA Triton Inference Server<br/>(Dynamic Batching, gRPC/HTTP, Multi-Model)"]
        VLLM["vLLM Inference Backend<br/>(PagedAttention KV-Cache & Continuous Batching)"]
        EVAL["Live LLMOps Guardrails & Tracing<br/>(Langfuse + Confident AI + OpenTelemetry)"]
    end

    KAFKA --> SPARK --> PG
    KAFKA --> CASS
    AIRFLOW -->|"Triggers Micro-DAG"| FASTAPI
    FASTAPI <--> LANGGRAPH <--> MCP
    FASTAPI -->|"Dispatches Epoch Task + Seed"| M1 & M2 & M3
    M1 & M2 & M3 -->|"Submits LoRA Delta + Merkle Proof"| MERKLE
    MERKLE --> SPOT --> KRUM --> HOLDOUT --> LEDGER
    LEDGER -->|"Verified Clean Weights (FedAvg)"| MLFLOW
    MLFLOW --> PG & S3
    MLFLOW -->|"Canary Rollout"| TRITON
    TRITON --> VLLM
    VLLM --> EVAL
    EVAL -.->|"Drift / Hallucination Alert"| AIRFLOW
```

---

## 📊 Live Engineering Progress Tracker

All steps are built following **strict Test-Driven Development (TDD)** and **Agile GitHub Flow**.  
Real-time session state is tracked in [`PROGRESS.md`](PROGRESS.md) and full technical specs in [`ARCHITECTURE.md`](ARCHITECTURE.md).

### 🌱 Milestone 1: Core Foundation, Verifiable Contracts & PoTW Engine
| Step | Component | Technology | Target File | Issue | Status |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **01** | Workspace Packaging & Type-Safe Config | `uv`, `pydantic-settings` | `src/veritasnet/config.py` | [#1](#) | 🟡 **In Progress** |
| **02** | Strict Pydantic v2 Task Manifests & Merkle Schemas | `Pydantic v2` | `src/veritasnet/schemas/domain.py` | — | ⏳ Queued |
| **03** | Cryptographic Merkle Tree & Verde Spot-Check Verifier | `hashlib`, `Cryptography` | `src/veritasnet/potw/verifier.py` | — | ⏳ Queued |

### ⛏️ Milestone 2: Deterministic Mining, Byzantine Defense & Economic Ledger
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **04** | Deterministic PyTorch + LoRA Miner Training Node | `PyTorch`, `PEFT` | `src/veritasnet/training/miner.py` | ⏳ Queued |
| **05** | Byzantine Defense Engine (Multi-Krum + Cosine Guard) | `NumPy`, `SciPy` | `src/veritasnet/training/aggregator.py` | ⏳ Queued |
| **06** | Economic Consensus, Staking Vault & Slashing Ledger | `Yuma / Shapley Consensus` | `src/veritasnet/ledger/consensus.py` | ⏳ Queued |

### 🗄️ Milestone 3: Storage Sovereignty & Agentic Governance
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **07** | PostgreSQL 16 + pgvector & MLflow v3 S3 Registry Client | `SQLAlchemy 2.0`, `pgvector`, `MLflow v3` | `src/veritasnet/db/registry.py` | ⏳ Queued |
| **08** | FastMCP Tool Server & LangGraph Autonomous Audit Agent | `FastMCP`, `LangGraph` | `src/veritasnet/agents/audit_graph.py` | ⏳ Queued |

### 🚀 Milestone 4: High-Concurrency Serving, Airflow & Production Deployment
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **09** | High-Concurrency FastAPI ASGI Gateway & Triton/vLLM Client | `FastAPI`, `Uvicorn`, `Triton Client` | `src/veritasnet/api/main.py` | ⏳ Queued |
| **10** | Apache Airflow 3.1 Retraining Micro-DAG & Docker Cluster | `Airflow 3.1`, `Langfuse`, `Docker Compose` | `docker-compose.yml` | ⏳ Queued |

---

## 🛠️ Tech Stack & Engineering Standards
- **Python 3.12+** with zero untyped code (`mypy --strict`).
- **TDD First:** Every single feature starts with a red `pytest` suite before production code is written.
- **Contract-First:** All API manifests, Merkle state proofs, and agent tools are enforced by immutable Pydantic v2 schemas.
- **Storage Sovereignty:** Customer-owned S3 object buckets and self-hosted PostgreSQL/MLflow clusters—zero proprietary cloud lock-in.
- **Workload Physics Separation:** I/O-bound coordination (`FastAPI ASGI`) strictly separated from GPU-bound inference (`NVIDIA Triton` + `vLLM`).
- **Agile GitHub Flow:** Every change has a GitHub Issue, feature branch, conventional commit, and CI-gated Pull Request.

---

## 📄 License
MIT © [M. Hesam Moradian](https://github.com/m-hesam-moradian)
