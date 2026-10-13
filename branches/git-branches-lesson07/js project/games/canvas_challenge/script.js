const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreDisplay = document.getElementById('canvasScore');

let score = 0;
let circle = { x: 300, y: 200, radius: 20 };

// ציור העיגול על הקנבס
function drawCircle() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // ניקוי המסך
    ctx.beginPath();
    ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
    ctx.fillStyle = '#ff4757';
    ctx.fill();
    ctx.closePath();
}

// מיקום העיגול מחדש
function moveCircle() {
    circle.x = Math.random() * (canvas.width - circle.radius * 2) + circle.radius;
    circle.y = Math.random() * (canvas.height - circle.radius * 2) + circle.radius;
    drawCircle();
}

// זיהוי לחיצה על העיגול
canvas.addEventListener('mousedown', (e) => {
    const rect = canvas.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;
    
    // חישוב המרחק מהלחיצה למרכז העיגול (משפט פיתגורס)
    const distance = Math.sqrt(Math.pow(clickX - circle.x, 2) + Math.pow(clickY - circle.y, 2));
    
    if (distance <= circle.radius) {
        score += 10;
        scoreDisplay.innerText = score;
        moveCircle();
    }
});

// תזוזה אוטומטית פעם בשנייה (מעלה את רמת הקושי)
setInterval(moveCircle, 1200);
drawCircle();