# ⚡ VanguardAI

> **Autonomous, Anti-Hallucinatory Agentic Career Copilot & Stealth Application Engine**  
> Built from scratch with Python 3.12+, LangGraph, FastMCP, PostgreSQL 16 (`pgvector`), Redis 7, and LiteLLM.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-e92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![LangGraph](https://img.shields.io/badge/Agents-LangGraph-000000?logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![FastMCP](https://img.shields.io/badge/Tools-FastMCP-6366f1)](https://github.com/jlowin/fastmcp)
[![PostgreSQL](https://img.shields.io/badge/Storage-PostgreSQL_16_%2B_pgvector-336791?logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)
[![Redis](https://img.shields.io/badge/Cache-Redis_7-dc382d?logo=redis&logoColor=white)](https://redis.io)
[![CI Gate](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/m-hesam-moradian/vanguard-ai/actions)
[![Progress](https://img.shields.io/badge/Roadmap-Milestone_1_%7C_Step_1-orange)](#-live-engineering-progress-tracker)

---

## 🏛️ System Architecture

```mermaid
flowchart TB
    subgraph Client["🖥️ Client Layer"]
        UI["CLI / Next.js Live Dashboard"]
    end

    subgraph Gateway["⚡ API & Edge Layer (FastAPI + Redis 7)"]
        API["FastAPI Async Server<br/>(REST + SSE Live Stream)"]
        RL["Redis Sliding-Window<br/>Rate Limiter & Circuit Breaker"]
        SC["Redis Semantic JD Cache<br/>& Portal DOM Selector Cache"]
    end

    subgraph Orchestrator["🧠 LangGraph Stateful Multi-Agent Engine"]
        N1["1. JD Intelligence Node<br/>(Skill Weights & Knockouts)"]
        N2["2. Hybrid RAG Retriever<br/>(Dense Vector + BM25 + Reranker)"]
        
        subgraph Adversarial["⚔️ 3. Adversarial Resume Subgraph"]
            D["STAR Bullet Tailor Agent"]
            C["ATS Scorer & Hallucination Critic"]
            D -->|"Draft JSON"| C
            C -->|"Score < 90% or Hallucination > 0%<br/>(Self-Correction Loop)"| D
        end

        N4["4. Typst PDF Compiler Node<br/>(Sub-10ms ATS-Proof Render)"]
        
        subgraph BrowserEngine["🌐 5. Self-Healing Stealth Browser Agent"]
            DOM["DOM Accessibility Tree Parser"]
            SOM["Vision LLM Set-of-Marks (SoM)<br/>Bounding-Box Fallback"]
            DOM -.->|"Selector Broken / Shadow DOM"| SOM
        end

        HITL{{"🛑 6. HITL Interrupt Gate<br/>(Pauses State & Streams Screenshot)"}}
        SUB["7. Final Portal Submit & Audit Log"]
    end

    subgraph MCP["🔧 FastMCP Standardized Tool Servers"]
        MCP_PDF["MCP Server: Typst Compiler"]
        MCP_PW["MCP Server: Playwright Stealth Pool"]
    end

    subgraph Storage["🗄️ Data & Persistence Layer (PostgreSQL 16)"]
        PG_VEC[("pgvector (HNSW Index)<br/>Master Career & Project Chunks")]
        PG_CHK[("LangGraph Checkpointer<br/>Resumable Thread State")]
        PG_AUD[("Relational Audit Tables<br/>Applications, JDs, PDF Hashes")]
    end

    subgraph LLMOps["🛡️ Unified AI Gateway & Observability"]
        LITE["LiteLLM Router + Tenacity Retries<br/>(Cost Budget & Auto-Failover)"]
        MODELS["Claude 3.7 Sonnet / GPT-4o / Local vLLM"]
        LF["Langfuse + OpenTelemetry<br/>(Trace Spans, Latency, Token Cost)"]
    end

    UI <-->|"HTTPS / SSE Stream"| API
    API --> RL --> SC --> N1
    N1 --> N2
    N2 <-->|"Cosine + Keyword Query"| PG_VEC
    N2 --> D
    C -->|"Verified Resume JSON"| N4
    N4 <-->|"JSON-RPC"| MCP_PDF
    N4 --> DOM
    DOM <-->|"Read/Write Learned Selectors"| SC
    DOM <-->|"JSON-RPC"| MCP_PW
    SOM <-->|"JSON-RPC"| MCP_PW
    DOM --> HITL
    SOM --> HITL
    HITL <-->|"Persist/Resume State"| PG_CHK
    HITL -->|"Human 1-Click Approve"| SUB
    SUB --> PG_AUD

    N1 & D & C & SOM --> LITE --> MODELS
    Orchestrator -.->|"Async OTel Spans"| LF
```

---

## 📊 Live Engineering Progress Tracker

All steps are built following **strict Test-Driven Development (TDD)** and **Agile GitHub Flow**.  
Real-time session state is tracked in [`PROGRESS.md`](PROGRESS.md) and full technical specs in [`ARCHITECTURE.md`](ARCHITECTURE.md).

### 🌱 Milestone 1: Core Foundation, Strict Contracts & Resilient AI Gateway
| Step | Component | Technology | Target File | Issue | Status |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **01** | Workspace Packaging & Type-Safe Config | `uv`, `pydantic-settings` | `src/vanguard/config.py` | [#1](#) | 🟡 **In Progress** |
| **02** | Strict Domain & Critic Schemas | `Pydantic v2` | `src/vanguard/schemas/domain.py` | — | ⏳ Queued |
| **03** | Resilient Multi-Provider AI Gateway | `LiteLLM`, `Tenacity` | `src/vanguard/llm/gateway.py` | — | ⏳ Queued |

### 🔎 Milestone 2: Hybrid Vector Memory & Typst PDF Server
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **04** | Async ORM Engine & `pgvector` Models | `SQLAlchemy 2.0`, `pgvector` | `src/vanguard/db/session.py` | ⏳ Queued |
| **05** | Hybrid Dense + Keyword Search Repository | `pgvector` HNSW, Reciprocal Rank Fusion | `src/vanguard/db/repository.py` | ⏳ Queued |
| **06** | Sub-10ms Typst PDF Compiler MCP Server | `FastMCP`, `Typst` | `src/vanguard/mcp/pdf_server.py` | ⏳ Queued |

### 🤖 Milestone 3: Adversarial LangGraph & Self-Healing Browser Engine
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **07** | Adversarial Tailor ⇄ Critic Subgraph | `LangGraph` Subgraph | `src/vanguard/agents/resume_subgraph.py` | ⏳ Queued |
| **08** | Self-Healing Stealth Browser MCP Server | `Playwright`, Vision SoM | `src/vanguard/mcp/browser_server.py` | ⏳ Queued |
| **09** | Master Graph with Checkpoints & HITL Gate | `LangGraph Checkpointer` | `src/vanguard/agents/master_graph.py` | ⏳ Queued |

### 🌐 Milestone 4: Distributed Scale, Streaming API & Production CI/CD
| Step | Component | Technology | Target File | Status |
| :---: | :--- | :--- | :--- | :---: |
| **10** | Redis Rate Limiter & Portal Selector Cache | `Redis 7` | `src/vanguard/cache/redis_client.py` | ⏳ Queued |
| **11** | FastAPI Async Server with SSE Stream & HITL | `FastAPI`, `SSE` | `src/vanguard/api/main.py` | ⏳ Queued |
| **12** | Langfuse Tracing & Pytest LLM-as-a-Judge Eval | `Langfuse`, `pytest` | `tests/evals/test_hallucination_gate.py` | ⏳ Queued |
| **13** | Production Multi-Stage Docker & CI/CD Gate | `Docker`, GitHub Actions | `.github/workflows/ci.yml` | ⏳ Queued |

---

## 🛠️ Tech Stack & Engineering Standards
- **Python 3.12+** with zero untyped code (`mypy --strict`).
- **TDD First:** Every single feature starts with a red `pytest` suite before production code is written.
- **Contract-First:** All API payloads and agent messages are enforced by immutable Pydantic v2 schemas.
- **Agile GitHub Flow:** Every change has an Issue, branch, conventional commit, and CI-gated Pull Request.

---

## 📄 License
MIT © [M. Hesam Moradian](https://github.com/m-hesam-moradian)
