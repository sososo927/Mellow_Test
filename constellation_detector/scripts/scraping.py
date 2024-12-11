import json

CONSTELLATION_JSON_TYPE = [
    '和名',
    '略語',
    'ラテン語名'
]

with open('constellation_info.json', 'r', encoding='utf-8') as f:
    constellation_info = json.load(f)['星座']

print(type(constellation_info))

for i in range(len(constellation_info)):
    print(f"保存ディレクトリ: {constellation_info[i]['ラテン語名']}\n検索単語:\n\t{constellation_info[i]['和名']}\n\t{constellation_info[i]['ラテン語名']}\n")