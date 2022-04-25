from rdflib import Graph, Namespace

# Load metadata ontology with individuals data in RDF/XML format
g = Graph()
# Creates the data entries in-memory database (triple store)
filename = 'Metadata-Ontology2.owl'
g.parse(filename, format="application/rdf+xml")
# Bind namespace for our metadata ontology
meta = Namespace('http://localhost/stephanmg/ontologies/2022/3/metadata-ontology#')
g.bind('meta', meta)

# basic SPARQL query to find all sheets which had an experiment conducted already
q = """
    PREFIX meta: <http://localhost/stephanmg/ontologies/2022/3/metadata-ontology#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?aname ?atitle ?adate ?atissue ?x ?y ?z
       WHERE { 
            ?general meta:createsExperiment ?experiment .
            ?general meta:Name ?aname .
            ?general meta:Title ?atitle .
            ?general meta:Date ?adate .
            ?x meta:hasDiet ?y . 
            ?experiment meta:Tissue ?atissue .
            FILTER (?atissue='Heart'^^xsd:string)
      }
"""



# query in-memory database nad print results to stdout
res = g.query(q)
count = 1
for r in res:
    print("*****************************************************************************")
    print(f"Experiment #{count}")
    print("*****************************************************************************")
    print("Get Name, title tissue and date for experiment.")
    print(f"Name of experimentator: {r.aname} (Working with tissue type: {r.atissue})")
    print(f"Title of experiment: {r.atitle} (Created on: {r.adate})")
    count += 1
    print("")
