import os
import pymysql
import pandas as pd
from src.config.DatabaseConfig import * # DB 접속 정보 불러오기
from sqlalchemy import create_engine

def open_file() :
    files = os.listdir('rsc/sql/')
    files_excel = [file for file in files if file.endswith(".xlsx")]
    all_datas = {}

    for file_excel in files_excel:
        all_datas[file_excel.split('.xlsx')[0]] = pd.read_excel('rsc/sql/'+file_excel).fillna('').drop('Unnamed: 0', axis=1)
        
    return all_datas

# 학습 데이터 초기화
def all_clear_db_data(db, table_names):
    # 기존 학습 데이터 삭제
    
    with db.cursor() as cursor:
        for table_name in table_names:
            sql = 'delete from ' + table_name
            cursor.execute(sql)

    # auto increment 초기화
    sql = '''
    ALTER TABLE answer_button AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)


# db에 데이터 저장
def insert_data(db, datas):
    link = "mysql+pymysql://%s:%s@%s:3306/%s"%(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
    engine = create_engine(link, encoding='utf-8')
    conn = engine.connect()
    for data in datas:
        datas[data].to_sql(data, con=engine, if_exists='append', index= False)

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4'
    )
    # DB 엑셀 파일 불러오기
    datas = open_file()
    # 기존 학습 데이터 초기화
    all_clear_db_data(db, datas.keys())
    insert_data(db, datas)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()

