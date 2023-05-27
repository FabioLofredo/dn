from pynput.keyboard import Key, Controller
import pandas as pd
import time
import numpy as np
import os



#notas = pd.read_csv('c:/notas.csv',sep="\t")
notas = pd.read_excel('notas.xlsx',sheet_name=0, header=None)
keyboard = Controller()

#clean the notes
notas.fillna(np.nan,inplace=True)
notas[notas.columns[0]] = notas[notas.columns[0]].astype('Int64')
notas[notas.columns[0]] = notas[notas.columns[0]].astype(str)
notas[notas.columns[0]].replace("<NA>", " ", inplace=True)
time.sleep(2)

for i in range(len(notas)):
    #type the grade
    for x in str(notas[notas.columns[0]].iloc[i]):
        keyboard.type(x)
    #uses TAB for skip the selection  
    if i!=len(notas)-1: 
        for j in range(5):
            time.sleep(0.1)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.1)
time.sleep(10)

