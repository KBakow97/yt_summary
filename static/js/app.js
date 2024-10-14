document.getElementById('yt-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const url = document.getElementById('yt-url').value;
    const phoneNumber = document.getElementById('phone-num').value;
    const model = document.getElementById('model').value;

    try {
        const response = await fetch('/yt_transcript/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url, phone_num: phoneNumber, model: model })
        });

        const data = await response.json();
        if (data.status === "success") {
            document.getElementById('response-message').textContent = "Message sent: " + data.message;
        } else {
            document.getElementById('response-message').textContent = "Error: " + data.message;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('response-message').textContent = 'Error fetching summary.';
    }
});
