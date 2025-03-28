from flask import Flask, request, jsonify
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

app = Flask(__name__)

stop_words = set(stopwords.words('english'))

# load model and vectorizer
with open('model.pkl', 'rb') as f:
  model = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
  tfidf = pickle.load(f)

def clean_text(text):
  if not isinstance(text, str) or not text:
    return ""
  text = text.lower()
  text = re.sub(r'[^a-zA-Z0-9\s.,:\'"]', '', text)  # Keep quotes
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  return ' '.join(tokens)

@app.route('/predict', methods=['POST'])
def predict():
  text = request.json.get('text')
  if not text:
    return jsonify({'error': 'Text is required'}), 400
  cleaned_text = clean_text(text)
  text_tfidf = tfidf.transform([cleaned_text])
  prediction = model.predict(text_tfidf)[0]
  return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
