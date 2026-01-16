import streamlit as st
import random

# ---------------------------------------------------------
#  CLASSROOM‑READY MODULE STRUCTURE
# ---------------------------------------------------------

def load_questions():
    """Return a list of quiz questions, choices, answers, and explanations."""
    return [
        {
            "q": "The base units for time, length and mass are respectively:",
            "choices": ["second, meter, kilogram", "minute, meter, gram", "hour, kilometer, gram"],
            "answer": "second, meter, kilogram",
            "explanation": "The SI base units are second (time), meter (length), and kilogram (mass)."
        },
        {
            "q": "In lab the temperature unit used is:",
            "choices": ["Kelvin", "degrees Celsius", "Fahrenheit"],
            "answer": "degrees Celsius",
            "explanation": "Lab thermometers typically use Celsius because it is practical for everyday temperature ranges."
        },
        {
            "q": "For theoretical calculations, the temperature unit used is:",
            "choices": ["Kelvin", "degrees Celsius", "Rankine"],
            "answer": "Kelvin",
            "explanation": "Kelvin is the SI base unit for temperature and is required for most physics and chemistry equations."
        },
        {
            "q": "The SI unit employed to count particles is:",
            "choices": ["the mole", "the liter", "the joule"],
            "answer": "the mole",
            "explanation": "A mole represents \(6.022×10^{23}\) particles and is the SI unit for amount of substance."
        },
        {
            "q": "Liquid nitrogen boils at –196 °C. What is this temperature in Kelvin?",
            "choices": ["77 K", "273 K", "196 K"],
            "answer": "77 K",
            "explanation": "Convert using K = °C + 273 → –196 + 273 = 77 K."
        },
        {
            "q": "One cm is how many meters?",
            "choices": ["0.10 m", "0.010 m", "0.001 m"],
            "answer": "0.010 m",
            "explanation": "1 cm = 1/100 m = 0.01 m."
        },
        {
            "q": "One mm is how many meters?",
            "choices": ["0.00100 m", "0.0100 m", "0.00010 m"],
            "answer": "0.00100 m",
            "explanation": "1 mm = 1/1000 m = 0.001 m."
        },
        {
            "q": "One cubic cm is how many mL?",
            "choices": ["0.10 mL", "10.0 mL", "1.00 mL"],
            "answer": "1.00 mL",
            "explanation": "By definition, 1 cm³ = 1 mL."
        },
        {
            "q": "One liter is how many mL?",
            "choices": ["100 mL", "1000 mL", "10,000 mL"],
            "answer": "1000 mL",
            "explanation": "1 L = 1000 mL by SI volume definition."
        },
        {
            "q": "50.0 mL is how many liters?",
            "choices": ["0.500 L", "0.0500 L", "0.00500 L"],
            "answer": "0.0500 L",
            "explanation": "Divide by 1000: 50.0 mL = 0.0500 L."
        },
        {
            "q": "The Celsius scale is based on the freezing and boiling points of:",
            "choices": ["mercury", "water", "ethanol"],
            "answer": "water",
            "explanation": "0 °C and 100 °C correspond to water’s freezing and boiling points at 1 atm."
        },
        {
            "q": "The Kelvin temperature scale is:",
            "choices": ["based on water", "not based on any substance", "based on oxygen"],
            "answer": "not based on any substance",
            "explanation": "Kelvin is based on absolute zero, not on properties of any material."
        },
        {
            "q": "At room temperature, water has a density close to:",
            "choices": ["1.00 g/mL", "0.10 g/mL", "10.0 g/mL"],
            "answer": "1.00 g/mL",
            "explanation": "Water’s density at ~25 °C is approximately 1.00 g/mL."
        },
        {
            "q": "On Mars, the mass of an object:",
            "choices": ["is the same", "is smaller", "is larger"],
            "answer": "is the same",
            "explanation": "Mass does not depend on gravity; weight does."
        },
        {
            "q": "One kg is how many milligrams?",
            "choices": ["1,000 mg", "100,000 mg", "1,000,000 mg"],
            "answer": "1,000,000 mg",
            "explanation": "1 kg = 1000 g and 1 g = 1000 mg → 1,000,000 mg."
        },
        {
            "q": "The SI system is based on:",
            "choices": ["multiples of ten", "multiples of two", "multiples of sixty"],
            "answer": "multiples of ten",
            "explanation": "SI prefixes scale by powers of ten, making conversions simple."
        },
        {
            "q": "In the SI system, mass is:",
            "choices": [
                "the amount of matter in an object measured in kg",
                "the weight of an object measured in N",
                "the volume of an object measured in L"
            ],
            "answer": "the amount of matter in an object measured in kg",
            "explanation": "Mass measures matter; weight measures gravitational force."
        },
        {
            "q": "The SI prefix with a value of 0.001 is:",
            "choices": ["micro", "milli", "centi"],
            "answer": "milli",
            "explanation": "Milli‑ means one‑thousandth (10⁻³)."
        },
        {
            "q": "The SI unit for energy is the:",
            "choices": ["calorie", "Joule", "watt"],
            "answer": "Joule",
            "explanation": "The joule (J) is the SI unit of energy and work."
        },
        {
            "q": "Room temperature is 25.0 °C. What is the corresponding Kelvin temperature?",
            "choices": ["273 K", "298 K", "250 K"],
            "answer": "298 K",
            "explanation": "K = °C + 273 → 25 + 273 = 298 K."
        }
    ]


def run_quiz():
    st.title("🔬 SI System Quiz — Classroom Edition")
    st.write("Questions appear in random order each time.")

    questions = load_questions()
    random.shuffle(questions)

    user_answers = []
    score = 0

    st.subheader("📘 Questions")

    for i, q in enumerate(questions):
        st.write(f"**{i+1}. {q['q']}**")
        choice = st.radio("", q["choices"], key=i)
        user_answers.append((choice, q))
        st.write("---")

    if st.button("Submit Quiz"):
        st.subheader("📊 Results & Explanations")

        for i, (user_choice, q) in enumerate(user_answers):
            if user_choice == q["answer"]:
                st.success(f"Q{i+1}: Correct! ✔️")
                score += 1
            else:
                st.error(f"Q{i+1}: Incorrect. ❌ Correct answer: **{q['answer']}**")

            st.info(f"Explanation: {q['explanation']}")
            st.write("---")

        st.subheader(f"🏁 Final Score: **{score} / {len(questions)}**")

        if score == len(questions):
            st.balloons()
            st.success("Perfect score! Outstanding mastery of SI units.")
        elif score > 15:
            st.info("Excellent work — you clearly understand the SI system.")
        elif score > 10:
            st.info("Good effort — review the explanations and try again.")
        else:
            st.warning("Keep practicing — the SI system becomes easy with repetition.")


# ---------------------------------------------------------
#  RUN THE APP
# ---------------------------------------------------------
run_quiz()
