const currentUser = localStorage.getItem('currentUser');
if (!currentUser) {
    window.location.href = '../login/index.html'; // הגנה על העמוד
}

document.getElementById('welcomeMsg').innerText = `שלום, ${currentUser}! בחרו אתגר:`;

document.getElementById('logoutBtn').addEventListener('click', () => {
    localStorage.removeItem('currentUser');
    window.location.href = '../login/index.html';
});