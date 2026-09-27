const form = document.getElementById("chat_form");
const input = document.getElementById("user_message");
const chatMessages = document.getElementById("chat_messages");


    form.addEventListener("submit", function(event) {

        // Prevent the page from refreshing
        event.preventDefault();

        const text = input.value.trim();

        // Don't send an empty message
        if (text === "") {
            return;
        }


        // Create user's message
        const userMessage = document.createElement("div");

        userMessage.className = "message user_message";

        userMessage.innerHTML = `
            <div class="message_box">
                ${text}
            </div>
        `;

        chatMessages.appendChild(userMessage);


        // Clear input
        input.value = "";


        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;


        // Temporary bot response
        setTimeout(function() {

            const botMessage = document.createElement("div");

            botMessage.className = "message bot_message";

            botMessage.innerHTML = `
                <div class="message_box">
                    🤖 Thank you for your question. 
                    I am checking the available UNIZULU study programmes...
                </div>
            `;

            chatMessages.appendChild(botMessage);

            chatMessages.scrollTop = chatMessages.scrollHeight;

        }, 700);

    });
