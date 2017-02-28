
var tulipWebApi = (function() {
	return {

		loadGraph: function(fileName, callback, errorCallback) {

			$.ajax({
				url: "/api/loadGraph",
				data: {
			        "network_name": fileName,
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
		        }
		    });
		}

	}
})();
