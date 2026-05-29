import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the whole magnetic snapping and instant catch block
old_snapping = """                // --- 磁力吸附輔助 (Magnetic Snapping Assist) ---
                let nearestSlot = null;
                let minDistToSlot = Infinity;
                for (const slot of puzzleState.slotRects) {
                    const occupied = puzzleState.chars.some(o => o !== c && o.locked && o.slotIndex === slot.slotIdx);
                    if (occupied) continue;
                    const sdx = c.x - slot.cx; // 已修正：中心點對中心點
                    const sdy = c.y - slot.cy;
                    const d = Math.sqrt(sdx * sdx + sdy * sdy);
                    if (d < minDistToSlot) {
                        minDistToSlot = d;
                        nearestSlot = slot;
                    }
                }

                if (nearestSlot && minDistToSlot < 65) {
                    // 靠近空格時施加阻尼與強化引力，輔助定位
                    const attractionStrength = (65 - minDistToSlot) / 65;
                    c.vx *= (1 - attractionStrength * 0.4); 
                    c.vy *= (1 - attractionStrength * 0.4);
                    const sdx = nearestSlot.cx - c.x;
                    const sdy = nearestSlot.cy - c.y;
                    c.vx += sdx * 0.12;
                    c.vy += sdy * 0.12;
                }

                // --- 判定吸附 (Remove Speed Gate for Instant Catch) ---
                for (const slot of puzzleState.slotRects) {
                    const occupied = puzzleState.chars.some(o => o !== c && o.locked && o.slotIndex === slot.slotIdx);
                    if (occupied) continue;
                    const sdx = c.x - slot.cx;
                    const sdy = c.y - slot.cy;
                    if (Math.sqrt(sdx * sdx + sdy * sdy) < 55) {
                        if (PUZZLE_CONFIG.answer[slot.slotIdx] === c.text) {
                            c.x = slot.cx;
                            c.y = slot.cy;
                            c.vx = 0; c.vy = 0;
                            c.locked = true; c.slotIndex = slot.slotIdx;
                            c.el.classList.add('locked');
                            slot.el.classList.add('filled');
                            slot.el.innerText = '';
                            _checkPuzzleSolved();
                        } else {
                            c.vx = (Math.random() - 0.5) * 6;
                            c.vy = -3 - Math.random() * 3;
                            slot.el.classList.add('error');
                            setTimeout(() => slot.el.classList.remove('error'), 500);
                            puzzleState.errorCount++;
                            if (puzzleState.errorCount >= 1) {
                                document.getElementById('puzzle-hint-msg').classList.add('visible');
                            }
                        }
                        break;
                    }
                }"""

new_snapping = """                // --- 磁力吸附輔助 (Magnetic Snapping Assist) ---
                const ccx = c.x + (c.el.offsetWidth || 80) / 2;
                const ccy = c.y + (c.el.offsetHeight || 42) / 2;

                let nearestSlot = null;
                let minDistToSlot = Infinity;
                for (const slot of puzzleState.slotRects) {
                    const occupied = puzzleState.chars.some(o => o !== c && o.locked && o.slotIndex === slot.slotIdx);
                    if (occupied) continue;
                    const sdx = ccx - slot.cx;
                    const sdy = ccy - slot.cy;
                    const d = Math.sqrt(sdx * sdx + sdy * sdy);
                    if (d < minDistToSlot) {
                        minDistToSlot = d;
                        nearestSlot = slot;
                    }
                }

                if (nearestSlot && minDistToSlot < 65) {
                    const attractionStrength = (65 - minDistToSlot) / 65;
                    c.vx *= (1 - attractionStrength * 0.4); 
                    c.vy *= (1 - attractionStrength * 0.4);
                    const sdx = nearestSlot.cx - ccx;
                    const sdy = nearestSlot.cy - ccy;
                    c.vx += sdx * 0.15;
                    c.vy += sdy * 0.15;
                }

                // --- 判定吸附 ---
                for (const slot of puzzleState.slotRects) {
                    const occupied = puzzleState.chars.some(o => o !== c && o.locked && o.slotIndex === slot.slotIdx);
                    if (occupied) continue;
                    const sdx = ccx - slot.cx;
                    const sdy = ccy - slot.cy;
                    if (Math.sqrt(sdx * sdx + sdy * sdy) < 40) {
                        if (PUZZLE_CONFIG.answer[slot.slotIdx] === c.text) {
                            c.x = slot.cx - (c.el.offsetWidth || 80) / 2;
                            c.y = slot.cy - (c.el.offsetHeight || 42) / 2;
                            c.vx = 0; c.vy = 0;
                            c.locked = true; c.slotIndex = slot.slotIdx;
                            c.el.classList.add('locked');
                            slot.el.classList.add('filled');
                            slot.el.innerText = '';
                            _checkPuzzleSolved();
                        } else {
                            c.vx = (Math.random() - 0.5) * 8;
                            c.vy = -4 - Math.random() * 4;
                            slot.el.classList.add('error');
                            setTimeout(() => slot.el.classList.remove('error'), 500);
                            puzzleState.errorCount++;
                            if (puzzleState.errorCount >= 1) {
                                document.getElementById('puzzle-hint-msg').classList.add('visible');
                            }
                        }
                        break;
                    }
                }"""

html = html.replace(old_snapping, new_snapping)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
