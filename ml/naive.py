import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix
data ={

       "text":[
           "free money offer now",
           "win lottery cash prize",
           "meeting schedule today",
           "project deadline tomorrow",
           "exclusive offer just for you",
           "lets discuss work progress"
       ],
       "label":["spam","spam","ham","ham","spam","ham"]
}

df=pd.DataFrame(data)
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(df["text"])
y=df["label"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=42)
nb=MultinomialNB()
nb.fit(x_train,y_train)
y_pred=nb.predict(x_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confursion Matrix:",confusion_matrix(y_test,y_pred))