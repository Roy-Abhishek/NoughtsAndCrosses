class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.X = True

    def __str__(self):
        return \
f'''
 {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}
----------------
 {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}
----------------
 {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}
'''

    def add_val(self, board_num):
        if self.X and self.board[board_num - 1] != ("O" and "X"):
            self.board[board_num - 1] = "X"
            return True
        elif not self.X and self.board[board_num - 1] != ("X" and "O"):
            self.board[board_num - 1] = "O"
            return True
        else:
            return False

    def check_if_finished(self):
        return (
            self.board[0] == self.board[1] == self.board[2] and self.board[0] != " " or
            self.board[3] == self.board[4] == self.board[5] and self.board[3] != " " or
            self.board[6] == self.board[7] == self.board[8] and self.board[6] != " " or
            self.board[0] == self.board[3] == self.board[6] and self.board[0] != " " or
            self.board[1] == self.board[4] == self.board[7] and self.board[1] != " " or
            self.board[2] == self.board[5] == self.board[8] and self.board[2] != " " or
            self.board[0] == self.board[4] == self.board[8] and self.board[0] != " " or
            self.board[2] == self.board[4] == self.board[6] and self.board[2] != " "
        )

    def check_if_tie(self):
        return (
            self.board[0] != " " and
            self.board[1] != " " and
            self.board[2] != " " and
            self.board[3] != " " and
            self.board[4] != " " and
            self.board[5] != " " and
            self.board[6] != " " and
            self.board[7] != " " and
            self.board[8] != " " and
            not self.check_if_finished()
        )

    def play(self):
        print("Type \"quit\" at any point in the game to quit the game")

        while True:
            turn = input("Enter letter which goes first (X/O): ").lower()

            if turn == "x":
                self.X = True
                break
            elif turn == "o":
                self.X = False
                break
            elif turn == "quit":
                print()
                quit()
            else:
                print("\nPlayer letter is not valid, please try again")
                continue
        
        print("\nBox numbers -")
        print(f'''
 1  |  2  |  3
----------------
 4  |  5  |  6
----------------
 7  |  8  |  9

________________
''')

        while not self.check_if_finished():
            if self.X:
                turn = "X"
            else:
                turn = "O"

            if self.check_if_tie():
                break

            print(self.__str__())
            turn_number = input(f"{turn}: ")
            
            if turn_number.lower() == "quit":
                quit()

            if turn_number.isdigit():
                turn_number = int(turn_number)
            else:
                print("Please enter a valid number")
                continue

            if turn_number == 0 or turn_number >= 10:
                print("Pleas enter a number in the range of 1 through 9")
                continue

            if not self.add_val(turn_number):
                print("Invalid placement, try again")
                continue

            self.X = not self.X

        print(self.__str__())
        
        if self.check_if_tie():
            print("Game tied\n")
        else:
            print(f"{turn} has won!!!\n")

        while True:
            game_again = input("Want to play again (Y/n): ").lower()
            if game_again == "y":
                self.play()
                quit()
            elif game_again == "n":
                quit()
            else:
                continue


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.play()
