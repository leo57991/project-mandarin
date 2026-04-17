# AI Agent Guidelines - Project Mandarin

This document outlines the core technical philosophies and implementations for the "Mandarin Mystery Adventure" project, specifically regarding text rendering and interactive storytelling.

## 1. Text Rendering Engine (Pretext)

All text layout and narrative animations in this project are inspired by or utilize the principles of **Pretext** (see [github.com/chenglou/pretext](https://github.com/chenglou/pretext)).

### Core Implementation
The project uses a custom `TextLayoutEngine` (defined in `index.html`) which handles:
- **Tag-based Styling**: Parsing narrative tags into specialized CSS-animated spans.
- **Nested Tag Support**: Recursively applies styles for strings like `[shake][impact]text[/impact][/shake]`.
- **CJK Line-breaking Rules**: Implements `NO_LINE_START` logic to prevent punctuation from appearing at the start of a line.

### Available Narrative Tags
Future agents should utilize these tags to maintain stylistic consistency:
- `[shake]`: For nervous, lying, or intense dialogue.
- `[ink]`: For clues or names being introduced for the first time.
- `[hint]`: For grammar errors or subtle detective hints.
- `[key]`: For highlighted clues already collected.
- `[crime]`: For death or case-related keywords (blood-red throb).
- `[impact]`: For high-stakes, dramatic final lines (large font, red glow, glitch effect).

## 2. Animation & Sound
- **Typewriter Effect**: Utilize `async function typeWriter(element, rawText)` for all sequential character reveals.
- **Chinese Scramble**: The typewriter reveals characters by flickering through random valid Chinese characters first.
- **Audio Feedback**: Use `AudioManager.play(name)` (typewriter, click, hover, clue, transition) to provide tactile feedback for every user action.

## 3. Visual Parity
Maintain the pixel-art aesthetic and existing layout at all costs. The title screen and opening intro visuals should match the reference version on GitHub (`leo57991.github.io/project-mandarin`).

---
*Note: This file is intended for AI agents to ensure architectural consistency during development.*
