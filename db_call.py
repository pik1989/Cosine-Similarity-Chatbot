import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import re

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

def preprocess(text):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]
    return ' '.join(stemmed_tokens)

def preprocess_with_stopwords(text):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = nltk.word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]
    return ' '.join(stemmed_tokens)

class QASystem:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath, escapechar='\\')
        self.questions_list = self.df['Questions'].tolist()
        self.answers_list = self.df['Answers'].tolist()
        self.vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
        self.X = self.vectorizer.fit_transform([preprocess_with_stopwords(q) for q in self.questions_list])

    def get_response(self, text):
        processed_text = preprocess_with_stopwords(text)
        vectorized_text = self.vectorizer.transform([processed_text])
        similarities = cosine_similarity(vectorized_text, self.X)
        max_similarity = np.max(similarities)

        if max_similarity > 0.6:
            high_similarity_questions = [q for q, s in zip(self.questions_list, similarities[0]) if s > 0.8]
            target_answers = []
            for q in high_similarity_questions:
                q_index = self.questions_list.index(q)
                target_answers.append(self.answers_list[q_index])
            Z = self.vectorizer.fit_transform([preprocess_with_stopwords(q) for q in high_similarity_questions])
            processed_text_with_stopwords = preprocess_with_stopwords(text)
            vectorized_text_with_stopwords = self.vectorizer.transform([processed_text_with_stopwords])
            final_similarities = cosine_similarity(vectorized_text_with_stopwords, Z)
            closest = np.argmax(final_similarities)
            return target_answers[closest]
        else:
            return "I can't answer this question."
