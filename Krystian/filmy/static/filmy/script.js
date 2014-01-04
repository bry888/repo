$(document).ready(function(){
	
        var num_boxes = 1;
        
        if (num_boxes < 10) {
        
        $('#add_phrase').click(function() {
            
        $('form').append('<br>{{ form.as_p }}');
        num_boxes += 1;
        
	});
        
        } else {
        $('form').append('<br><p>Wystarczy tego dobrego.</p>');
        }
	
});