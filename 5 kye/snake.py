class SnakesLadders():
    num = 1
    over = False
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.ladder = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
        self.sneak = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

    def check_board(self, player):
        if player == self.player1:
            if self.player1 in self.ladder.keys():
                self.player1 = self.ladder[self.player1]
            elif self.player1 in self.sneak.keys():
                self.player1 = self.sneak[self.player1]
        elif player == self.player2:
            if self.player2 in self.ladder.keys():
                self.player2 = self.ladder[self.player2]
            elif self.player2 in self.sneak.keys():
                self.player2 = self.sneak[self.player2]

    def play(self, die1, die2):
        if self.over:
            return 'Game over!'
        if self.num % 2 != 0:
            self.player1 += die2 + die1
            if self.player1 > 100:
                self.player1 = 100 - (self.player1 - 100)
            self.check_board(self.player1)
            if die1 != die2:
                self.num += 1
            if self.player1 == 100:
                self.over = True
                return 'Player 1 Wins!'
            return f'Player 1 is on square {self.player1}'
        elif self.num % 2 == 0:
            self.player2 += die2 + die1
            if self.player2 > 100:
                self.player2 = 100 - (self.player2 - 100)
            self.check_board(self.player2)
            if die1 != die2:
                self.num += 1
            if self.player2 == 100:
                self.over = True
                return 'Player 2 Wins!'
            return f'Player 2 is on square {self.player2}'


game = SnakesLadders()
print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
