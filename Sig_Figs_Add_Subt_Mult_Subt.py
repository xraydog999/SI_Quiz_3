import streamlit as st

st.title("🧮 Science Math Skills Quiz")
st.write("A 10‑question multiple‑choice quiz for science students. No answers are preselected.")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    # Addition (2)
    ("What is 12 + 7?",
     ["17", "19", "21"],
     "19"),

    ("A scientist mixes 23 mL and 18 mL of solution. What is the total volume?",
     ["41 mL", "38 mL", "35 mL"],
     "41 mL"),

    # Subtraction (2)
    ("A sample originally has a mass of 50 g but loses 12 g during heating. What is the final mass?",
     ["32 g", "38 g", "42 g"],
     "38 g"),

    ("A thermometer reads 28°C but the actual temperature is 6°C lower. What is the true temperature?",
     ["22°C", "20°C", "24°C"],
     "22°C"),

    # Multiplication (3)
    ("A box contains 6 test tubes. How many test tubes are in 7 boxes?",
     ["36", "42", "48"],
     "42"),

    ("A reaction produces 4 g of product per trial. How much is produced in 9 trials?",
     ["36 g", "45 g", "32 g"],
     "36 g"),

    ("A microscope magnifies an object 3×. If the object is 5 mm long, what is the magnified length?",
     ["10 mm", "15 mm", "20 mm"],
     "15 mm"),

    # Division (3)
    ("A 40 g sample is divided evenly into 5 portions. What is the mass of each portion?",
     ["5 g", "8 g", "10 g"],
     "8 g"),

    ("A scientist has 120 mL of solution and fills containers with 10 mL each. How many containers can be filled?",
     ["10", "12", "15"],
     "12"),

    ("A 72‑page lab manual is divided into 8 equal sections. How many pages per section?",
     ["8", "9", "12"],
     "9")
]

# -----------------------------
# QUIZ LOGIC
# -----------------------------
score = 0
responses = []

st.subheader("📘 Questions")

for i, (question, choices, answer) in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    user_choice = st.radio("", choices, key=i, index=None)  # ← No preselected answer
    responses.append((user_choice, answer))
    st.write("---")

# -----------------------------
# RESULTS
# -----------------------------
if st.button("Submit Quiz"):
    st.subheader("📊 Results & Feedback")

    for i, (user, correct) in enumerate(responses):
        if user == correct:
            st.success(f"Q{i+1}: Correct! ✔️")
            score += 1
        else:
            st.error(f"Q{i+1}: Incorrect. ❌ Correct answer: **{correct}**")

    st.write("---")
    st.subheader(f"🏁 Final Score: **{score} / {len(questions)}**")

    if score == len(questions):
        st.balloons()
        st.success("Perfect score! Excellent science math skills.")
    elif score >= 7:
        st.info("Great job — you're strong in science math.")
    elif score >= 5:
        st.info("Good effort — keep practicing.")
    else:
        st.warning("Review your math skills and try again.")
