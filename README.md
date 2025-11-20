# MCP Practice Repository

A comprehensive learning project for understanding Model Context Protocol (MCP) implementation using FastMCP and JSON-RPC 2.0. This repository demonstrates server-client communication, error handling, and protocol compliance testing.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## 🎯 Overview

This project implements a simple MCP server with a division tool and includes comprehensive testing for:
- Valid JSON-RPC 2.0 requests
- Error handling and validation
- Protocol compliance
- HTTP and JSON response analysis

## 📁 Project Structure
```
MCP_PRACTICE/
├── main.py              # FastMCP server for Divide tool
├── client.py            # HTTP client with 23 test requests
├── Resources.py         # Resources server (files, web content)
├── prompts.py           # Prompts server (Github Profile, format, divide)
├── sampling.py          # Sampling server (LLM interaction)
├── logs_progress.py     # Logs and progress server
├── roots.py             # Roots server (project analysis)
├── transport1.py        # Alternative transport implementation
├── statefulHTTP.py      # Stateful HTTP example
├── Tools.py             # Additional tools (Quiz, Summarize)
├── formula.py           # Sample resource file with formulas
├── Instructions.md      # Comprehensive testing guide
├── questions.md         # Learning questions about MCP
└── reponses.md          # Expected responses for all 23 requests
```

## ✨ Features

- **Multiple MCP Servers**: 6 different server implementations (Tools, Resources, Prompts, Sampling, Logs, Roots)
- **Comprehensive Testing**: 23 test cases across 6 testing phases
- **Tool Implementations**: Division, Quiz generation, Web summarization
- **Resource Handling**: File reading, web content fetching, templated resources
- **Prompt Management**: Github profile lookup, document formatting, number division prompts
- **MCP Protocol Features**: Sampling requests, logging, progress tracking, roots analysis
- **Error Validation**: Tests for malformed requests and edge cases
- **Dual Testing Methods**: Support for both Python client and Postman

## 🔧 Prerequisites

- Python 3.8+
- `uv` package manager
- Postman (optional, for manual testing)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Tayyaba-Akbar956/MCP-Practice.git
cd "MCP PRACTICE"
```

2. Install dependencies:
```bash
uv pip install fastmcp requests uvicorn
```

## 🚀 Usage

This project requires running different servers depending on what features you want to test.

### Mode 1: Tools Testing (Requests 1-11)
For testing tools (Division, Greetings) and error handling:
```bash
uv run uvicorn main:app --reload
```
The server will start at `http://localhost:8000/mcp/`

### Mode 2: Resources Testing (Requests 12-15)
For testing resources (File reading, Web fetching):
```bash
uv run uvicorn Resources:app --reload
```
The server will start at `http://localhost:8000/mcp/`

### Mode 3: Prompts Testing (Requests 16-19)
For testing prompts:
```bash
uv run uvicorn prompts:app --reload
```

### Mode 4: Sampling Testing (Requests 20-21)
For testing sampling (LLM interaction):
```bash
uv run uvicorn sampling:app --reload
```

### Mode 5: Logs Testing (Request 22)
For testing logs and progress:
```bash
uv run uvicorn logs_progress:app --reload
```

### Mode 6: Roots Testing (Request 23)
For testing roots:
```bash
uv run uvicorn roots:app --reload
```

### Mode 7: Transport Testing (Requests 1-11)
For testing transport1.py (same tools as main.py):
```bash
uv run uvicorn transport1:app --reload
```

### Running the Client

Execute the test client:
```bash
uv run client.py
```

## 🧪 Testing
For detailed testing instructions, please refer to [Instructions.md](Instructions.md).



## 📝 Notes

- Always run the server before executing client tests
- Test one scenario at a time for clear output analysis
- Review `responses.md` for expected responses for each request
- Check `instructions.md` for detailed testing steps

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Learning! 🚀**
