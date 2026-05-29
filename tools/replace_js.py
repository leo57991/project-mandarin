import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace HTML structure
if 'id="text-puzzle-overlay"' in html:
    html = re.sub(
        r'<div id="text-puzzle-overlay">.*?<!-- 結局畫面 -->',
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

        <!-- 結局畫面 -->''',
        html, flags=re.DOTALL
    )

# 2. Replace CSS
if '/* 文字物理謎題 UI */' in html:
    css_new = '''/* 刮刮樂顯影系統 */
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
        }'''
    html = re.sub(
        r'/\* 文字物理謎題 UI \*/.*?(?=/\* HUD & Side Buttons \*/)',
        css_new + '\n\n        ',
        html, flags=re.DOTALL
    )

# 3. Replace JS
js_new = '''// =====================================================
        // 刮刮樂顯影系統 (游龍顯影)
        // =====================================================
        let scratchCtx = null;
        let isScratching = false;
        let scratchSolved = false;

        function openScratchPuzzle() {
            const overlay = document.getElementById('scratch-overlay');
            const canvas = document.getElementById('scratch-canvas');
            scratchCtx = canvas.getContext('2d', { willReadFrequently: true });
            
            // 繪製遮罩層 (像是灰燼或燒焦的紙面)
            scratchCtx.globalCompositeOperation = 'source-over';
            scratchCtx.fillStyle = '#1c1c1c';
            scratchCtx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 畫一些紋理
            scratchCtx.fillStyle = '#2d2d2d';
            for(let i=0; i<150; i++) {
                scratchCtx.beginPath();
                scratchCtx.arc(Math.random()*canvas.width, Math.random()*canvas.height, Math.random()*40+10, 0, Math.PI*2);
                scratchCtx.fill();
            }

            scratchSolved = false;
            overlay.classList.add('active');

            canvas.addEventListener('mousedown', startScratch);
            canvas.addEventListener('mousemove', scratch);
            window.addEventListener('mouseup', endScratch);
            
            // Touch support
            canvas.addEventListener('touchstart', (e) => { e.preventDefault(); startScratch(e.touches[0]); }, {passive: false});
            canvas.addEventListener('touchmove', (e) => { e.preventDefault(); scratch(e.touches[0]); }, {passive: false});
            window.addEventListener('touchend', endScratch);
        }

        function closeScratch() {
            const overlay = document.getElementById('scratch-overlay');
            overlay.classList.remove('active');
            const canvas = document.getElementById('scratch-canvas');
            canvas.removeEventListener('mousedown', startScratch);
            canvas.removeEventListener('mousemove', scratch);
            window.removeEventListener('mouseup', endScratch);
        }

        function startScratch(e) {
            isScratching = true;
            scratch(e);
        }

        function endScratch() {
            isScratching = false;
            if (!scratchSolved) checkScratchProgress();
        }

        function scratch(e) {
            if (!isScratching || scratchSolved) return;
            const canvas = document.getElementById('scratch-canvas');
            const rect = canvas.getBoundingClientRect();
            
            // 計算縮放比例
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            
            let clientX = e.clientX;
            let clientY = e.clientY;
            if (e.touches && e.touches.length > 0) {
                clientX = e.touches[0].clientX;
                clientY = e.touches[0].clientY;
            }
            
            const x = (clientX - rect.left) * scaleX;
            const y = (clientY - rect.top) * scaleY;
            
            scratchCtx.globalCompositeOperation = 'destination-out';
            
            // 筆刷
            scratchCtx.beginPath();
            scratchCtx.arc(x, y, 45, 0, Math.PI * 2);
            scratchCtx.fill();
            
            // 龍火毛邊
            for(let i=0; i<5; i++) {
                scratchCtx.beginPath();
                scratchCtx.arc(x + (Math.random()-0.5)*60, y + (Math.random()-0.5)*60, Math.random()*15+5, 0, Math.PI*2);
                scratchCtx.fill();
            }
        }

        function checkScratchProgress() {
            if (scratchSolved) return;
            const canvas = document.getElementById('scratch-canvas');
            const imageData = scratchCtx.getImageData(0, 0, canvas.width, canvas.height);
            const pixels = imageData.data;
            let transparentCount = 0;
            
            const step = 4 * 16; 
            const totalPixels = Math.floor(pixels.length / step);
            
            for (let i = 3; i < pixels.length; i += step) {
                if (pixels[i] < 128) transparentCount++;
            }
            
            const percent = transparentCount / totalPixels;
            if (percent > 0.55) {
                scratchSolved = true;
                // 全部刮開動畫
                canvas.style.transition = 'opacity 1.5s ease-in-out';
                canvas.style.opacity = '0';
                
                showSystemMessage('已解讀江明的隱藏紙條！');
                
                setTimeout(() => {
                    gainClue('CLUE_JIANGMING_NOTE');
                    canvas.style.opacity = '1';
                    canvas.style.transition = '';
                    closeScratch();
                }, 3500);
            }
        }

        '''

html = re.sub(
    r'// =====================================================\n\s*// 文字物理謎題系統 \(Text Physics Puzzle\).*?(?=function _persistGameEnd\(type\))',
    js_new,
    html, flags=re.DOTALL
)

# 4. Trigger replacement in handleSceneClick
html = html.replace('openTextPuzzle();', 'openScratchPuzzle();')

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
