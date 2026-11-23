const form = document.getElementById('chatForm');
const input = document.getElementById('messageInput');
const btn = document.getElementById('sendBtn');
const errorBox = document.getElementById('error');
const messagesDiv = document.getElementById('messages');

const STORAGE_KEY = 'chat_history';


function validate() {
    const value = input.value;
    if (!value || !value.trim()) {
        btn.disabled = true;
        hideError();
        return false;
    }
    if (value.length > 500) {
        btn.disabled = true;
        showError('Max 500 characters');
        return false;
    }
    btn.disabled = false;
    hideError();
    return true;
}

function showError(msg) {
    errorBox.textContent = msg;
    errorBox.hidden = false;
}

function hideError() {
    errorBox.hidden = true;
}

input.addEventListener('input', validate);


function loadHistory() {
    const history = localStorage.getItem(STORAGE_KEY);
    return history ? JSON.parse(history) : [];
}

function saveHistory(history) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
}

function addMessageToHistory(role, text) {
    const history = loadHistory();
    history.push({
        role,
        text,
        time: new Date().toISOString()
    });
    saveHistory(history);
}


function formatTime(isoString) {
    const date = new Date(isoString);
    return date.toLocaleString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function renderMessage(role, text, time) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;

    const textDiv = document.createElement('div');
    textDiv.className = 'message-text';
    textDiv.textContent = text;

    const timeDiv = document.createElement('div');
    timeDiv.className = 'message-time';
    timeDiv.textContent = formatTime(time);

    msgDiv.appendChild(textDiv);
    msgDiv.appendChild(timeDiv);
    messagesDiv.appendChild(msgDiv);

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function renderHistory() {
    const history = loadHistory();
    history.forEach(msg => renderMessage(msg.role, msg.text, msg.time));
}


form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!validate()) return;

    const messageText = input.value.trim();

    btn.disabled = true;
    btn.textContent = 'Sending...';
    hideError();

    const userTime = new Date().toISOString();
    renderMessage('user', messageText, userTime);
    addMessageToHistory('user', messageText);

    input.value = '';

    try {
        const formData = new FormData();
        formData.append('message', messageText);

        const res = await fetch('/chat/send', {
            method: 'POST',
            body: formData,
        });

        const data = await res.json();

        if (!res.ok) {
            showError(data.error || 'Failed to send');
            btn.disabled = false;
            btn.textContent = 'Send';
            return;
        }

        const assistantTime = new Date().toISOString();
        renderMessage('assistant', data.reply, assistantTime);
        addMessageToHistory('assistant', data.reply);

    } catch (err) {
        showError('Network error. Please try again.');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Send';
        validate();
    }
});


window.addEventListener('DOMContentLoaded', () => {
    renderHistory();
    validate();
});