import sys
import pickle

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Get input text from command line
text = sys.argv[1]

# Preprocess and predict
text_tfidf = tfidf.transform([text])
prediction = model.predict(text_tfidf)[0]

# Output result
print(prediction)