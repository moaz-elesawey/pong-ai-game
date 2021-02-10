import pickle
import sys
import time


def train(save=False):

    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, r2_score
    from sklearn.ensemble import RandomForestRegressor

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt


    def clean_data(data_file):
        with open(data_file, 'rb') as f:
            data = pickle.load(f)
            features =  np.array(data['ball_y'], dtype=np.int32).reshape(-1, 1)
            targets = np.array(data['player1_y'], dtype=np.int32)

        return features, targets

    # load and clean the data
    X, y = clean_data(sys.argv[1])
    # print(X.shape, y.shape)

    # split the data to train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
    # print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

    # train the linear model
    linear_reg = RandomForestRegressor()
    print('.....training the model.....')
    linear_reg.fit(X_train, y_train)

    # test the model
    print('.....testing the model......')
    y_pred = linear_reg.predict(X_test)

    print('y_test: ', y_test[:10])
    print('y_pred: ', np.int32(y_pred[:10]))

    # checking the model accuracy
    print('Linear Regressor Accuracy Score is {:.3f}'.format(accuracy_score(y_test, np.array(y_pred, dtype=np.int32))))
    print('Linear Regressor Accuracy R2 is {:.3f}'.format(r2_score(y_test, np.array(y_pred, dtype=np.int32))))

    with open(f'./models/[{int(time.time())}]-model-best.pkl', 'wb') as f:
        pickle.dump(linear_reg, f)

def test(sample, model_file):
    with open(f'{model_file}', 'rb') as f:
        model = pickle.load(f)

        pred = model.predict([sample])

        return int(pred[0])

if __name__ == '__main__':
    train()

