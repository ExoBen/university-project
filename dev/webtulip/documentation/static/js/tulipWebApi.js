
var tulipWebApi = (function() {
	return {

		loadGraph: function(fileName, callback) {
			$.ajax({
				url: "/api/loadGraph", 
				data: { 
			        "name": fileName,
			    },
			    cache: false,
			    type: "GET",
				success: function(result) {
		        	callback(result);
		        }
		    });
		}

	}
})();


