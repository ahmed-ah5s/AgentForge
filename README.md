# AgentForge

**An Autonomous AI Agent Generation and Management Platform for Businesses**

AgentForge is a platform designed to help businesses transform their requirements into specialized AI agents.

Businesses describe their needs in natural language. AgentForge analyzes these requirements, plans suitable agents, generates structured agent blueprints, validates them, and prepares them for execution through a controlled runtime.

## The Problem

Businesses increasingly want to use AI agents, but building reliable agents requires technical knowledge, planning, configuration, and testing.

AgentForge aims to simplify this process by providing a structured platform for generating and managing AI agents.

## Proposed Solution

AgentForge follows a controlled workflow:

1. **Requirement Analysis** – Understand the business requirements.
2. **Agent Planning** – Identify the agents, tools, and workflows needed.
3. **Blueprint Generation** – Generate structured AI agent configurations.
4. **Blueprint Validation** – Check configurations before execution.
5. **Human Approval** – Allow users to review and approve generated agents.
6. **Execution and Monitoring** – Run approved agents and monitor their performance.

## Core Engineering Principle

**AI generates blueprints, not arbitrary executable code.**

AgentForge uses structured and validated agent configurations. A fixed, tested runtime executes these blueprints to improve reliability, security, and control.

## Technology Stack

| Component       | Technology                 |
| --------------- | -------------------------- |
| Backend         | Python, FastAPI            |
| Frontend        | Next.js, React, TypeScript |
| Styling         | Tailwind CSS               |
| Data Validation | Pydantic                   |
| Testing         | Pytest                     |
| Code Quality    | Ruff                       |
| Version Control | Git and GitHub             |

Additional technologies will be introduced as the project develops.

## Project Architecture

```text
AgentForge/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── pyproject.toml
│
├── frontend/
│   └── src/
│       └── app/
│
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or later
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/ahmed-ah5s/AgentForge.git
cd AgentForge
```

### 2. Run the Backend

Open a terminal:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Backend API:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

Health check:

`http://127.0.0.1:8000/health`

### 3. Run the Frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

`http://localhost:3000`

## Testing

Run backend tests:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m pytest
```

Run code quality checks:

```powershell
python -m ruff check .
```

## Current Development Status

The project is under active development.

Currently implemented:

- FastAPI backend foundation.
- Initial Next.js frontend.
- Application configuration management.
- Health check API endpoint.
- CORS middleware.
- Initial backend tests.

Planned development:

- Database integration and authentication.
- Business requirement analysis.
- AI agent planning and blueprint generation.
- Blueprint schema and validation.
- Controlled agent runtime.
- Human approval workflow.
- Knowledge base and RAG integration.
- Agent evaluation and monitoring dashboard.

## Project Goal

The long-term goal is to provide businesses with a reliable and controlled platform for creating, deploying, and managing specialized AI agents without requiring them to build every agent manually.

---

**Project:** AgentForge  
**Status:** In Development  
**Repository:** https://github.com/ahmed-ah5s/AgentForge
