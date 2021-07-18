def division (numb1,numb2):
    
    print("Enter your numbers here");
    
#if user divides 0 by 0, program must respond: "Error - You cannot divide by zero. Please choose an appropriate denominator."
    
    if numb2 == 0 and numb1 == 0: #numb2 is 0 and numb1 is 0
        print("Error - You cannot divide by zero. Please choose an appropriate denominator.");
        
    else:
#if user divides numb1 by numb2, the program should respond: "{0} divided by {1} = {2}."
#answer must be a decimal
        div_res = numb1 / numb2
        print("{0} divided by {1} = {2}".format(numb1, numb2, div_res));
