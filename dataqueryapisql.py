#!flask/bin/python

import logging
import json
import psycopg2
from flask import Flask, jsonify, make_response, request
from flask_httpauth import HTTPBasicAuth
from authenticate_user import authenticate_user
from create_query import Query


class InvalidUsage(Exception):
    status_code = 400
    
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
 

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):

    return authenticate_user(username, password, request.json)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'not found'}), 404)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response 

@app.route('/dataqueryapi', methods=['GET'])
@auth.login_required
def dataqueryapi():

    tablename = request.json.get('tablename')
    return_type = request.json.get('return_type')   
    column = request.json.get('column')

    new_query = Query(column, tablename, return_type)

    return new_query.execute_query(request.json.get('query_param'))    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
