import joblib
import re
import string
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Inisialisasi stop words dan stemmer
stop_words = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def load_model(model_path):
    return joblib.load(model_path)

def load_vectorizer(vectorizer_path):
    return joblib.load(vectorizer_path)

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

def predict(model="multinomial_nb_model.txt", vectorizer="tfidf_vectorizer.pkl", input_text):
    """
    Predict apakah input text adalah hoax atau tidak

    Args:
        model: model machine learning model (default: "multinomial_nb_model.txt")
        vectorizer: vectorizer yang digunakan (default: "tfidf_vectorizer.pkl")
        input_text: raw input text untuk diklasifikasi

    Returns:
        str: "Hoax" atau "Tidak Hoax" berdasarkan prediksi
    """
    # Preprocess the input text
    processed_text = preprocess_text(input_text)
    
    # Vectorize the input text
    vectorized_text = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction = model.predict(vectorized_text)
    
    # Map prediction to class label
    if prediction[0] == 0:
        return "Tidak Hoax"
    else:
        return "Hoax"