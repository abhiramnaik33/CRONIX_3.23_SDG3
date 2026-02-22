# CRONIX SDG3 AI Emergency Agent

An intelligent conversational agent built using **LangGraph** and **LangChain**. This project focuses on **Sustainable Development Goal 3 (SDG 3): Good Health and Well-being** by providing an automated AI assistant capable of handling both general conversations and critical emergency situations.

## Features

- **Emergency Detection:** Analyzes user input to dynamically classify conversations as either "normal" or "emergency".
- **Context Extraction:** Automatically gathers crucial missing information during emergencies, such as:
  - Name
  - Location
  - Type of Emergency
- **Dynamic Routing:** Intelligently routes the conversation flow based on the provided context and the severity of the situation using LangGraph.
- **AI-Powered:** Utilizes the `gemini-3-flash-preview:cloud` model via Ollama to handle complex reasoning, extraction, and natural conversations.

## Architecture

The agent is designed using a graph-based state machine (`LangGraph`):
1. **State Management:** Maintains conversation history and context variables (`graph/state.py`).
2. **Nodes (`nodes.py`):** Individual execution steps that invoke LLMs to validate context, answer questions, or ask for missing dynamic emergency details.
3. **Routing (`routes.py`):** Conditional edges that determine the next node based on the current state (e.g., whether full context is provided). 
4. **Schemas (`scheama.py`):** Pydantic models ensuring structured JSON outputs from the LLM for reliable state updates.

## Setup & Environment

1. Ensure you have Python installed.
2. Install the required dependencies (LangChain, LangGraph, Pydantic, etc.).
3. The AI models require configuring LangChain Ollama. Ensure your local or cloud setup is correctly pointing to `gemini-3-flash-preview:cloud`.