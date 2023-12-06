import cards
import games

class BJCard(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJDeck(cards.Deck):
    def populate(self):
        # 블랙잭 카드로 덱 채우기
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))

class BJHand(cards.Hand):
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        # 플레이어의 핸드와 합계를 출력하되, 합계가 있는 경우 표시
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # A를 고려하여 핸드의 합계 계산
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value

        contains_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        # 핸드가 버스트인지 확인 (합계가 21을 초과하는지)
        return self.total > 21

class BJPlayer(BJHand):
    def is_hitting(self):
        # 플레이어에게 히트 또는 스탠드 여부 묻기
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

class BJDealer(BJHand):
    def is_hitting(self):
        # 딜러의 합계가 17 미만이면 히트
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        # 딜러의 첫 번째 카드를 뒤집기
        first_card = self.cards[0]
        first_card.flip()

class BJGame(object):
    def __init__(self, names):
        # 플레이어, 딜러 및 덱을 포함하여 블랙잭 게임 초기화
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)

        self.dealer = BJDealer("Dealer")

        self.deck = BJDeck()
        self.deck.populate()

    @property
    def still_playing(self):
        # 게임에 아직 참여 중인 (버스트되지 않은) 플레이어 목록 가져오기
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        # 플레이어가 스탠드하거나 버스트할 때까지 추가 카드 제공
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def new_deck(self):
        # 새로운 덱 만들기, 채우기 및 섞기
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # 블랙잭 한 판 진행
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()       
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()   

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # 판이 끝난 후 핸드 초기화
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter the player name: ")
        names.append(name)

    print()

    game = BJGame(names)

    again = None
    while again != "n":
        game.play()
        game.new_deck()
        again = games.ask_yes_no("\nDo you want to play again?: ")

main()
input("\n\nPress the enter key to exit.")
