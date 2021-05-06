import pandas as pd

QnA = pd.read_csv('rsc/data_mapping/QnA.csv').drop('Unnamed: 0', axis = 1)
QnA = QnA.rename(columns={'장학종류':'title','장학혜택(금액)':'장학혜택'})
QnA['title'] = QnA['title'].apply(lambda x:x.replace(" ", ''))
QnA = QnA.fillna('')

titles = []
documents = []
urls = []

ward = ''
url = 'http://127.0.0.1/scholarship/'
eng = {'선발기준':'requirement', '장학혜택':'advantage', '제출서류':'document'}
for row in QnA.T:
    for col in QnA:
        if QnA[col][row] == '해당없음' or QnA[col][row] == '':
            continue
        if(col == 'title'):
            ward = QnA[col][row]
            titles.append(ward)
            documents.append(ward + ' 안내입니다. 원하는 내용을 선택해주세요.')
            urls.append(url + ward)
        else:
            titles.append(ward + ' ' + col)
            documents.append(QnA[col][row])
            urls.append(url + ward + '/' + eng[col])

data = {'title':titles, 'document':documents, 'url':urls}
total = pd.DataFrame(data, columns = ['title', 'document', 'url'])
print(total)
total.to_csv('rsc/data_mapping/QnA_mapping.csv')