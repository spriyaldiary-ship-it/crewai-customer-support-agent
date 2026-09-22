# 🤖 Multi-Agent Customer Support

A multi-agent customer support application built using **CrewAI** and **Streamlit**.

The application uses three sequential AI agents to answer a user query, search the web, and record the results.

## 🚀 Features

* 🤖 **Assistant Agent** — Answers the user's question using its own knowledge.
* 🌐 **Web Search Assistant** — Searches the web and provides a researched answer.
* 📝 **Entry Agent** — Records the customer support interaction.
* 💾 Automatically creates and writes to `answers.txt`.
* 🖥️ Simple Streamlit user interface.
* 🔐 API keys are stored securely using environment variables.

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

## 🛠️ Tech Stack

* Python
* CrewAI
* Streamlit
* OpenAI
* Serper Web Search
* python-dotenv

## 📁 Project Structure

```text
buildathon-support-crew/
│
├── app.py
├── README.md
├── .gitignore
├── .env              # Local only - not committed
├── answers.txt       # Generated locally
└── venv/             # Local virtual environment
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/spriyaldiary-ship-it/buildathon-support-crew.git
```

### 2. Open the project

```bash
cd buildathon-support-crew
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit crewai crewai-tools python-dotenv
```

### 6. Create `.env`

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

### 7. Run the application

```bash
python -m streamlit run app.py
```

## 💡 How It Works

1. The user enters a question in the Streamlit interface.
2. The **Assistant Agent** generates an answer using its own knowledge.
3. The **Web Search Assistant** searches the web and generates a researched answer.
4. The **Entry Agent** completes the recording step.
5. The application saves the query and both answers into `answers.txt`.
6. Both answers are displayed in the Streamlit interface.
7. The user can download `answers.txt`.

## 📄 Buildathon

This project was created as part of a **Gen AI Architecture / CrewAI Multi-Agent Customer Support Buildathon**.

## 🔗 Repository

GitHub:

https://github.com/spriyaldiary-ship-it/buildathon-support-crew

````

### Step 3 — Save

Press:

```text
Ctrl + S
````

### Step 4 — Push README to GitHub

In PowerShell:

```powershell
git add README.md
```

Then:

```powershell
git commit -m "Add project README"
```

Then:

```powershell
git push
```

After that, refresh your GitHub repository. You should see **README.md displayed automatically on the repository homepage**.
