function reverseEachWordInSentence(sentence) {
    let words=sentence.split(' ')
    let revwords=words.map((arr)=>{
        return arr.split('').reverse().join('')
    })
    return revwords.join(" ")
}

sentence="hello i am zala nirbhay"
console.log(reverseEachWordInSentence(sentence));
