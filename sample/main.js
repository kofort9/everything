// Paste the helpful function here:
function addListItem(text){
	// jqueary short cuts 
	var list = $('ul');
	var item = $('<li></li>');
	item.text(text);
	list.append(item);

  // list = document.querySelector('ul');
  // item = document.createElement('li');
  // item.innerText = text;
  // list.appendChild(item);
}

function makeNewItem(){
	var tbox = $('#textBox');
	//document.getElementById('textBox');
	var tboxValue= tbox.val();
	addListItem(tboxValue); 
}
// Now use the function to add elements to the list!
function hide(){
	//alert('CLICKED');

	var fcb = $('#myimg');
	fcb.hide();
}

function show(){
	var fcb = $('#myimg');
	fcb.show();
}

function setBorder(){
	var fcbimg = $('img#myimg');
	fcbimg.addClass('addBorder');
}
function removeBorder(){
	var fcbimg = $('img#myimg');
	fcbimg.removeClass('addBorder');
}

function messAround(){
	var fcbimg = $('img#myimg');
	fcbimg.animate(
	{width: '15px'}, 1500);
	fcbimg.animate(
		{width: '100px'}, 1500);
}
