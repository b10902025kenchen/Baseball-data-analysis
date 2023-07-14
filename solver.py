import numpy as np
# Set parameters
INNINGS = [6, 7, 8, 9]
ATTACKS = [0, 1]
GAPS = [-1, 0, 1]
MODELS = [1, 2] # 1: MLB, 2: CTBC
OUTS = 0
BASE = 2

import pandas as pd
import csv
all_results = []
for INNING in INNINGS:
    for ATTACK in ATTACKS:
        results = []
        for GAP in GAPS:
            for MODEL in MODELS:
                # Read files
                if ATTACK == 1:
                    WPCT = pd.read_excel('MLB_WPCT_home.xlsx')
                else:
                    WPCT = pd.read_excel('MLB_WPCT_away.xlsx')
                if MODEL == 1:
                    P24 = pd.read_excel('MLBP24.xlsx')
                else:
                    P24 = pd.read_excel('P24.xlsx')
                BUNT_TRANS = pd.read_excel('bunt_transfer.xlsx')

                # Extract values
                W = WPCT.iloc[INNING * 2 + ATTACK - 2, GAP+9: GAP+14].values
                W_arr = np.array(W)
                trans_arr = []
                swing_arr = []
                bunt1_arr = []
                bunt2_arr = []
                bunt3_arr = []
                if OUTS == 0 and BASE == 1:
                    trans_arr = np.array([0.15, 0.68, 0.17])
                    swing = P24.iloc[1, 8:13]
                    swing_arr = np.array(swing)
                    bunt1 = P24.iloc[9, 8:13]
                    bunt1_arr = np.array(bunt1)
                    bunt2 = P24.iloc[10, 8:13]
                    bunt2_arr = np.array(bunt2)
                    bunt3 = P24.iloc[4, 8:13]
                    bunt3_arr = np.array(bunt3)
                if OUTS == 0 and BASE == 12:
                    trans_arr = np.array([0.25, 0.62, 0.13])
                    swing = P24.iloc[4, 8:13]
                    swing_arr = np.array(swing)
                    bunt1 = P24.iloc[12, 8:13]
                    bunt1_arr = np.array(bunt1)
                    bunt2 = P24.iloc[14, 8:13]
                    bunt2_arr = np.array(bunt2)
                    bunt3 = P24.iloc[7, 8:13]
                    bunt3_arr = np.array(bunt3)
                if OUTS == 0 and BASE == 2:
                    trans_arr = np.array([0.15, 0.71, 0.14])
                    swing = P24.iloc[2, 8:13]
                    swing_arr = np.array(swing)
                    bunt1 = P24.iloc[10, 8:13]
                    bunt1_arr = np.array(bunt1)
                    bunt2 = P24.iloc[11, 8:13]
                    bunt2_arr = np.array(bunt2)
                    bunt3 = P24.iloc[5, 8:13]
                    bunt3_arr = np.array(bunt3)
                if OUTS == 1 and BASE == 1:
                    trans_arr = np.array([0.15, 0.68, 0.17])
                    swing = P24.iloc[9, 8:13]
                    swing_arr = np.array(swing)
                    bunt1 = P24.iloc[17, 8:13]
                    bunt1_arr = np.array(bunt1)
                    bunt2 = P24.iloc[18, 8:13]
                    bunt2_arr = np.array(bunt2)
                    bunt3 = P24.iloc[12, 8:13]
                    bunt3_arr = np.array(bunt3)
                val1 = np.dot(W_arr, swing)
                val2 = np.dot(W_arr, bunt2)
                tmp = np.array([np.dot(W_arr,bunt1), np.dot(W_arr, bunt2), np.dot(W_arr, bunt3)])
                val3 = np.dot(trans_arr, tmp)
                # if val1 <= val2 or val1 <= val3:
                print("INNING:", INNING, "ATTACK:", ATTACK, "GAP:", GAP, "OUTS:", OUTS, "BASE:", BASE, "MODEL:", MODEL)
                print("swing:", val1)
                print("success bunt:", val2)
                print("bunt:", val3)
                print("============================================")
                results.append(val1)
                results.append(val2)
                results.append(val3)
        all_results.append(results)

# Write output to csv
with open('output2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in all_results:
        writer.writerow(row)