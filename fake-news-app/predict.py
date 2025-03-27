import sys
import pickle

# load model and vectorizer
with open('model.pkl', 'rb') as f:
  model = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
  tfidf = pickle.load(f)

# get input from command line
text = sys.argv[1]

# preprocess and predict
text_tfidf = tfidf.transform([text])
prediction = model.predict(text_tfidf)[0]

# optput result
print(prediction)