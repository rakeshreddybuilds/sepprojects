// // // let name = "Zoro";
// // // let greeting = "hi " + name + " welcome to js";
// // // console.log(greeting);
// // // console.log("hello");

// // // let a = 12;
// // // let b = 22;
// // // console.log(a + b);

// // // Simple intrest Calculator
// // // let principal = 1000;
// // // let rate = 8;
// // // let time = 2;
// // // let interest = (principal * rate * time) / 100;
// // // console.log("Simple Intrest: " + interest);

// // // Swap Two Variables
// // let x = 8;
// // let y = 4;
// // let temp = x;
// // x = y;
// // y = temp;
// // console.log("x = " + x + ", y = " + y);

// // Check Even or Oddd using modulus operator
// // let number = 7;
// // let result = number % 2 === 0 ? "Even" : "ODD";
// // console.log(result);

// // let word = "Bankaii";
// // console.log(word.length);
// // console.log(word.repeat(2));

// // // Comparison Operators
// // let age = 19;
// // console.log(age > 21);
// // console.log(age > 12 && age < 20);

// // User input data

// let username;
// username = window.prompt("Whats your name: ");
// console.log(username);

let username;

document.getElementById("mySubmit").onclick = function(){
  username = document.getElementById("myText").value;
  console.log(username);
  document.getElementById("myH1").textContent = `hello ${username}`;
 
}