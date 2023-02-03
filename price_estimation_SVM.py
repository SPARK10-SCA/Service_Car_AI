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

# integer feature : MILEAGE, FIRSTDAY, REPAIRDAY, HQ, PRICE
# categorical feature : MODELTYPE, COMPANY, CARNAME, PART, SEVERITY

### 데이터 불러오기
dummy_data = pd.read_csv("./price_dataset_large.csv")

### Categoryical feature의 개수 확인
print('row 수 : {}, col 수 : {}'.format(dummy_data.shape[0],dummy_data.shape[1])) # row 수 : 836379, col 수 : 11
print("MODELTYPE : ",len(np.unique((list(dummy_data.MODELTYPE)))))
print("COMPANY : ",len(np.unique((list(dummy_data.COMPANY)))))
print("CARNAME : ",len(np.unique((list(dummy_data.CARNAME)))))

### 899개의 MODELTYPE 존재, 데이터를 정재할려고 노력해보았지만 데이터에 규칙성이 없어서
### 포기하고 MODELTYPE row 삭제

# MODELTYPE 정제
modeltype = list(dummy_data.MODELTYPE)
for i in range(len(modeltype)) :
    try : 
        modeltype[i] = modeltype[i].split(' ',1)[0]
    except :
        modeltype[i] = None
dummy_data.MODELTYPE = modeltype
print("MODELTYPE : ",len(np.unique((list(dummy_data.MODELTYPE)))))

# CARNAME 정제
carname = list(dummy_data.CARNAME)
for i in range(len(carname)) :
    try : 
        carname[i] = carname[i].split(' ',1)[0]
    except :
        carname[i] = None
dummy_data.CARNAME = carname
print("CARNAME : ",len(np.unique((list(dummy_data.CARNAME)))))

### Dateset PART의 종류 18000개를 우리의 모델이 가질 수 있는 14의 feature로 압축하기
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


### Dataset SEVERITY의 종류 18개를 주요 수리인 오버홀,교환,판금,수리,조정,도장,탈착으로 압축
severity = list(dummy_data.SEVERITY)
for i in range(len(severity)) :
    try :
        if severity[i].find("오버홀") > -1 :
            severity[i] = "오버홀"
        elif severity[i].find("교환") > -1 :
            severity[i] = "교환"
        elif severity[i].find("판금") > -1 :
            severity[i] = "판금"
        elif severity[i].find("수리") > -1 :
            severity[i] = "수리"
        elif severity[i].find("도장") > -1 :
            severity[i] = "도장"
        elif severity[i].find("조정") > -1 :
            severity[i] = "조정"
        elif severity[i].find("OH") > -1 :
            severity[i] = "OH"
        elif severity[i].find("탈착") > -1 :
            severity[i] = "탈착"
        else :
            severity[i] = None
    except :
            severity[i] = None
dummy_data.SEVERITY = severity

### 학습에 도움되지 않는 feature 값들 제거 (일단은 카테고리 feature들 다 제거)
dummy_data.drop(columns=['Unnamed: 0','MODELTYPE','COMPANY','CARNAME'],inplace=True)

### 데이터 결측값 제거
clean_data = dummy_data.copy(deep=True)
clean_data = clean_data.dropna('index')
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

### PART, SEVERITY는 LabelEncoder으로 변환
le = LabelEncoder()
clean_data['PART'] = le.fit_transform(clean_data['PART'])
clean_data['SEVERITY'] = le.fit_transform(clean_data['SEVERITY'])

### Outlier 확인
"""
fig, ax = plt.subplots(1,5,figsize=(16,4))
ax[0].boxplot(list(clean_data.MILEAGE))
ax[0].set_title("MILEAGE")
ax[1].boxplot(list(clean_data.FIRSTDAY))
ax[1].set_title("FIRSTDAY")
ax[2].boxplot(list(clean_data.REPAIRDAY))
ax[2].set_title("REPAIRDAY")
ax[3].boxplot(list(clean_data.HQ))
ax[3].set_title("HQ")
ax[4].boxplot(list(clean_data.PRICE))
ax[4].set_title("PRICE")
sns.pairplot(data=clean_data, x_vars=['MILEAGE','FIRSTDAY','REPAIRDAY','HQ','PRICE'], y_vars='PRICE',size=5)
plt.show()
"""

### Outlier 제거
def delete_outlier(data, column, threshold) :
    idx = []
    It = list(data[column])
    for i in range(len(It)) :
        if(It[i] > threshold) :
            idx.append(i)
    return idx

idx = delete_outlier(clean_data,'MILEAGE',200000)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = delete_outlier(clean_data,'FIRSTDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = delete_outlier(clean_data,'REPAIRDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = delete_outlier(clean_data,'PRICE',800000)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정


### test 데이터셋 생성 
y = clean_data[['PRICE']].to_numpy() # 가격만 빼내기
clean_data = clean_data.drop(columns=['PRICE']) # 원본 데이터에서 price 삭제

# value랑 column 나누기
x = clean_data.values 
columns = clean_data.columns

integer_value = np.c_[x[:,:3],x[:,-1]] # MILEAGE, FIRSTDAY, REPAIRDAY, HQ
category_value = x[:,3:5] # PART, SEVERITY


scaler = preprocessing.MinMaxScaler()
integer_scaled = scaler.fit_transform(integer_value) # Integer value 0~1 사이의 값으로 정규화
scaled_value = np.c_[integer_scaled,category_value] # Integer feature와 categoryical feature 합치기
clean_data = pd.DataFrame(scaled_value)
print(clean_data.shape)
x = clean_data.to_numpy()
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.85, random_state=42)

from sklearn.svm import SVR
 
svm_model = SVR(kernel='rbf')
 
svm_model.fit(x_train, y_train) # SVM 분류 모델 훈련
print("SVR Train data Accuracy : ",svm_model.score(x_train,y_train))
print("SVR Test data Accuracy : ",svm_model.score(x_test,y_test))

"""
y_pred = svm_model.predict(x_test)
print(y_pred[:10])
print(y_test[:10])
print("평균 오차 : ",mean_absolute_error(y_test,y_pred))
"""
 