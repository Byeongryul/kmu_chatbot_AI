from eunjeon import Mecab
from tqdm import tqdm
import pandas as pd
import argparse
import csv
import os

nlp = Mecab()

def preprocessing(fname):
    input_dir = 'rsc/training_data/' + fname + '.csv'
    output_dir = 'rsc/preprocessed_data/' + fname + '.csv'

    f = open(input_dir, 'r', encoding='utf-8')
    qs = f.readlines()

    word = []; POS = []; Tag = []; sentence = []
    sen_num = 0
    for q in tqdm(qs):
        q = q.replace('>', '<')
        vocabs = q.split('<')
        for vocab in vocabs:
            if ':' in vocab:
                ps = nlp.pos(vocab.split(":")[0])
                for p in ps:
                    sentence.append('sen_' + str(sen_num)), word.append(p[0]), POS.append(p[1])
                    if(p[0] == 'intent'):
                        Tag.append(vocab.split(':')[1])
                    else:
                        Tag.append('B-' + vocab.split(":")[1] if ps[0] == p else 'I-' + vocab.split(":")[1])
            else:
                ps = nlp.pos(vocab)
                for p in ps:
                    sentence.append('sen_' + str(sen_num)), word.append(p[0]), POS.append(p[1])
                    Tag.append('O')
        sen_num += 1

    datas = {'Sentence #': sentence,'Word': word,'POS': POS,'Tag': Tag}

    df = pd.DataFrame(datas)
    df.columns = ['Sentence #', 'Word', 'POS', 'Tag']
    df.to_csv(output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', type=str, default='test')
    args = parser.parse_args()
    preprocessing(args.fname)