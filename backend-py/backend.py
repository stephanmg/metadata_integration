#!/usr/bin/env python
# encoding: utf-8
import requests, json
from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin

################################################################################
# WEB APPLICATION SETUP
################################################################################
app = Flask(__name__)
cors = CORS(app, resources={r"/register": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

################################################################################
# PUBLIC REST API
################################################################################
@app.route('/api/query/statistics/Files', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query():
    return jsonify({'message': 'Count', 'count':1337})

@app.route('/api/query/statistics/Usage', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query_count():
    return jsonify({'message': 'Count', 'count':1337333})

@app.route('/api/query/statistics/Projects', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_query_count2():
    return jsonify({'message': 'Count', 'count':-100})


################################################################################
# INTERNAL REST API FOR WEB APPLICATION
################################################################################
@app.route('/register', methods = ['POST', 'GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    data = ""
    if request.method == 'GET':
        print("get!")
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        data = jsonify({"message": f"User {json_data['email']} was registered!" })
    return data

@app.route('/query', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def query():
    json_data = request.get_json(force=True)
    queryType = json_data['queryType']
    myresult = 0
    if "Files" == queryType:
        myresult = 111
    else:
        myresult = 1000
        
    response = requests.get(f'http://localhost:8181/api/query/statistics/{queryType}')
    json_data = json.loads(response.text)
    return jsonify({'mydata': json_data['count'], 'query': queryType})

################################################################################
# WEB APPLICATION START
################################################################################
app.run(host='localhost', port=8181)