from .board import Board
from .util import get_card_rule, get_card_attr
import random
    
class GameOrganizer:
    
    def __init__(self, p1, p2, showResult=True):
        self.player1 = p1
        self.player2 = p2
        self.players=(self.player1,self.player2)
        self.board=None
        self.player_turn=self.players[0]
        self.player_not_turn = self.players[1]
        self.disp = showResult
        self.winner = None
        
        random_numbers = random.sample(range(0, 25), 10)
        random_cards = [(num // 5 + 1) * 10 + (num % 5 + 1) for num in random_numbers]
        self.player1.hand_of_cards = random_cards[:5]
        self.player2.hand_of_cards = random_cards[5:]
        self.player1.valid_hand = [1] * 5
        self.player2.valid_hand = [1] * 5
        self.player1.player_id = 0
        self.player2.player_id = 1
    
    def progress(self):
        self.board = Board([1, 2, 3, 4, 5])
        if self.disp:
            self.board.output_board()
            self.show_cards()
            print()
        
        while(1):
            act = False
            react = False
            
            current_player = self.player_turn.player_id
            next_player = self.player_not_turn.player_id
            
            if self.disp:print("Turn is " + self.player_turn.name)
            if len(self.player_turn.hand_of_cards) > 2:
                act = True
                card, side = self.player_turn.act()
            if act and len(self.player_not_turn.hand_of_cards) > 2 and not side:
                react = self.player_not_turn.react(card)
                
            if self.disp and act:
                print(f"play card: {card}, side: {side}")
                
            if self.disp and react:
                if self.disp:print("prevented")

            self.board.play_card(card, side, current_player)
            self.board.react_card(react, next_player)
            self.board.process_act()
            
            if self.disp:
                self.board.output_board()
                self.show_cards()
                print()
            
            if len(self.player1.hand_of_cards) == 2 and len(self.player2.hand_of_cards) == 2:
                winner = self.board.check_winner(self.player1, self.player2)-1
                if self.disp:
                    print(f"Winner is {self.players[winner].name}.")
                break
            else:
                self.switch_player()
                
        return winner
            
    def switch_player(self):
        if self.player_turn == self.players[0]:
            self.player_turn = self.players[1]
            self.player_not_turn = self.players[0]
        else:
            self.player_turn = self.players[0]
            self.player_not_turn = self.players[1]
        
    def show_cards(self):
        self.player1.output_cards()
        self.player2.output_cards()