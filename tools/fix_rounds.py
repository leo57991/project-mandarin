import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

round_map_code = """const roundMap = {
                            START: 'round1Done',
                            CHEN_2: 'round2Done', CHEN_3: 'round3Done', CHEN_4: 'round4Done', CHEN_5_IDLE: 'round5Done',
                            ZHAO_2: 'round2Done', ZHAO_3: 'round3Done', ZHAO_4: 'round4Done', ZHAO_5: 'round5Done',
                            BARONESS_2: 'round2Done', BARONESS_3: 'round3Done', BARONESS_4: 'round4Done', BARONESS_5: 'round5Done',
                            FANG_2: 'round2Done', FANG_3: 'round3Done', FANG_4: 'round4Done', FANG_5_IDLE: 'round5Done'
                        };"""

html = re.sub(r'const roundMap = \{.*?\};', round_map_code, html, flags=re.DOTALL)

adv_logic = """
        function advanceDialogueRound(npcId) {
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
html = re.sub(r'function advanceDialogueRound\(npcId\) \{.*?\n        \}', adv_logic.strip(), html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
