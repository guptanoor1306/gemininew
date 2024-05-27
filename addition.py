import streamlit as st

# Initialize our Streamlit app
st.set_page_config(page_title="Addition Tutor")

st.header("Learn to Add with AI")

# Input fields for numbers
number1 = st.number_input("Enter first number:", format="%d")
number2 = st.number_input("Enter second number:", format="%d")

# Input for user's answer
user_answer = st.number_input("What is the sum of these two numbers?", format="%d")

# Button to submit the answer
submit = st.button("Check my answer")

# This function could be expanded to connect with an AI model
def explain_answer(num1, num2, user_ans):
    correct_answer = num1 + num2
    if user_ans == correct_answer:
        return "Correct! Great job."
    else:
        return f"Incorrect. The sum of {num1} and {num2} is {correct_answer}, not {user_ans}."

# Respond to the button click
if submit:
    explanation = explain_answer(number1, number2, user_answer)
    st.subheader("Feedback")
    st.write(explanation)
