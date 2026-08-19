# Linguistic Detective: Snow Country Train
# 語境偵緝：雪國列車

![Game Title Screen](assets/bg/bg_title_pixel.png)

## Overview

A browser-based Mandarin Chinese grammar learning game set aboard a murder mystery train in 1899. The game teaches four target grammar points through a consequence-based feedback mechanic: grammatical errors or impolite tones made during NPC dialogue cause suspects to withhold vital context, leading the player's investigation toward one of six distinct endings.

**Live Demo**: [https://leo57991.github.io/project-mandarin/](https://leo57991.github.io/project-mandarin/)

---

## Instructional Design Rationale

### The Problem
Conventional Mandarin grammar instruction relies heavily on explicit error correction — learners are immediately told when they are wrong. This approach reduces the communicative pressure that motivates grammar accuracy in real language use.

### The Design Response
This game employs **implicit negative feedback embedded in narrative consequences**: incorrect grammar choices or aggressive tones do not trigger explicit error messages, but instead offend NPCs, causing them to immediately terminate the conversation and withhold vital background context. Without this crucial information, players are led into investigative blind spots. Learners must infer the causal link between their language choices and narrative outcomes — approximating the stakes of real communicative failure.

### Target Grammar Points
1. **Honorifics & Politeness (敬語)** — Strategic use of formal vs. informal address in investigative contexts.
2. **Temporal Adverbs (時間副詞)** — Precision in establishing alibis through accurate temporal marking.
3. **Spatial Prepositions (空間方位詞)** — Grammatical accuracy in describing exact locations of crucial evidence.
4. **Syntactic Word Order (語序)** — Mastery of standard Mandarin sentence structures to decode narrative intent.

### Key Mechanics
- **Physical Evidence Collection**: All clues are 100% objective physical items found in the environment. There are no "false clues" — the challenge lies in extracting the correct context from suspects.
- **Branching narrative with 6 endings**: The final outcome is determined by the accumulation of grammatical choices. A single grammar error alienates a specific NPC leading to a dedicated bad ending, while multiple errors result in the player being kicked off the train.
- **NPC rapport system**: Dialogue options expand or contract based on prior interaction quality, incentivizing grammatical accuracy and polite tone as a social strategy.
- **Evaluation Report UI**: Post-game feedback surfaces the grammar decisions that shaped the outcome, offering dynamic hints based on the player's specific failure point.

---

## Development Approach

Instructional design, narrative structure, grammar point selection, and all pedagogical decisions were authored by **[Leo Guan]**. Code implementation was developed through an AI-assisted workflow, with the author directing all functional specifications and reviewing outputs iteratively.

**Tech stack**: 
- **Core**: Vanilla JavaScript (ES6+), HTML5 Canvas
- **Style**: CSS3 (Custom Seamless Side-scrolling Engine)
- **Audio**: Web Audio API
- **Text**: Custom Pretext-Lite Text Layout Engine (Supports CJK line-breaking)

---

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/leo57991/project-mandarin.git
   ```
2. Start a local server in the root directory:
   ```bash
   # Using Python
   python3 -m http.server 8765
   ```
3. Open your browser and visit: `http://localhost:8765`

---

## 關於本遊戲 (中文說明)

這是一款以 1899 年冬天的雪國列車為背景的橫捲軸偵探解謎遊戲。玩家將扮演「林探長」，在列車抵達終點站前，透過與乘客交談、搜集證據以及破解語法謎題，揪出隱藏在陰影中的兇手。

### 🌟 遊戲特色

- **沉浸式橫捲軸世界**：精美的等角透視 (Isometric) 視覺風格，支援無縫場景切換。
- **客觀物理證據**：遊戲中沒有「假線索」，所有的證據都是 100% 真實的物理物件。真正的挑戰在於使用正確的語法與禮貌的語氣，從嫌疑人口中套出線索背後的真相。
- **文字流體解謎**：獨創的「文字游龍（ASCII Metaball）」引擎，利用滑鼠的物理慣性與引力場進行顯影互動，重組關鍵線索。
- **多重分支結局**：包含 1 個真結局與 5 個壞結局。錯誤的語法會導致交涉破裂，並導向錯怪不同無辜者的結局。
- **偵探評鑑系統**：根據您的調查細節與溝通手腕，在結算畫面動態生成專屬的偵探等級評鑑與調查盲點提示。

### 🕹️ 操作指南

- **移動視角**：使用鍵盤 `A` / `D` 鍵左右橫移。
- **互動調查**：使用滑鼠點擊場景中的人物 (NPC) 或閃爍的物件。
- **文字謎題**：使用滑鼠推動文字方塊，將其撞入正確的語序空格中。
- **展示控制台 (Demo Mode)**：按下鍵盤 `Shift + D` 可隨時呼叫簡報專用的展示面板，支援一鍵獲取證據、瞬間傳送以及強制切換真假結局。
- **開發者模式**：按下鍵盤 `~` (反引號) 可開啟座標追蹤與極速移動模式。
