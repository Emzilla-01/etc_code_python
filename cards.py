# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:34:07 2019

https://en.wikipedia.org/wiki/Texas_hold_%27em
https://en.wikipedia.org/wiki/List_of_poker_hands

unicode_suits = ["♠", "♥", "♦", "♣"]

https://pydealer.readthedocs.io/en/latest/code.html#pydealer.const.POKER_RANKS

	 Hand-ranking categories
    #not in texas hold em #1.1	 Five of a kind # No jokers rn, would be f0==f1==f2==f3==f4 where jokers can be any card

1.2	 Straight flush # f0<f1<f2<f3<f4, s0==s1==s2==s3==s4
1.3	 Four of a kind # f0==f1==f2==f3, f4
1.4	 Full house # f0==f1==f2, f3==f4
1.5	 Flush # s0==s1==s2==s3==s4
1.6	 Straight # f0<f1<f2<f3<f4
1.7	 Three of a kind # f0==f1==f2, f3, f4
1.8	 Two pair # f0==f1, f2==f3, f4
1.9	 One pair # f0==f1, f2, f3, f4
1.10 High card # f0, f1, f2, f3, f4

Arrange the available cards in any manner such that these conditions apply.

Player hand enumeration:
    c0, c1, c2, c2, c4, c5, c6, c7
    
    In texas hold em, there are up to five community cards:
        flop, turn, river
        
    These are considered for each player's scored hand in showdown.
    
    Perhaps we can quickly scan through combinations.

    Value of hand should be coded not to use the order cards in a hand.
@author: orpha
"""

from datetime import datetime as dt
from random import shuffle as rshuf, seed as seed
from getpass import getuser
from copy import copy
#code smell: "data as code"
#we can move this to the constants file, eg: hold_em.constants
seed0 = seed(getuser()+str(dt.utcnow().timestamp()))
#SUITS = ["s", "h", "d", "c"] # unicode_suits = ["♠", "♥", "♦", "♣"]
SUITS = ["♠", "♥", "♣", "♦"]
FACES = [i for i in range(2, 15)]
FACE_NAMES = [
            'A',
            'K',
            'Q',
            'J',
            'T',
            '9',
            '8',
            '7',
            '6',
            '5',
            '4',
            '3',
            '2',
                ] # Please excuse my "code as data".
FACE_NAMES.reverse()
FACES_DICT = {FACE_NAMES.index(c)+2:c
              for c in FACE_NAMES
              }

#muck = list() # this could be obscured

class Deck():
    """
    A fresh deck of cards, shuffled on init.
    todo: seed the shuffle in a harder to predict way
            deck.deal(dest,     # player, community cards
            n=2,                # number of cards dealt, default is 2
            )
    """
    def shuffle(self, seed0=seed0):
        rshuf(self.deck, seed0)        
    def __init__(self, seed0=seed0):
        suits = SUITS
        faces = FACES
        self.deck = [(s, f) for f in faces for s in suits]
        self.shuffle()
#    def deal(self, to=muck, n=1):
#        assert(to in [muck, table, players])
#        pass
#x = d.deal(to=player, n=2)

d = Deck()
h = d.deck[-7:]
sorted(h,key=lambda c: c[0])
#h = [('♣', 9), ('♠', 11), ('♠', 4), ('♠', 7), ('♠', 2), ('♦', 8), ('♠', 10)] # Test case of 7 cards for flush & straight
#h = [('♣', 2), ('♠', 3), ('♠', 4), ('♠', 5), ('♠', 14), ('♦', 8), ('♠', 10)] # Test case- 
h = [('♣', 2, "hand"), ('♠', 3, "table"), ('♠', 4), ('♠', 5), ('♠', 14), ('♦', 5), ('♠', 10)] # Test case- 

key_sort_faces = lambda c: c[1]
key_sort_suits = lambda c: c[0]
strip_chars = ["[", "]", "(", ")"]
#five_high_str_sort = {i:i for i in range(1,15)}
#five_high_str_sort


class Scorer():
    def __init__(self, hand):       
        assert (len(hand) >= 2) and (len(hand) <=7)
        Scorer.hand=hand
        self.has_flush = 0
        self.has_straight = 0
        print(f"Unsorted hand: {self.hand}")
    def score(hand):
        """check position of hand according to all scoring functions"""
        pass
    def flush(self):
        for suit in SUITS:
            if [c[0] for c in Scorer.hand].count(suit) >= 5:
                self.has_flush = 1
                self.flush_list = [c for c in Scorer.hand if c[0] == suit]
                self.flush_list.sort(key= key_sort_faces, reverse=True)
                if len(self.flush_list) > 5:
                    self.flush_list = self.flush_list[:5]
                print(f"{FACES_DICT.get(self.flush_list[0][1])} high flush : {self.flush_list}")
    def straight(self):
        """Right now let's assume there is only one player we are scoring.
        Scoring players uses the highest card in their 2 card hand.
        Defining who wins a hand is the next step after each type of hand is accounted for.
        This makes a bit straight easier to define for now.
        Rules to be defined:
        - 5 cards such that each card is consecutive from highest to lowest face, eg: K,Q,J,T,9
            - exception for the ACE: A,2,3,4,5"""
        flag_5_hi = 0
        self.faces = list({key_sort_faces(c) for c in self.hand})[::-1]
        for f in self.faces:
            possible_range = [i for i in range(f, f-5, -1)]
            if 0 in possible_range:
                continue
            if possible_range == [5,4,3,2,1]:
                possible_range = [5,4,3,2,14]
                flag_5_hi = 1
            #print(f"stra trying: {possible_range}")
            if all([i in self.faces for i in possible_range]):
                self.has_straight = 1
                self.straight_list = sorted(self.hand, key=lambda f : possible_range.index(f[1]) if f[1] in possible_range else f[1] + 13)
                print(f"{self.straight_list[0]} high straight:{self.straight_list}")
                return()        
        #Count descending from ACE as highest, this way highest straight will be ranked as hand
        #include ACE in A,2,3,4,5 but use 5 as highest in this case
    def high_card(self, hand):
        self.high_card_list = copy(sorted(self.hand, key=lambda c: c[1], reverse=1))
        if len(self.high_card_list) > 5:
            self.high_card_list = self.high_card_list[:5]
        print(f"High card: {self.high_card_list[0]}")
    def pair(self, hand):
        pass
        
score = Scorer(h)
dir(score)
score.hand
score.high_card(h)
score.high_card_list
score.flush()
score.flush_list
score.has_flush
score.straight()
    
class Player():
    def __init__(self, pid, bank=100):
        """model of a player who may bet, check, fold, ante"""
        pass
    