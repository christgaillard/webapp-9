$(function(){
	$('button').click(function(){
		var user = $('#usr').val();
		$.ajax({
			url: 'https://serverlessopenclassroom.azurewebsites.net/api/test',
			//url: 'http://localhost:7071/api/test',
			//data: $('form').serialize(),
			data:JSON.stringify($("form").serializeArray()),
			type: 'POST',
			success: function(response){
				test = JSON.parse(response);
				console.log(test);
                $("#livres").html("livre 1 : "+ test[0] + "<br>"+"livre 2 : "+ test[1]+ "<br>"+"livre 3 : "+ test[2] + "<br>"+"livre 4 : "+ test[3]+"<br>"+"livre 5 : "+ test[4]);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});