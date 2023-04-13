from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import numpy as np

class Classifier:
    def __init__(self) -> None:
        self.vectorizer = CountVectorizer()
        self.clf = MultinomialNB()
        self.treshold = 0.4

    def train(self, X: list, Y: list) -> None:
        self.clf.fit(self.vectorizer.fit_transform(X), Y)

    def retrain(self, X: list, Y: list) -> None:
        self.clf.partial_fit(self.vectorizer.transform([X]), Y)

    def predict(self, X: str):
        x = self.vectorizer.transform([X]).reshape(1, -1)
        proba: float = self.clf.predict_proba(x).max()
        prediction: str = self.clf.predict(x)[0]
        if proba <= self.treshold:
            prediction = "undefined"
        return prediction, "%.2f" % proba
    
    def load(self):
        self.clf = joblib.load("model.sav")
    
    def safe(self):
        joblib.dump(self.clf, "model.sav")
