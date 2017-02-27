import json
from pprint import pprint

file_names = ["graph_response_30", "graph_response_200", "graph_response_1000", "graph_response_3000"]

for fn in file_names:

	with open(fn+'.json') as data_file:    
	    data = json.load(data_file)

	#pprint(data["counts"])
	#pprint(data["vertices"])
	#pprint(data["edges"])

	with open(fn+'.tlp', "w") as f:
		f.write('(tlp "2.0"\n')
		nodes = '(nodes'
		for i in data["vertices"]:
			nodes+=(" " + str(i["id"]))
			#print(i)
			#print("\n\n")
		nodes+=(')\n')
		f.write(nodes)

		edges = ''
		j = 1
		for i in data["edges"]:
			edges+=("(edge "+str(j)+" "+i["endpoints"][0]["id"]+" "+i["endpoints"][1]["id"]+")\n")
			j+=1
			#print(i)
			#print("\n\n")
		f.write(edges)

		f.write(')')
