from collections import deque
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
card_info_path = os.path.join(current_dir, '..', 'data', 'card_info.json')

with open(card_info_path, 'r') as file:
    card_info = json.load(file)
    
def is_sublist_in_list(two_element_list, list_of_four_element_lists):
    return any(two_element_list == four_element_list[:2] for four_element_list in list_of_four_element_lists)

def create_rank(rank, p_hair, p_cloth):
    card_rank = []
    
    for _ in range(5): # chara loop
        temp_list = []
        current_chara = rank.get()
        
        for hair in range(1, 6): # hair loop
            for cloth in range(1, 6): # cloth loop
                if (hair not in p_hair and cloth not in p_cloth):
                    if is_sublist_in_list([hair, cloth], card_info[current_chara-1]):
                        id = current_chara * 10 + cloth
                        temp_list.append(id)
                    
        rank.put(current_chara)
        card_rank.append(temp_list)
    
    return card_rank

# rule[0]: hair(0)/cloth(1), rule[1]: prohibit id
def get_card_rule(id):
    chara = id // 10 -1
    cloth = id % 10 -1
    return card_info[chara][cloth][2:]

# attr[0]: hair id, attr[1]: cloth id
def get_card_attr(id):
    chara = id // 10 -1
    cloth = id % 10 -1
    return card_info[chara][cloth][:2]

def test_n_battle(p1, p2, n):
    from src.game_organizer import GameOrganizer
    count_results = [0, 0]
    for _ in range(n):
        game = GameOrganizer(p1, p2, showResult=False)
        count_results[game.progress()] += 1
        
    print(f"{p1.name}: {count_results[0]} win")
    print(f"{p2.name}: {count_results[1]} win")