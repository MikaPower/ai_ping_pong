

import os
from datetime import datetime
import keras
import numpy
import pandas as pd
import shutil

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from keras.callbacks import Callback
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline


df = pd.read_csv('final_df_accX_only_valid.csv')
#df = pd.read_csv('accel_x_final_dataset.csv')

dataset = df.values

X = dataset[:,0:46].astype(float) # sensor data
Y = dataset[:,46].astype(int) # labels
#X = dataset[:,0:12].astype(float) # sensor data
#Y = dataset[:,12].astype(int) # labels

#%% md

## 3. Define Neural Network Model

#%% md

#%%

def create_model():
    # Define model
    global model
    model = Sequential()
    model.add(Dense(15, input_dim=46, activation='relu'))
    #model.add(Dense(15, input_dim=12, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(5, activation='softmax'))

    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

#%% md

## 4. Configure model callbacks including early stopping routine

#%%

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

loss_history = LossHistory()
early_stopping = EarlyStopping(monitor='val_accuracy', patience=20)

logdir="logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)

#%% md

## 5. Assemble classifier and train it

#%%

from keras.utils.np_utils import to_categorical

estimator = KerasClassifier(create_model, epochs=400, batch_size=100, verbose=False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=5)
Y_test = to_categorical(Y_test)

results = estimator.fit(X_train, Y_train, callbacks=[tensorboard_callback], validation_data=(X_test, Y_test))

#%% md

## 6. Perform 10-fold cross-validation on validation data

#%%

kfold = KFold(n_splits=10, shuffle=True, random_state=5)
cv_results = cross_val_score(estimator, X_test, Y_test, cv=kfold)
print("Baseline on test data: %.2f%% (%.2f%%)" % (cv_results.mean()*100, cv_results.std()*100))

#%% md

## 7. Plot accuracy for train and validation data

#%%

import matplotlib.pyplot as plt

figsize = (20, 10)
fig, ax = plt.subplots(figsize=figsize)

ax.plot(results.history['val_accuracy'], linewidth=0.4, color="green")
ax.plot(results.history['accuracy'], linewidth=0.4, color="red")
plt.figure()
plt.show()
