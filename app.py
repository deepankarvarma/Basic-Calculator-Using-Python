import streamlit as st

# Define the layout of the app
st.title("Basic Calculator")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.hdqwalls.com/download/dark-abstract-black-minimal-4k-q0-2560x1440.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
col1, col2 = st.columns(2)

# Define the input fields for the calculator
with col1:
    num1 = st.number_input("Enter the first number", value=0.0)
with col2:
    num2 = st.number_input("Enter the second number", value=0.0)

# Define the operations that the calculator can perform
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the selected operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
else:
    if num2 == 0:
        st.error("Cannot divide by zero")
        result = ""
    else:
        result = num1 / num2

# Display the result
if result != "":
    st.success(f"The result of {operation.lower()} is {result}")
