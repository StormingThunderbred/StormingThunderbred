#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random
def Quiz_Game(start,name,numb):
    '''Author:Asher
    Game: Pub Quiz
    Version: 3.0
    © 2021, Asher. All rights reserved
    
    This is a program for the demo of a multiple-choice quiz,
    which will be presented at an event. The main aim is to
    make a game which is user-friendly.'''
    
#setting the condition for starting the game.
    if start == 'play' and (numb==3 or numb==5):
        Copyright="© 2021 Asher, {0}. All rights reserved";
        Game_name="Pub Quiz";
        Message='''The rules of this game are simple.
You may type in one answer, but only one.
If you score 20 points or more, you win the game.
If you score 0, you will lose the game.
Welcome to the world of {0}, {1}.'''
        print(Copyright.format(Game_name))
        print(Message.format(Game_name, name))
        user_input=input('\nAre you happy to play the game with these rules? ');
        
#we either start the game or stop it depending on the user input
        if user_input =="y":
            listQuestions=["\n\nQ. In the manga series Sailor Moon, what is the name of the cat?","\n\nQ. how many copies of the Harry Potter novels have been sold?"
                           "\n\nQ. In The Lord of the Rings, what is the name of the dragon-like creatures the Nazgul ride on?","Do any of you even care?"
                           "\n\nQ. How many copies has One Piece sold?","In what year was Charlie and the Chocolate Factory published?"];
            listChoices=["\na. Apollo \nb. Artemis \nc. Luna","\na.500m \nb.720m \nc.340m",
            "\na. Fell-beasts \nb. Firedrakes \nc. Phoenixes","\na. no \nb. yes \nc. maybe",
            "\na.490m \nb.228m \nc.600m","\na.1991 \nb.1964 \nb.1885"];
            correct_answers=["c","a","a","c","a","b"];
            #make a new list of questions with answers:
            newList=[listQuestions[0]+listChoices[0],listQuestions[1]+listChoices[1],
                    listQuestions[2]+listChoices[2],listQuestions[3]+listChoices[3]
                    listQuestions[4]+listChoices[4],listQuestions[5]+listChoices[5]];
            #debugging
            print(listQuestions)
            #computer chooses a question at random;
            AI_question=random.choice(newList);
            print(AI_question)
            answer_input=input('\nEnter your answer: ')
            pos_AI_ques=int(newList.index(AI_question))
            
        elif user_input == "n":
            print('\nSo sad to see you go {0}. See you next time!!'.format(name))
        else:
            while user_input != "n" or user_input != "y":
                print('\nYou can only enter lowercase letters as your answer: n, to quit game or y,\n to play game')
                new_input=input('\nAre you happy to play the game with these rules? ')
                if new_input == "y":
                    print("o")
                    break
                elif new_input == "n":
                    print('\nSad to see you go {0}. See you next time!!'.format(name))
                    break
                
#catching some errors:
    elif start != "play":
        print('You must enter the word "play" into the function to continue')
    elif type(numb) != int or numb <= 0:
        print('\nYou must enter into the function an integer,\ni.e, whole numbers positive and negative, that is postive. Do not enter decimals, e.g. 2.5.')
    elif numb != int(3) or numb != int(5):
        print('\nYou can only choose a 3 or 5 question round.\nPlease enter 3 or 5 into the function.')
    
                
        
                
        
            

        