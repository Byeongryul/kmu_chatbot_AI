import pandas as pd
from src.config.DatabaseConfig import *
buttons = pd.read_csv('rsc/data_mapping/scholaship_button_mapping.csv').drop('Unnamed: 0', axis = 1).fillna('')
buttons.columns = buttons.loc[0]
buttons = buttons.drop(index = 0)

url = 'http://' + DB_HOST + '/'
urls = {}
titles, button_names, button_urls = [], [], []

def inputData(t, b, u):
    titles.append(t)
    button_names.append(b)
    button_urls.append(u)

for row in buttons.T:
    title, button_name, button_url = buttons['title'][row], buttons['button_name'][row], buttons['button_url'][row]
    if title == '':
        urls[button_name] = url + button_url + '/'
        inputData('', button_name, urls[button_name])
    elif title in urls:
        if button_name != '':
            urls[button_name] = urls[title] + button_url + '/'
            inputData(title, button_name, urls[button_name])
        else:
            if button_url != '':
                urls[title + '_url'] = button_url + '/'
                inputData(title, title + '_사이트로 이동', urls[title + '_url'])
            else:
                options = {'선발기준':'requirement', '장학혜택':'advantage', '제출서류':'document'}
                for k, v in options.items():
                    urls[title + ' ' + k] = urls[title] + button_url + v + '/'
                    inputData(title, title + ' ' + k, urls[title + ' ' + k])
data = {'title':titles, 'button_name':button_names, 'button_url':button_urls}
answer_button = pd.DataFrame(data)
answer_button.to_csv('rsc/sql/answer_button.csv')