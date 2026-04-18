let researchData = {};

// Fetch the JSON data from the root
fetch('/static/../research.json') 
    .then(response => response.json())
    .then(data => {
        researchData = data;
        loadChapter('chapter_1_psychological_framework');
    })
    .catch(error => console.error("Error loading research data:", error));

function loadChapter(chapterKey) {
    const grid = document.getElementById('bento-grid');
    grid.innerHTML = ''; 
    const content = researchData[chapterKey];

    if (chapterKey === 'chapter_6_bibliography') {
        renderBibliography(content, grid);
        return;
    }

    for (const [key, value] of Object.entries(content)) {
        const card = document.createElement('div');
        card.className = 'card';
        let cardHTML = `<h2>${key.replace(/_/g, ' ').toUpperCase()}</h2>`;
        
        for (const [detailKey, detailValue] of Object.entries(value)) {
            if (Array.isArray(detailValue)) {
                cardHTML += `<p><strong>${detailKey.replace(/_/g, ' ')}:</strong></p><ul>`;
                cardHTML += detailValue.map(item => `<li>${item}</li>`).join('');
                cardHTML += `</ul>`;
            } else if (typeof detailValue === 'object') {
                cardHTML += `<ul>`;
                for (const [subKey, subVal] of Object.entries(detailValue)) {
                    cardHTML += `<li><strong>${subKey}:</strong> ${subVal}</li>`;
                }
                cardHTML += `</ul>`;
            } else {
                if (detailKey.includes('interpretation') || detailKey.includes('position')) {
                    cardHTML += `<span class="footer-note">${detailValue}</span>`;
                } else {
                    cardHTML += `<p>${detailValue}</p>`;
                }
            }
        }
        card.innerHTML = cardHTML;
        grid.appendChild(card);
    }
}

function renderBibliography(data, grid) {
    for (const [category, sources] of Object.entries(data)) {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `<h2>${category.replace(/_/g, ' ').toUpperCase()}</h2><ul>${sources.map(s => `<li>${s}</li>`).join('')}</ul>`;
        grid.appendChild(card);
    }
}