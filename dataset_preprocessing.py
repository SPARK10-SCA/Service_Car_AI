import csv 
import pandas as pd
from tqdm import tqdm
cnt=0
w = open('custom.csv','w', newline='', encoding='utf-8')
wr = csv.writer(w)
dummy_data = pd.read_csv("./price_dataset_large.csv")
newcsv = pd.DataFrame(columns=['MODELTYPE', 'MILEAGE', 'COMPANY',
                      'FIRSTDAY','REPAIRDAY', 'CARNAME', 'PART', 'SEVERITY', 'HQ', 'PRICE'])
count = 0 

for i in tqdm(range(len(dummy_data))) :
    MODELTYPE =  dummy_data['MODELTYPE'][i]
    MILEAGE = dummy_data['MILEAGE'][i]
    COMPANY = dummy_data['COMPANY'][i]
    FIRSTDAY = dummy_data['FIRSTDAY'][i]
    REPAIRDAY = dummy_data['REPAIRDAY'][i]
    CARNAME = dummy_data['CARNAME'][i]
    PART = dummy_data['PART'][i]
    SEVERITY = dummy_data['SEVERITY'][i]
    HQ = dummy_data['HQ'][i]
    PRICE = dummy_data['PRICE'][i]
    if count <= 200000 and (PRICE) <= 30000 : 
        df2 = pd.DataFrame({'MODELTYPE': [MODELTYPE], 'MILEAGE': [MILEAGE],'COMPANY': [COMPANY], 'FIRSTDAY': [FIRSTDAY], 'REPAIRDAY' : [REPAIRDAY], 'CARNAME': [CARNAME], 'PART': [PART], 'SEVERITY': [SEVERITY],'HQ':[HQ], 'PRICE': [PRICE]})
        newcsv = pd.concat([newcsv,df2])
        count += 1
    elif (PRICE) > 30000 : 
        df2 = pd.DataFrame({'MODELTYPE': [MODELTYPE], 'MILEAGE': [MILEAGE],'COMPANY': [COMPANY], 'FIRSTDAY': [FIRSTDAY], 'REPAIRDAY' : [REPAIRDAY], 'CARNAME': [CARNAME], 'PART': [PART], 'SEVERITY': [SEVERITY],'HQ':[HQ], 'PRICE': [PRICE]})
        newcsv = pd.concat([newcsv,df2])
    
newcsv.to_csv("custom.csv")
