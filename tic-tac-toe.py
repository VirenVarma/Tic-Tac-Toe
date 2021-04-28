import time

print("\nExcited to play the old classic Tic-Tac-Toe game?")
print("Let's start!\n")

player1 = input("Please enter player-1 name: ").strip().title()
player2 = input("Please enter player-2 name: ").strip().title()
        
board = [" " for i in range(9)]

def print_board():
    row1 = "{} | {} | {}".format(board[0], board[1], board[2])
    row2 = "{} | {} | {}".format(board[3], board[4], board[5])
    row3 = "{} | {} | {}".format(board[6], board[7], board[8])
    
    print("\n"+row1)
    print("---------")
    print(row2)
    print("---------")
    print(row3+"\n")

def name_check():
    global player1
    global player2
    if player1 == player2:
        print("\nYou cannot have same name...")
        print("Please enter different names!\n")
        player1 = input("Please enter player-1 name: ").strip().title()
        player2 = input("Please enter player-2 name: ").strip().title()
        name_check()

def player_move(name):
    
    if name == player1:
        icon = "X"
    else:
        icon = "O"

    print("Your turn {}".format(name))
    choice = int(input("Enter your move (1-9): ").strip())

    if choice in range(1,10):  
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        else:
            print("\nThat space is taken...")
            print("Please enter another move!\n")
            player_move(name)
            
    else:
        print("\nInvalid move...")
        print("Please enter a move between (1-9)!\n")
        player_move(name)


def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
        

def is_draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    name_check()
    print_board()
    player_move(player1)
    print_board()
    
    if is_victory("X"):
        print("Congratulations! {} Wins! ".format(player1))
        break
    elif is_draw():
        print("It's a draw!")
        print("Well played {} and {}!".format(player1, player2))
        break

    player_move(player2)
    if is_victory("O"):
        print_board()
        print("Congratulations! {} Wins! ".format(player2))
        break    

time.sleep(5)