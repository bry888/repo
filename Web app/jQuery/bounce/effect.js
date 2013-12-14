$(document).ready(function(){
    $('.1').click(function(){
        $(this).effect('explode');
    });
	$('.2-1').click(function(){
        $(this).effect('bounce', {times:2}, 200); //twice in 200 miliseconds
    });
	$('.2-2').click(function(){
        $(this).effect('bounce', {times:8}, 600); //twice in 200 miliseconds
    });
	$('.2-3').click(function(){
        $(this).effect('bounce', {times:4}, 600); //twice in 200 miliseconds
    });
	$('.2-4').click(function(){
        $(this).effect('bounce', {times:2}, 400); //twice in 200 miliseconds
    });
	$('.3').click(function(){
        $(this).effect('slide');
    });
});