function updateEntries() {
    const numEntries = document.getElementById('num_entries').value;
    const entriesDiv = document.getElementById('entries');
    entriesDiv.innerHTML = '';

    for (let i = 0; i < numEntries; i++) {
        const entryDiv = document.createElement('div');
        entryDiv.className = 'entry';
        entryDiv.innerHTML = `
            <h3>Entry ${i + 1}</h3>
            <label for="budget_${i}">Advertising Budget with VAT (D):</label>
            <input type="number" step="any" id="budget_${i}" name="budget_${i}" required>
            <label for="clicks_${i}">Projected Clicks (E):</label>
            <input type="number" step="any" id="clicks_${i}" name="clicks_${i}" required>
        `;
        entriesDiv.appendChild(entryDiv);
    }
}

// Initialize entries on page load

document.addEventListener('DOMContentLoaded', () => {
    const resultsSection = document.querySelector('.results-section');
    if (resultsSection) {
        resultsSection.classList.add('fade-in');
    }
});