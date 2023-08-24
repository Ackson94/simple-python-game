from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
            else:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] != 'X' and board[row][col] != 'O':
                    board[row][col] = 'O'
                    break
                else:
                    print("That square is already occupied. Choose another.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)
    
    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
