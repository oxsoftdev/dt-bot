import os
import pyodbc

from .schemas import public_api, ws


class Store:

    def __init__(self):
        _cs = 'DRIVER={DRIVER};SERVER={SERVER};PORT={PORT};UID={UID};PWD={PWD};'
        self.cnxn = pyodbc.connect(_cs.format(**settings))
        # schemas
        self.public_api = public_api(self.cnxn)
        self.ws = ws(self.cnxn)

    @property
    def settings(self):
        return {
            'DRIVER': '{ODBC Driver 13 for SQL Server}',
            'SERVER': os.environ['MSSQL_SERVER'],
            'PORT': os.environ['MSSQL_SERVER_PORT'],
            'UID': os.environ['MSSQL_SERVER_UID'],
            'PWD': os.environ['MSSQL_SERVER_PWD']
        }
