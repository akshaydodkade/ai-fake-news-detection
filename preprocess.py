import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english')) - {"not", "without"}

def clean_text(text):
  if not isinstance(text, str) or not text:
    return ""
  text = text.lower()
  text = re.sub(r'[^a-zA-Z0-9\s.,:\'"]', '', text)  # Keep quotes, colons
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  return ' '.join(tokens)

# Load and preprocess data
fake = pd.read_csv('data/Fake.csv')
true = pd.read_csv('data/True.csv')

# Add labels
fake['label'] = 0
true['label'] = 1

# Combine datasets
data = pd.concat([fake, true], ignore_index=True)

# Clean text and drop rows with empty text after cleaning
data['text'] = data['text'].apply(clean_text)
data = data[data['text'].str.strip() != '']  # Remove rows with empty text
data = data.dropna(subset=['text'])  # Drop any remaining NaN

# Save preprocessed data
data.to_csv('data/preprocessed_data.csv', index=False)
print(f"Preprocessed {len(data)} rows successfully.")