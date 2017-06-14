# Data Query API SQL


### This is an API for accessing data in a SQL database using web requests
### The intent is to provide special customers query access 

## The web request components, formatting, and request examples

1. An Example query request:

    #!/usr/bin/python

    import requests

    api_address = '127.0.0.1'

    response = requests.get("http://{}:5000/dataqueryapi".format(api_address), json={'column': 'store_name', 'tablename': 'cabelas'}, auth=('john','BettyPage'))
    print response.text

2. The Components:

* The GET request has an ip address or domain name followed by the destination port (5000) and the api directory called dataqueryapi

* The JSON section is what we are actually requesting from the API.  Here is some more detail on what they do:

    tablename: required: This is the table you are attempting to access

    column: query: this is the column or columns you wish to look into

    return_type: all requests made to the API are JSON so the return type has to be designated in the request to the API: json, xml, list

    query_param: query: This is an optional parameter for query to give parameters for the query.  
        
        An example for query_param is "WHERE STORE_NAME IS NOT NULL"

* The auth section is username and password information for authenticating into the API. 



## Setting up the API Service

## setup instructions are not complete and not tested yet

* clone this repo

* install pip and use it to install dependencies

* apt install python-pip python-dev libpq-dev postgresql 

* pip install -r requirements.txt

* create the file /usr/bin/dataqueryapisql and paste the code from below into it

* create the file /etc/systemd/system/dataqueryapisql.service and paste the code from below into it

* chmod +x on /usr/bin/dataqueryapisql

* chmod 744 on /home/DataQueryApiSQL/datqueryapisqlapi.py

* sytemctl enable dataqueryapisql.service

* service dataqueryapisql start 


## /usr/bin/dataqueryapisql

#!/usr/bin/python

import subprocess

subprocess.call(["python", "/home/controller/dataqueryapisql.py"])


## code to cut and paste into dataqueryapisql.service on DATAQUERYAPISQL

## /etc/systemd/system/dataqueryapisql.service

[Unit]
Description=Start DATAQUERYAPISQL

[Install]
WantedBy=multi-user.target

[Service]
ExecStart=/usr/bin/dataqueryapisql

Restart=always


## once these programs are installed, run:

    systemctl enable dataqueryapisql 


## then, run:

    service dataqueryapisql start

## You can debug this process with:

    journalctl -xe

    pgrep dataqueryapisql

    tail -n 25 /var/log/syslog








