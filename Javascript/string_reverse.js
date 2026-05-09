//first way
function reverseString(str){
    return str.split('').reverse().join('')
}

//second way
function reverseString2(str){
    let rev=""
    for(let i=str.length-1;i>=0;i--){
        rev+=str[i]
    }
    return rev
}

console.log(reverseString2("nirbhay"));
