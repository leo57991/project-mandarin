import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

get_node_logic = """
        function getNPCDialogueNode(npcId) {
            const npc = gameState.npcs[npcId];

            if (npcId === 'CHEN_AFAR') {
                if (npc.round3Done) return 'CHEN_5_IDLE';
                return 'START';
            }
            if (npcId === 'ZHAO') {
                return 'START'; 
            }
            if (npcId === 'BARONESS') {
                return 'START';
            }
            if (npcId === 'FANG') {
                if (npc.round4Done) return 'FANG_5_IDLE';
                if (gameState.npcs['CHEN_AFAR'].round4Done && gameState.npcs['ZHAO'].round3Done) {
                    return 'FANG_4';
                }
                return 'START';
            }
            return 'START';
        }
"""
html = re.sub(r'function getNPCDialogueNode\(npcId\) \{.*?\n        \}(?=\n\n        function startDialogue)', get_node_logic.strip(), html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
