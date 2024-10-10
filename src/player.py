import random
from src.util import get_card_attr, get_card_rule

class Player:
    def __init__(self, name):
        self.hand_of_cards = []
        self.valid_hand = []
        self.player_id = []
        self.name = name
        
    def output_cards(self):
        print(self.name, "cards: ", self.hand_of_cards)
        
    def act(self, board):
        pass
    
    def react(self, board, id):
        pass

class PlayerRandom(Player):
    
    def act(self):
        card_index = random.randint(0, len(self.hand_of_cards)-1)
        side = random.randint(0, 1)
        card = self.hand_of_cards[card_index]
        self.hand_of_cards.pop(card_index)
        return card, side
    
    def react(self, id):
        react = random.choice([True, False])
        if react:
            card_index = random.randint(0, len(self.hand_of_cards)-1)
            card = self.hand_of_cards[card_index]
            self.hand_of_cards.pop(card_index)
            
        return react
    
class PlayerAlphaRandom(Player):
        
    def act(self):
        card_index = random.randint(0, len(self.hand_of_cards)-1)
        side = random.randint(0, 1)
        card = self.hand_of_cards[card_index]
        self.hand_of_cards.pop(card_index)
        return card, side
    
    def react(self, id):
        react = True
        rule = get_card_rule(id)
        for card in self.hand_of_cards:
            card_attr = get_card_attr(id)
            if card_attr[rule[0]] != rule[1]:
                react = False
                break

        if not react:
            react = random.choice([True, False])
        if react:
            card_index = random.randint(0, len(self.hand_of_cards)-1)
            card = self.hand_of_cards[card_index]
            self.hand_of_cards.pop(card_index)
            
        return react