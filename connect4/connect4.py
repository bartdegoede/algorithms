class Connect4(object):
    ROWS = 6
    COLUMNS = 7
    PLAYERS = ['X', 'O']

    def __init__(self):
        self.board = [['_' for x in range(self.COLUMNS)] for y in range(self.ROWS)]
        self.is_over = False
        self.turn = 0
        self.player = None

    def __repr__(self):
        print('\n')
        for row in reversed(self.board):
            print(*row, sep='|')
        return ''

    def play_piece(self, row, column, player_piece):
        self.board[row][column] = player_piece
        if self.is_winning_move(player_piece):
            self.is_over = True

    def is_available_location(self, column):
        return self.board[-1][column] == '_'

    def next_open_row(self, column):
        """For ease of navigation, 'drop' from the bottom"""
        for row in range(self.ROWS):
            if self.board[row][column] == '_':
                return row

    def play(self):
        if self.turn % 2 == 0:
            self.player = self.PLAYERS[0]
        else:
            self.player = self.PLAYERS[1]

        while True:
            column = int(input(f'Player {self.player}, make your selection (0-{self.COLUMNS - 1}):'))
            if self.is_available_location(column):
                row = self.next_open_row(column)
                self.play_piece(row, column, self.player)
                self.turn += 1
                break
            print('Invalid selection.')

    def check_horizontal(self, winning):
        for row in range(self.ROWS):
            # subtract 3 because you can't get 4 in a row if there's not enough
            # columns left
            for column in range(self.COLUMNS - 3):
                if self.board[row][column:column+4] == winning:
                    return True

    def check_vertical(self, winning):
        for row in range(self.ROWS - 3):
            # subtract 3 because you can't get 4 in a row if there's not enough
            # columns left
            for column in range(self.COLUMNS):
                if [self.board[row][column], self.board[row+1][column], self.board[row+2][column], self.board[row+3][column]] == winning:
                    return True

    def check_diagonal(self, winning):
        if self.check_upwards_diagonal(winning):
            return True
        if self.check_downwards_diagonal(winning):
            return True
        return False

    def check_upwards_diagonal(self, winning):
        for row in range(self.ROWS - 3):
            for column in range(self.COLUMNS - 3):
                if [self.board[row][column], self.board[row+1][column+1], self.board[row+2][column+2], self.board[row+3][column+3]] == winning:
                    return True

    def check_downwards_diagonal(self, winning):
        for row in range(3, self.ROWS):
            for column in range(self.COLUMNS - 3):
                if [self.board[row][column], self.board[row-1][column+1], self.board[row-2][column+2], self.board[row-3][column+3]] == winning:
                    return True

    def is_winning_move(self, player_piece):
        winning = [player_piece for _ in range(4)]
        if self.check_horizontal(winning):
            return True
        if self.check_vertical(winning):
            return True
        if self.check_diagonal(winning):
            return True
        return False

if __name__ == '__main__':
    game = Connect4()

    game_over = False
    turn = 0

    while not game.is_over:
        print(game)
        game.play()

    print(f'Game over! Player {game.player} won!')
