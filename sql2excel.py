#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlparse
# sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
import pandas as pd
import numpy as np
import os
class Sql2Excel():
    def __init__(self):
        self.SQL_statement = ''
        self.cols = None
        self.primary_key_list = []
        self.keys = []
        # field,description,datatype,num1,num2,key,isnull
        self.excel_fields = 7
        self.content_list = []
        self.content_arr = None
        return
    @classmethod
    def read_from_sql(self,SQL_create_table):
        self.SQL_statement = SQL_create_table
        self.cols,self.primary_key_list = self.get_columns(self.SQL_statement)
        self.keys = self.extract_primary_keys(self.primary_key_list)
        if(self.cols[0]):
            # field,description,datatype,num1,num2,key,isnull
            self.excel_fields = len(self.col2dict(self.cols[0]).keys()) # should be 7
        # print(self.col2dict(self.cols[0]))
        self.content_list = []
        for col in self.cols:
            for v in self.col2dict(col).values():
                self.content_list.append(v)
        self.content_arr = np.array(self.content_list).reshape((-1,self.excel_fields))
        # print(self.content_arr)
        return
    @classmethod 
    def to_np_arr(self):
        return self.content_arr
    @classmethod
    def to_csv(self):
        c_name_en = ['field', 'description', 'datatype', 'num1', 'num2', 'key', 'isnull']
        c_name_zh = ['名称_en','描述_zh','数据类型','精度','标度','主键','NULL值']
        df = pd.DataFrame(self.content_arr,columns=c_name_en)
        df.to_csv('generated.csv', index=True, header=True,encoding='utf-8')
        return
    @classmethod
    def to_markdown(self):
        # This requires pandas version above 1.0.0
        # pip install --upgrade pandas
        # https://pandas.pydata.org/docs/whatsnew/v1.0.1.html
        c_name = ['field', 'description', 'datatype', 'num1', 'num2', 'key', 'isnull']
        df = pd.DataFrame(self.content_arr,columns=c_name)
        print(df.to_markdown())
        return
    @classmethod
    def demo(self):
        f = open('sql.txt','r')
        print("Read from ./sql.txt.")
        SQL_create_table = f.read()
        f.close()
        self.read_from_sql(SQL_create_table)
        print("Export to clipboard..You can now PASTE.")
        self.to_clipboard()
        print("Export to generated.csv.")
        self.to_csv()
        # export to markdown requires pandas version >=1.0.0,you should first 'pip install --upgrade pandas'.
        # print(self.to_markdown)
        return
    @classmethod
    def test(self):
        f = open('sql.txt','r')
        print("Read from ./sql.txt.")
        SQL_create_table = f.read()
        f.close()
        self.read_from_sql(SQL_create_table)
        print("Export to clipboard..You can now PASTE.")
        self.to_clipboard()
        return
    @classmethod
    def to_clipboard(self):
        c_name = ['field', 'description', 'datatype', 'num1', 'num2', 'key', 'isnull']
        # df = pd.DataFrame(self.content_arr,columns=c_name)
        # df = pd.DataFrame(self.content_arr,columns=None)
        df = pd.DataFrame(self.content_arr,columns=c_name)
        df['description'] ='描述'
        df.to_clipboard(excel=True, index=False, header=False)
        # press 'delete', delete first row
        # 这里应该是能复制到系统粘贴板上的，Ubuntu vscode的ipynb这个功能看起来有问题
        return
    @classmethod
    def extract_definitions(self,token_list):
        # assumes that token_list is a parenthesis
        definitions = []
        tmp = []
        par_level = 0
        last =''
        is_meet_primary_key = False
        primary_key_list = []
        for token in token_list.flatten():
            if (str.lower(str(token))=='primary'):
                is_meet_primary_key =True
            if token.is_whitespace:
                continue
            elif token.match(sqlparse.tokens.Punctuation, '('):
                par_level += 1
                continue
            if token.match(sqlparse.tokens.Punctuation, ')'):
                if par_level == 0:
                    break
                else:
                    par_level += 1
            elif is_meet_primary_key:
                # 注意token是Token类型，不是str类型，直接与str类型的比对会发生错误
                    primary_key_list.append(str(token))
            elif token.match(sqlparse.tokens.Punctuation, ',') and not str.isdigit(last):
                if tmp:
                    definitions.append(tmp)
                # for t in tmp:
                #     print(str(t),end='')
                # print("")
                tmp = []
            else:
                tmp.append(token)
            last=str(token)
        if tmp:
            definitions.append(tmp)
        for k in primary_key_list:
            if str(k)==',':
                primary_key_list.remove(k)
        return definitions,primary_key_list
    @classmethod
    def get_columns(self,SQL):
        parsed = sqlparse.parse(SQL)[0]
        # extract the parenthesis which holds column definitions
        _, par = parsed.token_next_by(i=sqlparse.sql.Parenthesis)
        columns,primary_key_list = self.extract_definitions(par)
        return columns,primary_key_list
    @classmethod
    def extract_primary_keys(self,primary_key_list):
        primary_keys = []
        for k in primary_key_list:
            if(str.lower(k)!="primary" and str.lower(k)!="key"):
                primary_keys.append(str(k))
        return primary_keys
    @classmethod
    def extract_field_en_from_col(self,col):
        return str(col[0])
    @classmethod
    def extract_type_from_col(self,col):
        return str(col[1])
    @classmethod
    def get_comma_pos_from_col(self,col):
        pos_list = [i for i,x in enumerate(col) if str(x)==","]
        return pos_list[0]
    @classmethod
    def extract_num1_num2_from_col(self,col):
        num1, num2 = str(col[2]), 0
        is_common = "," not in [str(x) for x in col]
        if not is_common:
            num1 = str(col[self.get_comma_pos_from_col(col)-1])
            num2 = str(col[self.get_comma_pos_from_col(col)+1])
        return num1,num2
    @classmethod
    def getConvertedType_sybase2Gbase(self,type):
        type_convert_dict = {'varchar':'VarChar',
        'decimal':'Decimal','char':'Char','smallint':'SmallInt',
        'bigint':'BigInt','integer':'Int'}
        type = str.lower(type)
        for key, value in type_convert_dict.items():
            type = type.replace(key,value)
        return type
    @classmethod
    def extract_isNull_from_col(self,col):
        return 'not' not in str.lower(str(col[-1])).split()
    @classmethod
    def col2dict(self,col):
        col_dict = {
            'field':self.extract_field_en_from_col(col),
            'description':'',
            'datatype':self.getConvertedType_sybase2Gbase(self.extract_type_from_col(col)),
            'num1':self.extract_num1_num2_from_col(col)[0],
            'num2':self.extract_num1_num2_from_col(col)[1],
            'key': 'Y' if (self.extract_field_en_from_col(col) in self.keys) else 'N',
            'isnull':'Y' if self.extract_isNull_from_col(col) else 'N'
        }
        data_type = str(col_dict['datatype'])
        if(data_type == 'BigInt' or data_type == 'SmallInt' or data_type == 'SmallInt'):
            col_dict['num1'] = 'xxx'
        return col_dict
        
if __name__ == '__main__':
    sql2excel = Sql2Excel
    # sql2excel.test()
    sql2excel.demo()
    sql2excel.to_markdown()