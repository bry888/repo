$(document).ready(function() {
	$('.grade').hide();

	$('.art-name').mouseenter(function() {
		$(this).addClass('chosen').show("slide", { direction: "right" }, 1000);
	});
	$('.art-name').mouseleave(function() {
		$(this).removeClass('chosen').show("slide", { direction: "right" }, 1000);
	});
	
	$('.art-name').click(function(){
		$(this).next().show();
	});
});