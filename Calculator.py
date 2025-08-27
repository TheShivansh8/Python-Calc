importstreamlit as st
st.set_page_config(page_title="Auto Calc")
def calculator():
    print("My first Project Made by Chatgpt a Calculator (v1.0)")
    print("Supports: + and - only and for further wait for next upfate probably next month")

    num1 = float(input("Enter first number: "))
    op = input("Choose operation (+ or -): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result == num1 * num2
    elif op == "/":
        result == num1 / num2
    if num1 <= num 2:
        print ("Error")
           
    
    else:
        result = "Feature under development 🚧"

    print("Result:", result)

calculator()
