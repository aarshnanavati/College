const arrNum = [1,2,3,4,5,6,9,10]
const missArray=[];
const MissingValue = (arr) =>{
    const minValue = Math.min(...arr)
    const maxValue = Math.max(...arr)
    for(let i=minValue ; i<maxValue ; i++)
        {
            if(arr.indexOf(i)<0)
                {
                    missArray.push(i)
                }
        }
        return(missArray)
}
console.log(MissingValue(arrNum))