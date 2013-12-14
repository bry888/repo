$(document).ready(function() {
	$('.table-articles td').mouseenter(function() {
		$(this).addClass('chosen').show("slide", { direction: "right" }, 1000);
	});
	$('.table-articles td').mouseleave(function() {
		$(this).removeClass('chosen').show("slide", { direction: "right" }, 1000);
	});
	
	$('.table-articles td').click(function(){
		$(this).after('<td class=".grade"><div></div><div></div><div></div><div></div><div></div></td>');
	});
});