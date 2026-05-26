import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_logic = """function showClueDetail(clueId) {
            const detailPanel = document.getElementById('inv-details');
            const title = document.getElementById('clue-detail-title');
            const desc = document.getElementById('clue-detail-desc');
            const clue = inventory.find(i => i.id === clueId);
            if (!clue) return;

            detailPanel.style.display = 'block';
            title.innerText = clue.name || clue.id.replace('CLUE_', '');
            
            let content = clue.desc;
            
            desc.innerHTML = ''; // 清空舊內容
            typeWriter(desc, content);
        }"""

html = re.sub(r'function showClueDetail\(clueId\) \{.*?\n        \}(?=\n\n        function toggleInventory)', new_logic, html, flags=re.DOTALL)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
