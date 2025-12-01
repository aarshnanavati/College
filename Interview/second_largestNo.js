const intArray = [2,8,6,4]
const largestValue=(arr) =>{
    firstLargestValue = Math.max(...arr)
    index = arr.indexOf(firstLargestValue)
    arr.splice(index,1)
    secondLargestValue = Math.max(...arr)
    return(secondLargestValue)
}

console.log(largestValue(intArray))