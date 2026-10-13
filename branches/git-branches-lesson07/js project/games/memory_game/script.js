const board=document.querySelector(".board")
const arr=['🩷','😍','☎️','💎','🎨','👓','🧤','⚽','🧸','🪗','🍕',
    '🧁','🍇','🍉','🌼','🚲','✈️','☔','🌞','🥰','🦒','🐘','🐧','🐥',
    '🐞','🖼️','🛝','🎠','🎁','🪆','🎵','📖','🔦',
    '🐭','🐔','🦩','🦉','🦋','🌮','🍭','🍒','🍂','🚑','🚛','🏠']
let bool_arr=new Array(arr.length).fill(false)
let size=6
let num_of_steps=0
let num_of_pairs=0
let count_opens=[]
let pos=0
let time_passed=0
let gameInterval=0
let mat = Array.from({ length: size }, () => new Array(size).fill(''));
function start_game(new_size){
    time_passed=0
    if(timer)
        timer.innerHTML=""
    time_Passed()
    size=new_size
    board.innerHTML = ""; 
    num_of_steps = 0
    num_of_pairs = 0
    pos = 0
    bool_arr=new Array(arr.length).fill(false)
    board.style.gridTemplateColumns=`repeat(${size}, 1fr)`
    // 3. יצירת מטריצה חדשה בהתאם לגודל שנבחר
    mat = Array.from({ length: size }, () => new Array(size).fill(''));

    let activeFontSize = size === 8 ? "30px" : size === 6 ? "45px" : "60px";
    for(let i=0; i<size; i++)
    {
        for(let j=0; j<size; j++)
        {
            const box=document.createElement("div")
           
            box.style.border="solid black 3px"
            box.style.display = "flex";
            box.style.justifyContent = "center";
            box.style.alignItems = "center";
            box.style.fontSize = "0px";
            board.append(box)
            mat[i][j]=(box)
            box.addEventListener("click", ()=>{
            if(box.style.fontSize==="0px")
            {
                box.style.fontSize = activeFontSize;
                count_opens.push(box)
                pos++
                if(pos===2)
                {
                    num_of_steps++
                    if(count_opens[0].innerText===count_opens[1].innerText)
                    {
                        num_of_pairs++
                        count_opens.forEach(x=>x.style.backgroundColor="red")
                        count_opens=[]
                        pos=0
                       
                            
                            setTimeout(() => {
                            if(num_of_pairs===(size*size)/2){
                                const message = `כל הכבוד! סיימת ב-${num_of_steps} צעדים.`;
                                alert(message);
                            }
                            }, 300);
                        }
                    else{
                        setTimeout(() => {
                            count_opens.forEach(x=>x.style.fontSize="0px")
                            count_opens=[]
                            pos=0
                            }, 600);
                        }
                }}
            })
        
        }
    }
    
    let pict=0
    let r=0
    let c=0
    for(let i=0; i<(size*size)/2; i++)
    {
        pict=Math.floor(Math.random()*(arr.length))
        while (bool_arr[pict])
        {
            pict=Math.floor(Math.random()*(arr.length))
        }
        bool_arr[pict]=true
        let placed=0
        while(placed<2)
        {
            r=Math.floor(Math.random()*(size))
            c=Math.floor(Math.random()*(size))
            if(mat[r][c].innerText==='')
            {
                mat[r][c].innerText=arr[pict]
                placed++
            }
        }
    }
}
document.addEventListener("DOMContentLoaded", ()=>{
    start_game(6)
})
const size4=document.querySelector(".s-4x4")
const size6=document.querySelector(".s-6x6")
const size8=document.querySelector(".s-8x8")
size4.addEventListener("click", ()=>{
    start_game(4)
})
size6.addEventListener("click", ()=>{
    start_game(6)
})
size8.addEventListener("click", ()=>{
    start_game(8)
})
let timer=document.querySelector(".timer")
function time_Passed(){
    clearInterval(gameInterval)
    gameInterval=setInterval(()=>{
        time_passed++
        timer.innerText=`${Math.trunc(time_passed/60)}:${time_passed%60}`
    }, 1000)
}