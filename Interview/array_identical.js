function identical(array)
{
    var first=array[0]

    for(var i=0;i<array.length;i++)
        {
            if(array[i]!=first)
                {
                    return false;
                }
        }
        return true;
}

console.log(identical([10,10,10,10,10]))
console.log(identical([10,20,30,40,50]))
