import random

class Card:
    def __init__(self, name, description, consumable):
        self.name = name
        self.description = description
        self.is_consumable = consumable
        
    def use_card(self):
        raise NotImplementedError


class ConsumableCard(Card):
    def __init__(self, name, description):
        super().__init__(name, description, True)
    
    def use_card(self):
        #TODO
        print("consumable")


class WeaponCard(Card):
    def __init__(self, name, description):
        super().__init__(name, description, False)
        
    def use_card(self):
        #TODO
        print("Weapon")


class Unit:
    def __init__(self):
        self.deck = Deck()


class Deck:
    def __init__(self):
        self.deck = []  # list of cards
        self._default_card = WeaponCard("Fist", "TODO",)  # TODO, abstract this here

    def add_card(self, card):
        self.deck.append(card)
        return 0

    def draw_card(self):
        if len(self.deck) == 0:
            return self._default_card  # if empty deck return final card

        return self.deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.deck)


class Combat:
    def __init__(self, player_1, player_2):
        self._player_list = []
        self._player_list.append(player_1)
        self._player_list.append(player_2)

        # Shuffle all decks
        [player.deck.shuffle_deck() for player in self._player_list]
        
        self.active_player = random.choice(self._player_list)
        self.non_active_player_list = [other for other in self._player_list if other != self.active_player]
        
        self._turn_number = 1
        self.discard_pile = []  # TODO
        
    def combat_turn(self):
        self._turn_number += 1
        print("Turn : ", self._turn_number)
        
        current_card = self.active_player.deck.draw_card()
        current_card.use_card()
        
        self.discard_pile.append(current_card)
        
        self.non_active_player_list.append(self.active_player)
        self.active_player = self.non_active_player_list.pop(0)

    def end_game(self):
        pass


#test stuff

p1 = Unit()
p2 = Unit()

c1 = ConsumableCard("Pie", "A freshly baked apple pie")
w1 = WeaponCard("Sword", "A forged weapon the length of your arm")

p1.deck.add_card(c1)
p1.deck.add_card(w1)

p2.deck.add_card(c1)
p2.deck.add_card(w1)
p2.deck.add_card(w1)

test_game = Combat(p1, p2)
