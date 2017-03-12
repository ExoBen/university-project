from django.shortcuts import render
from django.conf import settings
import os
from django.http import JsonResponse
from tulip import tlp
import time

from .tlp_json_converter import TlpJsonConverter
from .network_optimiser import NetworkOptimiser

from documentation.models import Network

def loadGraph(request):
	# return list of all graphs the user can load
	if (request.method == "GET" and request.GET.get("network_name", None) != None):
		nameOfGraph = request.GET.get("network_name", None)

		toPrune = request.GET.get("toPrune", False)
		toPrune = toPrune == "true"

		toCliqueBundle = request.GET.get("toCliqueBundle", False)
		toCliqueBundle = toCliqueBundle == "true"

		toEdgeBundle = request.GET.get("toEdgeBundle", False)
		toEdgeBundle = toEdgeBundle == "true"

		networkFromDB = Network.objects.filter(network_name=nameOfGraph)[0]
		#print (networkFromDB.network_file.name)

		beforeTlpLoaded = time.time()
		currentNetwork = tlp.loadGraph(os.path.join(settings.MEDIA_ROOT, networkFromDB.network_file.name))
		afterTlpLoaded = time.time()
		
		tlpLoadTime = round(((afterTlpLoaded-beforeTlpLoaded)*1000.0), 1)

		if currentNetwork is None:
			return JsonResponse({"success": False, "message": "File failed to load"})
		else:
			pruningTime = False
			cliqueBundlingTime = False
			edgeBundlingTime = False
			nodesBeenPruned = []
			numDeletedClique = []
			numDeletedEdge = []


			if (toPrune):
				beforePruned = time.time()
				currentNetwork, nodesBeenPruned = NetworkOptimiser.nodePruning(currentNetwork)
				afterPruned = time.time()
				pruningTime = round(((afterPruned-beforePruned)*1000.0), 1)

			if (toCliqueBundle):
				beforeCliqueBundled = time.time()
				currentNetwork, numDeletedClique = NetworkOptimiser.cliqueBasedNodeBundling(currentNetwork)
				afterCliqueBundled = time.time()
				cliqueBundlingTime = round(((afterCliqueBundled-beforeCliqueBundled)*1000.0), 1)

			if (toEdgeBundle):
				beforeEdgeBundled = time.time()
				currentNetwork, numDeletedEdge = NetworkOptimiser.edgeBasedNodeBundling(currentNetwork)
				afterEdgeBundled = time.time()
				edgeBundlingTime = round(((afterEdgeBundled-beforeEdgeBundled)*1000.0), 1)

			graphInJson = TlpJsonConverter.tlp_to_json(nameOfGraph, currentNetwork, nodesBeenPruned, numDeletedClique, numDeletedEdge)

			return JsonResponse({
				"success": True, 
				"data": graphInJson, 
				"tlpLoadTime": tlpLoadTime, 
				"pruningTime": pruningTime, 
				"cliqueBundlingTime": cliqueBundlingTime, 
				"edgeBundlingTime": edgeBundlingTime
				})
	return JsonResponse({"success": False, "message": "Define name and use GET"}) 

def deleteGraph(request):
	if (request.method == "POST" and request.POST.get("network_name", None) != None):
		nameOfGraph = request.POST.get("network_name", None)
		networkToDelete = Network.objects.filter(network_name=nameOfGraph)[0]

		if networkToDelete is None:
			return JsonResponse({"success": False, "message": "File failed to delete"})
		
		else:
			networkToDelete.network_file.delete()
			networkToDelete.delete()
			return JsonResponse({"success": True, "message": "File deleted"})

	return JsonResponse({"success": False, "message": "Define name and use POST"}) 

