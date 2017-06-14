#!/usr/bin/python


class Dirty():

    bad_words = [ "drop", "insert", "select" ] 
    bad_char = [ "*", "`", "=" ]

    def __init__(self, input_string):

        self.input_string = input_string

    def clean_buffer(self):

        input_length = len(self.input_string)
        if input_length > 50:
            return False

    def clean_sql(self):

        if any(word in self.input_string for word in self.bad_words):
            return False

    def clean_meta(self):

        if any(char in self.input_string for char in self.bad_char):
            return False
 
