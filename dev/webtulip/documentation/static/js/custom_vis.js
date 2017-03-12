
var networkCreator = (function() {
	return {

    drawSimpleGraph: function(data, startTimer, ajaxTimer, loadingTlpTime, pruningTime, cliqueBundlingTime, edgeBundlingTime) {

      var beforeProcessInJsTimer = new Date();
      
	    arrayOfNodes = [];
      arrayOfEdges = [];

      data.nodes.forEach(function(node) {
        arrayOfNodes.push({id: node.id, label: node.id});
      });

      for (var j = 0; j<data.nodesBeenPruned.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.nodesBeenPruned[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#afa";
          }
        }
      }

      for (var j = 0; j<data.numDeletedClique.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.numDeletedClique[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#d88";
            arrayOfNodes[i]["shape"] = "box";
            arrayOfNodes[i]["font"] = {"size": 16+(data.numDeletedClique[j].numDeleted)};
          }
        }
      }

      for (var j = 0; j<data.numDeletedEdge.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.numDeletedEdge[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#b6e";
            arrayOfNodes[i]["shape"] = "box";
            arrayOfNodes[i]["font"] = {"size": 16+(data.numDeletedEdge[j].numDeleted)};
          }
        }
      }

      data.edges.forEach(function(edge) {
        arrayOfEdges.push({from: edge.from, to: edge.to});
      });

      numberOfNodes = arrayOfNodes.length;
      numberOfEdges = arrayOfEdges.length;

      // provide the data in the vis format
      var data = {
          nodes: new vis.DataSet(arrayOfNodes),
          edges: new vis.DataSet(arrayOfEdges)
      };

      // create a network
      var container = document.getElementById('main_network');

      var options = {
				layout: {
					improvedLayout:false
				},
				physics: {
					stabilization:true
					/*stabilization: {
				      enabled: true,
				      iterations: 1000,
				      updateInterval: 100,
				      onlyDynamicEdges: false,
				      fit: true
			    	},*/
				}
			};

      var afterProcessingInJsTimer = new Date();

      // initialize the network
      var createNetworkTimer = new Date();

      var network = new vis.Network(container, data, options);

      var networkCreatedTimer = new Date();
      var beforeDrawingTimer = new Date();

      var networkDataCollectedYet = false;
      
      network.on("afterDrawing", function(canvas, context) {
        if (!networkDataCollectedYet) {
          var afterDrawingTimer = new Date();
          outputStats(
            startTimer, 
            ajaxTimer, 
            beforeProcessInJsTimer, 
            afterProcessingInJsTimer, 
            createNetworkTimer, 
            networkCreatedTimer, 
            beforeDrawingTimer, 
            afterDrawingTimer, 
            loadingTlpTime, 
            pruningTime, 
            cliqueBundlingTime, 
            edgeBundlingTime,
            numberOfNodes,
            numberOfEdges);
          networkDataCollectedYet = true;
        }
      });
    }
	}
})();

var outputStats = function(
      startTimer, 
      ajaxTimer, 
      beforeProcessInJsTimer, 
      afterProcessingInJsTimer, 
      createNetworkTimer, 
      networkCreatedTimer, 
      beforeDrawingTimer, 
      afterDrawingTimer,
      loadingTlpTime,
      pruningTime,
      cliqueBundlingTime,
      edgeBundlingTime,
      numberOfNodes,
      numberOfEdges) {
  var timeToAjax = (ajaxTimer.getTime()-startTimer.getTime());
  var timeProcessingVis = (afterProcessingInJsTimer.getTime() - beforeProcessInJsTimer.getTime());
  var timeCreatingNetwork = (networkCreatedTimer.getTime() - createNetworkTimer.getTime())
  var timeDrawingNetwork = (afterDrawingTimer.getTime() - beforeDrawingTimer.getTime())
  var startToEnd = (afterDrawingTimer.getTime() - startTimer.getTime())

  var toAppend = ""

  toAppend +=
    "<table>"+
    "<tr><td>Time to load in the TLP</td><td>"+loadingTlpTime+"ms</td>"+
    "<tr><td>Time from click to AJAX response</td><td>" + timeToAjax +"ms</td>"+
    "<tr><td>Time spend processing in Vis.js</td><td>" + timeProcessingVis +"ms</td>"+
    "<tr><td>Time spend creating vis.js network</td><td>" + timeCreatingNetwork +"ms</td>"+
    "<tr><td>Time spend drawing</td><td>" + timeDrawingNetwork +"ms</td>"+
    "<tr><td>Sum of all JS times</td><td>" + (timeToAjax+timeProcessingVis+timeCreatingNetwork+timeDrawingNetwork) +"ms</td>"+
    "<tr><td>Time from first to last Date()</td><td>" + startToEnd +"ms</td>"+
    "<tr><td>Number of nodes</td><td>" + numberOfNodes+"</td>"+
    "<tr><td>Number of edges</td><td>" + numberOfEdges+"</td>";


  if (pruningTime) {
    toAppend += "<tr><td>Time to prune the network</td><td>" + pruningTime+"ms</td>";
  }
  if (cliqueBundlingTime) {
    toAppend += "<tr><td>Time to bundle on cliques</td><td>" + cliqueBundlingTime+"ms</td>";
  }
  if (edgeBundlingTime) {
    toAppend += "<tr><td>Time to bundle on edges</td><td>" + edgeBundlingTime+"ms</td>";
  }

  toAppend += "</table><br/>";

  $("#output").append(toAppend);

};