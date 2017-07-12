
function changeImage(){
	var image= $('#fcp');
	image.attr('src','openedfortune-cookie.jpg');
}
function crackedCookie(){

	fortunes= ['A beautiful smart and loving person will be coming into your life.', 
				'A dubious friend may be an enemy in camouflage.',
				'A feather in the hand is better than a bird in the air.',
				'A fresh start will put you on your way.',
				'A friend asks only for your time not your money.',
				'A friend is a present you give yourself.',
				'A gambler not only will lose what he has, but also will lose what he doesn’t have.',
				'A golden egg of opportunity falls into your lap this month.',
				'A good friendship is often more important than a passionate romance.',
				'A good time to finish up old tasks.'];

	var randomNumber =
		Math.random() *fortunes.length;
		randomNumber = Math.floor(randomNumber);
	var selectedFortune = fortunes[randomNumber];

	var crinkledPaper = $('div#fortune');
	crinkledPaper.text(selectedFortune);

	crinkledPaper.animate({
		width:'500px'}, 1500);
		
}

function setupEverything(){
	
	var changeimg = $('#fcp');
	changeimg.on('click', changeImage);
	changeimg.on('click', crackedCookie);
}

$(document).ready(setupEverything);

