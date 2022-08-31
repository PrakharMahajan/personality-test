# importing libraries
import pandas as pd
from sklearn import linear_model

# reading and initializing data-values
data = pd.read_csv('training_set.csv')
array = data.values
# array[0] = [['Female' 20 7 9 9 5 5 'dependable']]

# setting male = 1 & female = 0
for i in range(len(array)):
    if array[i][0] == "Male":
        array[i][0] = 1
    else:
        array[i][0] = 0

# data for training the model
df = pd.DataFrame(array)
X = df[[0, 1, 2, 3, 4, 5, 6]]
X_train = X.values

# labels for training the model
y = df[7]
y_train = y.values

for i in range(len(y_train)):
    y_train[i] = str(y_train[i])

# training the model
# we are using logistic regression
model = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)
model.fit(X_train, y_train)
