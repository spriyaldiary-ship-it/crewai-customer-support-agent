# 🤖 CrewAI Customer Support Agent

A multi-agent AI customer support application built with **CrewAI** and **Streamlit**.

The project demonstrates how multiple specialized AI agents can work sequentially to answer customer questions, perform web research, and record the final interaction.

## 🚀 Features

* 🤖 **Assistant Agent** — Generates an initial answer to the user's question.
* 🌐 **Web Search Assistant** — Performs web research and provides an updated answer.
* 📝 **Entry Agent** — Records the customer support interaction.
* 💾 Saves interaction results to `answers.txt`.
* 🖥️ Streamlit-based user interface.
* 🔐 API keys managed through environment variables.
* 🧩 Demonstrates sequential multi-agent orchestration using CrewAI.

## 🏗️ Architecture

```text
User
  │
  ▼
Streamlit UI
  │
  ▼
Assistant Agent
  │
  ▼
Web Search Assistant
  │
  ▼
Entry Agent
  │
  ▼
answers.txt
```

Each agent has a specific responsibility, demonstrating how a multi-agent workflow can divide a customer-support task into smaller steps.

## 🔄 Workflow

```text
User Question
      │
      ▼
Assistant Agent
      │
      ▼
Initial Answer
      │
      ▼
Web Search Assistant
      │
      ▼
Web-Researched Answer
      │
      ▼
Entry Agent
      │
      ▼
Save Interaction
      │
      ▼
answers.txt
```

## 🛠️ Technology Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Application development   |
| CrewAI        | Multi-agent orchestration |
| Streamlit     | Web interface             |
| OpenAI        | LLM-powered responses     |
| Serper        | Web search                |
| python-dotenv | Environment configuration |

## 📂 Project Structure

```text
buildathon-support-crew/
│
├── app.py
├── README.md
├── answers.txt
├── .gitignore
├── .env              # Local only - not committed
└── venv/             # Local virtual environment
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/spriyaldiary-ship-it/crewai-customer-support-agent.git
```

### 2. Open the project

```bash
cd crewai-customer-support-agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit crewai crewai-tools python-dotenv
```

### 6. Configure environment variables

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

**Never commit API keys or `.env` files to GitHub.**

### 7. Run the application

```bash
python -m streamlit run app.py
```

The Streamlit application will open in your browser.

## 💡 How It Works

1. The user enters a question through the Streamlit interface.
2. The **Assistant Agent** generates an initial response.
3. The **Web Search Assistant** researches the question using web search.
4. The **Entry Agent** records the interaction.
5. The results are saved to `answers.txt`.
6. The application displays the generated responses.
7. The user can download the recorded results.

## 🎯 Project Goal

The goal of this project is to gain practical experience building **multi-agent AI applications with CrewAI**.

It demonstrates:

* Agent specialization
* Sequential agent workflows
* Web-enabled AI research
* Customer-support automation
* LLM integration
* Streamlit application development

## 📚 Learning Outcomes

This project provided hands-on experience with:

* CrewAI
* AI agents
* Multi-agent orchestration
* Sequential workflows
* Web search tools
* OpenAI LLM integration
* Streamlit
* Environment variables
* Python application development

## 🔮 Future Improvements

Possible future enhancements include:

* Conversation memory
* Better customer-support knowledge bases
* RAG integration
* Agent task validation
* Structured response storage
* Customer history tracking
* Authentication
* Production database integration
* API-based deployment

## 📄 Buildathon Project

This project was created as part of a **Generative AI Architecture / CrewAI Multi-Agent Customer Support Buildathon**.

## 👩‍💻 Author

**Priyal**

Hands-on learning in:

**Generative AI • AI Agents • CrewAI • RAG • AI Automation**
