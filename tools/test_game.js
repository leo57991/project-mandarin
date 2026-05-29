const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('./index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: "dangerously" });

// Mock browser APIs
dom.window.HTMLMediaElement.prototype.play = () => {};
dom.window.HTMLMediaElement.prototype.pause = () => {};
dom.window.requestAnimationFrame = (cb) => setTimeout(cb, 16);
dom.window.localStorage = {
    getItem: () => null,
    setItem: () => {}
};

setTimeout(() => {
    try {
        const window = dom.window;
        const document = window.document;
        
        console.log("Starting game...");
        window.startGame();
        
        console.log("Current scene:", window.currentScene);
        
        // Let's manually add CLUE_MANUSCRIPT_PAGE to inventory
        console.log("Adding CLUE_MANUSCRIPT_PAGE...");
        window.gameState.clues.collected.push('CLUE_MANUSCRIPT_PAGE');
        window.gameState.clues.details['CLUE_MANUSCRIPT_PAGE'] = window.CLUE_TEMPLATES['CLUE_MANUSCRIPT_PAGE'];
        window.inventory.push(window.CLUE_TEMPLATES['CLUE_MANUSCRIPT_PAGE']);
        
        console.log("Calling showClueDetail('CLUE_MANUSCRIPT_PAGE')...");
        window.showClueDetail('CLUE_MANUSCRIPT_PAGE');
        
        const modal = document.getElementById('clue-modal-overlay');
        console.log("Modal display:", modal.style.display);
        
        const title = document.getElementById('clue-modal-title');
        console.log("Modal title:", title.innerText);
        
    } catch(e) {
        console.error("ERROR:", e);
    }
}, 500);
