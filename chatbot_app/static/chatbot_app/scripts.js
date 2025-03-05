function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) {
        alert("Please enter a message.");
        return;
    }

    const chatBox = document.getElementById('chat-box');

    // Display user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = `You: ${userInput}`;
    chatBox.appendChild(userMessageDiv);

    fetch('/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ message: userInput })  // Fix: Use 'message' instead of 'user_message'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server Response:", data);  // Debugging log
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            const botMessageDiv = document.createElement('div');
            botMessageDiv.textContent = `Bot: ${data.bot_response}`;
            chatBox.appendChild(botMessageDiv);
        }
    })
    .catch(error => console.error("Fetch Error:", error));
    
    
    document.getElementById('user-input').value = '';  // Clear input field
}

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
