function uniqueElements(arr) {
  let uniques = [];
  for (elem of arr) {
    if (!uniques.includes(elem)) {
      uniques.push(elem);
    }
  }
  return uniques;
}
console.log(uniqueElements([1, 2, 3, 2, 4, 1, 5]));
