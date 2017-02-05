

var networkCreator = (function() {
	return {

    drawSimpleGraph: function(result) {

      arrayOfNodes = [];
      arrayOfEdges = [];

      for (var i = 0; i < result.nodes.length; i++) {
        arrayOfNodes.push({id: i, label: });
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
      var options = {};

      // initialize your network!
      var network = new vis.Network(container, data, options);

    }
	}
})();
