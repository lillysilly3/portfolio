# MellowAI

A CLI AI coding agent powered by Google Gemini. Give it a natural language prompt and it will autonomously read, write, and run code in a sandboxed working directory to complete the task.

## Features

- Natural language prompts from the command line
- Autonomous multi-step reasoning with up to 20 iterations
- Function calling tools: list files, read files, write files, run Python files
- Sandboxed working directory to prevent access outside the project
- Verbose mode to inspect every function call and token usage

```
$ uv run python main.py "add a function that multiplies two numbers" --verbose
User prompt: add a function that multiplies two numbers
Prompt tokens: 412
Response tokens: 87
-> {'output': 'main.py\ncalculator/\n  operations.py\n  __init__.py\n'}
-> {'output': 'def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n'}
-> {'output': 'File written successfully'}
Done! I added a multiply(a, b) function to calculator/operations.py.
```

## Tech Stack

- Python 3.13+
- Google Gemini API (`google-genai` SDK)
- `uv` for dependency management

## Project Structure

- `main.py` — Entry point and agent loop
- `call_function.py` — Function call dispatcher
- `prompts.py` — System prompt
- `config.py` — Configuration constants
- `functions/` — Tool implementations (read, write, list, run)
- `tests/` — Test suite
- `calculator/` — Sample project for the agent to work on


[Full project on GitHub](https://github.com/lillysilly3/mellow-ai)

[← Back to Portfolio](/)
