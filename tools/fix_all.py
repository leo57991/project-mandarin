import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject HTML for the new modal
modal_html = """
        <!-- 獨立線索彈窗 -->
        <div id="clue-modal-overlay" onclick="this.style.display='none'">
            <div id="clue-modal-container" onclick="event.stopPropagation()">
                <div class="close-btn" style="position:absolute; top:15px; right:15px;" onclick="document.getElementById('clue-modal-overlay').style.display='none'">×</div>
                <h3 id="clue-modal-title" style="color:var(--ui-gold); margin-top:0; font-size:24px; border-bottom:1px solid rgba(212,175,55,0.3); padding-bottom:10px;"></h3>
                <div id="clue-modal-desc" style="font-size:16px; line-height:1.6; color:#ddd; margin-top:15px;"></div>
            </div>
        </div>

        <audio id="bgm" loop>"""
html = html.replace('<audio id="bgm" loop>', modal_html)

# 2. Inject CSS for the new modal
modal_css = """
        /* 獨立線索彈窗樣式 */
        #clue-modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 8000;
            display: none;
            justify-content: center;
            align-items: center;
        }
        #clue-modal-container {
            width: 500px;
            background: #1c1c1c;
            border: 2px solid var(--ui-gold);
            padding: 30px;
            box-shadow: 0 0 40px rgba(0,0,0,0.8);
            position: relative;
            border-radius: 8px;
        }
        
        /* 結局畫面 */"""
html = html.replace('/* 結局畫面 */', modal_css)

# 3. Replace showClueDetail
new_show_clue = """async function showClueDetail(clueParam) {
            const modal = document.getElementById('clue-modal-overlay');
            const title = document.getElementById('clue-modal-title');
            const desc = document.getElementById('clue-modal-desc');
            let clue = typeof clueParam === 'object' ? clueParam : inventory.find(i => i.id === clueParam);
            if (!clue) clue = gameState.clues.details[clueParam];
            if (!clue) return;

            modal.style.display = 'flex';
            title.innerText = clue.name || clue.id.replace('CLUE_', '');
            
            let content = clue.desc;
            
            desc.innerHTML = ''; // 清空舊內容
            typeWriter(desc, content);
        }"""

html = re.sub(
    r'async function showClueDetail\(clueParam\) \{.*?\n        \}',
    new_show_clue,
    html, flags=re.DOTALL
)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
