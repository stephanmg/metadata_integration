#!/usr/bin/env python
# encoding: utf-8
import requests, json
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
import api


# TODO: Use type annotations
# TODO: Get rid of CORS
# TODO: Use Swagger to create documentation for REST API
################################################################################
# WEB APPLICATION SETUP
################################################################################
app = Flask(__name__)
cors = CORS(app, resources={r"/register": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO: no real JSON data but string (in JS this works because its converted to an JS object!)
fake_data2 = '''
[
{ country: 'P01', value: 5 },
{ country: 'P02', value: 13.4 },
{ country: 'P03', value: 4.0 },
{ country: 'P08', value: 4.9 },
{ country: 'P14', value: 2.8 }
]
'''
fake_data = '''
{
  "nodes":[
		{"id":"P01","group":1},
		{"id":"P02","group":2},
		{"id":"P03","group":3},
		{"id":"P04","group":4},
		{"id":"P05","group":5},
		{"id":"P06","group":6},
		{"id":"P07","group":7},
		{"id":"P08","group":8},
		{"id":"P09","group":9},
		{"id":"P10","group":10},
		{"id":"P11","group":11},
		{"id":"P12","group":12},
		{"id":"P13","group":13},
		{"id":"P14","group":14},
		{"id":"P15","group":15},
		{"id":"P16","group":16},
		{"id":"P17","group":17},
		{"id":"P18","group":18}
	],
	"links":[
		{"source":"P01","target":"P03","value":1},
		{"source":"P02","target":"P04","value":3},
		{"source":"P03","target":"P04","value":10},
		{"source":"P01","target":"P04","value":20},
		{"source":"P05","target":"P04","value":1},
		{"source":"P06","target":"P04","value":1},
		{"source":"P06","target":"P04","value":1},
		{"source":"P07","target":"P02","value":1},
		{"source":"P06","target":"P03","value":1},
		{"source":"P04","target":"P07","value":1},
		{"source":"P01","target":"P18","value":1},
		{"source":"P01","target":"P17","value":1},
		{"source":"P07","target":"P09","value":1},
		{"source":"P07","target":"P12","value":1},
		{"source":"P07","target":"P18","value":1},
		{"source":"P07","target":"P13","value":5},
		{"source":"P17","target":"P14","value":3},
		{"source":"P17","target":"P15","value":1},
		{"source":"P12","target":"P08","value":10},
		{"source":"P12","target":"P10","value":1},
		{"source":"P10","target":"P16","value":1},
		{"source":"P16","target":"P11","value":5}
	]
}
'''

# TODO: Implement and contact to actual database (rdflib or mongodb)
################################################################################
# PUBLIC REST API
################################################################################
@app.route('/api/query/statistics/Files', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query():
    return jsonify({'message': 'Count', 'count':api.get_number_of_files_by_projects()})

@app.route('/api/query/statistics/Usage', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query_count():
    return jsonify({'message': 'Count', 'count':api.get_disk_usage_by_projects()})

@app.route('/api/query/statistics/Projects', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query_count2():
    return jsonify({'message': 'Count', 'count':api.get_number_of_projects()})

@app.route('/api/query/statistics/MyGDP', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def my_gdp():
    return jsonify(fake_data2)

@app.route('/api/query/statistics/Graph', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def my_graph():
    return jsonify(fake_data)


################################################################################
# INTERNAL USAGE OF REST API FOR WEB APPLICATION
################################################################################
@app.route('/register', methods = ['POST', 'GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    data = ""
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        data = jsonify({"message": f"User {json_data['email']} was registered!" })
    return data

@app.route('/query', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def query():
    json_data = request.get_json(force=True)
    queryType = json_data['queryType']

    if 'Graph' == queryType:
        response = requests.get(f'http://localhost:8181/api/query/statistics/{queryType}')
        return json.loads(response.text)
    elif 'MyGDP' == queryType:
        response = requests.get(f'http://localhost:8181/api/query/statistics/{queryType}')
        return json.loads(response.text)
    else:
        response = requests.get(f'http://localhost:8181/api/query/statistics/{queryType}')
        json_data = json.loads(response.text)
        return jsonify({'mydata': json_data['count'], 'query': queryType})

################################################################################
# WEB APPLICATION START
################################################################################
app.run(host='localhost', port=8181)