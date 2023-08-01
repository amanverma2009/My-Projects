print("\n")
Input_Operator = input("Enter Your Operation(+, -, *, /):")
if Input_Operator == "+":
    print("You Selected Addition")
elif Input_Operator == "-":
    print("You Selected Subtraction")
elif Input_Operator == "*":
    print("You Selected Multiplication")
elif Input_Operator == "/":
    print("You Selected Division")
else:
    print("Invalid")
    quit()
Input_Number1 = int(input("Enter The 1st Number:"))
Input_Number2 = int(input("Enter The 2nd Number:"))
if Input_Operator == "+":
    print("The Result Of The Operation Is:", Input_Number1+Input_Number2)
elif Input_Operator == "-":
    print("The Result Of The Operation Is:", Input_Number1-Input_Number2)
elif Input_Operator == "*":
    print("The Result Of The Operation Is:", Input_Number1*Input_Number2)
elif Input_Operator == "/":
    print("The Result Of The Operation Is:", Input_Number1/Input_Number2)
else:
    print("Something Went Wrong(Maybe You Typed The Wrong Operator or the Spelling Is Not As It is Shown Above At The Top.)")