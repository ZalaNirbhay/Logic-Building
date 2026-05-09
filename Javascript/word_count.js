// Count occurrences of each character
function countCharacters(str) {
  let words={}
  for(ch of str){
    if(words[ch]){
      words[ch]+=1
    }
    else{
      words[ch]=1
    }
  }
  return words
}
console.log(countCharacters("nirbhay"));