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
     ["based on water", "not based on any substance", "based on oxygen
