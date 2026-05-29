import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

adv_logic = """
        function advanceDialogueRound(npcId) {
            const npc = gameState.npcs[npcId];
            const clues = gameState.clues.collected;

            if (npcId === 'CHEN_AFAR') {
                if (clues.includes('CLUE_SCARF')) return 'CHEN_5_IDLE';
                return 'START';
            }
            if (npcId === 'ZHAO') {
                return 'START'; 
            }
            if (npcId === 'BARONESS') {
                return 'START';
            }
            if (npcId === 'FANG') {
                if (gameState.npcs['CHEN_AFAR'].dialogueNode === 'CHEN_4_FOLLOWUP' && gameState.npcs['ZHAO'].dialogueNode === 'ZHAO_3_FOLLOWUP') {
                    return 'FANG_4'; // Wait, dialogueNode might be END.
                }
                
                // Let's rely on clue combinations
                // Chen Round 4 is CLUE_FILM_CASE presented. Zhao Round 3 is CLUE_FILM_CASE presented.
                // It's easier to just check if both clues are collected and maybe use a generic IDLE state.
                if (clues.includes('CLUE_FILM_CASE') && clues.includes('CLUE_SCARF')) return 'FANG_4';
                
                return 'START';
            }
            return 'START';
        }
"""
html = re.sub(r'function advanceDialogueRound\(npcId\) \{.*?\n        \}', adv_logic.strip(), html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
