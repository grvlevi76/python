import sys

def main_struct():
    ttt = [[],[],[]]
    total_attempt = 9
    user = None
    usr_input= None
    won = None

    for i in range(3):
        for j in range(3):
            ttt[i].append(None)
    
    print("Note: rows and column denotes where u wanna put your x's or o's")
    print("Note: rows and column digit can't be more than 2 and less than 0")
    print("game visual look but in matrix form --> ")
    ttt_visually(ttt)

    print()
    while total_attempt>0 :

        if total_attempt % 2 != 0 :       #odd number - player 1 attempt
            user = "player 1"
            print("player 1 enter row and column for x(exp - 2,1): ",end='')

            while True:                   #to check if user entered position is right or not
                usr_input = eval(input())
                if ttt[usr_input[0]][usr_input[1]] != None:
                    print(ttt[usr_input[0]][usr_input[1]], "already exist at this position!! try other positions: ",end='')
                else:
                    break

            ttt[usr_input[0]][usr_input[1]] = 'x'

        else:                             #even num - player 2 attempt
            user = "player 2"
            print("player 2 enter row and column for 0(exp - 1,1): ",end='')

            while True:                     #to check if user entered position is right or not
                usr_input = eval(input())
                if ttt[usr_input[0]][usr_input[1]] != None:
                    print(ttt[usr_input[0]][usr_input[1]], "already exist at this position!! try other positions: ",end='')
                else:
                    break

            ttt[usr_input[0]][usr_input[1]] = 'o'

        ttt_visually(ttt)               # to see tic-tac-toe visually but in matrix form

        if total_attempt<6 :              # check win or not after initial 4 attempt 
            won = win_or_not(ttt)

            if won == True:
                print("\nHurray",user,"won the game")
                print("yayyy")
                return


        total_attempt = total_attempt-1

    if total_attempt == 0:
        print("\nIts a DRAW")
        return


def win_or_not(ttt):
    if ttt[0][0]==ttt[0][1]==ttt[0][2] or ttt[1][0]==ttt[1][1]==ttt[1][2] or ttt[2][0]==ttt[2][1]==ttt[2][2] or ttt[0][0]==ttt[1][0]==ttt[2][0] or ttt[0][1]==ttt[1][1]==ttt[2][1] or ttt[0][2]==ttt[1][2]==ttt[2][2] or ttt[0][0]==ttt[1][1]==ttt[2][2] or ttt[0][2]==ttt[1][1]==ttt[2][0]:
        return True
    else:
        return False 
    

def ttt_visually(ttt):
    
    for i in range(3):
        for j in range(3):
            print(ttt[i][j],"\t",end='')

        print()

ch = None
while(True):
    print("\n<=========== Welcome to tic-tac-toe ===========>")
    print("\nEnter: ")
    print("1 To START THE GAME\n2 TO SEE SCORE\nq TO EXIT")
    ch = input("Enter: ")

    match ch:
        case '1':
            print("\ngame started -->")
            main_struct()

        case '2':
            print("\nScore Board")

        case 'q'|'Q':
            print("thanks for playing the game!!!")
            sys.exit(0)

        case _:
            print("invalid input!!")

#two error remaining -
    #if user entered row and column digit is more than 2 or less then 0
    #ttt line based visual interface