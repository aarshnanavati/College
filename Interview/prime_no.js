var number = Number(prompt("Enter the number:"))
if(number == 1)
    {
        console.log("number is not prime neither composite")
    }
    else if(number<1)
        {
            console.log("prime number is not possible")
        }
        else
        {
        for(let i =2 ; i<number ; i++)
    {
        if(number %i == 0)
        {
            var result = `${number} is not possible`
        }
        else{
            var result = `${number} is prime`
        }
    }
    console.log(result)
    }