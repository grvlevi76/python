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

        #player 1 attempt - odd number
        if total_attempt % 2 != 0 :       
            user = "player 1"
            print("player 1 enter row and column for x(exp - 2,1): ",end='')

        else:         #player 2 attempt - even number         
            user = "player 2"
            print("player 2 enter row and column for 0(exp - 1,1): ",end='')

        while True:    # to check user entered row and column is valid or not

            usr_input = input()
            usr_input = list(usr_input)
            row= int(usr_input[0])
            column= int(usr_input[2])
            if row<0 or row>2 or column<0 or column>2:
                print("invalid out of bound input!")
                print("rows and column digit can't be more than 2 and less than 0! enter position again: ",end='')

            elif ttt[row][column] != None:
                print(ttt[row][column], "already exist at this position!! try other positions: ",end='')

            else:

                if(user =='player 1'):
                    ttt[row][column] = 'x'
                else:
                    ttt[row][column] = 'o'

                break


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
    
    print()
    for i in range(3):
        for j in range(3):
            if ttt[i][j]!=None:
                print(ttt[i][j],end='')
            else:
                print("_",end='')

            if(j!=2):
                print(" | ",end='')
            
        print()
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