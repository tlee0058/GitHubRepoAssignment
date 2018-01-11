function name()
{
		var fullname = "Lawrence Turton";
		
		function concat(name){
			return "MR." + name;
			
		}
		return concat(fullname);
}


console.log(name());

function name(fullname)
{
		return full.name.firstname + fullname.lastname;
}
//console.log(name({firstname:"Lawrence", lastname: "Turton"});

//function name(fullname) = var name = function()

function name(fullname)
{
		return 1 + 1;
}
//console.log(name(function(){return "embed";})


function runExpression()
{
	var a = 10;
	function add(b)
	
	{
		
		return a + b;
	};
	
	console.log(
	add(90),
	add(20),
	)
	
}
runExpression();

//constructor:

function Apple(x, y, color, score){
	this.x = x;
	this.y = y;
	this.color = color;
	this.score = score;
}
var apple1 = new Apple(10,20, "red", 200);
var apple2 = new Apple(100, 200, "green", 50);
var apple3 = new Apple(20, 200, "pink", 10);
//run apple1, apple2, apple3 on console

//prototype is shared object with different objects to save memory

function Apple(color, weight){
	this.color = color;
	this.weight = weight;
}
Apple.prototype = {
	this.eat : function(){return "eat the apple";},
	this.throw : function(){return "throw the apple";}
};
var apple1 = new Apple ("red", 99);
var apple2 = new Apple ("green", 109);
var apple3 = new Apple ("yellow", 299);


