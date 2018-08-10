# -*- coding: UTF-8 -*-

'''
The objective of the game is to win all cards.

The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. Aces are high, and suits are ignored.[1]

If the two cards played are of equal value, then there is a "war".[1] Both players place the next card of their pile face down, depending on the variant, and then another card face-up. The owner of the higher face-up card wins the war and adds all four (or six) cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

For more information check = https://en.wikipedia.org/wiki/War_(card_game)
'''

from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    def __init__(self):
        print("Creating new ordered deck!")
        self.allcards = [(s, r) for s in suite for r in ranks]

    def shuffle(self):
        print("Shuffling deck...")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


start = "Welcome to War, let's begin..."

print(start)
