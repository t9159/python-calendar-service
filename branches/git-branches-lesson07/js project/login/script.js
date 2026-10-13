const authForm = document.getElementById('authForm');
const formTitle = document.getElementById('formTitle');
const submitBtn = document.getElementById('submitBtn');
const toggleMode = document.getElementById('toggleMode');
const message = document.getElementById('message');
const div_password_again=document.querySelector(".div_password_again")
let isLoginMode = true;

toggleMode.addEventListener('click', () => {
    isLoginMode = !isLoginMode;
    formTitle.innerText = isLoginMode ? "התחברות למערכת" : "הרשמה למערכת";
    submitBtn.innerText = isLoginMode ? "היכנס" : "הירשם";
    toggleMode.innerText = isLoginMode ? "משתמש חדש? לחץ כאן להרשמה" : "כבר רשום? לחץ כאן להתחברות";
    message.innerText = "";
    const user = document.getElementById('username')
    const pass = document.getElementById('password')
    const password_again=document.getElementById("password_again")
    user.value=""
    pass.value=""
    password_again.value=""
    const div_password_again=document.querySelector(".div_password_again")
    if(!isLoginMode)
      {  div_password_again.style.display='block'
        password_again.required = true;
      }
    else
    {
        div_password_again.style.display='none'
        password_again.required = false;
    }
});

authForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;
    
    let users = JSON.parse(localStorage.getItem('users')) || {};

    if (isLoginMode) {
        if (users[user] && users[user].password === pass) {
            localStorage.setItem('currentUser', user);
            window.location.href = '../dashboard/index.html';
        } else {
            message.innerText = "שם משתמש או סיסמה שגויים!";
        }
    } else {
        if (users[user]) {
            message.innerText = "שם המשתמש כבר קיים במערכת!";
        } else {
            const pass_ag = document.getElementById("password_again")
            if(pass!==pass_ag.value)
            {
                 message.innerText = "אימות נכשל"
            }  
            else{
                users[user] = { password: pass, bestScore: 0 };
                localStorage.setItem('users', JSON.stringify(users));
                message.innerText = "נרשמת בהצלחה! כעת תוכל להתחבר.";
                message.style.color = "lightgreen";
                setTimeout(() => { toggleMode.click(); }, 1500);
            }
        }
    }
});