import numpy as np
import argparse
import csv
import os

#파일 오픈하고 리스트에 값 저장하기
def open_file() :
    files = os.listdir('rsc/low_data/')
    files_csv = [file for file in files if file.endswith(".csv")]
    all_datas = {}

    for file_csv in files_csv:
        #데이터 수집
        datas = []
        with open('rsc/low_data/' + file_csv, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                data = str(row[0]).strip() 
                datas.append(data)

            all_datas[file_csv.split('.')[0]] = datas
    return all_datas

def makeQ(datas, sizes, i):
    now = {}
    for key, values in sizes.items():
        now[key] = i % values
    data = {}
    for key, values in now.items():
        data[key] = datas[key][now[key]]
    result = []
    result.append('<intent:INT_WORD> '+data['word'])
    result.append('<intent:INT_GRE> '+data['hello'])
    result.append('<intent:INT_ABU> '+data['abu'])

    result.append('<intent:INT_WORD> '+data['word']+' '+ data['end_mark'])
    result.append('<intent:INT_WORD> '+data['hello'] +' '+ data['word'] )
    result.append('<intent:INT_ABU> '+data['abu']+' '+data['word'])
    result.append('<intent:INT_ABU> '+data['word'] +' '+data['abu'])
    result.append('<intent:INT_WORD> '+data['word'] +' '+ data['qu'])   
    result.append('<intent:INT_WORD> '+data['qu'] +' '+ data['word'])

    result.append('<intent:INT_WORD> '+data['word'] +' '+ data['qu']+' '+data['end_mark'])
    result.append('<intent:INT_WORD> '+data['qu']+' '+data['word'] +' '+ data['end_mark'])

    result.append('<intent:INT_ABU> '+data['abu'] +' '+data['word'] +' '+ data['qu']+' '+data['end_mark'])
    result.append('<intent:INT_ABU> '+data['word']+' '+data['abu'] +' '+ data['qu']+' '+data['end_mark'])
    result.append('<intent:INT_ABU> '+data['word']+' ' + data['qu']+' '+data['abu']+' '+data['end_mark'])
    result.append('<intent:INT_ABU> '+data['word']+' ' + data['qu']+' '+data['end_mark']+' '+data['abu'])

    result.append('<intent:INT_ABU> '+data['abu']+' '+ data['qu']+' '+data['word'] +' '+data['end_mark'])
    result.append('<intent:INT_ABU> ' + data['qu']+' '+data['abu']+' '+data['word']+' '+data['end_mark'])
    result.append('<intent:INT_ABU> '+ data['qu']+' '+data['word']+' ' +data['abu']+' '+data['end_mark'])
    result.append('<intent:INT_ABU> ' + data['qu']+' '+data['word']+' '+data['end_mark']+' '+data['abu'])
    return result

def make_training_data(line_size, fname):
    result = []
    datas = open_file()
    print(datas.keys())
    
    sizes = {}
    for key, values in datas.items():
        sizes[key] = len(values)   

    Q = len(makeQ(datas, sizes, 0))
    if line_size == -1: line_size = Q 
    for i in range(int(line_size/Q + 1)):
        result += makeQ(datas, sizes, i)
    
    
    if fname == 'test':
        output_dir = 'rsc/training_data/' + fname + '.csv'
    else:
        output_dir = 'rsc/training_data/' + fname + '_' + str(line_size) + '.csv'
    file = open(output_dir, "w", encoding='utf-8')
    for i in result[:line_size] :
        file.write(i + '\n')
    file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', type=str, default='test')
    parser.add_argument('--line_size', type=int, default=-1)
    args = parser.parse_args()
    make_training_data(args.line_size, args.fname)