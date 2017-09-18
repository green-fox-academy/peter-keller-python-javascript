# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit
def calculator(procedure,op1,op2):
    if procedure == "+":
        end_result = op1 + op2
    elif procedure == "-":
        end_result = op1 - op2
    elif procedure == "*":
        end_result = op1 * op2
    elif procedure == "/":
        if op2 != 0:
            end_result = op1 / op2
        else:
            end_result = "You can't divide with 0"
    elif procedure == "%":
        if op2 != 0:
            end_result = op1 % op2
        else:
            end_result = "It doesn't make sense!!!"
    else:
        end_result = "No operator given"
    print("The result is: ", end_result)

input1, input2, input3 = input("Please type in something: ").split()
calculator(input1,int(input2),int(input3))