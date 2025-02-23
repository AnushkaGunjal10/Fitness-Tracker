import streamlit as st
import pandas as pd
import requests  # Assuming Gemini API uses HTTP requests

# Set page configuration
st.set_page_config(page_title="Fitness Tracker", page_icon="💪", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #93cdf8;
        }
        html, body {
            color: #ffffff !important;
        }
        input, select, textarea {
            color: white !important;
            background-color: black !important;
        }
        .stButton>button {
            background-color:#e1058d;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🏋️‍♂️ Fitness Tracker")

# User Inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=300.0, step=0.1)
height = st.number_input("Enter your height (inches):", min_value=20, max_value=100, step=1)
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])

def get_diet_chart(weight, age, height, activity_level):
    height_m = height * 0.0254  # Convert inches to meters
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        diet_type = "High-Calorie Diet 🍞🍗"
        meal_plan = {
            "Meal": ["Breakfast 🍳", "Mid-Morning Snack 🍎", "Lunch 🍛", "Evening Snack 🥜", "Dinner 🥗"],
            "Food": [
                "Oatmeal with nuts and banana, boiled eggs, and milk",
                "Protein smoothie with fruits and yogurt",
                "Grilled chicken, rice, vegetables, and salad",
                "Peanut butter toast with banana",
                "Fish or paneer with quinoa and steamed veggies"
            ]
        }
    elif bmi >= 25:
        diet_type = "Weight-Loss Diet 🥗🍵"
        meal_plan = {
            "Meal": ["Breakfast 🍳", "Mid-Morning Snack 🍎", "Lunch 🍛", "Evening Snack 🥜", "Dinner 🥗"],
            "Food": [
                "Scrambled eggs with whole wheat toast, green tea",
                "Greek yogurt with almonds",
                "Grilled fish/chicken, quinoa, and steamed vegetables",
                "A handful of mixed nuts and green tea",
                "Salad with lean protein and olive oil dressing"
            ]
        }
    else:
        diet_type = "Balanced Diet 🥑🍚"
        meal_plan = {
            "Meal": ["Breakfast 🍳", "Mid-Morning Snack 🍎", "Lunch 🍛", "Evening Snack 🥜", "Dinner 🥗"],
            "Food": [
                "Multigrain toast with peanut butter and a fruit smoothie",
                "Handful of nuts and a protein shake",
                "Brown rice, lentils, mixed vegetables, and curd",
                "Fruit salad with seeds",
                "Grilled paneer or chicken with whole wheat roti and soup"
            ]
        }
    
    return diet_type, pd.DataFrame(meal_plan)

if st.button("Get Diet Plan"):
    if name and age and weight and height:
        diet_type, meal_plan_df = get_diet_chart(weight, age, height, activity_level)
        
        # Display Diet Plan
        st.success(f"Hello {name}, here is your recommended {diet_type}:")
        st.table(meal_plan_df)
    else:
        st.warning("Please fill in all fields to get your diet plan.")
