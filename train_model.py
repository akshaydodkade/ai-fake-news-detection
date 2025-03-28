import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load preprocessed data
data = pd.read_csv('data/preprocessed_data.csv')
X = data['text']
y = data['label']

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42, stratify=y
)

# Train model with class weighting
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Report:\n", report)

# Save model and vectorizer
with open('python-service/model_updated4.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('python-service/tfidf_updated4.pkl', 'wb') as f:
    pickle.dump(tfidf, f)