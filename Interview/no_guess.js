var sno = 4
var num = Number(prompt('Enter your guess number between 1 to 9:'))
if(num>sno)
    {
        alert("Its too high guess again!!")
    }
else if(num<sno)
    {
        alert("Its too low guess again!!")
    }
else
{
    alert("guess matched!!")
}