# Integer feature (MinMaxScaler) : FIRSTDATE, REPAIRDATE, HQ, PRICE
# Categorical feature (LabelEncoder) : COMPANY, REPAIRPART, REPAIRMETOHD
# Model : GradientBoostingRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder
import functions
import joblib

### 데이터 불러오기
dataset = pd.read_csv("./dataset/price_dataset_final.csv")

### COMPANY feature 정제
### issue : 국산차와 외제차의 비율이 22:1로 국산차가 압도적으로 많음
company = list(dataset.COMPANY)
for i in range(len(company)) :
    if any(substring in company[i] for substring in ['현대',"기아","한국GM","쌍용",'르노']) :
       company[i] = "국산차"
    else : 
        company[i] = "외제차"
dataset.COMPANY = company

### REPAIRPART의 종류 18000개를 우리의 모델이 가질 수 있는 14개의 feature로 압축하기
repari_parts = list(dataset.PART)
for i in range(len(repari_parts)) :
    try : 
        repari_parts[i] = functions.get_parts(repari_parts[i])
    except :
        repari_parts[i] = None
dataset.PART = repari_parts

### REPAIRMETHOD의 종류 18개를 주요 수리인 7개의 feature로 압축
repair_method = list(dataset.SEVERITY)
for i in range(len(repair_method)) :
    try :
        repair_method[i] = functions.get_severity(repair_method[i])
    except :
            repair_method[i] = None
dataset.SEVERITY = repair_method

### 데이터셋에서 학습에 사용하지 않는 Feature들 제거
dataset.drop(columns=['Unnamed: 0','MODELTYPE','MILEAGE','CARNAME'],inplace=True)

### Missing value 제거
clean_data = dataset.copy(deep=True)
clean_data = clean_data.dropna('index')
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

### Outlier 제거
idx = functions.delete_outlier(clean_data,'FIRSTDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_outlier(clean_data,'REPAIRDAY',20250101)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_outlier(clean_data,'PRICE',800000)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

idx = functions.delete_small_price(clean_data,'PRICE',10000)
clean_data = clean_data.drop(idx) 
clean_data = clean_data.reset_index(drop=True) # 인덱스 재설정

clean_data.to_csv("preprocessed_dataset.csv")

### COMPANY, REPAIRPART, REPAIRMETOHD는 One-hot Encoder로 정제
# COMPANY OneHotEncoder 저장
ohe = OneHotEncoder(sparse=False)
ohe_trained = ohe.fit_transform(clean_data[['COMPANY']])
print(ohe_trained)
clean_data = pd.concat([clean_data.drop(columns=['COMPANY']),
           pd.DataFrame(ohe_trained, columns=['COMPANY_' + col for col in ohe.categories_[0]])], axis=1)
joblib.dump(ohe, "ohe_COMPANY.save") 
# PART OneHotEncoder 저장
ohe_trained = ohe.fit_transform(clean_data[['PART']])
clean_data =  pd.concat([clean_data.drop(columns=['PART']),
           pd.DataFrame(ohe_trained, columns=['PART_' + col for col in ohe.categories_[0]])], axis=1)
joblib.dump(ohe, "ohe_REPAIRPART.save") 
# REPAIRMETHOD OneHotEncoder 저장
ohe_trained = ohe.fit_transform(clean_data[['SEVERITY']])
clean_data =  pd.concat([clean_data.drop(columns=['SEVERITY']),
           pd.DataFrame(ohe_trained, columns=['SEVERITY_' + col for col in ohe.categories_[0]])], axis=1)
joblib.dump(ohe, "ohe_REPAIRMETHOD.save") 
print()
print("최종 학습데이터 : ",clean_data)

### 최종 학습 데이터 생성
target = clean_data[['PRICE']].to_numpy() # 가격만 빼내기
clean_data = clean_data.drop(columns=['PRICE']) # 원본 데이터에서 price 삭제
values = clean_data.values 
columns = clean_data.columns
integer_value = values[:,:3] # FIRSTDAY, REPAIRDAY, HQ
category_value = values[:,3:] # COMPANY, REPAIRPART, REPAIRMETOHD

### FIRSTDATE, REPAIRDATE는 MinMaxScaler로 정규화
scaler = preprocessing.MinMaxScaler()
integer_scaled = scaler.fit_transform(integer_value) # Integer value 0~1 사이의 값으로 정규화
joblib.dump(scaler, "scaler.save") # MinMaxScaler 저장
scaled_value = np.c_[integer_scaled,category_value] # Integer feature와 categoryical feature 합치기
clean_data = pd.DataFrame(scaled_value)
values = clean_data.to_numpy()
x_train, x_test, y_train, y_test = train_test_split(values ,target, train_size=0.85, random_state=42)

### GradientBoostingRegressor 알고리즘 사용
gb = GradientBoostingRegressor(min_samples_leaf=10, min_samples_split=5, learning_rate=0.5,max_depth=3, n_estimators=1000)
gb.fit(x_train, y_train) # 모델 학습

### GradientBoostingRegressor 모델 저장하고 테스트
joblib.dump(gb, 'GradientBoostingRegressor.pkl') 
y_gb_predict = gb.predict(x_test)
print("\nGradientBoostingRegressor Train data Accuracy : ",gb.score(x_train,y_train))
print("GradientBoostingRegressor Test data Accuracy : ",gb.score(x_test,y_test))
print("평균 오차 : ",mean_absolute_error(y_test,y_gb_predict))