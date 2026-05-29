import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update getNPCDialogueNode
new_get_node = """function getNPCDialogueNode(npcId) {
            const npc = gameState.npcs[npcId];

            if (npcId === 'CHEN_AFAR') {
                if (npc.round3Done) return 'CHEN_5_IDLE';
                if (npc.round1Done) return 'END';
                return 'START';
            }
            if (npcId === 'ZHAO') {
                if (npc.round1Done) return 'END';
                return 'START'; 
            }
            if (npcId === 'BARONESS') {
                if (npc.round1Done) return 'END';
                return 'START';
            }
            if (npcId === 'FANG') {
                if (npc.round4Done) return 'FANG_5_IDLE';
                if (gameState.npcs['CHEN_AFAR'].round4Done && gameState.npcs['ZHAO'].round3Done && !npc.round4Done) {
                    return 'FANG_4';
                }
                if (npc.round1Done) return 'END';
                return 'START';
            }
            return 'START';
        }"""

html = re.sub(r'function getNPCDialogueNode\(npcId\) \{.*?\n        \}(?=\n\n        function startDialogue)', new_get_node, html, flags=re.DOTALL)

# 2. Update the roundMap logic in renderDialogueNode
old_roundMap_logic = """if (roundMap[nodeId]) {
                            gameState.npcs[npcId][roundMap[nodeId]] = true;
                        }"""

new_roundMap_logic = """if (roundMap[nodeId]) {
                            if (choice.isCorrect !== false) {
                                gameState.npcs[npcId][roundMap[nodeId]] = true;
                            }
                        }"""

html = html.replace(old_roundMap_logic, new_roundMap_logic)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
