const form = document.querySelector('form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const message = document.querySelector('#message').value;
    const shift = document.querySelector('#shift').value;
    const action = document.querySelector('input[name="action"]:checked').value;

    const response = await fetch(`/${action}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `message=${message}&shift=${shift}`
    });

    const result = await response.text();
    document.querySelector('#output').innerText = result;
});