#!/usr/bin/env pyhton3

import sqlite3 

class Database: 
    def __init__(self,database_name):
        self.connection = sqlite3.connect(database_name,check_same_thread=False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,type,value,traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
    
    def create_table(self,_tablename):
        self.cursor.execute(
            """CREATE TABLE {}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(
                _tablename
            ) 
        )
    
    def add_column(self,_tablename,_columnname,_columntype):
        self.cursor.execute(
            """ALTER TABLE {} ADD COLUMN {} {};""".format(_tablename,_columnname,_columntype))
    
    def insert_3(self,_tablename,_column1,_column2,_column3,_value1,_value2,_value3):
        self.cursor.execute(
            """INSERT INTO {}({},{},{}) VALUES (
                {},{},{}
            );""".format(_tablename,_column1,_column2,_column3,_value1,_value2,_value3))

    def insert_4(self,_tablename,_column1,_column2,_column3,_column4,_value1,_value2,_value3,_value4):
        self.cursor.execute(
            """INSERT INTO {}({},{},{},{})VALUES (
                '{}','{}',{},{}
            )

            ;""".format(_tablename,_column1,_column2,_column3,_column4,_value1,_value2,_value3,_value4))