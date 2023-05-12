import psycopg
from psycopg.rows import dict_row
import os

# This class helps us interact with the database.
# It wraps the underlying psycopg library that we are using.

# If the below seems too complex right now, that's OK.
# That's why we have provided it!
class DatabaseConnection:
    DATABASE_NAME = "My_first_project" 

    # This method connects to PostgreSQL using the psycopg library. We connect
    # to localhost and select the database name given in argument.
    def connect(self):
        try:
            self.connection = psycopg.connect(
                f"postgresql://localhost/{self.DATABASE_NAME}",#connection to postgres through local host
                row_factory=dict_row)#this tells psycopg that instead of returning a tuple, it should return dict.
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! " \
                    f"Did you create it using `createdb {self.DATABASE_NAME}`?")

    # This method seeds the database with the given SQL file.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename):#opens sql file and runs it
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:#way of executing sql in a database
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()#this commits it to database

    # This method executes an SQL query on the database.
    # It allows you to set some parameters too. You'll learn about this later.
    def execute(self, query, params=[]):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:#is this a sql command that yielded a data response?
                result = cursor.fetchall()#if so, then add the records to result var
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'

    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
