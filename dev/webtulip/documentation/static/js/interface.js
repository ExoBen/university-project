
$("input[name='loadGraph']").click(function() {
	graphToLoad = $("#graphToLoad").val();
	
	tulipWebApi.loadGraph(graphToLoad, function(result) {
		console.log(result)
		$("#loadedJSON").text(result);
	});

});