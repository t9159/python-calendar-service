const grid = document.getElementById('grid');
const targetDisplay = document.getElementById('targetNum');
const timerDisplay = document.getElementById('timer');
const scoreDisplay = document.getElementById('score');

let numbers = [];
let targetNum = 0;
let score = 0;
let timeLeft = 60;
let gameInterval;

function initGame() {
    for (let i = 1; i <= 100; i++) numbers.push(i);
    numbers.sort(() => Math.random() - 0.5);
    
    numbers.forEach(num => {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.innerText = num;
        cell.addEventListener('click', () => checkNumber(num, cell));
        grid.appendChild(cell);
    });
    
    setNewTarget();
    startTimer();
}

function setNewTarget() {
    const activeCells = Array.from(document.querySelectorAll('.cell:not(.hidden)'));
    if (activeCells.length === 0) {
        endGame("ניצחת! סיימת את כל הלוח!");
        return;
    }
    const randomCell = activeCells[Math.floor(Math.random() * activeCells.length)];
    targetNum = parseInt(randomCell.innerText);
    targetDisplay.innerText = targetNum;
}

function checkNumber(num, cellElement) {
    if (num === targetNum) {
        score += 10;
        scoreDisplay.innerText = score;
        cellElement.classList.add('hidden');
        setNewTarget();
    }
}

function startTimer() {
    gameInterval = setInterval(() => {
        timeLeft--;
        timerDisplay.innerText = timeLeft;
        if (timeLeft <= 0) {
            endGame(`הזמן נגמר! הניקוד שלך: ${score}`);
        }
    }, 1000);
}

function endGame(msg) {
    clearInterval(gameInterval);
    alert(msg);
    window.location.href = '../../dashboard/index.html';
}

initGame();