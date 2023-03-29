import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.layers import Input, Dense, Activation, TextVectorization, Embedding, GlobalAveragePooling1D
from keras.models import Model
from keras.callbacks import ModelCheckpoint

import tensorflow as tf

df = pd.read_csv('datasets/IMDB Dataset.csv')
ohe = OneHotEncoder()
y_ohe = ohe.fit_transform(df['sentiment'].to_numpy().reshape((-1,1))).todense()
X_train, X_test, y_train, y_test = train_test_split(df['review'], y_ohe)

vocab_size = 1000

def avg_embedding_softmax_model(vectorize_layer, vocab_size=vocab_size):
    input_layer = Input(shape=(1,), dtype=tf.string)
    x = input_layer
    x = vectorize_layer(x)
    x = Embedding(vocab_size, 2, name='projecao', embeddings_regularizer='l2')(x)
    x = GlobalAveragePooling1D()(x)
    x = Dense(2, name='classificador', use_bias=False)(x)
    x = Activation('softmax')(x)
    return Model(input_layer, x)

vectorize_layer = TextVectorization(output_mode='int', max_tokens=vocab_size, pad_to_max_tokens=True, output_sequence_length=200)
vectorize_layer.adapt(X_train)
clf = avg_embedding_softmax_model(vectorize_layer)
print(clf.summary())
clf.compile(loss='categorical_crossentropy', metrics=['accuracy'])

# Gather data

def get_data(n_epoch):
    projecoes = clf.get_layer('projecao').get_weights()[0]
    vocabulario = vectorize_layer.get_vocabulary()
    y_pred_ohe = clf.predict(vocabulario)
    y_pred = ohe.inverse_transform(y_pred_ohe)
    
    df = pd.DataFrame()
    df['dim_1'] = projecoes[:,0]
    df['dim_2'] = projecoes[:,1]
    df['word'] = vocabulario
    df['prediction'] = y_pred
    df['epoch'] = [n_epoch] * len(vocabulario)
    return df

df = get_data(0)
print(len(df))
for n_epoch in range(1, 50):
    clf.fit(X_train, y_train, epochs=1, verbose=1)
    df_ = get_data(n_epoch)
    df = pd.concat((df,df_))
    print(len(df))

df.to_csv('embeddings_over_epochs.csv')
