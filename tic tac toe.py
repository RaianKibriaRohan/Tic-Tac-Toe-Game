def permission():
    global i1
    per = input("Want to start a game?")
    i1 = input("[y/n]: ")
    return i1
for i in range(1000):
    permission()
    if i1=="y":
        print("Welcome to the Tic Tac Toe game :)")
        board1 = """
        Here is the board

        0  | 1  | 2  
        ---|--- |---
        3  | 4  | 5  
        ---|--- |---
        6  | 7  | 8
        
        Let the game begin
        """
        lst1=[]
        for i in range(9):
            lst1.append(" ")
        def board():
            board1 = f"""
             {lst1[0]} | {lst1[1]} | {lst1[2]}  
            ---|---|---
             {lst1[3]} | {lst1[4]} | {lst1[5]}
            ---|---|---
             {lst1[6]} | {lst1[7]} | {lst1[8]}
            """
            print(board1)
        flag = True
            
        def play(name):
            
            while flag:
                move=int(input(f'{name}: '))
                if 0<=move<=8:
                    if move in lst1:
                        print("This place is already blocked")
                        continue
                    else:
                        lst1.append(move)
                    # return move
                else:
                    print("Please enter the number between 1-8")
                return move
        def info():
            p1=input("Enter player 1 name: ")
            p2=input("Enter player 2 name: ")
            print(board1)
            print(f"{p1}'s sign is - X\n{p2}'s sign is - O")
            input("Pree enter to start")
            board()
            for i in range(9):
                if i%2==0:
                    if flag==False:
                        break
                    else:
                        turn = play(p1)
                        lst1[turn] = "X"
                else:
                    if flag==False:
                        break
                    else:
                        turn = play(p2)
                        lst1[turn] = "O"
                board()
                matching(p1, p2)
                
                    
        def matching(player1, player2):
            global flag
            if (lst1[0] or lst1[1]==" " or lst1[2]==" " or lst1[3]==" " or lst1[4]==" " or lst1[5]==" " or lst1[6]==" " or lst1[7]==" " or lst1[8]==" "):
                if (lst1[0]==lst1[1]==lst1[2]=="X" or lst1[0]==lst1[3]==lst1[6]=="X" or lst1[0]==lst1[4]==lst1[8]=="X" or
            lst1[6]==lst1[4]==lst1[2]=="X" or lst1[6]==lst1[7]==lst1[8]=="X" or lst1[8]==lst1[5]==lst1[2]=="X" or
            lst1[1]==lst1[4]==lst1[7]=="X" or lst1[3]==lst1[4]==lst1[5]=="X"):
                    print(f'Congratulation. {player1} is the winner!!!')
                    flag = False
                    
                elif (lst1[0]==lst1[1]==lst1[2]=="O" or lst1[0]==lst1[3]==lst1[6]=="O" or lst1[0]==lst1[4]==lst1[8]=="O" or
            lst1[6]==lst1[4]==lst1[2]=="O" or lst1[6]==lst1[7]==lst1[8]=="O" or lst1[8]==lst1[5]==lst1[2]=="O" or
            lst1[1]==lst1[4]==lst1[7]=="O" or lst1[3]==lst1[4]==lst1[5]=="O"):
                    print(f'Congratulation. {player2} is the winner!!!')
                    flag = False
                else:
                    pass
            else:
                print("DRAW. Please Try again.")
            
        info()
    else:
        break

