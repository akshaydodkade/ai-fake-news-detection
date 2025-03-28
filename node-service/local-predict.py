import sys
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english')) - {"not", "without"}

inputs = [
  "Senior U.S. Republican senator: 'Le",
  "Senior U.S. Republican senator: 'Let",
  "NASA successfully launches new telescope to study exoplanets."
]

# Load model and vectorizer
with open('model_updated4.pkl', 'rb') as f:
  model = pickle.load(f)
with open('tfidf_updated4.pkl', 'rb') as f:
  tfidf = pickle.load(f)

def clean_text(text):
  if not isinstance(text, str) or not text:
    return ""
  text = text.lower()
  text = re.sub(r'[^a-zA-Z0-9\s.,:\'"]', '', text)  # Keep quotes, colons
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  return ' '.join(tokens)

# Get input text from command line
text = sys.argv[1]

# Preprocess and predict
cleaned_text = clean_text(text)
text_tfidf = tfidf.transform([cleaned_text])
prediction = model.predict(text_tfidf)[0]

# Output result
print(prediction)