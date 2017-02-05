import json

class TlpJsonConverter:

	def tlp_to_json(name, tlpNetwork):
		jsonNetwork = {"nodes": []}

		for node in tlpNetwork.getNodes():
			currentNode = {"id": node.id, "outEdges": []}

			for connectedNode in tlpNetwork.getOutNodes(node):
				currentNode["outEdges"].append(connectedNode.id)

			jsonNetwork["nodes"].append(currentNode)


		return json.dumps(jsonNetwork)


	# def json_to_tlp(json):
	#	return "tlp"