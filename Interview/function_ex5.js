function factorial(num)
{
    result=1;
    for(var i =2;i<=num;i++)
        {
            result = result*i;
        }
        return result;
}
console.log(factorial(4))