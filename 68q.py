def evaluate_expression():
  
    exp = input("Enter a basic mathematical expression: ")
    
    try:
       
        result = eval(exp)
        

        print(result)
        
    except Exception as e:
        print(f"Invalid expression or error encountered: {e}")

# Run the program

evaluate_expression()
#eval(): Dynamically evaluates the string expression as standard Python code and returns the numerical result.