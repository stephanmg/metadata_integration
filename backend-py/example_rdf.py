import rdflib
g = rdflib.Graph()
## TODO: export to json-ld or rdf 
g.parse("foaf.rdf")

knows_query = """
SELECT DISTINCT ?aname ?bname
WHERE {
    ?a foaf:knows ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}"""


## TODO: need a GO for our controlled vocabulary (from the excel sheet) we wish to 
# use, then we can have a visual query builder in the frontend, making use of preciesly this
# controlled vocabulary to do different queries on the data base. 
# JSON can be gneerated and exchanged with the front end, or cache the
# query as a graph (possible via CONSTRUCT queries) and query the sub-graph
# in the frontend for efficiency reasons...

knows_query_construct = """
CONSTRUCT {
    ?aname foaf:knows ?bname
} WHERE {
    ?a foaf:knows ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}
"""

qres = g.query(knows_query_construct)
print(qres)

def to_json(res):
    print("TO_JSON")
    my_json_data = """
{ 'nodes' : [
"""
    size = len(qres) - 1
    index_set = {}
    # nodes
    index = 0
    for row in qres:
        a, b, c = row
        index_set[c.toPython()] = index
        tmp = "\t{" + f" 'id': {index}, 'name': '{c}'" + " }" + f"{index < size and ',' or ''}\n"
        my_json_data = my_json_data + tmp
        index += 1

    index = 0
    for row in qres:
        a, b, c = row
        index_set[a.toPython()] = index
        tmp = "\t{" + f" 'id': {index}, 'name': '{a}'" + " }" + f"{index < size and ',' or ''}\n"
        my_json_data = my_json_data + tmp
        index += 1

    my_json_data = my_json_data + "],\n"
    my_json_data = my_json_data + "'links': [\n"

    # links
    index = 0
    for row in qres:
        a, b, c = row
        try:
           tmp = "\t{'source': " + f"{index_set[c.toPython()]}" + ", 'target': " + f"{index_set[a.toPython()]}" + "}" +  f"{index < size and ',' or ''}\n" 
           my_json_data = my_json_data + tmp
        except KeyError:
            print("Person does not know any other person, should not happen ever!")
            # person does not know any other person
            pass
        index += 1
    
    my_json_data = my_json_data + "]}"
    
    return my_json_data

print(to_json(qres))
with open("myjsondata.json", "w") as f:
    f.write(to_json(qres))
