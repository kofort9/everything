//if the last element of the question is a question mark answer

function chooseResponse(){

	var responses = ['It is certain',
					'It is decidedly so',
					'Without a doubt',
					'Yes definitely',
					'You may rely on it',
					'As I see it, yes',
					'Most likely',
					'Outlook good',
					'Yes',
					'Signs point to yes',
					'Reply hazy try again',
					'Better not tell you now',
					'Cannot predict now',
					'Concentrate and ask again',
					'Do not count on it',
					'My reply is no',
					'My sources say no',
					'Outlook not so good',
					'Very doubtful'];

	
	var randomNum =
		Math.random() *response.length;
		randomNumber = Math.floor(randomNumber);
	var selectedResponse = responses[randomNumber];

			//alert(selectedResponse);
	var eightBall = $('div#the8ball');
	eightBall.text(selectedResponse);


function askAQuestion() {
	// body...
	var question = $('input');
	var questionText= question.text(text);

	var arrayofwords = questionText.split(" ");
	var lastWord = arrayofwords[arrayofwords.length];

	if (lastWord.lastindexof('?') < 0){

		chooseResponse();




	}else{
		return;
	}
}




// function setupEverything(){

// 	 var button = $('button#ask');
// 	 button.on('click', askAQuestion);
// }

//$(document).ready(setupEverything);