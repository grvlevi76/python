#keep user's score and print their last best score (least lives took to win the game

import random
import sys

def guess(r_num):
    total_lives = 7

    while(total_lives>0):
        print("\nTotal lives left =",total_lives)            
        user_num = int(input("Guess the number: "))

        if user_num>r_num:
            print("Wrong number!!!")
            print("hint: Less than",user_num)
        elif user_num<r_num:
            print("Wrong number!!!")
            print("hint: greater than",user_num)
        else:
            print("\nCorrect number!!!")
            print("You won \nyayyy partyyy")
            break
                    
        total_lives = total_lives-1
                
        if total_lives==0:
            print("\nNo lives left")
            print("Correct number was",r_num)
            print("You lose blud") 

def score(filename):
    print("filename:",filename)
    #read score fromm file


            

ch=None
while(True):
    file = open("score_board.txt","a+")  

    print("<======== Welcome to guess the number game ========>")
    print("\nEnter: ")
    print("1 To START THE GAME\n2 TO SEE SCORE\nq TO EXIT")
    ch = input("Enter: ")

    match ch:
        case '1':
            print("\ngame started")
            random_num = random.randint(1,100)
            print("random number generated")

            guess(random_num)

        case '2':
            print("\nYOUR BEST SCORES --->")
            score(file)
                
        case 'q':
            print("Thanks for playing the game see ya blud!!!")
            file.close()
            sys.exit(0)

        case _:
            print("Invalid input!!!\n")