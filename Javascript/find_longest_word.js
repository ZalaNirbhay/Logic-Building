// Find the longest word in a sentence
function longestWord(sentence) {
    let words=sentence.split(/[\s!,.?;:]+/);
   return words.reduce((longest,current)=> current.length > longest.length ? current:longest,"")
}
console.log(longestWord("JavaScript is super powerful!"));

    