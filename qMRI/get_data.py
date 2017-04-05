import os, sys
import pandas as pd
import numpy as np

def create_df(data_main_dir, pH_dir,list_files):
    CEST_df = pd.DataFrame()
    for file in list_files:
        if not file.startswith('.'):
            d = data_main_dir + pH_dir+ '/' + file
            #print(d)
            df  = pd.read_csv(d,header=None).T
            df['Conc'] = file[0:5]
            CEST_df = pd.concat([CEST_df,df], axis=0, join='outer', join_axes=None, ignore_index=True)
    return CEST_df

def load_data(pH_directories,data_main):
    DATA = pd.DataFrame()
    for pH in pH_directories:
        files = os.listdir(data_main + pH)
        df = create_df(data_main,pH,files)
        df['pH'] = pH[2:]
        DATA = pd.concat([DATA,df], axis=0, join='outer', join_axes=None, ignore_index=True)

    Spectra = DATA.drop(['Conc', 'pH'], axis = 1).values.T
    Concentration = np.array(DATA['Conc'].values).astype(float)
    pH = np.array(DATA['pH'].values).astype(float)
    ppm = pd.read_csv(data_main + 'ppm.txt',header=None).values
    return Spectra, Concentration, pH, ppm
