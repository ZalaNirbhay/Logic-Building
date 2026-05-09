function missingNumber(arr) {
  let max = Math.max(...arr);
  let missing = [...arr];
  for (let i = 1; i < max; i++) {
    if (!arr.includes(i)) {
      missing.push(i);
    }
  }
  return missing.sort((a, b) => a - b);
}

console.log(missingNumber([4, 7, 55, 8, 65, 25]));

function remover(arr, i) {
  return arr.splice(i, 1);
}

function removeDuplicates(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] == arr[j]) {
        remover(arr, j);
      }
    }
  }

  return arr;
}

console.log(removeDuplicates([1, 1, 2, 2, 5, 1, 2, 8]));

function fbc(n) {
  s = [];

  s.push(1);
  s.push(1);

  for (let i = 2; i < n; i++) {
    s.push(s[i - 1] + s[i - 2]);
  }

  return s.slice(0, n);
}

console.log(fbc(0));
