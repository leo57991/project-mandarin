import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r"assets/bg_", r"assets/bg/bg_"),
    (r"assets/npc_", r"assets/characters/npc_"),
    (r"assets/player_", r"assets/characters/player_"),
    (r"assets/clue_", r"assets/clues/clue_"),
    (r"assets/prop_", r"assets/clues/prop_"),
    (r"assets/dragon_", r"assets/ui/dragon_"),
    (r"assets/bgm.mp3", r"assets/audio/bgm.mp3"),
    (r"assets/sfx/", r"assets/audio/sfx/"),
    (r"assets/\$\{ent.img\}", r"assets/ui/${ent.img}"),
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Paths updated successfully!")
