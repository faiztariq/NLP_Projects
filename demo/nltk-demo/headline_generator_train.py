import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from pickle import dump, load
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Dense, LSTM, SimpleRNN

seqlen = 10
batchsize = 512

def myGenerator():
    while 1:
        for i in range(batchnum): 
            X_batch = []
            y_batch = []
            for j in range(batchsize):
                X_batch.append(encoded_text[i*batchsize+j:i*batchsize+j+seqlen])
                y_batch.append(encoded_text[i*batchsize+j+seqlen:i*batchsize+j+seqlen+1])
                
            X_batch = np.array([to_categorical(x, num_classes=vocab_size) for x in X_batch])
            y_batch = np.array(to_categorical(y_batch, num_classes=vocab_size))

            yield (X_batch, y_batch)

path_to_csv = ".\demo\\nltk-demo\dataset\data_nytimes_front_page.csv"
df = pd.read_csv(path_to_csv, sep=',',index_col = "id")
print(df.shape)
df.head()

text = df["title"].str.cat(sep='\n')
text_size = len(text)
print('Text Size: %d' % text_size)

chars = sorted(list(set(text)))
mapping = dict((c, i) for i, c in enumerate(chars))
dump(mapping, open('mapping.pkl', 'wb'))

vocab_size = len(mapping)
print('Vocabulary Size: %d' % vocab_size)

encoded_text = [mapping[char] for char in text]
encode_size = len(encoded_text)
print('Code Size: %d' % encode_size)

batchnum = int((encode_size - seqlen) / batchsize)

model = Sequential()
model.add(LSTM(300, return_sequences=True, input_shape=(seqlen, vocab_size)))
model.add(LSTM(150, return_sequences=True))
model.add(LSTM(75))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

my_generator = myGenerator()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit_generator(my_generator, steps_per_epoch = batchnum, epochs = 10, verbose=1)
model.save('model_3lay.h5')