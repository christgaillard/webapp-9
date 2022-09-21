$(function(){
	$('button').click(function(){
		var user = $('#usr').val();
		$.ajax({
			url: 'https://openclassroom.azurewebsites.net/api/test',
			//data: $('form').serialize(),
			data:JSON.stringify($("form").serializeArray()),
			type: 'POST',
			success: function(response){
				console.log(response);
				const obj = JSON.parse(response);
				$("#categ").html(obj[0].categories);
                $("#livres").html(obj[0].recommendation);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});