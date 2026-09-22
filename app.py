import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool


# ==============================
# ENVIRONMENT
# ==============================

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY is missing in .env")
    st.stop()

if not os.getenv("SERPER_API_KEY"):
    st.error("SERPER_API_KEY is missing in .env")
    st.stop()


# ==============================
# PAGE
# ==============================

st.set_page_config(
    page_title="Multi-Agent Customer Support",
    page_icon="🤖"
)

st.title("🤖 Multi-Agent Customer Support")
st.write("CrewAI + Streamlit")


# ==============================
# INPUT
# ==============================

query = st.text_area(
    "Enter your question:",
    placeholder="Example: How do I reset my password?"
)


# ==============================
# BUTTON
# ==============================

if st.button("Get Answers", type="primary"):

    if not query.strip():
        st.warning("Please enter a question.")
        st.stop()

    # ==============================
    # SEARCH TOOL
    # ==============================

    search_tool = SerperDevTool()

    # ==============================
    # AGENT 1
    # ==============================

    assistant = Agent(
        role="Assistant",
        goal="Answer the user's question using your own knowledge.",
        backstory=(
            "You are a helpful customer support assistant. "
            "Give a clear and useful answer."
        ),
        allow_delegation=False,
        verbose=True
    )

    # ==============================
    # AGENT 2
    # ==============================

    web_search_assistant = Agent(
        role="Web Search Assistant",
        goal="Search the web and answer the user's question.",
        backstory=(
            "You are a web research customer support assistant. "
            "Search the internet and provide a useful answer."
        ),
        tools=[search_tool],
        allow_delegation=False,
        verbose=True
    )

    # ==============================
    # AGENT 3
    # ==============================

    entry_agent = Agent(
        role="Entry Agent",
        goal="Record the customer support interaction.",
        backstory=(
            "You are responsible for recording customer "
            "support information accurately."
        ),
        allow_delegation=False,
        verbose=True
    )

    # ==============================
    # TASK 1
    # ==============================

    task1 = Task(
        description=f"""
Answer this question using your own knowledge:

{query}

Give a clear and helpful answer.
""",
        expected_output="A clear customer support answer.",
        agent=assistant
    )

    # ==============================
    # TASK 2
    # ==============================

    task2 = Task(
        description=f"""
Search the web for this question:

{query}

Use the search tool and provide a clear answer
based on the information you find.
""",
        expected_output="A clear web-researched answer.",
        agent=web_search_assistant
    )

    # ==============================
    # TASK 3
    # ==============================

    task3 = Task(
        description="""
Review the previous agents' answers and confirm
that the customer support interaction has been recorded.
""",
        expected_output="A confirmation message.",
        agent=entry_agent,
        context=[task1, task2]
    )

    # ==============================
    # CREW
    # ==============================

    crew = Crew(
        agents=[
            assistant,
            web_search_assistant,
            entry_agent
        ],
        tasks=[
            task1,
            task2,
            task3
        ],
        process=Process.sequential,
        verbose=True
    )

    # ==============================
    # RUN
    # ==============================

    with st.spinner("Running the 3 agents..."):

        result = crew.kickoff()

    # ==============================
    # GET ANSWERS
    # ==============================

    answer1 = str(task1.output.raw)
    answer2 = str(task2.output.raw)
    entry_result = str(task3.output.raw)

    # ==============================
    # SAVE FILE
    # ==============================

    answers_file = Path(__file__).resolve().parent / "answers.txt"

    content = f"""
MULTI-AGENT CUSTOMER SUPPORT
============================================================

USER QUERY
============================================================
{query}

ANSWER 1 - ASSISTANT
============================================================
{answer1}

ANSWER 2 - WEB SEARCH ASSISTANT
============================================================
{answer2}

ENTRY AGENT
============================================================
{entry_result}

============================================================
END OF SUPPORT RECORD
============================================================
"""

    # Write the file
    answers_file.write_text(
        content,
        encoding="utf-8"
    )

    # ==============================
    # VERIFY FILE
    # ==============================

    if answers_file.exists() and answers_file.stat().st_size > 0:

        st.success("✅ answers.txt created and written successfully!")

        st.info(
            f"File location:\n{answers_file}"
        )

    else:

        st.error("❌ answers.txt was not written correctly.")

    # ==============================
    # DISPLAY ANSWERS
    # ==============================

    st.subheader("1️⃣ Assistant Answer")
    st.write(answer1)

    st.subheader("2️⃣ Web Search Assistant Answer")
    st.write(answer2)

    st.subheader("3️⃣ Entry Agent")
    st.write(entry_result)

    # ==============================
    # DOWNLOAD
    # ==============================

    st.download_button(
        label="⬇️ Download answers.txt",
        data=content,
        file_name="answers.txt",
        mime="text/plain"
    )