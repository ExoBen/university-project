import json
from pprint import pprint

class SasToTlp:

    def sas_to_tlp(new_network):

        data = json.loads(new_network)

        output = ""

        output += '(tlp "2.0"\n'
        nodes = '(nodes'
        for i in data["vertices"]:
            if i["id"].startswith("Alert_"):
                nodes+= " " + str(100000)+str(i["id"])[6:]
            else:
                nodes+=(" " + str(i["id"]))
        nodes+=(')\n')
        output += nodes

        edges = ''
        j = 1
        for i in data["edges"]:
            edge1 = i["endpoints"][0]["id"]
            if edge1.startswith("Alert_"):
                edge1 = str(100000)+edge1[6:]
            edge2 = i["endpoints"][1]["id"]
            if edge2.startswith("Alert_"):
                edge2 = str(100000)+edge2[6:]
            edges+=("(edge "+str(j)+" "+edge1+" "+edge2+")\n")
            j+=1
        output += edges
        output += ')'

        return output
