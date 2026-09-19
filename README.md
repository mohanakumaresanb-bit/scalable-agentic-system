# scalable-agentic-system

A Python-based agentic system developed as part of the Datazoic technical task.

## Features

* Intent-based request routing
* Tool registry and execution
* Input validation
* RAG-based retrieval
* System search tool
* PayPal mock API
* Unit tests

## Project Structure

```text
agentic-system/
├── app/
├── tools/
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` and add the required API keys.

## Run

```bash
python -m app.main
```

## Test

```bash
pytest
```

## Notes

* The PayPal integration uses a mock API.
* Do not commit real API keys or `.env` files to GitHub.

