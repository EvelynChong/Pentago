# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:12:59 2019

@author: PRAV0024
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:21:55 2019

@author: EVEL0013
"""
import numpy as np
import random 

def display_board(board):
    print(board)
    

def check_victory(board,turn,rot):

    player1_win = 0
    player2_win = 0
    
#checking for horizontal winning for player 1   
    if all(board[0, 0:5]==1):             
        player1_win=1
    elif all(board[1, 0:5]==1):
      player1_win=1
    elif all(board[2, 0:5]==1):
      player1_win=1
    elif all(board[3, 0:5]==1):
      player1_win=1            
    elif all(board[4, 0:5]==1):
      player1_win=1    
    elif all(board[5, 0:5]==1):
      player1_win=1    
    
    elif all(board[0, 1:6]==1):
      player1_win=1
    elif all(board[1, 1:6]==1):
      player1_win=1
    elif all(board[2, 1:6]==1):
      player1_win=1
    elif all(board[3, 1:6]==1):
      player1_win=1            
    elif all(board[4, 1:6]==1):
      player1_win=1    
    elif all(board[5, 1:6]==1):
      player1_win=1   
#checking for vertical winning player 1     
    elif all(board[0:5, 0:1]==1):
      player1_win=1
    elif all(board[0:5, 1:2]==1):
      player1_win=1
    elif all(board[0:5, 2:3]==1):
      player1_win=1            
    elif all(board[0:5, 3:4]==1):
      player1_win=1    
    elif all(board[0:5, 4:5]==1):
      player1_win=1  
    elif all(board[0:5, 5:6]==1):
      player1_win=1  
    elif all(board[1:6, 0:1]==1):
      player1_win=1
    elif all(board[1:6, 1:2]==1):
      player1_win=1
    elif all(board[1:6, 2:3]==1):
      player1_win=1            
    elif all(board[1:6, 3:4]==1):
      player1_win=1  
    elif all(board[1:6, 4:5]==1):
      player1_win=1 
    elif all(board[1:6, 5:6]==1):
      player1_win=1 
    
    
#checking for horizontal winning player 2   
    if all(board[0, 0:5]==2):             
      player2_win=1
    elif all(board[1, 0:5]==2):
      player2_win=1
    elif all(board[2, 0:5]==2):
      player2_win=1
    elif all(board[3, 0:5]==2):
      player2_win=1            
    elif all(board[4, 0:5]==2):
      player2_win=1    
    elif all(board[5, 0:5]==2):
      player2_win=1    
    elif all(board[0, 1:6]==2):
      player2_win=1
    elif all(board[1, 1:6]==2):
      player2_win=1
    elif all(board[2, 1:6]==2):
      player2_win=1
    elif all(board[3, 1:6]==2):
      player2_win=1            
    elif all(board[4, 1:6]==2):
      player2_win=1    
    elif all(board[5, 1:6]==2):
      player2_win=1   
#checking for vertical winning player 2       
    elif all(board[0:5, 0:1]==2):
      player2_win=1
    elif all(board[0:5, 1:2]==2):
      player2_win=1
    elif all(board[0:5, 2:3]==2):
      player2_win=1            
    elif all(board[0:5, 3:4]==2):
      player2_win=1    
    elif all(board[0:5, 4:5]==2):
      player2_win=1  
    elif all(board[0:5, 5:6]==2):
      player2_win=1  
    elif all(board[1:6, 0:1]==2):
      player2_win=1
    elif all(board[1:6, 1:2]==2):
      player2_win=1
    elif all(board[1:6, 2:3]==2):
      player2_win=1            
    elif all(board[1:6, 3:4]==2):
      player2_win=1    
    elif all(board[1:6, 4:5]==2):
      player2_win=1  
    elif all(board[1:6, 5:6]==2):
      player2_win=1
    
    
#checking for negatively slope diagonal player 2
    elif all(board[0:1, 0:1] ==2 and board[1:2, 1:2] ==2 and board[2:3, 2:3] ==2 and board[3:4, 3:4] ==2 and board[4:5, 4:5] ==2):
      player2_win = 1
    elif all(board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5]== board[5:6, 5:6]==2):
      player2_win = 1

#checking for positively slope diagonal player 2  
    elif all(board[0:1, 5:6] == board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] ==board[4:5, 1:2] ==2):
      player2_win = 1
    elif all(board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] == board[4:5, 1:2] ==board[4:5, 0:1]==2):
      player2_win = 1           
    elif all(board[0:1, 1:2] == board[1:2, 2:3] == board[2:3, 3:4] == board[3:4, 4:5] ==board[4:5, 5:6]==2):
      player2_win = 1
    elif all(board[1:2, 0:1] == board[2:3, 1:2] == board[3:4, 2:3] == board[4:5, 3:4] ==board[5:6, 4:5]==2):
      player2_win = 1
    elif all(board[0:1, 4:5] == board[1:2, 3:4] == board[2:3, 2:3] == board[3:4, 1:2] ==board[4:5, 0:1]==2):
      player2_win = 1
    elif all(board[1:2, 5:6] == board[2:3, 4:5] == board[3:4, 3:4] == board[4:5, 2:3] ==board[5:6, 1:2]==2):
      player2_win = 1
    
 
#checking for negatively slope diagonal player 1
    elif all(board[0:1, 0:1] == board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5] ==1):
      player1_win = 1
    elif all(board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5]== board[5:6, 5:6]==1):
      player1_win = 1

#checking for positively slope diagonal player 1
    elif all(board[0:1, 5:6] == board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] ==board[4:5, 1:2] ==1):
      player1_win = 1
    elif all(board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] == board[4:5, 1:2] ==board[4:5, 0:1]==1):
      player1_win = 1
    elif all(board[0:1, 1:2] == board[1:2, 2:3] == board[2:3, 3:4] == board[3:4, 4:5] ==board[4:5, 5:6]==1):
      player1_win = 1
    elif all(board[1:2, 0:1] == board[2:3, 1:2] == board[3:4, 2:3] == board[4:5, 3:4] ==board[5:6, 4:5]==1):
      player1_win = 1
    elif all(board[0:1, 4:5] == board[1:2, 3:4] == board[2:3, 2:3] == board[3:4, 1:2] ==board[4:5, 0:1]==1):
      player1_win = 1
    elif all(board[1:2, 5:6] == board[2:3, 4:5] == board[3:4, 3:4] == board[4:5, 2:3] ==board[5:6, 1:2]==1):
      player1_win = 1

               
                
                
      #preview of next move           
    if rot == 1:
         board[:3,3:6] = np.rot90(board[:3,3:6],1)
    elif rot == 2 :
        board[:3,3:6] = np.rot90(board[:3,3:6],3)
    elif rot == 3 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],1)
    elif rot == 4 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],3)
    elif rot == 5 :
        board[3:6,0:3] = np.rot90(board[3:6,0:3],1)
    elif rot == 6 :
        board[3:6,0:3] = np.rot90(board[3:6,0:3],3)
    elif rot == 7 :
        board[:3,:3] = np.rot90(board[:3,:3],1)
    elif rot == 8 :
        board[:3,:3] = np.rot90(board[:3,:3],3)  
    # return board 
    
    player1_win = 0
    player2_win = 0
    
#checking for horizontal winning for player 1   
    if all(board[0, 0:5]==1):             
        player1_win=1
    elif all(board[1, 0:5]==1):
      player1_win=1
    elif all(board[2, 0:5]==1):
      player1_win=1
    elif all(board[3, 0:5]==1):
      player1_win=1            
    elif all(board[4, 0:5]==1):
      player1_win=1    
    elif all(board[5, 0:5]==1):
      player1_win=1    
    
    elif all(board[0, 1:6]==1):
      player1_win=1
    elif all(board[1, 1:6]==1):
      player1_win=1
    elif all(board[2, 1:6]==1):
      player1_win=1
    elif all(board[3, 1:6]==1):
      player1_win=1            
    elif all(board[4, 1:6]==1):
      player1_win=1    
    elif all(board[5, 1:6]==1):
      player1_win=1   
#checking for vertical winning player 1     
    elif all(board[0:5, 0:1]==1):
      player1_win=1
    elif all(board[0:5, 1:2]==1):
      player1_win=1
    elif all(board[0:5, 2:3]==1):
      player1_win=1            
    elif all(board[0:5, 3:4]==1):
      player1_win=1    
    elif all(board[0:5, 4:5]==1):
      player1_win=1  
    elif all(board[0:5, 5:6]==1):
      player1_win=1  
    elif all(board[1:6, 0:1]==1):
      player1_win=1
    elif all(board[1:6, 1:2]==1):
      player1_win=1
    elif all(board[1:6, 2:3]==1):
      player1_win=1            
    elif all(board[1:6, 3:4]==1):
      player1_win=1  
    elif all(board[1:6, 4:5]==1):
      player1_win=1 
    elif all(board[1:6, 5:6]==1):
      player1_win=1 
    
    
#checking for horizontal winning player 2   
    if all(board[0, 0:5]==2):             
      player2_win=1
    elif all(board[1, 0:5]==2):
      player2_win=1
    elif all(board[2, 0:5]==2):
      player2_win=1
    elif all(board[3, 0:5]==2):
      player2_win=1            
    elif all(board[4, 0:5]==2):
      player2_win=1    
    elif all(board[5, 0:5]==2):
      player2_win=1    
    elif all(board[0, 1:6]==2):
      player2_win=1
    elif all(board[1, 1:6]==2):
      player2_win=1
    elif all(board[2, 1:6]==2):
      player2_win=1
    elif all(board[3, 1:6]==2):
      player2_win=1            
    elif all(board[4, 1:6]==2):
      player2_win=1    
    elif all(board[5, 1:6]==2):
      player2_win=1   
#checking for vertical winning player 2       
    elif all(board[0:5, 0:1]==2):
      player2_win=1
    elif all(board[0:5, 1:2]==2):
      player2_win=1
    elif all(board[0:5, 2:3]==2):
      player2_win=1            
    elif all(board[0:5, 3:4]==2):
      player2_win=1    
    elif all(board[0:5, 4:5]==2):
      player2_win=1  
    elif all(board[0:5, 5:6]==2):
      player2_win=1  
    elif all(board[1:6, 0:1]==2):
      player2_win=1
    elif all(board[1:6, 1:2]==2):
      player2_win=1
    elif all(board[1:6, 2:3]==2):
      player2_win=1            
    elif all(board[1:6, 3:4]==2):
      player2_win=1    
    elif all(board[1:6, 4:5]==2):
      player2_win=1  
    elif all(board[1:6, 5:6]==2):
      player2_win=1
    
    
#checking for negatively slope diagonal player 2
    elif all(board[0:1, 0:1] ==2 and board[1:2, 1:2] ==2 and board[2:3, 2:3] ==2 and board[3:4, 3:4] ==2 and board[4:5, 4:5] ==2):
      player2_win = 1
    elif all(board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5]== board[5:6, 5:6]==2):
      player2_win = 1

#checking for positively slope diagonal player 2  
    elif all(board[0:1, 5:6] == board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] ==board[4:5, 1:2] ==2):
      player2_win = 1
    elif all(board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] == board[4:5, 1:2] ==board[4:5, 0:1]==2):
      player2_win = 1           
    elif all(board[0:1, 1:2] == board[1:2, 2:3] == board[2:3, 3:4] == board[3:4, 4:5] ==board[4:5, 5:6]==2):
      player2_win = 1
    elif all(board[1:2, 0:1] == board[2:3, 1:2] == board[3:4, 2:3] == board[4:5, 3:4] ==board[5:6, 4:5]==2):
      player2_win = 1
    elif all(board[0:1, 4:5] == board[1:2, 3:4] == board[2:3, 2:3] == board[3:4, 1:2] ==board[4:5, 0:1]==2):
      player2_win = 1
    elif all(board[1:2, 5:6] == board[2:3, 4:5] == board[3:4, 3:4] == board[4:5, 2:3] ==board[5:6, 1:2]==2):
      player2_win = 1
    
 
#checking for negatively slope diagonal player 1
    elif all(board[0:1, 0:1] == board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5] ==1):
      player1_win = 1
    elif all(board[1:2, 1:2] == board[2:3, 2:3] == board[3:4, 3:4] == board[4:5, 4:5]== board[5:6, 5:6]==1):
      player1_win = 1

#checking for positively slope diagonal player 1
    elif all(board[0:1, 5:6] == board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] ==board[4:5, 1:2] ==1):
      player1_win = 1
    elif all(board[1:2, 4:5] == board[2:3, 3:4] == board[3:4, 2:3] == board[4:5, 1:2] ==board[4:5, 0:1]==1):
      player1_win = 1
    elif all(board[0:1, 1:2] == board[1:2, 2:3] == board[2:3, 3:4] == board[3:4, 4:5] ==board[4:5, 5:6]==1):
      player1_win = 1
    elif all(board[1:2, 0:1] == board[2:3, 1:2] == board[3:4, 2:3] == board[4:5, 3:4] ==board[5:6, 4:5]==1):
      player1_win = 1
    elif all(board[0:1, 4:5] == board[1:2, 3:4] == board[2:3, 2:3] == board[3:4, 1:2] ==board[4:5, 0:1]==1):
      player1_win = 1
    elif all(board[1:2, 5:6] == board[2:3, 4:5] == board[3:4, 3:4] == board[4:5, 2:3] ==board[5:6, 1:2]==1):
      player1_win = 1  
      
           #preview of next move           
    if rot == 1:
         board[:3,3:6] = np.rot90(board[:3,3:6],3)
    elif rot == 2 :
        board[:3,3:6] = np.rot90(board[:3,3:6],1)
    elif rot == 3 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],3)
    elif rot == 4 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],1)
    elif rot == 5 :
        board[3:6,0:3] = np.rot90(board[3:6,0:3],3)
    elif rot == 6 :
        board[3:6,0:3] = np.rot90(board[3:6,0:3],1)
    elif rot == 7 :
        board[:3,:3] = np.rot90(board[:3,:3],3)
    elif rot == 8 :
        board[:3,:3] = np.rot90(board[:3,:3],1)  
    # return board 

    
    
    

 
   
    if player1_win == 1 and player2_win == 1:
        #print ('draw')
        return 3
    elif player1_win == 0 and player2_win == 1:
        #print("player2_win")
        return 2 
    elif player1_win == 1 and player2_win == 0:
        #print("player1 win")
        return 1 
    else:
        #print("keep moving")
        return 0 

 
def check_move(board,row,col):    
    
    if board[row, col] == 0:
        return True
    else:
        return False
    
    
def apply_move(board,turn,row,col,rot):      
    board[row,col] = turn
    
    if rot == 1:
         board[:3,3:6] = np.rot90(board[:3,3:6],3)
    elif rot == 2 :
        board[:3,3:6] = np.rot90(board[:3,3:6],1)
    elif rot == 3 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],3)
    elif rot == 4 :
        board[3:6,3:6] = np.rot90(board[3:6,3:6],1)
    elif rot == 5 :
        board[3:6,:3] = np.rot90(board[3:6,:3],3)
    elif rot == 6 :
        board[3:6,:3] = np.rot90(board[3:6,:3],1)
    elif rot == 7 :
        board[:3,:3] = np.rot90(board[:3,:3],3)
    elif rot == 8 :
        board[:3,:3] = np.rot90(board[:3,:3],1)
    return board

         
def simulation(board,turn):#computer direct win

    
    for r in range (6):
        for c in range(6):
            for rot in range(1,9):
                new_board_1 = np.copy(board)
                if check_move( new_board_1, r, c)== True:
                    new_board_1 = apply_move( new_board_1, turn, r, c, rot)
                    if check_victory(new_board_1,turn, rot) == turn:#checking direct win for both
                        return [r,c,rot]
    return [-1]
       
                
                
def block_1_rounds(board): #pick a move for computer (row, col, rot) st, for all following human moves(row',col',rot) human does not win
    loss_list = []
    turn=1
    for r in range (6):         # if such a (row, col, rot) does not exist, pick random(com move 1)     
         for c in range(6):
             for rot in range(1,9):
                 new_board_2=np.copy(board)
                 if check_move( new_board_2, r, c)== True:
                    new_board_2 = apply_move( new_board_2, turn, r, c, rot)
                 simulation(new_board_2,2)         #checking if player 1 have direct win
                 if len(simulation(new_board_2,2))==3:
                     loss_list.append([r,c,rot]) #there is a move to make player not win
    return loss_list        
       
def computer_move (board,turn,level):
    
    if level == 1:
        row_count = random.randint(0, 5)
        column_count = random.randint(0, 5)
        rot = random.randint(1, 8)
        check_move(board, row_count, column_count)
        
        while check_move(board, row_count, column_count) == False:
           row_count = random.randint(0, 5)
           column_count = random.randint(0, 5)
                
            
       
        return [row_count, column_count, rot]
    
    
    elif level == 2:
         
         x = simulation(board,2)
         if len(x) ==3:
             row_count=x[0]
             column_count=x[1]
             rot=x[2]
             return x
         if len(x)==1:
             y= block_1_rounds(board)
             if len(y)==0:
                 return computer_move (board, turn, 1)
                 
             else:
                 z = random.choice(y)
                 return z
                 

                 
        
            

         

                          
    # no one win
                                         
        
        
def menu():
    board = np.zeros((6,6))
    display_board(board)
    
    
    num_player=int(input("How many players:"))
    while num_player < 1 or num_player >2:
        print("Only 1 or 2 Players allowed")
        num_player=int(input("How many players:"))
    turn = int(input("Who starts first:"))
    while turn != 1 and turn!= 2:
        print("Error")
        turn = int(input("Who starts first:"))
    print("Get ready!")    

# 2 Players       
    while num_player ==2:       
        display_board(board)       
        while turn != 1 and turn!= 2:
             print("Error")
             turn = int(input("Who starts first:"))
        if turn == 1 :
            print("It is player 1\'s turn")
        elif turn == 2:
            print("It is player 2\'s turn")    
        #1st Player
        if turn==1:
           while True:
                 row_count = input("Make your selection (0-5) for the row : ")
                 if row_count.isdigit():
                     row_count=int(row_count)
                     while row_count<0 or row_count>5:
                        print('Value out of range, input again')
                        row_count = int(input("Make your selection (0-5) for the row : "))
                     break
                 else:
                     row_count = input("Make your selection (0-5) for the row : ")
           while True:
                column_count = int(input("Make your selection (0-5) for the col : "))
                if column_count.isdigit():
                    column_count=int(column_count)
                    while column_count<0 or column_count>5:
                        print('Value out of range, input again')
                        column_count = int(input("Make your selection (0-5) for the col : "))
                    break
                else:
                     column_count = int(input("Make your selection (0-5) for the col : "))
           while True:
                rot = int(input("Make your selection (1-8) for the rot : "))
                if rot.isdigit(rot):
                    rot=int(rot)
                    while rot<0 or rot>8:
                        print('Value out of range, input again')
                        rot = int(input("Make your selection (1-8) for the rot :  "))
                    break
                else:
                    rot = int(input("Make your selection (1-8) for the rot : "))
           
            
            
            
            
                
        #2nd Player      
        if turn == 2:
            row_count = int(input("Make your selection (0-5) for the row : "))
            column_count = int(input("Make your selection (0-5) for the col : "))
            rot = int(input("Make your selection (1-8) for the rot : "))
            while row_count<0 or row_count>5:
                print('Value out of range, input again')
                row_count = int(input("Make your selection (0-5) for the row : "))
            while column_count<0 or column_count>5:
                print('Value out of range, input again')
                column_count = int(input("Make your selection (0-5) for the col : "))
            while rot<1 or rot>8:
                print('Value out of range, input again')
                rot = int(input("Make your selection (1-8) for the rot :  "))    
        
        
        while check_move(board, row_count, column_count) == False:
            print('Entry taken, do again')
            row_count = int(input("Make your selection (0-5) for the row : "))
            column_count = int(input("Make your selection (0-5) for the col : "))
            rot = int(input("Make your selection (1-8) for the rot : "))
            
        board = apply_move(board, turn, row_count, column_count, rot)
        if check_victory(board,turn,rot) == 1:
            print('PLAYER 1 WINS')
            return board
            
        elif check_victory(board,turn,rot) == 2:
            print('PLAYER 2 WINS')
            return board
            
        elif check_victory(board,turn,rot) == 3:
            print('DRAW')
            return board
            
        turn = turn % 2 + 1   

#Player vs Computer
                                                                                                                                                         

    else:
        
        display_board(board)
        level = int(input('level 1 or 2?'))
        while level != 1 and level!= 2:
             print("Error")
             level = int(input('level 1 or 2?'))
        if level == 1:
            print ('Level 1, Easy Level')
            while num_player ==1:
                print("")
                display_board(board)
                if turn == 1 :
                    print("It is player\'s turn")
                    row_count = int(input("Make your selection (0-5) for the row : "))
                    column_count = int(input("Make your selection (0-5) for the col : "))
                    rot = int(input("Make your selection (1-8) for the rot : "))
                    while row_count<0 or row_count>5:
                        print('value out of range, input again')
                        row_count = int(input("Make your selection (0-5) for the row : "))
                    while column_count<0 or column_count>5:
                        print('value out of range, input again')
                        column_count = int(input("Make your selection (0-5) for the col : "))
                    while rot<0 or rot>8:
                        print('value out of range, input again')
                        rot = int(input("Make your selection (1-8) for the rot :  "))
                    while check_move(board, row_count, column_count) == False:
                        print('do again')
                        row_count = int(input("Make your selection (0-5) for the row : "))
                        column_count = int(input("Make your selection (0-5) for the col : "))
                        rot = int(input("Make your selection (1-8) for the rot : "))
                elif turn == 2:
                     print("It is computer\'s turn")
                     x = computer_move(board, turn, level)
                     
                     row_count=x[0]
                     column_count=x[1]
                     rot=x[2]
                     
                board = apply_move(board, turn, row_count, column_count, rot)
                if check_victory(board,turn,rot) == 1:
                    print('PLAYER 1 WINS, END OF GAME!!!')
                    return board
                elif check_victory(board,turn,rot) == 2:
                    print('COMPUTER WINS, END OF GAME !!!')
                    return board
                elif check_victory(board,turn,rot) == 3:
                    print('DRAW, END OF GAME!!!')
                    return board
                turn = turn % 2 + 1   
                             

    
        elif level==2:
          print('Level 2, medium Level')
          while num_player ==1:
                print("")
                display_board(board)
                if turn == 2 :
                    print("It is player\'s turn")
                    row_count = int(input("Make your selection (0-5) for the row : "))
                    column_count = int(input("Make your selection (0-5) for the col : "))
                    rot = int(input("Make your selection (1-8) for the rot : "))
                    while row_count<0 or row_count>5:
                        print('value out of range, input again')
                        row_count = int(input("Make your selection (0-5) for the row : "))
                    while column_count<0 or column_count>5:
                        print('value out of range, input again')
                        column_count = int(input("Make your selection (0-5) for the col : "))
                    while rot<0 or rot>8:
                        print('value out of range, input again')
                        rot = int(input("Make your selection (1-8) for the rot :  "))
                    while check_move(board, row_count, column_count) == False:
                        print('do again')
                        row_count = int(input("Make your selection (0-5) for the row : "))
                        column_count = int(input("Make your selection (0-5) for the col : "))
                        rot = int(input("Make your selection (1-8) for the rot : "))
                elif turn == 1:
                     
                     print("It is computer\'s turn")
                     x = computer_move(board, turn, level) 
                     
                     row_count=x[0]
                     column_count=x[1]
                     rot=x[2]
                     
                board = apply_move(board, turn, row_count, column_count, rot)
                if check_victory(board,turn,rot) == 1:
                    print('PLAYER 1 WINS, END OF GAME!!!')
                    return board
                elif check_victory(board,turn,rot) == 2:
                    print('COMPUTER WINS, END OF GAME!!!')
                    return board
                elif check_victory(board,turn,rot) == 3:
                    print('DRAW, END OF GAME!!!')
                    return board
                turn = turn % 2 + 1   
                        
 
    


menu()