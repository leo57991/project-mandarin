import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Canvas
if '<canvas id="global-ascii-bg"></canvas>' not in html:
    html = html.replace('<body>', '<body>\n    <canvas id="global-ascii-bg"></canvas>')

# 2. Add CSS
css_to_add = '''
        #global-ascii-bg {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: -1; 
            pointer-events: none;
        }
        #game-container {
            z-index: 10;
        }
'''
if '#global-ascii-bg' not in html:
    html = html.replace('/* 全局 HUD 容器 */', css_to_add + '/* 全局 HUD 容器 */')
    
# 3. Add JS Engine
js_engine = '''
        // --- Ascii Fluid Engine (Pretext Inspired) ---
        let globalAsciiEngine = null;
        class AsciiFluidEngine {
            constructor() {
                this.globalCanvas = document.getElementById('global-ascii-bg');
                if(!this.globalCanvas) return;
                this.globalCtx = this.globalCanvas.getContext('2d', { alpha: false });
                
                this.scratchCanvas = null;
                this.scratchCtx = null;
                this.isScratching = false;

                this.resize();
                window.addEventListener('resize', () => this.resize());
                
                this.numParticles = 25;
                this.particles = [];
                for(let i=0; i<this.numParticles; i++) {
                    this.particles.push({x: this.globalCanvas.width/2, y: this.globalCanvas.height/2});
                }
                
                this.target = {x: this.globalCanvas.width/2, y: this.globalCanvas.height/2};
                
                this.chars = [' ', '.', '-', ':', '=', '+', '*', '#', '%', '龍'];
                this.gridSize = 16;
                this.frameCount = 0;
                
                window.addEventListener('mousemove', (e) => {
                    this.target.x = e.clientX;
                    this.target.y = e.clientY;
                });
                
                this.loop();
            }
            
            resize() {
                this.globalCanvas.width = window.innerWidth;
                this.globalCanvas.height = window.innerHeight;
            }
            
            bindScratch(canvas, ctx) {
                this.scratchCanvas = canvas;
                this.scratchCtx = ctx;
                this.isScratching = true;
            }
            
            unbindScratch() {
                this.isScratching = false;
                this.scratchCanvas = null;
                this.scratchCtx = null;
            }
            
            loop() {
                this.render();
                this.frameCount++;
                requestAnimationFrame(() => this.loop());
            }
            
            render() {
                const spring = 0.25;
                const damp = 0.8;
                this.particles[0].x += (this.target.x - this.particles[0].x) * spring;
                this.particles[0].y += (this.target.y - this.particles[0].y) * spring;
                
                for(let i=1; i<this.numParticles; i++) {
                    this.particles[i].x += (this.particles[i-1].x - this.particles[i].x) * 0.4;
                    this.particles[i].y += (this.particles[i-1].y - this.particles[i].y) * 0.4;
                }

                // Global background fade
                this.globalCtx.fillStyle = '#06060a'; 
                this.globalCtx.fillRect(0, 0, this.globalCanvas.width, this.globalCanvas.height);
                
                this.globalCtx.font = `${this.gridSize}px monospace`;
                this.globalCtx.textAlign = 'center';
                this.globalCtx.textBaseline = 'middle';
                
                let minX = this.globalCanvas.width, maxX = 0, minY = this.globalCanvas.height, maxY = 0;
                for(let p of this.particles) {
                    minX = Math.min(minX, p.x); maxX = Math.max(maxX, p.x);
                    minY = Math.min(minY, p.y); maxY = Math.max(maxY, p.y);
                }
                const radius = 120;
                minX = Math.max(0, minX - radius);
                maxX = Math.min(this.globalCanvas.width, maxX + radius);
                minY = Math.max(0, minY - radius);
                maxY = Math.min(this.globalCanvas.height, maxY + radius);
                
                const startCol = Math.floor(minX / this.gridSize);
                const endCol = Math.ceil(maxX / this.gridSize);
                const startRow = Math.floor(minY / this.gridSize);
                const endRow = Math.ceil(maxY / this.gridSize);
                
                for(let r = startRow; r <= endRow; r++) {
                    for(let c = startCol; c <= endCol; c++) {
                        const cx = c * this.gridSize + this.gridSize/2;
                        const cy = r * this.gridSize + this.gridSize/2;
                        
                        let sum = 0;
                        for(let i=0; i<this.numParticles; i++) {
                            const p = this.particles[i];
                            const dx = cx - p.x;
                            const dy = cy - p.y;
                            const d2 = dx*dx + dy*dy;
                            if(d2 < 15000) {
                                const weight = (1 - (i/this.numParticles)*0.6); 
                                sum += (500 / (d2 + 1)) * weight;
                            }
                        }
                        
                        if(sum > 0.05) {
                            let charIdx = Math.floor(sum * 2);
                            if(charIdx >= this.chars.length) charIdx = this.chars.length - 1;
                            const char = this.chars[charIdx];
                            if(char !== ' ') {
                                this.globalCtx.fillStyle = `rgba(212,175,55,${Math.min(1, sum*0.4)})`;
                                this.globalCtx.fillText(char, cx, cy);
                            }
                        }
                    }
                }
                
                if(this.isScratching && this.scratchCtx && this.scratchCanvas) {
                    this.scratchCtx.globalCompositeOperation = 'destination-out';
                    this.scratchCtx.font = `${this.gridSize}px monospace`;
                    this.scratchCtx.textAlign = 'center';
                    this.scratchCtx.textBaseline = 'middle';
                    
                    const rect = this.scratchCanvas.getBoundingClientRect();
                    const sMinX = Math.max(0, minX - rect.left);
                    const sMaxX = Math.min(this.scratchCanvas.width, maxX - rect.left);
                    const sMinY = Math.max(0, minY - rect.top);
                    const sMaxY = Math.min(this.scratchCanvas.height, maxY - rect.top);
                    
                    const sStartCol = Math.floor(sMinX / this.gridSize);
                    const sEndCol = Math.ceil(sMaxX / this.gridSize);
                    const sStartRow = Math.floor(sMinY / this.gridSize);
                    const sEndRow = Math.ceil(sMaxY / this.gridSize);
                    
                    for(let r = sStartRow; r <= sEndRow; r++) {
                        for(let c = sStartCol; c <= sEndCol; c++) {
                            const localCx = c * this.gridSize + this.gridSize/2;
                            const localCy = r * this.gridSize + this.gridSize/2;
                            
                            const globalCx = localCx + rect.left;
                            const globalCy = localCy + rect.top;
                            
                            let sum = 0;
                            for(let i=0; i<this.numParticles; i++) {
                                const p = this.particles[i];
                                const dx = globalCx - p.x;
                                const dy = globalCy - p.y;
                                const d2 = dx*dx + dy*dy;
                                if(d2 < 15000) {
                                    const weight = (1 - (i/this.numParticles)*0.6); 
                                    sum += (800 / (d2 + 1)) * weight;
                                }
                            }
                            
                            if(sum > 0.1) {
                                let charIdx = Math.floor(sum * 2);
                                if(charIdx >= this.chars.length) charIdx = this.chars.length - 1;
                                const char = this.chars[charIdx];
                                if(char !== ' ') {
                                    this.scratchCtx.globalAlpha = Math.min(1, sum*0.8);
                                    this.scratchCtx.fillText(char, localCx, localCy);
                                }
                            }
                        }
                    }
                    this.scratchCtx.globalAlpha = 1.0;
                    this.scratchCtx.globalCompositeOperation = 'source-over';
                    
                    // Check progress
                    if (this.frameCount % 30 === 0 && !window.scratchSolved) {
                        const imgData = this.scratchCtx.getImageData(0,0, this.scratchCanvas.width, this.scratchCanvas.height);
                        let cleared = 0;
                        for(let i=3; i<imgData.data.length; i+=4) {
                            if (imgData.data[i] < 128) cleared++;
                        }
                        const total = this.scratchCanvas.width * this.scratchCanvas.height;
                        if (cleared / total > 0.3) {
                            window.scratchSolved = true;
                            showSystemMessage('江明的隱藏文字已完全顯現。', 'success');
                            setTimeout(() => {
                                closeScratch();
                                gameState.clues.collected.push('CLUE_JIANGMING_NOTE');
                                const clueObj = {
                                    id: 'CLUE_JIANGMING_NOTE',
                                    isDistorted: false,
                                    name: '江明的絕筆信',
                                    desc: '「我若遇害，必是趙福生所為。他已暗中倒戈，手稿萬不可落入他手。」',
                                    truth: '江明臨死前寫下的血書，直指趙福生是內鬼。'
                                };
                                gameState.clues.details['CLUE_JIANGMING_NOTE'] = clueObj;
                                inventory.push(clueObj);
                                checkAccuseButtonVisible();
                                saveGame();
                                document.getElementById('PUZZLE_NOTE').style.display = 'none';
                                showClueDetail(clueObj);
                            }, 1500);
                        }
                    }
                }
            }
        }
        
        window.onload = () => {
            globalAsciiEngine = new AsciiFluidEngine();
        };
'''

