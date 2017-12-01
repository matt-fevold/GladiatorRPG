import random


class Card:
    def __init__(self, name, description, consumable, is_damage, damage_amount, is_heal, heal_amount, card_asset):  # TODO add kwargs
        self.name = name
        self.description = description
        self.is_consumable = consumable
        self.is_damage = is_damage
        self.is_heal = is_heal
        self.card_asset = card_asset

        self.damage_amount = damage_amount
        self.heal_amount = heal_amount
        
    def use_card(self, player, enemy):
        if self.is_damage:
            enemy.stats.health -= self.damage_amount
        if self.is_heal:
            player.stats.health += self.heal_amount


class ConsumableCard(Card):
    def __init__(self, name, description, heal_amount, asset):
        super().__init__(name, description, True, False, 0, True, heal_amount, asset)


class Stats:
    def __init__(self, level=0, health=10, _class=None):
        self.level = level
        self.health = health
        self._class = _class


class WeaponCard(Card):
    def __init__(self, name, description, damage_amount, asset):
        super().__init__(name, description, False,  True, damage_amount, False, 0, asset)


class Inventory:
    def __init__(self):
        self.currency = 0


class Unit:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.stats = Stats()
        self.inventory = Inventory()


class Slave(Unit):
    def __init__(self, name):
        super().__init__(name)


class Gladiator(Unit):
    def __init__(self, name):
        super().__init__(name)


class Deck:
    def __init__(self):
        self.deck = []  # list of cards
        self._default_card = WeaponCard("Fist", "TODO", .5, "TODO")  # TODO, abstract this here

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


# Test Stuff

p1 = Gladiator("Me")
p2 = Slave("You")

c1 = ConsumableCard("Pie", "A freshly baked apple pie", 2, "TODO")
w1 = WeaponCard("Sword", "A forged weapon the length of your arm", 2, "TODO")

p1.deck.add_card(c1)
p1.deck.add_card(w1)

p2.deck.add_card(c1)
p2.deck.add_card(w1)
p2.deck.add_card(w1)

test_game = Combat(p1, p2)
