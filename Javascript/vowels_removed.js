// Remove vowels from a string
function removeVowels(str) {
    newstr=""
    for(let i=0;i<str.length;i++){
        if(!str[i].match(/[aeiouAEIOU]/g)){
            newstr+=str[i]
        }
    }
    return newstr;
}
console.log(removeVowels("javascript"));