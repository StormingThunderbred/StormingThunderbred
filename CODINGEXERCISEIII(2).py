def Quiz_Game (input):
    
#program must start with the following: "Please press enter to start: ".
    
    input("Press press enter to start: ")

#program must command: ""Please enter your name here: "

    print("Welcome to Pub Quiz, intelligent quiz-lover!");
    input("Please enter your name here: ");
    
#if player enters their name, program must respond with following details:

print('''© Asher, 2021 {0}. All rights reserved. The rules of this game are simple:
      Type your answer manually into the program.
      The program will do its best to return your answers, but understand that it is not a guarantee.
      You may enter one answer and only one.
      If you score 20 points or more, you win. If you score 0, you lose. Welcome to the world of Pub Quiz, [player_name]!!''')
        
#define the questions and their answers
#define Question 1
#program must respond depending on whether program is correct or incorrect
input("In Sailor Moon, what is the name of Sailor Moon's pet cat?"
      "Is it Luna, Artemis or Apollo?");
input("Please enter your answer: ");

#if player enters 'Luna' into program, program must respond with the following:"Congrats, [name of player]. You got 10 points!!"

if answer == Luna:
    print("Congrats, [player_name]. You got 10 points!!");
    
#if player enters either 'Artemis' or 'Apollo', program must respond with the following:"Aww, what a shame. That wasn’t the correct answer. You got 0 points"
    
while answer == ("Artemis", "Apollo"):
    for obj in ("Tuple[str, str]"):
        print(obj)
    print("Aww, what a shame. That wasn’t the correct answer. You got 0 points!!")
    

#define Question 2
input("How many copies of Harry Potter have been sold worldwide? Is it: a) 500 million b) 700 million c) 100 million?")
input("Please enter your answer: ")
     
if answer == ("500 million"):
    print("Congrats, [name of player]. You got 10 points!!");

while "answer" == ("700 million" "100 million"):
    for obj in "tuple[str, str]":
        print(obj)
    print("Aww, what a shame. That wasn’t the correct answer. You got 0 points")   
        
#define Question 3
input("Who wrote the novel Nutcracker & Mouse-King?"
      "ETA Hoffman, Goethe or Cornelia Funke?")
input("Please enter your answer here: ")

if answer == ("ETA Hoffman"):
    print("Congrats, [name of player]!!! You got 10 points!!!");

while answer == ("Goethe","Cornelia Funke"):
    print("Aww, what a shame [player_name]!!! You got 0 points!!!");
 
#program must count-up points and use them to calculate the score. 

if "score" == ("20" or "40"):
    print("Bravo, bravo [Name of player]! You’ve won the round!");

while "score" == ("0"):
    print("Oh dear. So close and yet so far. Good luck next time [Name of player]!")

#program must ask player if they wish to play again.
#If player selects Y, program must restart. But if player selects N, program must shut down.
    
    print("Would you like to play again? Y/N?");
    input("Please enter your answer here: ");
    
#if player selects N, program must shut down
    if "answer" == ("N"):
        print("You are the Wiggerzink. Goodbye.");

#if player selects Y, program must restart
    while "answer" == ("Y"):
        input("Program restart")
