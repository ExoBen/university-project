import json

class TlpJsonConverter:

	def tlp_to_json(name, tlpNetwork, nodesBeenPruned, numDeletedClique, numDeletedEdge):
		jsonNetwork = {"nodes": [], "edges": [], "nodesBeenPruned": [], "numDeletedClique": [], "numDeletedEdge": []}

		for node in tlpNetwork.getNodes():
			jsonNetwork["nodes"].append({"id": node.id})

		for edge in tlpNetwork.getEdges():
			jsonNetwork["edges"].append({"from": tlpNetwork.source(edge).id, "to": tlpNetwork.target(edge).id})

		for node in nodesBeenPruned:
			jsonNetwork["nodesBeenPruned"].append({"id": node.id})

		for nodeNumPair in numDeletedClique:
			jsonNetwork["numDeletedClique"].append({"id": nodeNumPair["node"].id, "numDeleted": nodeNumPair["numDeleted"]})

		for nodeNumPair in numDeletedEdge:
			jsonNetwork["numDeletedEdge"].append({"id": nodeNumPair["node"].id, "numDeleted": nodeNumPair["numDeleted"]})

		return jsonNetwork
