// function toggleborder(){
// 	$('#poster').toggleClass('border');

// }
// function changeImage(){
// 	var image = $('#poster');
// 	if(image.text() == NYC.jpg){
// 		image.attr('src', '5-East.jpg');
// 	} else{
// 		image.attr('src', 'NYC.jpg');
// 	} 
	

function changeImage(){
	var poster = $('#poster');

	var animalSelect = $('#animals');
	var animalVal =animalSelect.val();

alert(animalVal);
	if (animalVal == 'cat'){
		poster.attr('src', 'cat.jfif');

	} 
	else if (animalVal == 'dog'){
		poster.attr('src', 'dog.jpg');

	}
	else {
		poster.attr('src', 'snake.jpg');
	}
}


function setupEverything(){
	alert('Set up');
	// var button = $('#borderButton');
	// button.on('click', toggleborder);

	// var posterImage = $('#poster');
	// posterImage.on('click', changeImage); 

	var animalSelect = $('#animals');
	animalSelect.on('change', changeImage);
	//alert('Set up');
}

$(document).ready(setupEverything);


