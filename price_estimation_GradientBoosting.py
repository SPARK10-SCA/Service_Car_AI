import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score
from sklearn.metrics import mean_absolute_error
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import functions
import joblib

# integer feature : MILEAGE, FIRSTDAY, REPAIRDAY, HQ, PRICE
# categorical feature : MODELTYPE, COMPANY, CARNAME, PART, SEVERITY

### 데이터 불러오기
dummy_data = pd.read_csv("./dataset/price_dataset_large.csv")

### Categoryical feature의 개수 확인
print('row 수 : {}, col 수 : {}'.format(dummy_data.shape[0],dummy_data.shape[1])) # row 수 : 836379, col 수 : 11

### MODELTYPE 정제
modeltype = list(dummy_data.MODELTYPE)
for i in range(len(modeltype)) :
    try : 
        modeltype[i] = modeltype[i].split(' ',1)[0]
    except :
        modeltype[i] = None
dummy_data.MODELTYPE = modeltype
#print("MODELTYPE : ",len(np.unique((list(dummy_data.MODELTYPE)))))

### CARNAME 정제
carname = list(dummy_data.CARNAME)
for i in range(len(carname)) :
    try : 
        carname[i] = carname[i].split(' ',1)[0]
    except :
        carname[i] = None
dummy_data.CARNAME = carname
#print("CARNAME : ",len(np.unique((list(dummy_data.CARNAME)))))

### Dateset PART의 종류 18000개를 우리의 모델이 가질 수 있는 14의 feature로 압축하기
parts = list(dummy_data.PART)
for i in range(len(parts)) :
    try : 
        parts[i] = functions.get_parts(parts[i])
    except :
        parts[i] = None
dummy_data.PART = parts


### Dataset SEVERITY의 종류 18개를 주요 수리인 오버홀,교환,판금,수리,조정,도장,탈착으로 압축
severity = list(dummy_data.SEVERITY)
for i in range(len(severity)) :
    try :
        severity[i] = functions.get_severity(severity[i])
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
#print((np.unique((list(clean_data['PART']))))) # 11 Part 존재
clean_data['SEVERITY'] = le.fit_transform(clean_data['SEVERITY'])
#print((np.unique((list(clean_data['SEVERITY']))))) # 8 SEVERITY 존재

"""
### Outlier 확인
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
idx = functions.delete_outlier(clean_data,'MILEAGE',200000)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_outlier(clean_data,'FIRSTDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_outlier(clean_data,'REPAIRDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_outlier(clean_data,'PRICE',800000)
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
### MinMaxScaler 저장
joblib.dump(scaler, "scaler.save")
scaled_value = np.c_[integer_scaled,category_value] # Integer feature와 categoryical feature 합치기
clean_data = pd.DataFrame(scaled_value)
print(clean_data.shape)
x = clean_data.to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.85, random_state=42)


### GradientBoostingRegressor 알고리즘 사용
gb = GradientBoostingRegressor(min_samples_leaf=10, min_samples_split=5, learning_rate=0.5, max_depth=3, n_estimators=1000)
gb.fit(x_train, y_train)
### GradientBoostingRegressor 모델 저장
joblib.dump(gb, 'GradientBoostingRegressor.pkl') 

y_gb_predict = gb.predict(x_test)


print("\nGradientBoostingRegressor Train data Accuracy : ",gb.score(x_train,y_train))
print("GradientBoostingRegressor Test data Accuracy : ",gb.score(x_test,y_test))

print("평균 오차 : ",mean_absolute_error(y_test,y_gb_predict))


"""
### RandomForestRegressor 알고리즘 사용
rtr = RandomForestRegressor(n_estimators=100, random_state = 42)
rtr.fit(x_train, y_train)
joblib.dump(rtr, 'RandomForestRegressor.pkl') 

y_rtr_predict = rtr.predict(x_test)

print("\nRandomForestRegressor Train data Accuracy : ",rtr.score(x_train, y_train))
print("RandomForestRegressor test data Accuracy : ",rtr.score(x_test,y_test))
print("예측값과 정답값의 평균 오차 : ",mean_absolute_error(y_test,y_rtr_predict))
"""