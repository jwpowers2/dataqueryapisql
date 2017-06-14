#!/usr/bin/python

import requests
import argparse


# make command-line interface for this using argparse
# return types are json, xml, list


parser = argparse.ArgumentParser(
    prog='----- DATA QUERY API SQL REQUEST CLI -----',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description = ('''\
        \n\n\n\n\n
        ###################################################################################
        

        This is the CLI for making a request to the Data Query API (SQL)
 
        
        Here is an example request for Linux:

        ./api_request 138.197.222.81 -t cabelas -c id,store_name, address -rt json 


        Here is an example which passes some query parameters (optional):

        ./api_request 138.197.222.81 -t cabelas -c id,store_name -rt xml -p "WHERE state='Alberta'"


        #################################################################################### 
        \n\n\n\n\n    
    '''))

parser.add_argument("address", help="the address of the API you are going to query")
parser.add_argument("-t", "--tablename", help="the tablename you would like to query")
parser.add_argument("-c", "--column", help="the column you are going to query")
parser.add_argument("-rt", "--return_type", help="the return type of the data you have queries")
parser.add_argument("-p", "--query_param", help="optional query parameters")

args = parser.parse_args()

#data = {'tablename': 'cabelas', 'column': 'id, store_name, state', 'return_type': 'json', 'query_param':'WHERE state=\'Alberta\''}

data = {'tablename': args.tablename, 'column': args.column, 'return_type': args.return_type, 'query_param': args.query_param}

#url = '138.197.222.81'

url = args.address

response = requests.get("http://{}:5000/dataqueryapi".format(url), json=data, auth=('john','BettyPage'))

print response.text

