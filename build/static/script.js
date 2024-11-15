document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('mushroom-form');
    
    form.addEventListener('submit', handleFormSubmit);
});

function handleFormSubmit(event) {
    event.preventDefault(); 

    const formData = new FormData(event.target);

    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
    console.log(data);

    fetch('/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(result => {
        document.querySelector('h2').textContent = result.prediction_text || 'Prediction unavailable.';
    })
    .catch(error => console.error('Error:', error));
}

