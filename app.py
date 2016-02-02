import pandas as pd
data = pd.read_csv('./data/titanic.csv', index_col='PassengerId')

print data

data2 = data[(data.Sex == "male")].count()

print len(data)