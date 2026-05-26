import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix DOM Structure
html = html.replace('<!-- 偵探手札面板 -->', '</div>\n        <!-- 偵探手札面板 -->')
html = html.replace("""                </div>
            </div>


        </div>""", """                </div>
            </div>""")

# 2. Fix handleInterrogation
new_interrogation = """function handleInterrogation(npcId, clueId) {
            toggleEvidenceSelect(false);
            
            const node = dialogueTree[npcId];
            if (node.INTERROGATION && node.INTERROGATION[clueId]) {
                const targetNode = node.INTERROGATION[clueId];
                renderDialogueNode(npcId, targetNode);
            } else {
                dialogueTree[npcId]['_TEMP_FAIL'] = {
                    text: "不好意思，我不太清楚...",
                    choices: [{ text: "（收起證據）", nextNode: "END" }]
                };
                renderDialogueNode(npcId, '_TEMP_FAIL');
            }
        }"""

html = re.sub(r'function handleInterrogation\(npcId, clueId\) \{.*?\n        \}', new_interrogation, html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
