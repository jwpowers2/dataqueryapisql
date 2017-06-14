#!/usr/bin/python

import logging
import json
import psycopg2
from string_cleaning import Dirty


def authenticate_user(username, password, request_json):

    if (request_json.get("tablename")) is not None:
        tablename = request_json.get("tablename")
    else:
        return False

    if (request_json.get("column")) is not None:
        column = request_json.get("column")
    else:
        return False
    
    if (request_json.get("return_type")) is not None:
        return_type = request_json.get("return_type")
    else:
        return False

    if (request_json.get("query_param")) is not None:
        query_param = request_json.get("query_param")
        clean_me = Dirty(query_param)
        clean_me.clean_buffer()
        clean_me.clean_sql()
    

    candidate_list = [username, password, return_type, tablename, column]

    for sec_candidate in candidate_list:
        
        clean_me = Dirty(sec_candidate)
        clean_me.clean_buffer()
        clean_me.clean_sql()
        clean_me.clean_meta()


    try:
        conn=psycopg2.connect("dbname=users host=localhost user=admin password=BettyPage")
	cur = conn.cursor()
        cur.execute("""SELECT name FROM users WHERE name='{}' AND password='{}' AND tablename='{}'""".format(username, password, tablename))
        user_name = cur.fetchall()

        if (user_name):

            cur.close()
            conn.close()
            logging.warning("Authenticated user: {}".format(user_name))
            return True

        else:
            cur.close()
            conn.close()
            return False

    except:
	return False
            

