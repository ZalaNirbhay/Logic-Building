// Find the second smallest number in an array
function secondSmallest(arr) {
    let sortedArr = arr.sort((a, b) => a - b);
return sortedArr[1];
}
console.log(secondSmallest([4, 2, 9, 7, 5]));