operator = input("Select an operator: ")
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
match operator:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "%":
        print(x%y)
    case "/":
        print(x/y)

    case _ :
        print("You entered wrong values, pleas recheck... ")