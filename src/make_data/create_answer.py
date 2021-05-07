import pandas as pd

QnA = pd.read_csv('rsc/data_mapping/QnA.csv').drop('Unnamed: 0', axis = 1).fillna('')
QnA = QnA.rename(columns={'장학종류':'title','장학혜택(금액)':'장학혜택'})
answer_button = pd.read_csv('rsc/sql/answer_button.csv').drop('Unnamed: 0', axis = 1).fillna('')

titles = []
documents = []
urls = []

title = ''
for row in QnA.T:
    for col in QnA:
        if QnA[col][row] == '해당없음' or QnA[col][row] == '':
            continue
        if(col == 'title'):
            title = QnA[col][row]
            titles.append(title)
            documents.append(title + ' 안내입니다. 원하는 내용을 선택해주세요.')
            idx = answer_button[answer_button['button_name'] == title].index[0]
        else:
            titles.append(title + ' ' + col)
            documents.append(QnA[col][row])
            idx = answer_button[answer_button['button_name'] == title + ' ' + col].index[0]
        url = answer_button['button_url'][idx]
        urls.append(url)

data = {'title':titles, 'document':documents, 'url':urls}
answer = pd.DataFrame(data, columns = ['title', 'document', 'url'])
answer.to_csv('rsc/sql/answer.csv')

inner = pd.merge(answer_button, answer['url'], left_on='button_url', right_on='url', how='inner').drop('url', axis=1)
outer = pd.merge(answer_button, answer['url'], left_on='button_url', right_on='url', how='outer')
left = outer[outer['url'].isna()].drop('url', axis=1)
outside = left[left['button_name'].str.contains('사이트로 이동')]
outside['button_name'] = '사이트로 이동'
answer_button = pd.concat([inner, outside])
answer_button.to_csv('rsc/sql/answer_button.csv')
