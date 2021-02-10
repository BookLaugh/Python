# ------------------------------- CARD class -----------------------------------------
# 
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.values = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit

# -------------------------------- DECK class --------------------------------------------
class Deck:

	def __init__(self):

		self.all_cards = []

		for suit in suits:
			for rank in ranks:

				created_card = Card(suit,rank)

				self.all_cards.append(created_card)

	def shuffle(self):

		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()

# -------------------------------- PLAYER class ------------------------------------------
class Player:

	def __init__(self,name):

		self.name = name
		self.all_cards = []

	def take_cards(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards)== type([]):
			# list of multipe card objects
			self.all_cards.extend(new_cards)
		else:
			# list of a sinlge card object
			self.all_cards.append(new_cards)


	def __str__(self):
		return 'Player {} has {} cards'.format(self.name,len(self.all_cards))

# -------------------------------- Game Logic ---------------------------------------------
# -------------------------------- Game Setup ---------------------------------------------
print("\n")
print("                                 	                  Welcome to the War Card Game !  ")
print('\n')
print("                              Each player turns up a card at the same time and the player with the higher card takes")
print("                              both cards and puts them face down on the bottom of his stack. If the cards are the")
print("                              same rank,then it is a War -- each player turns up additional card from their stack")
print("                              It will last untill one player wins")
print("\n")

title1 = input("Player1 -- Provide a nickname: ")
print('\n')
title2 = input("Player2 -- Provide a nickname: ")

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())

game_on = True

# ---------------------------------- Game On -------------------------------------------------
round_num = 0

while game_on:

	round_num+=1
	print(f'Round {round_num}')

	if len(player_one.all_cards)== 0:
		print('\n')
		print(f"{title1} , out of cards!  Game is Over!")
		print("")
		print(f"{title2} Wins!")
		game_on = False
		break

	if len(player_two.all_cards)== 0:
		print('\n')
		print(f"{title2} , out of cards!  Game is Over!")
		print("")
		print(f"{title1} Wins!")
		game_on = False
		break

# -------------------------------- Starting a new round -----------------------------------------
	player_one_table = []
	player_one_table.append(player_one.take_cards())

	player_two_table = []
	player_two_table.append(player_two.take_cards())

# --------------------------------- War Instance ------------------------------------------------
	at_war = True
	while at_war:	

		if player_one_table[-1].values > player_two_table[-1].values:

			player_one.add_cards(player_one_table)
			player_one.add_cards(player_two_table)

			at_war = False

		elif player_one_table[-1].values < player_two_table[-1].values:

			player_two.add_cards(player_one_table)
			player_two.add_cards(player_two_table)

			at_war = False

		else:

			print("WAR!")

			if len(player_one.all_cards) < 5:
				print('\n')
				print(f"{title1} wasn't able to declare a WAR!")
				print("")
				print(f"{title2} Wins!")

				game_on = False
				break

			elif len(player_two.all_cards) < 5:
				print('\n')
				print(f"{title2} wasn't able to declare a WAR!")
				print("")
				print(f"{title1} Wins!")

				game_on = False
				break

			else:
				for nums in range(5):
					player_one_table.append(player_one.take_cards())
					player_two_table.append(player_two.take_cards())
			

		

