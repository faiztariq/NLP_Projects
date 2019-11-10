from pickle import load
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random

seqlen = 10

def generate_seq(model, mapping, seq_length, seed_text, n_chars):
    in_text = seed_text
    for _ in range(n_chars):
        encoded = [mapping[char2] for char2 in in_text]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        encoded = to_categorical(encoded, num_classes=len(mapping))
        probs = model.predict_proba(encoded)
        yhat = random.choices(range(0,vocab_size), weights=probs[0], k=1)[0]
        out_char = ''
        for char, index in mapping.items():
            if index == yhat:
                out_char = char
                break
        in_text += out_char
        if char =="\n":
            break
    return in_text
 
model = load_model('model_3lay.h5')
mapping = load(open('mapping.pkl', 'rb'))

vocab_size = len(mapping)
 
print(generate_seq(model, mapping, seqlen, 'Tump tells', 400))