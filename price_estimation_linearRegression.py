import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score
from sklearn.metrics import mean_absolute_error
from sklearn import preprocessing

### 데이터 불러오기
dummy_data = pd.read_csv("./repair_price_dataset.csv")
#print('row 수 : {}, col 수 : {}'.format(dummy_data.shape[0],dummy_data.shape[1])) # 445090,9

### 899개의 MODELTYPE 존재, 데이터를 정재할려고 노력해보았지만 데이터에 규칙성이 없어서
### 포기하고 MODELTYPE row 삭제
"""
print(len(np.unique((list(dummy_data.MODELTYPE)))))
modeltype = list(dummy_data.MODELTYPE)
for i in range(len(modeltype)) :
    try : 
        modeltype[i] = modeltype[i].split(' ',1)[0]
       # modeltype[i] = modeltype[i].split('1',1)[1]
       # modeltype[i] = modeltype[i].split('2',1)[1]
       # modeltype[i] = modeltype[i].split('3',1)[1]
       # modeltype[i] = modeltype[i].split('4',1)[1]
       # modeltype[i] = modeltype[i].split('5',1)[1]
       # modeltype[i] = modeltype[i].split('6',1)[1]
       # modeltype[i] = modeltype[i].split('7',1)[1]
       # modeltype[i] = modeltype[i].split('8',1)[1]
       # modeltype[i] = modeltype[i].split('9',1)[1]
       # modeltype[i] = modeltype[i].split('0',1)[1]
    except :
        modeltype[i] = None
dummy_data.MODELTYPE = modeltype
"""

### Dateset PART의 종류 18000개를 우리의 모델이 가질 수 있는 14의 feature로 압축하기
"""
Frontbumper
Rearbumper
Frontfender(R)
Frontfender(L)
Rearfender(R)
Rearfender(L)
Trunklid
Boonet
Reardoor(L)
Reardoor(R)
Headlights(R)
Headlights(L)
FrontWheel(R)
FrontWheel(L)
Frontdoor(R)
Frontdoor(L)
Sidemirror(R)
Sidemirror(L)
"""
parts = list(dummy_data.PART)
for i in range(len(parts)) :
    try : 
        if parts[i].find('프런트범퍼' or "프런트 범퍼" or "앞범퍼" or "후론트 범퍼" or "후론트범퍼") > -1:
            parts[i] = "Frontbumper"
        elif parts[i].find('리어범퍼' or "리어 범퍼" or "뒤범퍼") > -1 :
            parts[i] = "Rearbumper"
        elif parts[i].find('프런트펜더' or "프런트 펜더" or "프런트휀다" or "앞펜더" or "앞휀다" or"앞휀더"or"후론트휀다"or"후혼트 휀다" ) > -1 :
           parts[i] = "Frontfender"
        elif parts[i].find('리어펜더' or "리어휀다" or "리어 휀다" or "뒤펜더" or "뒤휀다" or "뒤헨더") > -1 :
           parts[i] = "Rearfender"
        elif parts[i].find('본넷' or "본네트") > -1 :
           parts[i] = "Bonnet"
        elif parts[i].find('트렁크') > -1 :
           parts[i] = "Trunklid"
        elif parts[i].find('리어도어' or "도어(뒤") > -1 :
           parts[i] = "Reardoor"
        elif parts[i].find('프런트도어' or "도어(앞" or "후론트 도어") > -1 :
           parts[i] = "Frontdoor"
        elif parts[i].find('미러') > -1 :
           parts[i] = "Sidemirror"
        elif parts[i].find('휠') > -1 :
           parts[i] = "FrontWheel"
        elif parts[i].find('헤드라이트') > -1 :
           parts[i] = "Headlights"
        else :
            parts[i] = None
    except :
        parts[i] = None
dummy_data.PART = parts

