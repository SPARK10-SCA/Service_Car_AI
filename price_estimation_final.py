# Integer feature (MinMaxScaler) : FIRSTDATE, REPAIRDATE, HQ, PRICE
# Categorical feature (LabelEncoder) : COMPANY, REPAIRPART, REPAIRMETOHD
# Model : GradientBoostingRegressor
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

### 데이터 불러오기
dataset = pd.read_csv("./dataset/price_dataset_large.csv")

### COMPANY feature 정제
### issue : 국산차와 외제차의 비율이 22:1로 국산차가 압도적으로 많음
company = list(dataset.COMPANY)
for i in range(len(company)) :
    if any(substring in company[i] for substring in ['현대',"기아","한국GM","쌍용",'르노']) :
       company[i] = "국산차"
    else : 
        company[i] = "외제차"
dataset.COMPANY = company

### REPAIRPART 차원축소

### REPAIRMETHOD 차원축소

### 데이터셋에서 학습에 사용하지 않는 Feature들 제거
dataset.drop(columns=['Unnamed: 0','MODELTYPE','HQ','MILEAGE','CARNAME'],inplace=True)

### Missing value 제거

### Outlier 제거

### REPAIRPART, REPAIRMETOHD은 LabelEncoder로 정제

### COMPANY, CARNAME은 One-hot Encoder로 정제

### FIRSTDATE, REPAIRDATE는 MinMaxScaler로 정규화

### 최종 학습 데이터 생성

### GradientBoostingRegressor 알고리즘 사용






