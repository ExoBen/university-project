
$("input[name='loadGraph']").click(function() {
	var startTimer = new Date();
	var graphToLoad = $("#graphToLoad").val();
	var toPrune = false;
	if ($("#prune").is(':checked')) {
		toPrune = true;
	}
	var toCliqueBundle = false;
	if ($("#cbundle").is(':checked')) {
		toCliqueBundle = true;
	}
	var toEdgeBundle = false;
	if ($("#ebundle").is(':checked')) {
		toEdgeBundle = true;
	}

	tulipWebApi.loadGraph(graphToLoad, toPrune, toCliqueBundle, toEdgeBundle, function(result) {
		var ajaxTimer = new Date();

		networkCreator.drawSimpleGraph(
			result.data, 
			startTimer, 
			ajaxTimer, 
			result.tlpLoadTime, 
			result.pruningTime, 
			result.cliqueBundlingTime, 
			result.edgeBundlingTime);
	}, function(error) {
		console.error(error)
	});

});

$("input[name='deleteGraph']").click(function() {
	var graphToDelete = $("#graphToDelete").val();

	tulipWebApi.deleteGraph(graphToDelete, function(result) {
		$("#deleted").text(result);
		$('#graphToDelete option[value=' + graphToDelete + ']').remove();
	}, function(error) {
		$("#deleted").text(error);
		console.error(error)
	});

});
