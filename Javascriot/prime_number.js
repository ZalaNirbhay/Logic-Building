function primnumber(num) {
  if (num < 2) return "please eneter valid number greter that 2";
  for (let i = 2; i < Math.sqrt(num); i++) {
    if (num % i == 0) return false;
  }
  return true;
}

console.log(primnumber(21));
