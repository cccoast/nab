# -*- coding:utf-8 -*- 
import sys
if '..' not in sys.path:
    sys.path.append('..')
from future_mysql.dbBase import DB_BASE

from sqlalchemy import Column, Integer, String, DateTime, Numeric, Index, Float
from sqlalchemy import Table

import pandas as pd
import numpy as np

trans = lambda x: x.encode('utf8') if isinstance(x,unicode) else x

integer_t = 4
double_t  = 8
long_long_string_t = 512
long_string_t = 128
medium_long_string_t = 64
medium_string_t = 32
account_string_t = 24
short_string_t = 16
date_string_t = 12
status_string_t = 10
mini_string_t  = 6
money_string_t = 10
char_string_t = 1

###base 
class nba(DB_BASE):

    def __init__(self, db_name='nba', table_name=None):
        super(nba, self).__init__(db_name)
        self.table_struct = None
        self.col_sizes = []
        
    def create_table(self):
        if self.table_struct is not None:
            self.table_struct = self.quick_map(self.table_struct)

    def check_table_exist(self):
        if self.table_struct is not None:
            return self.table_struct.exists()
        else:
            raise Exception("no table specified")
        
    def get_row_counts(self):
        session = self.get_session()
        n = session.query(self.table_struct).count()
        session.close()
        return n
    
    def get_col_names(self):
        return [ trans(i) for i in self.get_column_names(self.table_struct)]
    
    def get_col_length(self):
        return len(self.get_column_names(self.table_struct))
    
    def get_col_sizes(self):
        return self.col_sizes

def import_data():
    pass

if __name__ == '__main__':
    pass    
    
    
    