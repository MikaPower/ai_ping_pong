# convlstm model
import os
import coremltools as ct

from tensorflow.keras.utils import to_categorical
from numpy import mean
from numpy import std
from numpy import dstack
from numpy import argmax
from numpy.ma import arange
from pandas import read_csv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import TimeDistributed, Conv1D, MaxPooling1D

import matplotlib.pyplot as plt

# load a single file as a numpy array
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import ConvLSTM2D


def load_file(filepath):
    dataframe = read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values


# load a list of files and return as a 3d numpy array
def load_group(filenames, prefix=''):
    loaded = list()
    for name in filenames:
        data = load_file(prefix + name)
        loaded.append(data)
    # stack group so that features are the 3rd dimension
    loaded = dstack(loaded)
    return loaded


# load a dataset group, such as train or test
def load_dataset_group():
    # load all 6 files as a single array
    # total acceleration
    filenames = os.listdir('datasets/LSTM dataset/')
    axxis = {'x': [], 'y': []}
    for file in filenames:
        df = read_csv('datasets/LSTM dataset/' + file)

        dataset = df.values

        X = dataset[:, 0:46].astype(float)  # sensor data
        Y = dataset[:, 46].astype(int)  # labels

        axxis['x'].append(X)
        axxis['y'].append(Y)

    X = dstack(axxis['x'])

    return X, Y

# load the dataset, returns train and test X and y elements
def load_dataset(prefix=''):
    # load all train
    X, Y = load_dataset_group()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=5)
    Y_train = to_categorical(Y_train)
    Y_test = to_categorical(Y_test)
    print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)
    return X_train, Y_train, X_test, Y_test

# fit and evaluate a model
def evaluate_model(trainX, trainy, testX, testy):
    # define model
    verbose, epochs, batch_size = 1, 25, 64
    n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    # reshape into subsequences (samples, time steps, rows, cols, channels)
    n_steps, n_length = 1, 46
    trainX = trainX.reshape((trainX.shape[0], n_steps, 1, n_length, n_features))
    testX = testX.reshape((testX.shape[0], n_steps, 1, n_length, n_features))
    # define model
    model = Sequential()
    model.add(ConvLSTM2D(filters=64, kernel_size=(1,3), activation='relu', input_shape=(n_steps, 1, n_length, n_features)))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)
    # evaluate model
    _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
    confusion_matrix_and_stats(model, testX, testy)
    return accuracy


def confusion_matrix_and_stats(model, testX, testy):
    pred = model.predict(testX)
    pred = argmax(pred, axis=1)
    y_true = argmax(testy, axis=1)

    from sklearn.metrics import confusion_matrix
    CM = confusion_matrix(y_true, pred, labels=[0, 1, 2, 3, 4, 5])
    from mlxtend.plotting import plot_confusion_matrix
    fig, ax = plot_confusion_matrix(conf_mat=CM, figsize=(10, 5), class_names=['td', 'te', 'b', 'fd', 'fe', 'r'])
    plt.title("convLSTM")
    plt.show()
    from sklearn.metrics import classification_report, accuracy_score, f1_score
    print(classification_report(y_true, pred))
    f1 = f1_score(y_true, pred, average='micro')
    print('F1 score: %f' % f1)

# summarize scores
def summarize_results(scores):
    print(scores)
    m, s = mean(scores), std(scores)
    print('Accuracy: %.3f%% (+/-%.3f)' % (m, s))

# run an experiment
def run_experiment(repeats=10):
    # load data
    trainX, trainy, testX, testy = load_dataset()
    # repeat experiment
    scores = list()
    for r in range(repeats):
        score = evaluate_model(trainX, trainy, testX, testy)
        score = score * 100.0
        print('>#%d: %.3f' % (r+1, score))
        scores.append(score)
    # summarize results
    summarize_results(scores)


# run the experiment
if __name__ == "__main__":
    run_experiment()