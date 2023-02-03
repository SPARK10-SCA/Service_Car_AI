import joblib
import functions
from sklearn import preprocessing
import numpy as np

### GradientBoostingModel
# Train data Accuracy :  0.9738587342457055
# Test data Accuracy :  0.9665893857030463
# 정답, 예측 평균 오차 :  5221.055507167929
GradientBoostingModel = joblib.load('MODEL_GradientBoostingRegressor.pkl') # 

modelinput = functions.get_model_input(30903,20160101,20180519,2.0,'리어 휀다(우)','판금')

print(GradientBoostingModel.predict([modelinput]))


