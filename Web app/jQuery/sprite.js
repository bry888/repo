$(document).ready(function() {
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
			case 65:
				$('img').animate({left: "-=10px"}, 'fast');
				break;
			case 83:
				$('img').animate({down: "+=10px"}, 'fast');
				break;
			case 87:
				$('img').animate({up: "-=10px"}, 'fast');
				break;
			case 68:
				$('img').animate({right: "+=10px"}, 'fast');
				break;
			default:
				break;
		}
	});
});