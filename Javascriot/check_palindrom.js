//using string reverse method along with split and join 
function palindromCheck(num){
    let num1 = num.split('').reverse().join('');
    return (num==num1) ? "Yes it is ":"No it's not "
}

console.log(palindromCheck("1221"))