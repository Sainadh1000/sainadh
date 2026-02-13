import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding,Dense,GlobalAveragePooling1D
from tensorflow.keras.models import Sequential

imdb=tf.keras.datasets.imdb
(x_train,y_train),(x_test,y_test)=imdb.load_data(num_words=5000)

x_train_pad = pad_sequences(x_train, maxlen=100)
x_test_pad  = pad_sequences(x_test, maxlen=100)

model=Sequential(
    [Embedding(5000,16,input_length=(100,)),# top 5000 frequent words,16 dimension each token(word)convert into 16 vectors, no_of inputs
    GlobalAveragePooling1D(),
    Dense(16,activation='relu'),
    Dense(1,activation='sigmoid')]
)

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.summary()



model.fit(x_train_pad,y_train,epochs=10,validation_data=(x_test_pad,y_test),verbose=1)
model.summary()

word_index=imdb.get_word_index()
word_index={k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

def encode_review(text):
  words=text.lower().split()
  encoded=[]
  for word in words:
    if word in word_index and word_index[word]<5000:
      encoded.append(word_index[word])
    else:
      encoded.append(2)
  return encoded


new_sentence = input("Enter your review: ")

encoded = encode_review(new_sentence)

from tensorflow.keras.preprocessing.sequence import pad_sequences
padded = pad_sequences([encoded], maxlen=100)

prediction = model.predict(padded)

score = prediction[0][0]

print("Prediction Score:", score)

if score > 0.5:
    print("Positive Review ")
else:
    print("Negative Review ")
