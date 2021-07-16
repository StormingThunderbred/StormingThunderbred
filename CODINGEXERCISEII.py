def division (a,b):
    
#if user divides 0 by 0, program must respond: "Error - You cannot divide by zero. Please choose an appropriate denominator."
    
    if b == 0 and a == 0: #b is 0 and a is 0
        print("Error - You cannot divide by zero. Please choose an appropriate denominator.");
        
#if user divides a by b, the product must be a decimal
#program must also respond: "The first or second number = my answer."
    else:
        print("product = a/b.")
        print("The first or second number = my answer.");