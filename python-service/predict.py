from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load model and vectorizer
with open('model.pkl', 'rb') as f:
  model = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
  tfidf = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
  text = request.json.get('text')
  if not text:
    return jsonify({'error': 'Text is required'}), 400
  text_tfidf = tfidf.transform([text])
  prediction = model.predict(text_tfidf)[0]
  return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
