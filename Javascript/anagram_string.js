// Check if two strings are anagrams
function areAnagrams(str1, str2) {
  string1 = str1.split("").sort().join("");
  string2 = str2.split("").sort().join("");
  if (string1 === string2) {
    return true;
  } else {
    return false;
  }
}
console.log(areAnagrams("listen", "silent"));
