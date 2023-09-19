css = '''
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #F5F5F5;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
}

.chat-message {
    margin: 10px 0;
    padding: 10px 20px;
    border-radius: 10px;
    display: flex;
    align-items: flex-start;
    max-width: 70%;
}

.chat-message.user {
    background-color: #E25822 ;
    color: #FFFFFF;
    margin-left: auto;
}

.chat-message.bot {
    background-color: #526D82;
    color: #FFFFFF;
}

.chat-message .avatar {
    width: 30px;
    height: 30px;
    margin-right: 10px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    flex: 1;
}

.user-input {
    width: 100%;
    padding: 10px;
    border: 1px solid #007BFF;
    border-radius: 5px;
    margin-top: 20px;
}

.process-button {
    background-color: #007BFF;
    color: #FFFFFF;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.process-button:hover {
    background-color: #0056b3;
}

/* Add the animation style to the header */
@keyframes color-change {
    0% { color: #ff5733; }
    50% { color: #33ff57; }
    100% { color: #5733ff; }
}

/* Modern header styles */
.header-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #526D82; /* Blue background for header */
    color: #fff; /* White text color */
    padding: 2rem;
    border-radius: 10px; /* Rounded corners on all sides */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Adding a subtle shadow */
    margin-bottom: 75px;
}

.header-title {
    text-align: center;
    font-size: 2.5rem; /* Slightly smaller font size */
    margin-bottom: 1rem; /* A bit more spacing at the bottom */
}

/* Optional: Add a hover effect to the header */
.header-container:hover {
    background-color: #FFD2D7; /* Darker blue on hover */
}



</style>
'''
header_html = '''
<div class="header-container">
    <div class="header-title">Chat with multiple PDFs</div>
</div>
'''

bot_template = '''
<div class="chat-message bot">
    <img class="avatar" src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <img class="avatar" src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    <div class="message">{{MSG}}</div>
</div>
'''

file_upload_interface = '''
<div class="file-upload-container">
    <p>Upload your PDFs here:</p>
    <input type="file" accept=".pdf" multiple>
    <button class="process-button">Process</button>
</div>
'''
