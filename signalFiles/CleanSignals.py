import os
import pandas as pd
import re

os.chdir('/Users/meganstiles/Desktop/github/DSI-Religion-2017/modelOutputSingleDocs/307 Signals/')

signals = pd.read_csv('signalOutput-coco_3_cv_3_netAng_30_twc_10_tfidfNoPro_pronoun_bin_1-20B770.csv')

signals = signals.drop(signals.columns [[0,2,3,4,]], axis=1)

test = signals.loc[[1]][[0]]

for i in range(0,len(signals)):
    name = signals['groupId'][i]
    name = re.sub('_train', '', str(name))
    name = re.sub('_test', '', name)
    signals['groupId'][i] = name

#Read in Rank filte
os.chdir('/Users/meganstiles/Desktop/github/DSI-Religion-2017/refData/')
ranks = pd.read_csv('docRanks.csv') 

for i in range(0,len(ranks)):
    name = ranks['groupName'][i]
    name = re.sub('.txt', '', name)
    ranks['groupId'][i] = name

clean = pd.merge(signals, ranks, how = 'inner', on='groupId')    
    
groups = ['ACLU', 'Rabbinic', 'SeaShepherds', 'Unitarian', 'WBC', 'MalcolmX', 'YV', 'JohnPiper',
'Bahai', 'DorthyDay', 'LiberalJudaism', 'AEU', 'MehrBaba', 'ISIS', 'Shepherd', 'Anderson']

for group in groups:
    for i in range(0,len(clean)):
        if group in clean['groupId'][i]:
            clean['groupName'][i] = group

clean.to_csv('SingleDocSignals.csv')

os.chdir('/Users/meganstiles/Desktop/github/DSI-Religion-2017/modelOutputSingleDocs/307 Signals/')
Four= pd.read_csv('SingleDocSignals.csv')
#Convert to 4 classes instead

#Drop 3 class column

i = 0
for i in range(0,len(Four)):
    score = Four['rank'][i]
    if score == 1 or score == 2:
        score = 'low'
        Four['rank'][i] = score
    if score == 3 or score ==4:
        score = 'mid'
        Four['rank'][i] = score
    if score == 5 or score == 6:
        score = 'high'
        Four['rank'][i] = score
    if score == 7 or score == 8 or score ==9:
        score = 'highest'
        Four['rank][i'] = score

Four.to_csv('fourclasssignals.csv')