import streamlit as st

# Initialize our Streamlit app
st.set_page_config(page_title="Addition Tutor")

st.header("Learn to Add with AI")

# Input fields for numbers
number1 = st.number_input("Enter first number:")
number2 = st.number_input("Enter second number:")

# Input for user's answer
user_answer = st.number_input("What is the sum of these two numbers?")

# Button to submit the answer
submit = st.button("Check my answer")

# This function provides instructional feedback
def provide_feedback(num1, num2, user_ans):
    correct_answer = num1 + num2
    if user_ans == correct_answer:
        return f"Good job! The sum of {num1} and {num2} is indeed {correct_answer}. You got it!"
    else:
        return f"Oops! It looks like you haven't added correctly. Let's try again. Here's how you can add {num1} and {num2}:\n\n" \
               f"1. Write down the first number: {num1}\n" \
               f"2. Write down the second number: {num2}\n" \
               f"3. Add the digits in the same place value column starting from the right\n" \
               f"4. Carry over if necessary\n" \
               f"5. Write down the result\n" \
               f"6. Double-check your calculation\n\n" \
               f"Now, try adding again and enter your answer below."

# Respond to the button click
if submit:
    feedback = provide_feedback(number1, number2, user_answer)
    st.subheader("Feedback")
    st.write(feedback)