if 'AsciiFluidEngine' not in html:
    html = html.replace('function startGame() {', js_engine + '\n        function startGame() {')

# 4. Modify scratch functions
def replace_func(func_name, new_body, source):
    pattern = re.compile(rf'function {func_name}\([^)]*\)\s*{{.*?^        }}', re.MULTILINE | re.DOTALL)
    return pattern.sub(new_body, source)

open_scratch = '''function openScratchPuzzle() {
            const overlay = document.getElementById('scratch-overlay');
            const canvas = document.getElementById('scratch-canvas');
            scratchCtx = canvas.getContext('2d', { willReadFrequently: true });
            
            scratchCtx.globalCompositeOperation = 'source-over';
            scratchCtx.fillStyle = '#1c1c1c';
            scratchCtx.fillRect(0, 0, canvas.width, canvas.height);
            
            scratchCtx.fillStyle = '#2d2d2d';
            for(let i=0; i<150; i++) {
                scratchCtx.beginPath();
                scratchCtx.arc(Math.random()*canvas.width, Math.random()*canvas.height, Math.random()*40+10, 0, Math.PI*2);
                scratchCtx.fill();
            }

            window.scratchSolved = false;
            overlay.classList.add('active');
            
            if (globalAsciiEngine) {
                globalAsciiEngine.bindScratch(canvas, scratchCtx);
            }
        }'''

close_scratch = '''function closeScratch() {
            const overlay = document.getElementById('scratch-overlay');
            overlay.classList.remove('active');
            if (globalAsciiEngine) {
                globalAsciiEngine.unbindScratch();
            }
        }'''

# We completely remove the old startScratch, scratch, endScratch
start_scratch_remove = r'function startScratch\(e\) \{.*?\}\n'
scratch_remove = r'function scratch\(e\) \{.*?\}\n'
end_scratch_remove = r'function endScratch\(e\) \{.*?\}\n'

html = replace_func('openScratchPuzzle', open_scratch, html)
html = replace_func('closeScratch', close_scratch, html)

html = re.sub(start_scratch_remove, '', html, flags=re.DOTALL)
html = re.sub(scratch_remove, '', html, flags=re.DOTALL)
html = re.sub(end_scratch_remove, '', html, flags=re.DOTALL)


with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
