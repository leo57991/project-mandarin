# Goal Description
Replace the basic canvas scratch-off minigame and the ugly dragon cursor with a "Variable Typographic ASCII" particle system. The mouse will act as an attractor for a swarm of ASCII particles (creating a fluid, dragon-like trail), which will dynamically reveal the secret text underneath as it sweeps across the screen.

## User Review Required
> [!IMPORTANT]
> The current scratch mechanic uses a static cursor and basic canvas erasing. To achieve the "pretext / variable typographic ASCII" look, we will:
> 1. Remove the static `dragon_cursor_small.png`.
> 2. Implement a real-time ASCII particle engine on the canvas.
> 3. The mouse will guide a fluid simulation of ASCII characters (using characters like ` .,-~:;=!*#$@` or even Chinese characters like `一二三四五龍`).
> 4. As these ASCII particles move over the canvas, they will "burn" or "clear" the dark overlay, revealing the hidden Jiang Ming text underneath.
> 
> Does this sound like the "cool" effect you are looking for?

## Proposed Changes

### `index.html`
- **[MODIFY]** HTML Structure: Update `#scratch-container` to remove the static cursor and prepare for a dual-layer canvas system (one for the dark overlay to be erased, one for rendering the ASCII particle dragon).
- **[MODIFY]** CSS: Update `#scratch-overlay` to remove the image cursor. Make the typography of the secret text look more like an authentic hidden message.
- **[MODIFY]** JavaScript: 
  - Remove the old `scratch` drawing logic (the simple arc erasing).
  - Introduce a Particle System class (x, y, vx, vy, life).
  - In `requestAnimationFrame`, update particles to follow the mouse (creating a swirling, dragon-like movement).
  - Render these particles as ASCII characters (changing based on velocity or density).
  - Use these ASCII particles to clear the hidden text overlay (`globalCompositeOperation = 'destination-out'`).

## Verification Plan
1. Open the game, collect the film case, and click the Note puzzle.
2. Verify that moving the mouse creates a beautiful ASCII particle effect following the cursor.
3. Verify that the ASCII particles successfully scratch away the overlay to reveal the secret text.
4. Ensure performance is smooth (60fps) by managing particle counts efficiently.
