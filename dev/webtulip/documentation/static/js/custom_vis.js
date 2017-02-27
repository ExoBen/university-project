
var networkCreator = (function() {
	return {

    drawSimpleGraph: function(result) {

      arrayOfNodes = [];
      arrayOfEdges = [];

      for (var i = 0; i < result.nodes.length; i++) {
        arrayOfNodes.push({id: i, label: i});
        result.nodes[i].outEdges.forEach(function(element) {
          arrayOfEdges.push({from: i, to: element})
        });
      }

      var nodes = new vis.DataSet(arrayOfNodes);

      var edges = new vis.DataSet(arrayOfEdges);

      // create a network
      var container = document.getElementById('main_network');

      // provide the data in the vis format
      var data = {
          nodes: nodes,
          edges: edges
      };

      var options = {
				layout: {
					improvedLayout:false
				},
				physics: {
					//stabilization:false
					stabilization: {
			      enabled: true,
			      iterations: 1000,
			      updateInterval: 100,
			      onlyDynamicEdges: false,
			      fit: true
			    },
				}
			};

			/*var options = {
			  physics:{
			    enabled: true,
			    barnesHut: {
			      gravitationalConstant: -2000,
			      centralGravity: 0.3,
			      springLength: 95,
			      springConstant: 0.04,
			      damping: 0.09,
			      avoidOverlap: 0
			    },
			    forceAtlas2Based: {
			      gravitationalConstant: -50,
			      centralGravity: 0.01,
			      springConstant: 0.08,
			      springLength: 100,
			      damping: 0.4,
			      avoidOverlap: 0
			    },
			    repulsion: {
			      centralGravity: 0.2,
			      springLength: 200,
			      springConstant: 0.05,
			      nodeDistance: 100,
			      damping: 0.09
			    },
			    hierarchicalRepulsion: {
			      centralGravity: 0.0,
			      springLength: 100,
			      springConstant: 0.01,
			      nodeDistance: 120,
			      damping: 0.09
			    },
			    maxVelocity: 50,
			    minVelocity: 0.1,
			    solver: 'barnesHut',
			    stabilization: {
			      enabled: true,
			      iterations: 1000,
			      updateInterval: 100,
			      onlyDynamicEdges: false,
			      fit: true
			    },
			    timestep: 0.5,
			    adaptiveTimestep: true
			  }
			}*/


			console.log("Network created");

      // initialize your network!
      var network = new vis.Network(container, data, options);
			console.log("Network visualised");
    }
	}
})();
