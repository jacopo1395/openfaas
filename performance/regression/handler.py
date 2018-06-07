import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import json 

def handle(req):
    j = json.loads(req)

    X1 = j["X_train"]
    X_train=[]
    for value in X1:
        X_train.append(value["vector"])

    X2 = j["X_train"]
    X_test=[]
    for value in X2:
        X_test.append(value["vector"])

    y_train = j["y_train"]
    y_test = j["y_test"]

    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    # Make predictions using the testing set
    y_pred = regr.predict(X_test)

    # The coefficients
    print('Coefficients: ', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(y_test, y_pred))
