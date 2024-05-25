import streamlit as st

def main():
    st.title("USMAN AZIZ")
    num1 = st.number_input("Enter number 1:")
    num2 = st.number_input("Enter number 2:")
    operation = st.selectbox("Enter operator", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        result = 0
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Division by zero!")
                return
        st.success(f"Result: {result}")

main()
