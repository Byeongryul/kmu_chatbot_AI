from src.model.intentNerModel import IntentNerModel

intentNer = IntentNerModel()
datas = intentNer.input2intentNer('장학금 받고 싶다.')

intent_name = ''
ner_predicts = []
ner_tags = []
for data in datas:
    key = list(data.keys())[0]
    value = list(data.values())[0]
    if 'intent' in value:
        intent_name = key
    else:
        ner_predicts.append((value, key))
        ner_tags.append(key)    
    

print(intent_name)
print(ner_predicts)
print(ner_tags)