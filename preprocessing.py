import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string 
from collections import Counter
cnt = Counter()
import nltk
nltk.download('stopwords')


class preprocessing_pipline:
    def __init__(self, data):
        self.data = data
        self.preprocess()
        #self.tokens = self.tokenize(self.data)
        #self.most_common = self.get_most_freq_words()
        
    def tokenize(self, text):
        combined_text = ' '.join(text)
        tokens = word_tokenize(combined_text)
        return tokens
    
    def get_most_freq_words(self):
        word_count = Counter(self.tokens)
        most_common = word_count.most_common()
        return most_common
    
    def lower_case(self, text):
        return text.lower()
    def remove_punctuation(self, text):
        PUNCT_TO_REMOVE = string.punctuation
        translation_table = str.maketrans('', '', PUNCT_TO_REMOVE)
        return text.translate(translation_table)
    def remove_stopwords(self, text): # we will maybe not use this function, because we are doing text generation
        STOPWORDS = set(stopwords.words('english'))
        return " ".join([word for word in str(text).split() if word not in STOPWORDS])
    # Removal of Rare words 
    # This can help in reducing the size, so help for model generalization and avoid noises
    def remove_rare_words(self, text):
        RAREWORDS = set([w for (w, wc) in cnt.most_common(10)])
        return " ".join([word for word in str(text).split() if word not in RAREWORDS])
    
    def preprocess(self):
        self.data = self.data.apply(self.lower_case)
        self.data = self.data.apply(self.remove_punctuation)
        self.data = self.data.apply(self.remove_stopwords)
        self.data = self.data.apply(self.remove_rare_words)
        return self.data
    def preprocess_light(self):
        self.data = self.data.apply(self.lower_case)
        self.data = self.data.apply(self.remove_punctuation)
        return self.data

# Test 

import os

path = 'Trump Rally Speeches/'
files = os.listdir(path)
files = [path + file for file in files]
 
dates = []
locations = []
years = []
days = []
months = []
speeches_text = []
 
month_ab = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']
for file in files:
    for month in month_ab:
        if month in file:
            locations.append(file[file.find('/')+1:file.find(month)])
            break
    for i, mont in enumerate(month_ab):
        if month in file:
            date = file[file.find(month):file.find('.txt')]
            dates.append(date)
            months.append(date[:3])
            days.append(str(date[3]))
            years.append(date[-4:])
            break   
        
# Extracting the text from the file
for file in files:
    with open(file, 'r') as f:
        speeches_text.append(f.read()) 
        
df = pd.DataFrame({'Speech':files, 'Date':dates, 'Location':locations, 'Year':years, 'Month':months, 'Day':days, 'Speech_Text':speeches_text})

# Preprocessing the data
preprocessing = preprocessing_pipline(df['Speech_Text'])
df['Speech_pr'] = preprocessing.data
# light preprocessing
preprocessing_light = preprocessing_pipline(df['Speech_Text'])
df['Speech_pr_light'] = preprocessing_light.preprocess_light()
 
# Results
print(df['Speech_pr'][0][:100])
print(df['Speech_Text'][0][:100])
print(df['Speech_pr_light'][0][:100])
