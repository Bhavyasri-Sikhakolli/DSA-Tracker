import streamlit as st
import json
import os


# ---------- DATA FUNCTIONS ----------

def load_problems():
    if os.path.exists("problems.json"):
        with open("problems.json", "r") as file:
            return json.load(file)
    return []


def save_problems(problems):
    with open("problems.json", "w") as file:
        json.dump(problems, file, indent=4)


# ---------- PAGE CONFIGURATION ----------

st.set_page_config(
    page_title="DSA Practice Tracker",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 DSA Practice Tracker")
st.write("Track your DSA problem-solving journey in one place.")


# Load existing problems
problems = load_problems()


# ---------- DASHBOARD STATISTICS ----------

total_problems = len(problems)
solved_problems = sum(1 for problem in problems if problem["status"] == "Solved")
pending_problems = total_problems - solved_problems

if total_problems > 0:
    progress = solved_problems / total_problems
else:
    progress = 0


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Total Problems", total_problems)

with col2:
    st.metric("✅ Solved", solved_problems)

with col3:
    st.metric("⏳ Pending", pending_problems)


st.progress(progress)
st.write(f"Overall Progress: {solved_problems}/{total_problems} solved")


# ---------- ADD PROBLEM ----------

st.header("➕ Add New Problem")

with st.form("add_problem_form"):

    name = st.text_input("Problem Name")

    col1, col2, col3 = st.columns(3)

    with col1:
        platform = st.selectbox(
            "Platform",
            ["GeeksforGeeks", "LeetCode", "HackerRank", "Other"]
        )

    with col2:
        topic = st.text_input("Topic", placeholder="Arrays, Strings, Stack...")

    with col3:
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

    submitted = st.form_submit_button("Add Problem")

    if submitted:

        if name.strip() == "":
            st.error("Please enter a problem name.")

        elif topic.strip() == "":
            st.error("Please enter a topic.")

        else:
            new_problem = {
                "name": name,
                "platform": platform,
                "topic": topic,
                "difficulty": difficulty,
                "status": "Pending"
            }

            problems.append(new_problem)
            save_problems(problems)

            st.success(f"'{name}' added successfully! 🎉")
            st.rerun()


# ---------- VIEW PROBLEMS ----------

st.header("📋 Your Problems")

if len(problems) == 0:

    st.info("No problems added yet. Add your first DSA problem above!")

else:

    for i, problem in enumerate(problems):

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

            with col1:
                st.subheader(problem["name"])
                st.write(f"**Topic:** {problem['topic']}")

            with col2:
                st.write(f"**Platform:** {problem['platform']}")

            with col3:
                st.write(f"**Difficulty:** {problem['difficulty']}")

            with col4:

                if problem["status"] == "Solved":
                    st.success("Solved ✅")

                else:
                    if st.button("Mark Solved", key=f"solve_{i}"):

                        problems[i]["status"] = "Solved"
                        save_problems(problems)

                        st.rerun()


# ---------- SEARCH BY TOPIC ----------

st.header("🔎 Search by Topic")

search_topic = st.text_input(
    "Enter a topic to search",
    placeholder="Example: Arrays"
)

if search_topic:

    results = [
        problem for problem in problems
        if search_topic.lower() in problem["topic"].lower()
    ]

    if results:

        st.write(f"Found {len(results)} problem(s):")

        for problem in results:
            st.write(
                f"**{problem['name']}** — "
                f"{problem['difficulty']} — "
                f"{problem['status']}"
            )

    else:
        st.warning("No problems found for this topic.")


# ---------- STATISTICS ----------

st.header("📊 Statistics")

if problems:

    easy = sum(1 for p in problems if p["difficulty"] == "Easy")
    medium = sum(1 for p in problems if p["difficulty"] == "Medium")
    hard = sum(1 for p in problems if p["difficulty"] == "Hard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🟢 Easy", easy)

    with col2:
        st.metric("🟡 Medium", medium)

    with col3:
        st.metric("🔴 Hard", hard)

    topics = {}

    for problem in problems:
        topic = problem["topic"]

        if topic in topics:
            topics[topic] += 1
        else:
            topics[topic] = 1

    st.subheader("Problems by Topic")

    st.bar_chart(topics)

else:

    st.info("Add some problems to see your statistics.")