from enum import Enum


class XOGame:
    STATUS = Enum('Status', ['RUNNING', 'WIN', "BREAK"])

    def __init__(self):
        self.board = {key: ' ' for key in range(1, 10)}
        self.current_player = 'X'
        self.game_status = self.STATUS.RUNNING
        self.current_cell = 0
        self.move_count = 0

    def print_board(self):
        print(" ┌─────┬─────┬─────┐")
        print(f" │  {self.board[7]}  │  {self.board[8]}  │  {self.board[9]}  │")
        print(" ├─────┼─────┼─────┤")
        print(f" │  {self.board[4]}  │  {self.board[5]}  │  {self.board[6]}  │")
        print(" ├─────┼─────┼─────┤")
        print(f" │  {self.board[1]}  │  {self.board[2]}  │  {self.board[3]}  │")
        print(" └─────┴─────┴─────┘")

    def check_winner(self):
        win_lines = [(7, 8, 9), (4, 5, 6), (1, 2, 3),  # horizontal
                     (1, 4, 7), (2, 5, 8), (3, 6, 9),  # vertical
                     (3, 5, 7), (1, 5, 9)]  # diagonal
        for line in win_lines:
            if all(self.board[cell] == self.current_player for cell in line):
                self.game_status = self.STATUS.WIN
                self.change_color(line)
                return True
        return False

    def change_color(self, cells):
        for cell in cells:
            self.board[cell] = f"\033[1;31m{self.board[cell]}\033[0m"

    def print_result(self):
        self.print_board()
        if self.game_status == self.STATUS.RUNNING:
            print("\nDraw!")
        elif self.game_status == self.STATUS.WIN:
            print(f'\n{self.current_player} is the winner!!!')
        else:
            print("Exiting the game.")

    def set_current_cell(self):
        while self.game_status == self.STATUS.RUNNING:
            cell = input(f'Type cell [1-9] or 0 for exit game: ')
            if len(cell) == 1 and '0' <= cell <= '9':
                self.current_cell = int(cell)
                if cell == '0':
                    self.game_status = self.STATUS.BREAK
                elif self.board[int(cell)] == ' ':
                    break
                else:
                    print("The cell is occupied.")
            else:
                print('Invalid input')

    def set_current_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while self.move_count < 9:
            self.print_board()
            self.set_current_cell()
            if self.current_cell == 0:
                break
            self.board[self.current_cell] = self.current_player
            if self.move_count > 3 and self.check_winner():
                break
            self.set_current_player()
            self.move_count += 1
        self.print_result()


if __name__ == "__main__":
    game = XOGame()
    game.play()
