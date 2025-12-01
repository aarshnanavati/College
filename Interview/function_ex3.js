//take a string as arguement and return capitalized string

function capitalize(str)
{
    return str[0].toUpperCase()+str.slice(1);
}
console.log(capitalize("sunny"));