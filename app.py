import os
import uuid
from flask import Flask, request, render_template, send_file
import pdfplumber
import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_desc = request.form['jobdesc']
        resumes = request.files.getlist('resumes')

        resume_texts = []
        filenames = []

        for resume in resumes:
            if not resume.filename.lower().endswith('.pdf'):
                continue
            unique_name = f"{uuid.uuid4()}_{resume.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            resume.save(filepath)
            raw_text = extract_text_from_pdf(filepath)
            processed_text = preprocess_text(raw_text)
            resume_texts.append(processed_text)
            filenames.append(resume.filename)

        job_processed = preprocess_text(job_desc)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([job_processed] + resume_texts)
        scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        df = pd.DataFrame({
            'Resume': filenames,
            'Score': [round(score, 4) for score in scores]
        }).sort_values(by='Score', ascending=False)

        df.columns.name = None
        csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume_ranking_report.csv')
        df.to_csv(csv_path, index=False)

        return render_template('index.html', results=df.values.tolist(), headers=df.columns.tolist(), download=True)

    return render_template('index.html', results=None, headers=None, download=False)

@app.route('/download')
def download():
    return send_file('uploads/resume_ranking_report.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
