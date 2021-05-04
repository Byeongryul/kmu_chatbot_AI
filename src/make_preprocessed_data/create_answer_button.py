import pandas as pd

QnA = pd.read_csv('rsc/data_mapping/QnA.csv').drop('Unnamed: 0', axis = 1)
title = QnA['장학종류']
document = QnA['장학종류'] + ' 안내입니다. 원하는 내용을 선택해주세요.'
url = 'http://127.0.0.1/scholarship/' + QnA['장학종류']
total = pd.DataFrame(title)
total = total.rename(columns={'장학종류':'title'})
total['document'] = document
total['url'] = url


#for row in QnA.T:
#    for col in QnA:
        
#        print(QnA[col][row])
    
print(total)