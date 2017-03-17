
class TlpJsonConverter:

	def tlp_to_json(name, network, nodesBeenPruned, numDeletedClique, numDeletedEdge):
		jsonNetwork = {"nodes": [], "edges": [], "nodesBeenPruned": [], "numDeletedClique": [], "numDeletedEdge": []}

		for node in network.getNodes():
			jsonNetwork["nodes"].append({"id": node.id})

		for edge in network.getEdges():
			jsonNetwork["edges"].append({"from": network.source(edge).id, "to": network.target(edge).id})

		for nodeNumPair in nodesBeenPruned:
			# if a node has since been removed by another algorithm then don't send it across the network
			for node in network.getNodes():
				if node == nodeNumPair["node"]:
						jsonNetwork["nodesBeenPruned"].append({"id": nodeNumPair["node"].id, "number": nodeNumPair["number"]})

		for nodeNumPair in numDeletedClique:
			# if a node has since been removed by another algorithm then don't send it across the network
			for node in network.getNodes():
				if node == nodeNumPair["node"]:
					jsonNetwork["numDeletedClique"].append({"id": nodeNumPair["node"].id, "numDeleted": nodeNumPair["numDeleted"]})

		for nodeNumPair in numDeletedEdge:
			# if a node has since been removed by another algorithm then don't send it across the network
			for node in network.getNodes():
				if node == nodeNumPair["node"]:
					jsonNetwork["numDeletedEdge"].append({"id": nodeNumPair["node"].id, "numDeleted": nodeNumPair["numDeleted"]})

		return jsonNetwork
