function nonReapeatingCharacter(str) {
  let words = {};

    //counting the frequency of each character in the string
  for (let chr of str) {
    if (words[chr]) {
      words[chr] += 1;
    } else {
      words[chr] = 1;
    }
  }

  //first way
//   for (let key of Object.entries(words)) {
//     if (key[1] === 1) {
//       return key[0];
//     }
//   }

 //second way
// for(let chr of str){
//     if(words[chr] === 1){
//         return chr;
//     }
// }

 //third way
for(let key in words){
    if(words[key] === 1){
        return key;
    }}
    //returrning null if there is no non-repeating character
  return null;
}

str = "aabbccdde";
console.log(nonReapeatingCharacter(str));
