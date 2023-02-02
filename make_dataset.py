import pandas as pd
from tqdm import tqdm

def next_file_num(file_name): # 다음 파일 이름 가져오기
    num = int(file_name[3:])
    num += 1
    num = str(num)
    numlen = 7 - len(num)
    result = ""
    while len(result) < numlen:
        result += "0"
    return "as-"+result + num

def str_to_int(num) : # 1,000,000 -> 1000000
    s = ""
    for i in num :
        if(i != ',') :
            s += i
    return int(s)

file_location = "./origin_xls/"
file_name = 'as-0000002'
file_extension = '.xls'

MODELTYPE = list()
MILEAGE = list()
COMPANY = list()
FIRSTDAY = list()
CARNAME = list()
PART = list()
SEVERITY = list()
PRICE = list()

newcsv = pd.DataFrame(columns=['MODELTYPE', 'MILEAGE', 'COMPANY',
                      'FIRSTDAY','REPAIRDAY', 'CARNAME', 'PART', 'SEVERITY', 'HQ', 'PRICE'])

for i in tqdm(range(100000)):
    file = file_location + file_name + file_extension
    try:
        df = pd.read_excel(file)
    except: # 파일이 존재하지 않을 경우
        file_name = next_file_num(file_name) 
        continue
    
    modeltype = df['Unnamed: 2'][2]  # 모델
    mileage = (df['Unnamed: 2'][3])  # 주행 거리
    try : # 주행거리가 결측값일 경우
        mileage = str_to_int(mileage)
    except :
        mileage = None
    company = df['Unnamed: 5'][1]  # 제작사/차종
    firstday = df['Unnamed: 5'][2]  # 최초 등록일
    repairday = df['Unnamed: 5'][3] # 수리 등록일
    carname = df['Unnamed: 8'][1]  # 차량 명칭
    parts = df['Unnamed: 2'][21:]  # 작업항목 및 부품명
    severity = list(df['Unnamed: 4'][21:])  # 작업
    hq = list(df['Unnamed: 5'][21:])
    price = list(df['Unnamed: 8'][21:])  # 공임 (target)
    for index, part in enumerate(parts):
        try : # 가격이 결측값일 경우
            cost = str_to_int(price[index])
            if cost == 0 : continue # 가격이 0인 경우 pass
        except :
            cost = None
        df2 = pd.DataFrame({'MODELTYPE': [modeltype], 'MILEAGE': [mileage],'COMPANY': [company], 'FIRSTDAY': [firstday], 'REPAIRDAY' : [repairday], 'CARNAME': [carname], 'PART': [part], 'SEVERITY': [severity[index]],'HQ':[hq[index]], 'PRICE': [cost]})
        newcsv = pd.concat([newcsv,df2])
    file_name = next_file_num(file_name)
    #if i == 1000000 : break

newcsv.to_csv("price_dataset.csv")