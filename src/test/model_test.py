from src.model.intentNerModel import IntentNerModel
intentNer = IntentNerModel()
test_datas = [
  '2차 국가장학금',
  '헬로우',
  'ㄱㅐ',
  '2차 국가장학금 어떻게 되니?',
  ' 헬로우 2차 국가장학금',
  ' ㄱㅐ 2차 국가장학금',
  ' 2차 국가장학금 ㄱㅐ',
  '2차 국가장학금 지원자격',
  '지원자격 2차 국가장학금',
  '2차 국가장학금 지원자격 어떻게 되니?',
  '지원자격 2차 국가장학금 어떻게 되니?',
  'ㄱㅐ 2차 국가장학금 지원자격 어떻게 되니?',
  '2차 국가장학금 ㄱㅐ 지원자격 어떻게 되니?',
  '2차 국가장학금 지원자격 ㄱㅐ 어떻게 되니?',
  '2차 국가장학금 지원자격 어떻게 되니? ㄱㅐ',
  'ㄱㅐ 지원자격 2차 국가장학금 어떻게 되니?',
  '지원자격 ㄱㅐ 2차 국가장학금 어떻게 되니?',
  '지원자격 2차 국가장학금 ㄱㅐ 어떻게 되니?',
  '지원자격 2차 국가장학금 어떻게 되니? ㄱㅐ',
  '국가 장학금 언제 나와요?',
  '국장 금액이 얼마나 되나요?',
  '씨발.. 장학금 언제 나오냐',
  '아니 돈 얼마나 줌? 국장임',
  '높은 곳에서는 새가 날고 낮은 곳에서 물이 흐르니 내 성적은 바닥을 기며 혀를 낼름 거리는데 장학금 받을 수 있을까?'
]
for q in test_datas:
  predict = intentNer.input2intentNer(q)
  intent_name = ''
  ner_predicts, ner_tags = [], []
  temp = {}
  for data in predict:
    key, value = list(data.keys())[0], list(data.values())[0]
    if 'intent' in value: intent_name = key
    else: temp[key] = temp[key] + value if key in temp else value
  for k, v in temp.items(): ner_predicts.append((v, k)), ner_tags.append(k)

  print(intent_name)
  print(ner_predicts)
  print(ner_tags)
  print()
