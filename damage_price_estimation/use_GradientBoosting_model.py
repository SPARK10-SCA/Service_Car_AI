import joblib
import functions
from sklearn import preprocessing
import numpy as np

### GradientBoosting Model ###
# Train data Accuracy :  0.9769720228632816
# Test data Accuracy :  0.9693762295523924
# 정답, 예측값 평균 오차 :  4355.083554398043
GradientBoostingModel = joblib.load('./model/MODEL_GradientBoostingRegressor.pkl')

### RandomForestRegressor Model ###
# Train data Accuracy :  0.9944419060728779
# test data Accuracy :  0.9678152327543915
# 정답, 예측값 평균 오차 :  3981.205360295778
RandomForestRegressorModel = joblib.load('./model/MODEL_RandomForestRegressor.pkl')

### BMW 5시리즈 55440원
modelinput = functions.get_model_input(110718,20141119,20180512,1.68,'뒤범퍼(단독작업)','탈착')

### 벤츠 G350 350000원
modelinput2 = functions.get_model_input(11387,20170601,20180425,100.0,'본네트(보수)','도장')

### 현대 싼타페(15) 8250원
modelinput3 = functions.get_model_input(25674, 20170207, 20181029, 0.25,'후론트 도어 몰딩(우)','교환')


print("정답 값 : ",'55440원')
print("RandomForestRegressorModel 예측값 : ",RandomForestRegressorModel.predict([modelinput]))
print("GradientBoostingModel 예측값 : ",GradientBoostingModel.predict([modelinput]))


print("정답 값 : ",'350000원')
print("RandomForestRegressorModel 예측값 : ",RandomForestRegressorModel.predict([modelinput2]))
print("GradientBoostingModel 예측값 : ",GradientBoostingModel.predict([modelinput2]))


print("정답 값 : ",'8250원')
print("RandomForestRegressorModel 예측값 : ",RandomForestRegressorModel.predict([modelinput3]))
print("GradientBoostingModel 예측값 : ",GradientBoostingModel.predict([modelinput3]))

