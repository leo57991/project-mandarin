# Linguistic Detective: Snow Country Train
# 語境偵緝：雪國列車

![Game Title Screen](assets/bg_title_pixel.png)

## Overview

A browser-based Mandarin Chinese grammar learning game set aboard a murder mystery train in 1899. The game teaches four target grammar points through a consequence-based feedback mechanic: grammatical errors made during NPC dialogue and investigation silently corrupt clues, altering the narrative toward one of five distinct endings.

Designed and built as a final project for **[Course Name]**, **[Your University]** (2026).

**Live Demo**: [https://leo57991.github.io/project-mandarin/](https://leo57991.github.io/project-mandarin/)

---

## Instructional Design Rationale

### The Problem
Conventional Mandarin grammar instruction relies heavily on explicit error correction — learners are immediately told when they are wrong. This approach reduces the communicative pressure that motivates grammar accuracy in real language use.

### The Design Response
This game employs **implicit negative feedback embedded in narrative consequences**: incorrect grammar choices do not trigger error messages, but instead subtly misdirect the investigation. Learners must infer the causal link between their language choices and narrative outcomes — approximating the stakes of real communicative failure.

### Target Grammar Points
1. **Honorifics & Politeness (敬語)** — Strategic use of formal vs. informal address in investigative contexts.
2. **Temporal Adverbs (時間副詞)** — Precision in establishing alibis through accurate temporal marking.
3. **Spatial Prepositions (空間方位詞)** — Grammatical accuracy in describing exact locations of crucial evidence.
4. **Syntactic Word Order (語序)** — Mastery of standard Mandarin sentence structures to decode narrative intent.

### Key Mechanics
- **Branching narrative with 5 endings**: The final outcome is determined by the accumulation of grammatical choices throughout the play.
- **NPC rapport system**: Dialogue options expand or contract based on prior interaction quality, incentivizing grammatical accuracy as a social strategy.
- **Evaluation Report UI**: Post-game feedback surfaces the grammar decisions that shaped the outcome, making implicit consequences explicit at the reflection stage.

---

## Development Approach

Instructional design, narrative structure, grammar point selection, and all pedagogical decisions were authored by **[Your Name]**. Code implementation was developed through an AI-assisted workflow, with the author directing all functional specifications and reviewing outputs iteratively.

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
- **語境物理謎題**：獨創的「文字物理引擎」，玩家需要透過物理碰撞將打亂的字元歸位，重組關鍵線索。
- **動態對話系統**：具備排版引擎與文字特效，支援中文避頭尾排列，提供視覺小說般的閱讀體驗。
- **偵探評鑑系統**：根據您的調查細節與語法精確度，在結局獲得專屬的偵探等級評鑑。

### 🕹️ 操作指南

- **移動視角**：使用鍵盤 `A` / `D` 鍵左右橫移。
- **互動調查**：使用滑鼠點擊場景中的人物 (NPC) 或閃爍的物件。
- **文字謎題**：使用滑鼠推動文字方塊，將其撞入正確的語序空格中。
- **開發者模式**：按下鍵盤 `~` (反引號) 可開啟座標追蹤與極速移動模式。
