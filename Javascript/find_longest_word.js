// Find the longest word in a sentence
function longestWord(sentence) {
    let words=sentence.split(" ")
   return words.reduce((longest,current)=> current.length > longest.length ? current:longest,"" )
}
console.log(longestWord("Coding is a wonderful experience"));

