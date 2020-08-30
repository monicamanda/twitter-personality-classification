import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split  

dataset = pd.read_csv('dataset/final-feature.csv') 
label = {'Openness': 1,'Conscientiousness': 2, 'Extraversion': 3, 'Agreeableness': 4, 'Neuroticism': 5} 
dataset.Label = [label[item] for item in dataset.Label] 

test_size = 0.1
dtest = str(int(test_size*100))
dtrain = str(int(float('%.1f' % round((1.0-test_size)*100))))

# SENTIMENT FEATURE

Xsen = dataset.loc[:, ['Positive','Negative']]
Ysen = dataset.loc[:, ['Label']]

x_train, x_test, y_train, y_test = train_test_split(Xsen, Ysen, test_size=test_size, shuffle=False)
model_gnb = GaussianNB()
model_gnb.fit(x_train, y_train.values.ravel())
predict_gnb = model_gnb.predict(x_test)

print('\n SENTIMENT FEATURE')
print('\n accuracy: ', round((accuracy_score(predict_gnb, y_test)*100), 2), '%')
print('\n', classification_report(y_test, predict_gnb))

# EMOTION FEATURE

Xemo = dataset.loc[:, ['Anger','Anticipation','Disgust','Fear','Joy','Sadness','Surprise','Trust']]
Yemo = dataset.loc[:, ['Label']]

x_train, x_test, y_train, y_test = train_test_split(Xemo, Yemo, test_size=test_size, shuffle=False)
model_gnb = GaussianNB()
model_gnb.fit(x_train, y_train.values.ravel())
predict_gnb = model_gnb.predict(x_test)

print('\n EMOTION FEATURE')
print('\n accuracy: ', round((accuracy_score(predict_gnb, y_test)*100), 2), '%')
print('\n', classification_report(y_test, predict_gnb))

# SOCIAL FEATURE

Xsoc = dataset.loc[:, ['Following', 'Followers', 'Retweet', 'Favorite']]
Ysoc = dataset.loc[:, ['Label']]

x_train, x_test, y_train, y_test = train_test_split(Xsoc, Ysoc, test_size=test_size, shuffle=False)
model_gnb = GaussianNB()
model_gnb.fit(x_train, y_train.values.ravel())
predict_gnb = model_gnb.predict(x_test)

print('\n SOCIAL FEATURE')
print('\n accuracy: ', round((accuracy_score(predict_gnb, y_test)*100), 2), '%')
print('\n', classification_report(y_test, predict_gnb))

# ALL FEATURE

Xall = dataset.loc[:, ['Positive','Negative','Anger','Anticipation','Disgust','Fear','Joy','Sadness','Surprise','Trust','Following','Followers','Retweet','Favorite']]
Yall = dataset.loc[:, ['Label']]

x_train, x_test, y_train, y_test = train_test_split(Xall, Yall, test_size=test_size, shuffle=False)
model = GaussianNB()
model_gnb = model.fit(x_train, y_train.values.ravel())
predict_gnb = model_gnb.predict(x_test)

print('\n TOTAL FEATURE')
print('\n accuracy: ', round((accuracy_score(predict_gnb, y_test)*100), 2), '%')
print('\n', classification_report(y_test, predict_gnb))

print('GNB test score: ', model_gnb.score(x_test, y_test))
print('GNB train score: ', model_gnb.score(x_train, y_train))

# ==============================================================================

# print('\nCARA 1')
# from sklearn import linear_model
# from sklearn.model_selection import cross_validate
# from sklearn.metrics import make_scorer
# from sklearn.metrics import confusion_matrix

# cv_results = cross_validate(model_gnb, Xall, Yall.values.ravel(), cv=6)
# sorted(cv_results.keys())
# print('test score: ', cv_results['test_score'])
# scores = cross_validate(model_gnb, Xall, Yall.values.ravel(), cv=6,
#                         scoring=('r2', 'neg_mean_squared_error'),
#                         return_train_score=True)
# print('test mse: ', scores['test_neg_mean_squared_error'])
# print('train r2: ', scores['train_r2'])

# print('\nCARA 2')
# from sklearn.model_selection import cross_val_score, cross_val_predict
# from sklearn import metrics

# print('Test score:', model_gnb.score(x_test, y_test))
# print('Train score:', model_gnb.score(x_train, y_train))

# scores = cross_val_score(model_gnb, Xall, Yall.values.ravel(), cv=6)
# print('Cross-validated scores:', scores)
# predictions = predict_gnb
# predictions = cross_val_predict(model_gnb, Xall, Yall.values.ravel(), cv=6)
# plt.scatter(Yall.values.ravel(), predictions)
# accuracy = metrics.r2_score(Yall.values.ravel(), predictions)
# print('Cross-predicted accuracy:', accuracy)

# ==============================================================================

indexLabel = ['Openness','Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']

plot_confusion_matrix(model_gnb, x_test, y_test)
plt.title('Confusion Matrix with Dataset '+ dtrain +':'+ dtest)
plt.savefig('result/'+ dtrain +'-'+ dtest +'-confusion-matrix.png')

print("\n- visualizing to 'result/confusion-matrix.png' complete.")

filename = 'result/big5_model.sav'
joblib.dump(model_gnb, filename)

print("\n- writing to '" + filename + "' complete.")

loaded_model = joblib.load(filename)
predict_mdl = loaded_model.predict(x_train)
predict_all = np.append(predict_mdl, predict_gnb)

datapred = pd.read_csv('dataset/final-feature.csv') 
datapred['Predicted'] = predict_all
label = {1 : 'Openness', 2 : 'Conscientiousness', 3 : 'Extraversion', 4 : 'Agreeableness', 5 : 'Neuroticism'} 
datapred.Predicted = [label[item] for item in datapred.Predicted] 

datapred.to_csv('result/predicted-personality.csv', index=False)

print("\n- writing to 'result/predicted-personality.csv' complete.")

df = pd.read_csv('result/predicted-personality.csv')
label = {'Openness': 1,'Conscientiousness': 2, 'Extraversion': 3, 'Agreeableness': 4, 'Neuroticism': 5} 
df.Label = [label[item] for item in df.Label] 
df.Predicted = [label[item] for item in df.Predicted] 

actual = df['Label'].tolist()
predict = df['Predicted'].tolist()
