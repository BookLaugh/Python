import random 

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

game_on = True	


class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)


class Deck:
	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				self.all_cards.append(Card(suit,rank)) # A list of all 52 cards

	def __str__(self):
		test_card = '' # An empty string just for the beginning
		for card in self.all_cards:
			test_card += '\n' + card.__str__() # Adds each each cars object to the 'test_card'
		return "All cards:" + test_card

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal(self):
		taken_card = self.all_cards.pop()
		return taken_card


class Hand:
	def __init__(self):
		self.cards = [] # Starts with an empty list it holds cards with values
		self.value = 0  # A value of particular object
		self.ace = 0	

	def add_cards(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.ace += 1 # 

	def adjust_for_ace(self):
		if self.value > 21 and 'Ace' in self.cards:
			self.value = self.value - 10
			self.ace -= 1






class Chips:
	def __init__(self):
		self.total = 80 # A starting money that may player have 
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

	
def take_bet(chips):

	while True:
		try:
			chips.bet = int(input("\nHow many chips would you like to bet ? "))
		except ValueError:
			print("Sorry, a bet must be an integer!")
		else:
			if chips.bet > chips.total:
				print("Error, your bet can't exceed your ",chips.total)
			else:
				break

def hit(deck,hand):

	hand.add_cards(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global game_on

	while True:
		x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower()=='h':
			hit(deck,hand) # hit() function defined above to Hit
		elif x[0].lower()=='s':
			print("Player stands. Dealer is playing.")
			game_on = False
		else:
			print("Sorry, please try again.")
			continue
		break	

def show_some(player,dealer):
	print("\nDealer's Hand:")
	print(" <card hidden> ")
	print('',dealer.cards[1])
	print("\nPlayer's Hand:",*player.cards, sep='\n')

def show_all(player,dealer):
	print("\nDealer's Hand:",*dealer.cards, sep='\n')
	print("Dealer's Hand =",dealer.value)
	print("\nPlayer's Hand:",*player.cards, sep='\n')
	print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer busts!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and Player tie! It's a push.")


# ---------------------------------- Game Logic is on on the way :) ---------------------------------

while True:
	# We are gonna print an openning statement
	print("                        Welcome to BlackJack! Get as close to 21 as you can without going over it!")
	print("                         Dealer hits untill he reaches 17. Aces count as 1 or 11.")
	# Create & shuffle the deck, deal two cards to each player

	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_cards(deck.deal())
	player_hand.add_cards(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_cards(deck.deal())
	dealer_hand.add_cards(deck.deal())

	# Setting up the player's chips 

	player_chips = Chips() # remember default value is =80

	take_bet(player_chips)

	show_some(player_hand,dealer_hand) # show cards but dealer's one card is <hidden>

	while game_on: # this variable is from hit_or_stand 

		# To Hit or Stand ?
		hit_or_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		# if player's hand exceeds 21, run player_busts() and break out of loop 
		if player_hand.value>21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	# If player hasn't busted, play Dealer's hand untill Dealer reaches 17
	if player_hand.value<=21:

		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		# show  all cards 
		show_all(player_hand,dealer_hand)

		# run various of winning scenarios

		if dealer_hand.value>21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	# Inform Player of their total chips 
	print("\nPlayer's winnings stand at",player_chips.total)


	# Ask to play again

	new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

	if new_game[0]=='y':
		game_on=True
		continue
	else:
		print("Thanks fro playing!")
		break
