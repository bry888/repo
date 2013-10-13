$(document).ready(function(){

	$('.toggle').hide();
	
	$('#title').mouseenter(function() {
       $('.toggle').slideDown('fast');
	});
   
	$('#title').mouseleave(function() {
       $('.toggle').slideUp('fast');
	});
	
});