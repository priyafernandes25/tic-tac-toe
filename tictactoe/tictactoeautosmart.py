import os
import sys
import random
game=[" "," "," "," "," "," "," "," "," "]
count=0

def begin():
    n=2
    print("Press\n1) Player1 ='x' and player2='0'\n2) Player1 ='0' and player2='x'\n")
    tr=int(input())
    if tr==1:
        player1='x'
        player2='0'
    else:
        player1='0'
        player2='x'
        
    while True:
        print("Player 1's turn ")
        player(player1)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()
        print("Player 2's turn ")
        player_computer(player1,player2)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()
            
def player(p):
    global count
    if count!=9:
        print("Choose an empty space from 1-9")
        t=int(input())
        if game[t-1] != " ":
            print("Space not empty")
            player(p)
        else:
            game[t-1]=p
            print_game()
            count=count+1
    else:
        print("The game is draw")
        sys.exit()
        
        
def player_computer(p1,p2):
    block=blockopponent(p1,p2)
    win=wincomp(p1,p2)
    global count
    if count!=9:
        t=random.randint(1,9)
        while True:
            if game[t-1]!=" ":
                t=random.randint(1,9)
            else:
                break
        if win !=10:
            t=win
        elif block!=10:
            t=block
        game[t-1]=p2
        print_game()
        count=count+1
    else:
        print("The game is draw")
        sys.exit()

def checksimulation(p1,p2,g):
    
    for i in range(8):
        if g[i]==" ":
            g[i]=6
            
    solution1=list(set((g[0],g[1],g[2])))
    solution2=list(set((g[0],g[3],g[6])))
    solution3=list(set((g[1],g[4],g[7])))
    solution4=list(set((g[3],g[4],g[5])))
    solution5=list(set((g[2],g[5],g[8])))
    solution6=list(set((g[2],g[4],g[6])))
    solution7=list(set((g[6],g[7],g[8])))
    solution8=list(set((g[0],g[4],g[8])))
    
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=6:
            if result[i][0]==p1:
                return 2
            elif result[i][0]==p2:
                return 1
            else:
                return 3
    return 4

    
            
    
def blockopponent(p1,p2):
    move=10
    for i in range(0,9):
        
    #copy gameboard
        gamedummy=game.copy()
        #wherever the game has ' ' insert p1
        
        if gamedummy[i]==" ":
            gamedummy[i]=p1
        #check condition for winning
            result=checksimulation(p1,p2,gamedummy)
            if result==2:
                move=i+1
                break
    print(move)
    return move
    #sort the list according to winning
    #whichever position is at index 1 insert p2 there
    

def wincomp(p1,p2):
    move=10
    for i in range(0,9):
        
    #copy gameboard
        gamedummy=game.copy()
        #wherever the game has ' ' insert p2
        
        if gamedummy[i]==" ":
            gamedummy[i]=p2
        #check condition for winning
            result=checksimulation(p1,p2,gamedummy)
            if result==1:
                move=i+1
                break
    print(move)
    return move
#def wincomp():
    #copy gameboard
    #wherever the game has ' ' insert p2
    #check condition for winning
    #sort the list according to winning
    #whichever position is at index 1 insert p2 there
    


def print_game():
    os.system('cls')
    print()
    print(game[0]+" | "+game[1]+"| "+game[2])
    print("__|__|__")
    print(game[3]+" | "+game[4]+"| "+game[5])
    print("__|__|__")
    print(game[6]+" | "+game[7]+"| "+game[8])


def check_result(p1,p2):
    value=6
    for i in range(8):
        if game[i]==" ":
            game[i]=6
            
    solution1=list(set((game[0],game[1],game[2])))
    solution2=list(set((game[0],game[3],game[6])))
    solution3=list(set((game[1],game[4],game[7])))
    solution4=list(set((game[3],game[4],game[5])))
    solution5=list(set((game[2],game[5],game[8])))
    solution6=list(set((game[2],game[4],game[6])))
    solution7=list(set((game[6],game[7],game[8])))
    solution8=list(set((game[0],game[4],game[8])))
    
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=6:
            if result[i][0]==p1:
                print("Player 1 wins.")
            else:
                print("Player 2 wins.")
            value=5
            
    for i in range(8):
        if game[i]==6:
            game[i]=" "
            
    if value==5:
        return 1
    else:
        return 2
    
    
    
print("The pattern of tic tac toe board is as follows:")
print("1 |2 |3 ")
print("__|__|__")
print("4 |5 |6 ")
print("__|__|__")
print("7 |8 |9 ")
begin()