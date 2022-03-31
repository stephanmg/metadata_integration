import rdflib
g = rdflib.Graph()
## TODO: export to json-ld or rdf from Excel, then import into db (rdflib/MongoDB)
g.parse("foaf.rdf")

# Semantic query on graph (who knows who) returning pairs of persons
knows_query = """
SELECT DISTINCT ?aname ?bname
WHERE {
    ?a foaf:knows ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}"""

# Semantic query for constructing triples to represent relationships in a graph representation
# TODO: Need a ontology / controlled vocabulary (need to be fixed as the data
# model in the Excel sheet before with an ER model / UML modelling) to make querying possible 
# and easy. Additionally the ontology / controlled vocabulary allows to create easily
# frontend graphical user interfaces (categories / dropdown menus from the nodes in the
# data model) to build e.g. visual SPARQL queries to query the graph-based database
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
    """ helper method to convert query result into JSON """
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

## export simple json suitable for d3js visualization in frontend
## TODO: Create actual JSON data not array of javascript objects to generalize this
print(to_json(qres))
with open("myjsondata.json", "w") as f:
    f.write(to_json(qres))