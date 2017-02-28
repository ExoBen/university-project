
$("input[name='loadGraph']").click(function() {
	graphToLoad = $("#graphToLoad").val();

	tulipWebApi.loadGraph(graphToLoad, function(result) {
		networkCreator.drawSimpleGraph(result);
	}, function(error) {
		console.error(error)
	});

});

$("input[name='deleteGraph']").click(function() {
	graphToDelete = $("#graphToDelete").val();

	tulipWebApi.deleteGraph(graphToDelete, function(result) {
		$("#deleted").text(result);
		$('#graphToDelete option[value=' + graphToDelete + ']').remove();
	}, function(error) {
		$("#deleted").text(error);
		console.error(error)
	});

});
