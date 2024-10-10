import json

# 1:short, 2:two-side, 3:semi-long 4:bob, 5:long
# 1:hensou, 2:yukata, 3:shifuku, 4:mizugi, 5:seifku
# [hair id, cloth id, hair/cloth(0/1), hair/cloth id]
card_info = [
    [[3,1,1,3],[1,2,0,2],[1,3,0,4],[1,4,1,1],[1,5,1,4]],
    [[4,1,1,4],[2,2,1,1],[2,3,1,2],[2,4,0,3],[2,5,0,1]],
    [[2,1,0,5],[3,2,1,5],[3,3,1,1],[3,4,0,1],[3,5,1,2]],
    [[5,1,1,2],[4,2,1,3],[4,3,1,5],[4,4,0,2],[4,5,0,5]],
    [[1,1,1,5],[5,2,1,4],[5,3,0,3],[5,4,1,3],[5,5,0,4]]
]

with open('card_info.json', 'w') as file:
    json.dump(card_info, file)
