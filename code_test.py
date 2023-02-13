import pandas as pd
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse=False)
train = pd.DataFrame({'num1':[1,2,3,4,5], 'num2':[10,20,30,40,50], 'cat1':['a', 'a', 'b', 'c', 'c']})
print(train.cat1)

train_cat = ohe.fit_transform(train[['cat1']])
print(ohe.categories_[0])