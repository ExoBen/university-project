
var tulipWebApi = (function() {
	return {

		loadGraph: function(fileName, callback, errorCallback) {

			$.ajax({
				url: "/api/loadGraph",
				data: {
			        "name": fileName,
			    },
			    cache: false,
			    type: "GET",
				success: function(result) {
					if (result.success) {
		        		callback(result.data);
					} else {
						if (typeof errorCallback === "function") {
							errorCallback(result.message);
						}
					}
		        }
		    });
		}

	}
})();
