from django.shortcuts import render
from django.http import JsonResponse

from tulip import tlp
# Create your views here.

def loadGraph(request):

	# return list of all graphs the user can load
	print (request)
	sample = tlp.loadGraph("sample.tlp")
	print(sample)
	return JsonResponse({'graph':'loaded'})

# def saveGraph(request):

# 	# overwrites if no parameter, saves to new file if file name given
# 	print (request)
# 	return JsonResponse({'graph':'saved'})

# def importGraph(request):

# 	# user uploads / points to graph and gives it a name etc.
# 	print (request)
# 	return JsonResponse({'graph':'import'})

# def exportGraph(request):

# 	# export a graph to a file
# 	print (request)
# 	return JsonResponse({'graph':'export'})