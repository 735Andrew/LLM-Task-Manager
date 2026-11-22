const form = document.getElementById('loginForm');
const input = document.getElementById('key');
const btn = document.getElementById('submitBtn');
const errorBox = document.getElementById('error');

const KEY_REGEX = /^[A-Za-z0-9_-]{8,255}$/;

const MESSAGES = {
    format:  'Allowed: Latin letters, numbers, "-" and "_" (8–255 characters)',
    invalid: 'Invalid access key',
};

function showError(msg) {
    errorBox.textContent = msg;
    errorBox.hidden = false;
}
function hideError() {
    errorBox.hidden = true;
}

function validate() {
    const value = input.value;
    if (!value) {
        btn.disabled = true;
        hideError();
        return false;
    }
    if (!KEY_REGEX.test(value)) {
        btn.disabled = true;
        showError(MESSAGES.format);
        return false;
    }
    btn.disabled = false;
    hideError();
    return true;
}

input.addEventListener('input', validate);

window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const err = params.get('error');
    if (err && MESSAGES[err]) {
        showError(MESSAGES[err]);
    }
});

form.addEventListener('submit', (e) => {
    if (!validate()) {
        e.preventDefault();
    }
});