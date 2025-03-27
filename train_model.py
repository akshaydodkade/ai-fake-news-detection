import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# load preprocessed data
data = pd.read_csv('data/processed_data.csv')

# features and labels
X = data['combined']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# vectorize text
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.fit_transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# evaluate
y_pred = model.predict(X_test_tfidf)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Report:\n', classification_report(y_test, y_pred))

# save model and vectorizer
with open('fake-news-app/model.pkl', 'wb') as f:
  pickle.dump(model, f)
with open('fake-news-app/tfidf.pkl', 'wb') as f:
  pickle.dump(tfidf, f)
print('Model and Vectorizer saved!')