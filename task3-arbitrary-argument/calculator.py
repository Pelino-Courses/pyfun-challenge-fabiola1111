def calculate(numbers, operation):
    """
   this codes Perform basic arithmetic operation on a list of numbers.
    
   
    """
    if not numbers:
        raise ValueError("You must enter at least one number.")

    result = numbers[0]

    if operation == "add":
        for num in numbers[1:]:
            result += num
    elif operation == "subtract":
        for num in numbers[1:]:
            result -= num
    elif operation == "multiply":
        for num in numbers[1:]:
            result *= num
    elif operation == "divide":
        for num in numbers[1:]:
            if num == 0:
                raise ValueError("You can't divide by zero.")
            result /= num
    else:
        raise ValueError("Invalid operation. Choose add, subtract, multiply, or divide.")

    return result 
    
try:
    user_input = input("Enter numbers separated by spaces: ")
    number_list = [float(x) for x in user_input.split()]
    operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()
    output = calculate(number_list, operation)
    print("Result:", output)

except ValueError as error:
    print("Error:", error)
