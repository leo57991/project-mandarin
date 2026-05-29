import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove stats from notebook
html = re.sub(r'<div style="margin-top:10px; font-size:12px; color:var\(--ui-gold\)">\s*羈絆：禮貌 \$\{gameState\.rapport\[id\]\.polite\} \| 強硬 \$\{gameState\.rapport\[id\]\.aggressive\}\s*</div>', '', html)

# 2. Modify ending screen calculation
old_ending_stats = """            let rapportHtml = `<div style="margin-top:20px; border-top:2px solid var(--ui-gold); padding-top:10px;">
                <h3 style="color:var(--ui-gold); margin-bottom:10px;">人際羈絆與風格</h3><div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">`;
            
            for (let npc in gameState.rapport) {
                let r = gameState.rapport[npc];
                // 若有解鎖隱藏情報給予特殊標記
                let bonusMark = r.bonusUnlocked ? `<span style="color:#d4c4a8; font-size:12px;">(已解鎖隱藏情報: ${r.bonusUnlocked})</span>` : '';
                rapportHtml += `<div class="eval-item" style="background:rgba(255,255,255,0.05); padding:10px;">
                    <div><strong style="color:var(--ui-gold)">${gameState.npcs[npc].name}</strong> ${bonusMark}</div>
                    <div style="font-size:12px;">禮貌值: ${r.polite} | 強硬值: ${r.aggressive}</div>
                </div>`;
            }
            rapportHtml += `</div></div>`;
            document.getElementById('eval-body').innerHTML += rapportHtml;"""

new_ending_stats = """            let totalPolite = 0;
            let totalAggressive = 0;
            for (let npc in gameState.rapport) {
                totalPolite += gameState.rapport[npc].polite;
                totalAggressive += gameState.rapport[npc].aggressive;
            }
            
            let detectiveStyle = "理智中立派";
            let styleColor = "#d4c4a8";
            let styleDesc = "你在審問過程中拿捏得當，既不咄咄逼人，也不過分軟弱。";
            if (totalPolite > totalAggressive + 2) {
                detectiveStyle = "溫和禮貌派";
                styleColor = "#4CAF50";
                styleDesc = "你善於以禮服人，用溫和的態度卸下嫌疑人的心防。";
            } else if (totalAggressive > totalPolite + 2) {
                detectiveStyle = "鐵血強硬派";
                styleColor = "#F44336";
                styleDesc = "你辦案雷厲風行，用強硬的態度逼迫嫌疑人吐露真相。";
            }
            
            let rapportHtml = `<div style="margin-top:20px; border-top:2px solid var(--ui-gold); padding-top:10px;">
                <h3 style="color:var(--ui-gold); margin-bottom:10px;">探長風格評估</h3>
                <div style="background:rgba(255,255,255,0.05); padding:15px; border-left:4px solid ${styleColor};">
                    <div style="font-size:18px; font-weight:bold; color:${styleColor}; margin-bottom:5px;">【${detectiveStyle}】</div>
                    <div style="font-size:14px; color:#ccc;">${styleDesc}</div>
                    <div style="font-size:12px; color:#888; margin-top:8px;">(總禮貌選項次數: ${totalPolite} | 總強硬選項次數: ${totalAggressive})</div>
                </div>
            </div>`;
            document.getElementById('eval-body').innerHTML += rapportHtml;"""

html = html.replace(old_ending_stats, new_ending_stats)

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
