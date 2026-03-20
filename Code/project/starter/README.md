# Udaplay: AI Research Agent for Video Games

An intelligent agent that answers questions about the video game industry using internal knowledge (RAG) and web search fallback.

## Overview

Udaplay is built as part of the Udacity AI Agent course. It demonstrates:
- Retrieval-Augmented Generation (RAG) using ChromaDB vector database
- LLM-powered evaluation of retrieved documents
- Web search integration with Tavily API
- State machine-based agent workflow
- Structured output reporting

## Features

- **Semantic Search**: Queries ChromaDB for relevant game information
- **Intelligent Evaluation**: Uses Ollama/Mistral to assess if retrieved data answers the question
- **Web Fallback**: Automatically searches the web when internal knowledge is insufficient
- **Structured Reports**: Provides detailed query reports with sources and evaluation results
- **Conversation History**: Maintains history of interactions

## Architecture

### Tools
- `retrieve_game()`: Semantic search in ChromaDB collection
- `evaluate_retrieval_tool()`: LLM-based evaluation of document usefulness
- `web_search_tool()`: Web search using Tavily API

### Agent States
1. **RETRIEVE**: Get relevant games from vector DB
2. **EVALUATE**: Check if results are useful for the question
3. **WEB**: Fallback to web search if evaluation fails
4. **ANSWER**: Generate final response from available data

## Setup

### Prerequisites
- Python 3.8+
- Ollama (for Mistral model)
- ChromaDB vector database
- API keys for OpenAI and Tavily

### Installation

1. **Clone/Setup Project**:
   ```bash
   cd udacity_right_env/Code/project/starter
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt  # If exists, or manually install:
   pip install chromadb ollama tavily-python python-dotenv
   ```

3. **Environment Variables**:
   Create `.env` file:
   ```
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

4. **Setup ChromaDB**:
   - Ensure `chromadb/` directory exists with populated collection
   - Collection name: `udaplay`

5. **Start Ollama**:
   ```bash
   ollama serve
   ollama pull mistral
   ```

## Usage

### Basic Query
```python
from udaplay_agent import UdaPlayAgent

agent = UdaPlayAgent()
result = agent.query("When was Pokémon Gold released?")
agent.print_report(result)
```

### Example Queries
- "When was GTA launched?"
- "When was Pokémon Gold and Silver released?"
- "When was Tekken 7 released?"
- "Was Mortal Kombat X released for PlayStation 5?"
- "Which one was the first 3D platformer Mario game?"

## Project Structure

```
udacity_right_env/Code/project/starter/
├── Udaplay_02_starter_project.ipynb  # Main implementation
├── chromadb/                         # Vector database
├── .env                              # Environment variables
└── README.md                         # This file
```

## Key Components

### Vector Database Setup
- Uses ChromaDB for persistent storage
- Game metadata includes: Name, Platform, YearOfRelease, Description
- Semantic search with embeddings

### Evaluation Logic
- Prompts Mistral to evaluate document relevance
- Returns JSON with `useful` boolean and `reason` string
- Handles parsing errors gracefully

### Web Search Integration
- Tavily API for reliable search results
- Extracts titles, content snippets, and URLs
- Limits to 3 results for efficiency

## Troubleshooting

### Common Issues
- **Ollama not responding**: Ensure `ollama serve` is running and `mistral` model is pulled
- **ChromaDB errors**: Check `chromadb/` directory exists and collection is populated
- **API key errors**: Verify `.env` file has correct keys
- **TypeError in generate_answer**: Ensure data types match (dict for internal, list for web)

### Debug Tips
- Test individual tools first:
  ```python
  games = retrieve_game("Pokémon")
  print(games)
  ```
- Check evaluation:
  ```python
  eval_result = evaluate_retrieval_tool("question", games[0])
  print(eval_result)
  ```

## Future Enhancements

- Add long-term memory persistence
- Implement more sophisticated evaluation prompts
- Add support for multiple vector collections
- Integrate with additional APIs (Steam, IGDB, etc.)
- Add conversation context awareness

## License

This project is part of Udacity coursework. See LICENSE.md for details.
- OpenAI
- Tavily
- dotenv

### Directory Structure
```
project/
├── starter/
│   ├── games/           # JSON files with game data
│   ├── lib/             # Custom library implementations
│   │   ├── llm.py       # LLM abstractions
│   │   ├── messages.py  # Message handling
│   │   ├── ...
│   │   └── tooling.py   # Tool implementations
│   ├── Udaplay_01_starter_project.ipynb  # Part 1 implementation
│   └── Udaplay_02_starter_project.ipynb  # Part 2 implementation
```

## Getting Started

1. Create and activate a virtual environment
2. Install required dependencies
3. Set up your `.env` file with necessary API keys
4. Follow the notebooks in order:
   - Complete Part 1 to set up your vector database
   - Complete Part 2 to implement the AI agent

## Testing Your Implementation

After completing both parts, test your agent with questions like:
- "When was Pokémon Gold and Silver released?"
- "Which one was the first 3D platformer Mario game?"
- "Was Mortal Kombat X released for PlayStation 5?"

## Advanced Features

After completing the basic implementation, you can enhance your agent with:
- Long-term memory capabilities
- Additional tools and capabilities

## Notes
- Make sure to implement proper error handling
- Follow best practices for API key management
- Document your code thoroughly
- Test your implementation with various types of queries
