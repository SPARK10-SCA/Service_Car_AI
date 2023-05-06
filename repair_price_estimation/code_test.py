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
dummy_data = pd.read_csv("./dataset/price_dataset_price_preprocessing.csv")

### Categoryical feature의 개수 확인
print('row 수 : {}, col 수 : {}'.format(dummy_data.shape[0],dummy_data.shape[1])) # row 수 : 836379, col 수 : 11

### MODELTYPE 정제
price = (dummy_data.PRICE)
print(price.mean())

