import re

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css = """
        #evidence-selector {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            width: 80vw;
            height: 70vh;
            background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
            border: 3px solid var(--ui-gold);
            z-index: 7000;
            display: none;
            flex-direction: column;
            padding: 40px;
            box-sizing: border-box;
            box-shadow: 0 0 100px rgba(0,0,0,1);
            color: #d4c4a8;
        }
        #evidence-selector .selector-header {
            font-size: 28px;
            text-align: center;
            border-bottom: 2px solid var(--ui-gold);
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-family: 'Noto Serif TC', serif;
        }
        #evidence-selector #evidence-grid {
            flex: 1;
            overflow-y: auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 20px;
        }
        #evidence-selector .menu-btn {
            margin-top: 20px;
            align-self: center;
        }
"""

if '#evidence-selector {' not in html:
    html = html.replace('</style>', css + '\n    </style>')

with open('/Users/leo57/.gemini/antigravity/scratch/mandarin-mystery-adventure/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