### Dataset SEVERITY의 종류 18개를 우리 모델이 가질 수 있는 4개의 feature로 압축 하기
### 4-> 오버홀, 3 -> 교환, 판금 , 2-> 수리, 조정, 도장 , 1-> OH, 탈착
severity = list(dummy_data.SEVERITY)
for i in range(len(severity)) :
    try :
        if severity[i].find("오버홀") > -1 :
            severity[i] = 4
        elif severity[i].find("교환" or "판금") > -1 :
            severity[i] = 3
        elif severity[i].find("수리" or "조정" or "도장") > -1 :
            severity[i] = 2
        else :
            severity[i] = 1
    except :
            severity[i] = None
dummy_data.SEVERITY = severity

### 학습에 도움되지 않는 feature 값들 제거
dummy_data.drop(columns=['MODELTYPE','Unnamed: 0','CARNAME'],inplace=True)

### 데이터 결측값 제거
clean_data = dummy_data.copy(deep=True)
clean_data = clean_data.dropna('index')
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정
# print(clean_data.dropna('index').shape) # 445090 -> 68464

### 중요 feature의 개수 확인
print(len(np.unique((list(clean_data.PART))))) # 11 Part 존재
#print(len(np.unique((list(clean_data.CARNAME))))) # 323개의 CARNAME 존재
print(len(np.unique((list(clean_data.COMPANY))))) # 28개의 COMPANY 존재
print(len(np.unique((list(clean_data.SEVERITY))))) # 4개의 SEVERITY 존재
#np.set_printoptions(threshold=np.inf) # numpy에서 모든 데이터 출력하게 하기
#print(np.unique((list(clean_data.PART))))
#print(np.unique((list(clean_data.COMPANY))))
#print(np.unique((list(clean_data.SEVERITY)))
#print(np.unique((list(clean_data.CARNAME))))

### COMPANY, CARNAME, PART, SEVERITY는 one-hot-encoding으로 변환
clean_data = pd.get_dummies(clean_data)

### Outlier 제거
idx = []
It = list(clean_data['MILEAGE'])
for i in range(len(It)) :
    if(It[i] > 200000) :
        idx.append(i)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = []
It = list(clean_data['FIRSTDAY'])
for i in range(len(It)) :
    if(It[i] > 20250101) :
        idx.append(i)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = []
It = list(clean_data['PRICE'])
for i in range(len(It)) :
    if(It[i] > 800000) :
        idx.append(i)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정
#clean_data = clean_data.reset_index(drop = True)

#clean_data.to_csv("repair_price_cleandata.csv")

print(clean_data.shape)

### Outlier 확인
fig, ax = plt.subplots(1,3,figsize=(16,4))
ax[0].boxplot(list(clean_data.MILEAGE))
ax[0].set_title("MILEAGE")
ax[1].boxplot(list(clean_data.FIRSTDAY))
ax[1].set_title("FIRSTDAY")
ax[2].boxplot(list(clean_data.PRICE))
ax[2].set_title("PRICE")
sns.pairplot(data=clean_data, x_vars=['MILEAGE','FIRSTDAY','PRICE'], y_vars='PRICE',size=3)
plt.show()

# test 데이터셋 생성 
y = clean_data[['PRICE']].to_numpy() # 가격만 빼내기
clean_data = clean_data.drop(columns=['PRICE']) # 원본 데이터에서 price 삭제

x = clean_data.values 
columns = clean_data.columns

scaler = preprocessing.MinMaxScaler()
tmp = scaler.fit_transform(x) # 0~1 사이의 값으로 values 정규화
clean_data = pd.DataFrame(tmp)
clean_data.columns = columns

x = clean_data.to_numpy()
#print(x)
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.85, random_state=2)

lr = LinearRegression(fit_intercept=True, copy_X = True)
lr.fit(x_train,y_train)

print('Train dats\'s Accuracy : {}'.format(lr.score(x_train, y_train)))
y_predict = lr.predict(x_test)

print("Test dats\'s Accuracy : {}".format(lr.score(x_test, y_test)))
print("Test dats\'s Accuracy : {}".format(r2_score(y_test, lr.predict(x_test))))

print("mean_absolute_error : ",mean_absolute_error(y_test, y_predict))