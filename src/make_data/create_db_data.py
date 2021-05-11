import pandas as pd
from src.config.DatabaseConfig import *
df = pd.read_excel('rsc/data_mapping/ward.xlsx').fillna('')

for i in range(6, 10):
    df = df.drop('Unnamed: ' + str(i), axis=1)

main_url = 'http://' + DB_HOST + '/'
urls = {}
b_titles, b_names, b_urls = [], [], []
a_titles, a_documents, a_urls = [], [], []
options = {'선발기준':'requirement', '장학혜택':'advantage', '제출서류':'document'}

def b_InputData(t, b, u):
    b_titles.append(t)
    b_names.append(b)
    b_urls.append(u)

def a_InputData(t, d, u):
    a_titles.append(t)
    a_documents.append(d)
    a_urls.append(u)

for row in df.T:
    title, name, url = df['title'][row], df['button_name'][row], df['url'][row]
    # 장학금 url 추가
    if title == '':
        urls[name] = main_url + url + '/'
        b_InputData('', name, urls[name])
        a_InputData(name, name + ' 안내입니다. 원하는 내용을 선택해주세요.', urls[name])
    elif title in urls:
        # 외부 장학금
        if 'http' in str(url):
            b_InputData(title, name + ' 사이트로 이동', url)
        # 기본 장학금 안내 문구
        else:
            urls[name] = urls[title] + str(url) + '/'
            b_InputData(title, name, urls[name])
            a_InputData(name, name + ' 안내입니다. 원하는 내용을 선택해주세요.', urls[name])
            # 상세 설명부
            for k, v in options.items():
                if df[k][row] != '':
                    temp = name + ' ' + k
                    urls[temp] = urls[name] + v + '/'
                    b_InputData(name, temp, urls[temp])
                    a_InputData(temp, df[k][row], urls[temp])
  
answer_button = {'title':b_titles, 'button_name':b_names, 'button_url':b_urls}
answer_button = pd.DataFrame(answer_button)
answer = {'title':a_titles, 'document':a_documents, 'url':a_urls}
answer = pd.DataFrame(answer)
answer_button.to_excel('rsc/sql/answer_button.xlsx')
answer.to_excel('rsc/sql/answer.xlsx')