async function sendMail() {
    const recipient = document.getElementById('recipient').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    const type = document.getElementById('emailType').value;
    const loader = document.getElementById('loader');
    const btn = document.getElementById('sendBtn');

    if (!recipient || !subject || !message) {
        alert("Please fill all fields!");
        return;
    }

    // Show loading
    loader.style.display = 'flex';
    btn.disabled = true;

    try {
        const response = await fetch('/send_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                recipient: recipient,
                subject: subject,
                message: message,
                type: type
            })
        });

        const data = await response.json();

        if (data.status === 'success') {
            alert("✅ Success! Email has been sent.");
            // Reset form
            document.getElementById('recipient').value = '';
            document.getElementById('subject').value = '';
            document.getElementById('message').value = '';
        } else {
            alert("❌ Error: " + data.message);
        }
    } catch (error) {
        alert("❌ Connection Error!");
    } finally {
        loader.style.display = 'none';
        btn.disabled = false;
    }
}