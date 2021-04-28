
import pandas as pd
import os
dir_name = os.getcwd() + '/rsc/data_mapping/'

files = os.listdir(dir_name)
files_xlsx = [file for file in files if file.endswith(".xlsx")]
if len(files_xlsx) != 0:
    for file_xlsx in files_xlsx:
        file_xlsx = dir_name + file_xlsx
        df = pd.read_excel(file_xlsx, header=None)
        df.to_csv(file_xlsx.split('.xlsx')[0] + '.csv')
        os.remove(file_xlsx)