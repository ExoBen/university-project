
var tulipWebApi = (function() {
	return {

		loadGraph: function(fileName, toPrune, toCliqueBundle, toEdgeBundle, callback, errorCallback) {

			$.ajax({
				url: "/api/loadGraph",
				data: {
			        "network_name": fileName,
			        "toPrune": toPrune,
			        "toCliqueBundle": toCliqueBundle,
			        "toEdgeBundle": toEdgeBundle,
			    },
			    cache: false,
			    type: "GET",
				success: function(result) {
					if (result.success) {
		        		callback(result);
					} else {
						if (typeof errorCallback === "function") {
							errorCallback(result.message);
						}
					}
		        },
				error: function() {
					if (typeof errorCallback === "function") {
						errorCallback("Unknown server error.");
					}
		        }
		    });
		},

		deleteGraph: function(fileName, callback, errorCallback) {

			$.ajax({
				url: "/api/deleteGraph",
				data: {
			        "network_name": fileName,
			    },
			    cache: false,
			    type: "POST",
				success: function(result) {
					if (result.success) {
		        		callback(result.message);
					} else {
						if (typeof errorCallback === "function") {
							errorCallback(result.message);
						}
					}
		        },
				error: function() {
					if (typeof errorCallback === "function") {
						errorCallback("Unknown server error.");
					}
		        }
		    });
		}

	}
})();
