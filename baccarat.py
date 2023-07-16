import random

class Baccarat:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.player = []
        self.banker = []

    def deal(self):
        self.player.append(self.deck.pop())
        self.banker.append(self.deck.pop())


    def score(self, hand):
        t = sum(hand)
        if t > 10:
            t = t % 10
        return t

    def play(self):
        self.deal()
        player_score = self.score(self.player)
        banker_score = self.score(self.banker)

        print(f"Player hand: {self.player} ({player_score})")
        print(f"Banker hand: {self.banker} ({banker_score})")

        if player_score in [8, 9]:
            print("Player wins with a natural!")
            return
        elif banker_score in [8, 9]:
            print("Banker wins with a natural!")
            return

        if player_score <= 5:
            self.player.append(self.deck.pop())
        if banker_score <= 5:
            self.banker.append(self.deck.pop())

        player_score = self.score(self.player)
        banker_score = self.score(self.banker)

        print(f"Player hand: {self.player} ({player_score})")
        print(f"Banker hand: {self.banker} ({banker_score})")

        if player_score > banker_score:
            print("Gratz! Player wins!")
        elif player_score < banker_score:
            print("Banker wins!")
        else:
            print("Tie!")

game = Baccarat()
game.play()
