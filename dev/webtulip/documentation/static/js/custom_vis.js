
var networkCreator = (function() {
	return {

    drawSimpleGraph: function(data, startTimer, ajaxTimer, loadingTlpTime, pruningTime, cliqueBundlingTime, edgeBundlingTime) {

      var beforeProcessInJsTimer = new Date();
      
	    arrayOfNodes = [];
      arrayOfEdges = [];

      data.nodes.forEach(function(node) {
        arrayOfNodes.push({id: node.id, label: "id: " + node.id});
      });

      // checks data for any nodes that have been pruned and styles accordingly
      for (var j = 0; j<data.nodesBeenPruned.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.nodesBeenPruned[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#afa";
            arrayOfNodes[i]["shape"] = "elipse";
            arrayOfNodes[i]["font"] = {"size": 14+(Math.log((10*data.nodesBeenPruned[j]["number"])))};
            arrayOfNodes[i]["label"] += ", n: "+data.nodesBeenPruned[j]["number"];
          }
        }
      }

      // checks data for any nodes that have been clique-based bundled and styles accordingly
      for (var j = 0; j<data.numDeletedClique.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.numDeletedClique[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#d88";
            arrayOfNodes[i]["shape"] = "box";
            arrayOfNodes[i]["font"] = {"size": 16+5+(Math.log10((10*data.numDeletedClique[j].numDeleted))*2.5)};
            arrayOfNodes[i]["label"] += ", n: " + String(data.numDeletedClique[j].numDeleted);
          }
        }
      }

      // checks data for any nodes that have been edge-based bundled and styles accordingly
      for (var j = 0; j<data.numDeletedEdge.length; j++) {
        for (var i = 0; i<arrayOfNodes.length; i++) {
          if (data.numDeletedEdge[j].id === arrayOfNodes[i].id) {
            arrayOfNodes[i]["color"] = "#b6e";
            arrayOfNodes[i]["shape"] = "box";
            arrayOfNodes[i]["font"] = {"size": 16+5+(Math.log((10*data.numDeletedEdge[j].numDeleted))*2.5)};
            arrayOfNodes[i]["label"] += ", n: " + String(data.numDeletedEdge[j].numDeleted);
          }
        }
      }

      console.log(arrayOfNodes);

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
    "<tr><td>Time to load in the TLP</td><td>"+loadingTlpTime+"</td>"+
    "<tr><td>Time from click to AJAX response</td><td>" + timeToAjax +"</td>"+
    "<tr><td>Time spend processing in Vis.js</td><td>" + timeProcessingVis +"</td>"+
    "<tr><td>Time spend creating vis.js network</td><td>" + timeCreatingNetwork +"</td>"+
    "<tr><td>Time spend drawing</td><td>" + timeDrawingNetwork +"</td>"+
    "<tr><td>Sum of all JS times</td><td>" + (timeToAjax+timeProcessingVis+timeCreatingNetwork+timeDrawingNetwork) +"</td>"+
    "<tr><td>Time from first to last Date()</td><td>" + startToEnd +"</td>"+
    "<tr><td>Number of nodes</td><td>" + numberOfNodes+"</td>"+
    "<tr><td>Number of edges</td><td>" + numberOfEdges+"</td>";


  if (pruningTime) {
    toAppend += "<tr><td>Time to prune the network</td><td>" + pruningTime+"</td>";
  }
  if (cliqueBundlingTime) {
    toAppend += "<tr><td>Time to bundle on cliques</td><td>" + cliqueBundlingTime+"</td>";
  }
  if (edgeBundlingTime) {
    toAppend += "<tr><td>Time to bundle on edges</td><td>" + edgeBundlingTime+"</td>";
  }

  toAppend += "</table><br/>";

  $("#output").append(toAppend);

};