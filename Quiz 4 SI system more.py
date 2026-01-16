# Quiz 4 SI system more
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

            "explanation": "Kelvin is based on absolute zero, not on properties of any material"


