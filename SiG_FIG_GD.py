import streamlit as st

st.title("🧮 Science Math Skills Quiz")
st.write("A 10‑question multiple‑choice quiz for science students. No answers are preselected.")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    # Addition (2)
    ("What is 12.2 + 7.21?",
     ["19.41", "19.4", "19"],
     "19.4"),

    ("A scientist mixes 23.00 mL and 18.00 mL of solution. What is the total volume?",
     ["41 mL", "41.0 mL", "41.00 mL"],
     "41.00 mL"),

    # Subtraction (2)
    ("A sample originally has a mass of 20.820 g but loses 12.0 g during heating. What is the final mass?",
     ["8.8 g", "8.82 g", "8.820 g"],
     "8.8, g"),

    ("A thermometer reads 28.7°C but the actual temperature is 6.1°C lower. What is the true temperature?",
     ["22°C", "22.6°C", "23°C"],
     "22.6°C"),

    # Multiplication (3)
    ("A box contains 6 test tubes. How many test tubes are in 7 boxes?",
     ["36", "42", "42.0"],
     "42"),

    ("A reaction produces 4.10 g of product per trial. How much is produced in 9 trials?",
     ["36 g", "37 g", "36.9 g"],
     "36.9 g"),

    ("Multiply 2.00  x 4.0  x  6 ?",
     ["50  ", "48  ", "48.0  "],
     "50  "),

    # Division (3)
    ("A 40 g sample is divided evenly into 5 portions. What is the mass of each portion?",
     ["8.0 g", "8 g", "10 g"],
     "8 g"),

    (" 6.00   x  3.0  /  2.00 ?",
     ["9", "9.00", "9.0"],
     "9.0"),

    ("  4.240  x  3.56  / 2.00",
     ["7.54", "7.55", "7.60"],
     "7.55")
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