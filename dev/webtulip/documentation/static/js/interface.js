
$("input[name='loadGraph']").click(function() {
	graphToLoad = $("#graphToLoad").val();

	tulipWebApi.loadGraph(graphToLoad, function(result) {
		networkCreator.drawSimpleGraph(result);
	}, function(error) {
		console.error(error)
	});

});
