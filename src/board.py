import queue
from .util import create_rank, get_card_rule

class Board:
    
    def __init__(self, initial_ranks=None):
        self.prohibited_hair = []
        self.prohibited_cloth = []
        self.history_card = []
        self.history_player = []
        self.prevent = []
        self.prevent_player = []
        self.num_hands = [5] * 2
        self.rank = queue.Queue()
        
        if initial_ranks:
            for rank in initial_ranks:
                self.rank.put(rank)
        else :
            for i in range(1, 5):
                self.rank.put(rank)
        
    def add_hair_rule(self, num):
        if num not in self.prohibited_hair:
            self.prohibited_hair.append(num)
            
    def add_cloth_rule(self, num):
        if num not in self.prohibited_cloth:
            self.prohibited_cloth.append(num)
            
    def change_rank(self):
        first = self.rank.get()
        second = self.rank.get()
        
        self.rank.put(first)
        self.rank.put(second)
        
    def play_card(self, card_id, side, player_id):
        self.history_player.append(player_id)
        
        if side:
            self.history_card.append(0)
        else:
            self.history_card.append(card_id)
                
    def react_card(self, react, pid):
        if react:
            self.prevent.append(1)
            self.prevent_player.append(pid)
        else:
            self.prevent.append(0)
            self.prevent_player.append(-1)
    
    def process_act(self):
        if not self.prevent[-1]:
            card = self.history_card[-1]
            if card == 0:
                self.change_rank()
        
            else:
                info = get_card_rule(card)
                if info[0] == 0:
                    self.add_hair_rule(info[1])
                else:
                    self.add_cloth_rule(info[1])
            
                
    def check_winner(self, p1, p2):
        card_rank = self.get_card_rank()
        p1_rank = 5
        p2_rank = 5
        for i, sublist in enumerate(card_rank):
            for card in sublist:
                if card in p1.hand_of_cards:
                    p1_rank = i
                if card in p2.hand_of_cards:
                    p2_rank = i
        
        if p2_rank < p1_rank:
            return 2
        else:
            return 1
            
    def output_board(self):
        print("current ranks   : ", list(self.rank.queue))
        print("prohibited hair : ", self.prohibited_hair)
        print("prohibited cloth: ", self.prohibited_cloth)
        
    def get_card_rank(self):
        return create_rank(rank=self.rank, p_cloth=self.prohibited_cloth, p_hair=self.prohibited_hair)
        