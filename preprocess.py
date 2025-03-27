import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# download nltk data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# load datasets
fake = pd.read_csv('data/Fake.csv')
true = pd.read_csv('data/True.csv')

# add labels
fake['label'] = 0
true['label'] = 1

# combine datasets
data = pd.concat([fake, true], ignore_index=True)

# clean text function
stop_words = set(stopwords.words('english'))

def clean_text(text):
  text = text.lower()
  text = re.sub(r'[^a-zA-Z\s]', '', text)
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  return ' '.join(tokens)

# apply cleaning to title and text
data['title'] = data['title'].apply(clean_text)
data['text'] = data['text'].apply(clean_text)

data['combined'] = data['title'] + ' ' + data['text']

# save preprocessed dta
data[['combined', 'label']].to_csv('data/processed_data.csv', index=False)
print('Data preprocessing complete!')