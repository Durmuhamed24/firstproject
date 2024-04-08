def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2  
def multi(num1,num2):
    return num1*num2
def  divide(num1,num2):
     return num1/num2
 
    
operations={
    "+": add,
    "-": sub,
    "*":multi,
    "/":divide,
    
    
 }
def calculator():
    num1=float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_contiue =True
    while should_contiue:
        operation_symbol =input("Pick an operation : ")  
        num2 =float(input("What' s the next number?: ")) 
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}") 
        if input(f"Type 'y' to continue calculating with {answer} : ")=="y":
           num1=answer
        else:    
            should_contiue=False
            calculator()
calculator()                