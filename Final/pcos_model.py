import pandas as pd
import numpy as np

X_data = pd.read_csv('out.csv')
y_data = pd.read_csv('final.csv')


def label_preprocessing(placeholder_variable):
    if(placeholder_variable=="Yes"):
        return 1
    if(placeholder_variable=="No"):
        return 0
    if(placeholder_variable=="Yes(Detected Positive)"):
        return 1
    if(placeholder_variable=="No(Detected Negative)"):
        return 0
y_data = y_data.result.apply(label_preprocessing)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, random_state = 3, test_size = 0.1)

from sklearn.naive_bayes import GaussianNB
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.ensemble import RandomForestClassifier
# random_forest_model = RandomForestClassifier()
# random_forest_model.fit(X_train, y_train)

# training_accuracy = random_forest_model.score(X_train, y_train)
# testing_accuracy = random_forest_model.score(X_test, y_test)

def training_model():
    random_forest_model = GaussianNB()
    random_forest_model.fit(X_train, y_train)
    return random_forest_model

    