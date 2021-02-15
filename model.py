from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def create_model():
    model = load_model('model.hdf5')
    print(model.outputs)
    return model

def preprocess_data(input_str,tokenizer):

    tokens = tokenizer.texts_to_sequences(input_str)
    padded = pad_sequences(tokens, maxlen=100)
    return padded

