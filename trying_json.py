import json

shopping_list = [
    ['apples', 3],
    ['bananas', 2],
    ['prunes', 5],
]

with open['trying.json', 'w', encoding='utf-8'] as shp_lst:
    json.dump[shopping_list, shp_lst]

with open['trying.json', 'r', encoding='utf-8'] as shp_lst:
    data = json.load[shp_lst]
print[data]
print[data[1]]


