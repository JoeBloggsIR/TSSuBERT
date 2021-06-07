# Libraries import

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense,Dropout, Input, Concatenate
from tensorflow.keras import regularizers
from transformers import *
from transformers import BertTokenizer, TFBertModel, BertConfig,TFDistilBertModel,DistilBertTokenizer,DistilBertConfig

# Retrieve the existing tokenizer and pre-trained model from DistilBert.

dbert_tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
dbert_model = TFDistilBertModel.from_pretrained('distilbert-base-uncased')

# Function for model creation

def create_model():
    inps = Input(shape = (max_len,), dtype='int64')
    masks= Input(shape = (max_len,), dtype='int64')
    dbert_layer = dbert_model(inps, attention_mask=masks)[0][:,0,:]
    freq_layer = Input(shape = (len(dbert_tokenizer.vocab)-1), dtype='float64') # the first token (PAD token) is not used in the tokens frequencies
    dense0 = Dense(50,activation='relu',kernel_regularizer=regularizers.l2(0.01))(freq_layer)
    dropout0= Dropout(0.5)(dense0)
    concatted = Concatenate()([dbert_layer, dropout0])
    dense = Dense(512,activation='relu',kernel_regularizer=regularizers.l2(0.01))(concatted)
    dropout= Dropout(0.5)(dense)
    pred = Dense(1, activation='relu',kernel_regularizer=regularizers.l2(0.01))(dropout)
    model = tf.keras.Model(inputs=[inps,masks,freq_layer], outputs=pred)
    print(model.summary())
    return model

# Tokenizer vocabulary update (add htg, mtn, url and rtw tokens)

dbert_tokenizer.vocab["htg"]=len(dbert_tokenizer.vocab)
dbert_tokenizer.vocab["mtn"]=len(dbert_tokenizer.vocab)
dbert_tokenizer.vocab["url"]=len(dbert_tokenizer.vocab)
dbert_tokenizer.vocab["rtw"]=len(dbert_tokenizer.vocab)

dbert_model.resize_token_embeddings(len(dbert_tokenizer))

model=create_model()