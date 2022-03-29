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
    response = requests.get(f'http://localhost:8181/api/query/statistics/{queryType}')
    json_data = json.loads(response.text)
    return jsonify({'mydata': json_data['count'], 'query': queryType})

################################################################################
# WEB APPLICATION START
################################################################################
app.run(host='localhost', port=8181)