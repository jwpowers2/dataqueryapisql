import json
import sys
import logging
import psycopg2


class Query():

    def __init__(self, column, tablename, return_type):

        self.column = column
        self.tablename = tablename
        self.return_type = return_type

    def build_query_statement(self, query_param):

        if (self.return_type == "xml"):

            xml_query = "SELECT xmlelement(name results, xmlagg(xmlelement(name row, xmlforest({1})))) FROM {0}".format(self.tablename, self.column) 

            if (query_param):
                xml_query = "SELECT xmlelement(name results, xmlagg(xmlelement(name row, xmlforest({1})))) FROM {0} {2}".format(self.tablename, self.column, query_param) 

            return xml_query
        
        else:

            standard_query = "SELECT {} FROM {}".format(self.column, self.tablename)

            if (query_param):
                standard_query = "SELECT {} FROM {} {}".format(self.column, self.tablename, query_param)

            return standard_query

    def execute_query(self, query_param, one=False):

        query = self.build_query_statement(query_param)

        try:
            conn=psycopg2.connect(dbname="aggs", host="localhost", port="5432", user="aggmaster", password="p11a2s3s5")

            if self.return_type == "json":

	        cur = conn.cursor()
                cur.execute(query)
                r = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
                cur.close()
                conn.close()
                return json.dumps((r[0] if r else None) if one else r)

            elif self.return_type == "xml":

	        cur = conn.cursor()
                cur.execute(query)
                query_result = cur.fetchall()
                cur.close()
                conn.close()
                return query_result.pop(0)
                 

            elif self.return_type == "list":

	        cur = conn.cursor()
                cur.execute(query)
                query_result = cur.fetchall()
                cur.close()
                conn.close()
                return json.dumps(query_result)   

            else:
                cur.close()
                conn.close()

        except psycopg2.Error, e:
	    logging.warning("Bad CONN as {}".format(e))

