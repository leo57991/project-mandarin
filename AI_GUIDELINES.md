# Mandarin Mystery Adventure (Seamless Side-Scrolling Engine)
## Architecture & CSS Guidelines

### 1. Camera & Player Movement
- This is a continuous seamless scrolling engine (100vw).
- **Background Size**: `100vh` height. The `width` is auto-scaled.
- The `index.html` within `isometric-version/` mounts a container `#world` scaled exactly to `VIEW_H * 2 * 3` (3 segments).
- The camera (`camX`) moves natively according to `Math.floor()` to prevent sub-pixel rendering.

### 2. Entity Proportions and Anchors
#### **Floor Base Anchor (Y-Axis)**
- The floor centerline for the carpet aisle is defined as `--ground-y: 98%`.
- Do **NOT** change this value! All future NPCs and items should be anchored to `top: var(--ground-y)`.
- The CSS `transform: translate(-50%, -100%) scaleX(...)` ensures the entity's **bottom center** touches the 98% line accurately without floating above tables.

#### **Character Height Scaling**
- The standard height for an adult NPC (e.g., Chen A-fa, Zhao) relative to the train carriage background is `65vh`. 
- **Rule**: Set NPC heights to `height: 65vh; width: auto;` in CSS. Do not use absolute pixel widths (`px`), as it breaks immersion on different screen sizes.
- This ensures the heads of characters properly align with the ceiling's hanging gas lamps, and their waists correctly match the table height.

#### **Interactive Items (Props & Evidence)**
- Props like suitcases or dropped evidence should either sit on the floor (`top: var(--ground-y)`) or safely mount onto a specific pixel-fixed coordinate corresponding to a table surface.

*(Generated automatically to ensure consistent rendering for all future UI and NPC additions.)*
