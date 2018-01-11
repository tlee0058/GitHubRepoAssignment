console.log("Hello world"); //hidden in console
document.write("Hi Bitch"); //show on webpage
console.log(200);
console.log(true);
console.log(null);

var num = 10;
console.log(num);

console.log("string", 10.11, true, false, null, undefined, num);

function makeCoffee (sugar, milk) //function is parameter; sugar, milk are arguments//
	{ 
	
	var instructions = "Boil water,";
	instructions += "pour into cup.";
	instructions += "add coffee granules,";
	instructions += "add" + sugar + "spoons of sugar,";
	instructions += "add" + milk + "%milk.";
	return instructions;
	}
console.log(makeCoffee(2,20));

var car = { //define an object//
	color : "red", //a property//
	speed : 200,
	drive : function(){ return "drive";} // a method//
	
	
};

var shoppinglist = [ //define an arrays/list
	"Apple", 
	"Orange",
	"Pear"
	
];

var car = {
	make: "Volvo",
	speed: 160,
	engine: {
		size: 2.0,
		make: "bmw",
		fule: "petrol",
		pistons: [ {maker: "BMW"}, {speed: 200}] //within piston can be another object defined//
	},
	drive: function(){return "dive";} //method can be included in object//
};

var array = [
	"string",
	100,
	["embed", 200],
	{car: "ford"}
	
];


var car = {
	make : "volvo",
	speed : 160,
	engine : {
		size : 2.0,
		make : "BMW",
		fuel : "petrol",
		pistons : [ {maker: "BMW"}, {maker: "BMW"}],
	}
	//drive: function(){return "drive";},//
};


console.log(car)

var array = [
	"string",
	100,
	["embed", 200],
	{car : "ford"}
	//function(){return "drive";}
	];

console.log(array)

//OBJECT STUFF

console.log(car.make); //to grab one of the members
//same as
console.log(car["make"]);
//same as 
//console.log(car.drive()); // run function
console.log(car.engine.pistons[0]);
car["engine"]["pistons"][1];
//car["drive"]();

var pointer = "make";
console.log(car[pointer]);

car.make = "ford"; //to change one of the values
car.model = "V6"; // to add a new members
delete car.color // delete in object







//ARRAY STUFF
console.log(array[0]);
//console.log[4](); //return the functions
a = 10;
console.log(array[a - 5 -2]);

array[0] = "new string";//to modify
array[0] += "concat";
array[5] = "new string" // to add to the 5th elementFromPoint
array.shift(); // delete first item
array.unshift(); //reverse
array.pop(); //delete the last item
array.splice(1,0,"new"); //insert in between (position, how many item to delete, and what to insert//
array.push(200,300,"string")//add to the end

//for loop is when you know how mmany times but not while loop
for(var num =1; num < 6: num = num +1)
{ console.log("I'm counting! The number is", num);
}

var num = 1;
while (num < 6){
	console.log("Im counting! The number is", num);
num = num + 1;}


//break is program immedicately exit the loop, contine is loop end sattement is execute and looping will continue,
// print the first 3 lines then immedicately exit:
var num = 1;
while (num < 6)
{ console.log(I"m counting! The number is", num);
if (num ==3)
{ break;}
num = num + 1;}
//will count from 1 to 5 but forget to say about 3 then force it to skip the rest of that loop and continue from the top of the loop
for (var num = 1; num < 6; num += 1){
	if(num ==3)
	{continue;}
console.log("I'm counting! The number is", num);
}


//once the return statement runs, any subsequent lines of code will not be executed


;

















