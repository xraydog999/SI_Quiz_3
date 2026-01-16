# Quiz 3 SI system
import streamlit as st

st.title("🔬 SI System Multiple‑Choice Quiz")
st.write("Test your knowledge of the SI system. Good luck!")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    ("The base units for time, length and mass are respectively:",
     ["second, meter, kilogram", "minute, meter, gram", "hour, kilometer, gram"],
     "second, meter, kilogram"),

    ("In lab the temperature unit used is:",
     ["Kelvin", "degrees Celsius", "Fahrenheit"],
     "degrees Celsius"),

    ("For theoretical calculations, the temperature unit used is:",
     ["Kelvin", "degrees Celsius", "Rankine"],
     "Kelvin"),

    ("The SI unit employed to count particles is:",
     ["the mole", "the liter", "the joule"],
     "the mole"),

    ("Liquid nitrogen boils at –196 °C. What is this temperature in Kelvin?",
     ["77 K", "273 K", "196 K"],
     "77 K"),

    ("One cm is how many meters?",
     ["0.10 m", "0.010 m", "0.001 m"],
     "0.010 m"),

    ("One mm is how many meters?",
     ["0.00100 m", "0.0100 m", "0.00010 m"],
     "0.00100 m"),

    ("One cubic cm is how many mL?",
     ["0.10 mL", "10.0 mL", "1.00 mL"],
     "1.00 mL"),

    ("One liter is how many mL?",
     ["100 mL", "1000 mL", "10,000 mL"],
     "1000 mL"),

    ("50.0 mL is how many liters?",
     ["0.500 L", "0.0500 L", "0.00500 L"],
     "0.0500 L"),

    ("The Celsius scale is based on the freezing and boiling points of:",
     ["mercury", "water", "ethanol"],
     "water"),

    ("The Kelvin temperature scale is:",
     ["based on water", "not based on any substance", "based on oxygen"],
     "not based on any substance"),

    ("At room temperature, water has a density close to:",
     ["1.00 g/mL", "0.10 g/mL", "10.0 g/mL"],
     "1.00 g/mL"),

    ("On Mars, the mass of an object:",
     ["is the same", "is smaller", "is larger"],
     "is the same"),

    ("One kg is how many milligrams?",
     ["1,000 mg", "100,000 mg", "1,000,000 mg"],
     "1,000,000 mg"),

    ("The SI system is based on:",
     ["multiples of ten", "multiples of two", "multiples of sixty"],
     "multiples of ten"),

    ("In the SI system, mass is:",
     ["the amount of matter in an object measured in kg",
      "the weight of an object measured in N",
      "the volume of an object measured in L"],
     "the amount of matter in an object measured in kg"),

    ("The SI prefix with a value of 0.001 is:",
     ["micro", "milli", "centi"],
     "milli"),

    ("The SI unit for energy is the:",
     ["calorie", "Joule", "watt"],
     "Joule"),

    ("Room temperature is 25.0 °C. What is the corresponding Kelvin temperature?",
     ["273 K", "298 K", "250 K"],
     "298 K")
]

# -----------------------------
# QUIZ LOGIC
# -----------------------------
score = 0
responses = []

st.subheader("📘 Questions")

for i, (question, choices, answer) in enumerate(questions):
    st.write(f"**{i+1}. {question}**")
    user_choice = st.radio("", choices, key=i)
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
            st.error(f"Q{i+1}: Incorrect. ❌  Correct answer: **{correct}**")

    st.write("---")
    st.subheader(f"🏁 Final Score: **{score} / {len(questions)}**")

    if score == len(questions):
        st.balloons()
        st.success("Perfect score! Outstanding work!")
    elif score > 15:
        st.info("Great job — you really know your SI units!")
    elif score > 10:
        st.info("Good effort — keep practicing!")
    else:
        st.warning("Consider reviewing the SI system and trying again.")
