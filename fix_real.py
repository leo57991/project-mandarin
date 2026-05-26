import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the missing scratch-overlay HTML
# We will replace the text-puzzle-overlay completely.
html = re.sub(
    r'<!-- 文字物理謎題面板 -->\s*<div id="text-puzzle-overlay">.*?</div>\s*(?=<!-- 獨立線索彈窗 -->)',
    '''<!-- 刮刮樂顯影面板 -->
        <div id="scratch-overlay">
            <div id="scratch-container">
                <div id="scratch-text-layer">
                    我若遇害，必是趙福生所為。<br>
                    他已暗中倒戈，手稿萬不可落入他手。<br>
                    <br>
                    —— 江明 絕筆
                </div>
                <canvas id="scratch-canvas" width="600" height="400"></canvas>
            </div>
            <button class="menu-btn" style="position:absolute; bottom:40px;" onclick="closeScratch()">放棄調查</button>
        </div>
        
        ''',
    html, flags=re.DOTALL
)

# 2. Fix the missing scratch-overlay CSS
# We replace the text puzzle CSS with scratch overlay CSS
html = re.sub(
    r'/\* ===== 文字物理謎題面板 ===== \*/.*?/\* HUD & Side Buttons \*/',
    '''/* 刮刮樂顯影系統 */
        #scratch-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 7000;
            display: none;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            cursor: url('assets/dragon_cursor.png') 16 16, auto;
        }
        #scratch-overlay.active { display: flex; }
        #scratch-container {
            position: relative;
            width: 600px;
            height: 400px;
            background: #fff8e7;
            border: 2px solid #5c3a21;
            box-shadow: 0 0 50px rgba(255,100,50,0.4);
            overflow: hidden;
            border-radius: 8px;
            cursor: url('assets/dragon_cursor.png') 16 16, auto;
        }
        #scratch-text-layer {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            font-family: 'Noto Serif TC', serif;
            font-size: 26px;
            color: #3e2723;
            line-height: 1.8;
            text-align: center;
            font-weight: bold;
            padding: 40px;
            box-sizing: border-box;
            background-image: url('assets/clue_note_fragment.png');
            background-size: cover;
            background-position: center;
        }
        #scratch-canvas {
            position: absolute;
            top: 0; left: 0;
        }

        /* HUD & Side Buttons */''',
    html, flags=re.DOTALL
)

# 3. Fix the showClueDetail looking up the wrong element
html = html.replace("const desc = document.getElementById('clue-detail-desc');", "const desc = document.getElementById('clue-modal-desc');")

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
