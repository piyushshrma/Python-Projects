board = ['-','-','-','-','-','-','-','-','-']

def winCond():
    if(board[0]==board[1]==board[2]=='X' or
       board[3]==board[4]==board[5]=='X' or
       board[6]==board[7]==board[8]=='X' or
       board[0]==board[3]==board[6]=='X' or
       board[0]==board[4]==board[8]=='X' or
       board[1]==board[4]==board[7]=='X' or
       board[2]==board[4]==board[6]=='X' or
       board[2]==board[5]==board[8]=='X'):
        print("User 1 wins")
        return True
        
    elif(board[0]==board[1]==board[2]=='O' or
         board[3]==board[4]==board[5]=='O' or
         board[6]==board[7]==board[8]=='O' or
         board[0]==board[3]==board[6]=='O' or
         board[0]==board[4]==board[8]=='O' or
         board[1]==board[4]==board[7]=='O' or
         board[2]==board[4]==board[6]=='O' or
         board[2]==board[5]==board[8]=='O'):
        print("User 2 wins")
        return True

    return False

def display_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

for i in range(5):
    print(f"User 1's chance")
    loc1 = int(input("Where do you want to mark: "))
    board[loc1 - 1] = 'X'
    if winCond():
        display_board()
        break
    display_board()
    
    print(f"User 2's chance")
    loc2 = int(input("Where do you want to mark: "))
    board[loc2 - 1] = 'O'
    if winCond():
        display_board()
        break
    display_board()