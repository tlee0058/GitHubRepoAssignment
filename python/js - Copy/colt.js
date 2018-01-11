var p1 = document.querySelector("#p1");
var p2 = document.querySelector("#p2");
var reset = document.querySelector("reset");
var numInput = document.querySelector("input");
var wsDisplay = document.querySelector("p span");
var p = document.querySelector("p");
var score = 0;
var score2 = 0;
var h1s1 = document.querySelector("#h1s1");
var h2s2 = document.querySelector("#h2s2");
var gameOver = false; //not ended in the beginning
var winningScore = 5;


p1.addEventListener("click", function(){
	if(!gameOver){
		score++;
		if(score === winningScore){
			h1s1.classList.add("winner");
		gameOver = true}
h1s1.textContent = score;}});

p2.addEventListener("click", function(){
	if(!gameOver){
		score2++;
		if(score2 === winningScore){
		gameOver = true}
h2s2.textContent = score2;}});
	
reset.addEventListener("click", function(){
		p1 = 0;
		p2 = 0;
		h1s1.textContent = 0;
		h2s2.textContent = 0; //or equals to h2s2
		p1s1.classList.remove("winner");
		p2s2.classList.remove("winner");
		gameOver = false;
});

function resetbutton(){
	p1 = 0;
	p2 = 0;
	h1s1.textContent = 0;
	h2s2.textContent = 0;
	h1s1.classList.remove("winner");
	h2s2.classList.remove("winner");
	gameOver = false;
}

numInput.addEventListener("change", function(){
	wsDisplay.textContent = numInput.value;
	winningScore = Number(numInput.value);
	reset();

});
	


	
	





		







		
		
	

	

