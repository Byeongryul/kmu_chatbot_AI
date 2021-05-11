import pandas as pd
from src.config.DatabaseConfig import * # DB 접속 정보 불러오기


link = "mysql+pymysql://%s:%s@%s:3306/%s"%(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
datas = pd.read_sql_table('answer', link)

urlpatterns = []

for row in datas.T:
    url = datas['url'][row].split('scholarship/')[1]
    #urlpatterns.append(path(url, views.scholarship, {'title':datas['title'][row]}))
    print(url)

# def scholarship(url):
#     sql = 'select title from answer where url like "http://' + DB_HOST + '/scholarship/'+ url +'";'
#     print(sql)
#     title = pd.read_sql_query(sql, link)
#     return title

# print(scholarship('inside/enrolled/linc/requirement/'))

'''
# views 파일
from testapp.models import *
from testapp.views import make_answer_json
from django.http import JsonResponse

# Create your views here.
def scholarship(request, title):
    result_json = make_answer_json(title)
    return JsonResponse(result_json, json_dumps_params={'ensure_ascii': False})
'''
'''
# urls 파일
from django.urls import path
from scholarship import views

import pandas as pd
from config.DatabaseConfig import * # DB 접속 정보 불러오기
link = "mysql+pymysql://%s:%s@%s:3306/%s"%(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
datas = pd.read_sql_table('answer', link)

urlpatterns = []

for row in datas.T:
    url = datas['url'][row].split('scholarship/')[1]
    urlpatterns.append(path(url, views.scholarship, {'title':datas['title'][row]}))
'''