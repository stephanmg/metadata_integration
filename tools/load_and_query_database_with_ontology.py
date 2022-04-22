from rdflib import Graph, Namespace

# Create 
g = Graph()
g.parse('Metadata-Ontology.owl', format="application/rdf+xml")
meta = Namespace('http://localhost/stephanmg/ontologies/2022/3/metadata-ontology#')
g.bind('meta', meta)

q = """
    PREFIX meta: <http://localhost/stephanmg/ontologies/2022/3/metadata-ontology#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?aname ?atitle ?adate ?atissue
       WHERE { 
            ?general meta:createsExperiment ?experiment .
            ?general meta:Name ?aname .
            ?general meta:Title ?atitle .
            ?general meta:Date ?adate .
            ?experiment meta:Tissue ?atissue .
            FILTER (?atissue='Heart'^^xsd:string)
      }
"""

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
