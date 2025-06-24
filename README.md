# 🧠 AI-Powered Resume Ranker

An intelligent Flask web application to **rank resumes** for a job profile using **Natural Language Processing (NLP)**. It extracts, processes, and compares PDF resumes to a given job description using **TF-IDF vectorization** and **cosine similarity**.

---

## 🎯 Objective

To automate and streamline the HR process by:
- Extracting content from resumes
- Matching and ranking resumes based on job description relevance
- Providing an easy-to-use web interface and downloadable reports

---

## 🛠️ Tech Stack & Tools

| Tool / Library | Purpose |
|----------------|---------|
| **Python** | Core programming language |
| **Flask** | Web application framework |
| **pdfplumber** | Extract text from PDF resumes |
| **SpaCy** | Preprocess text (lemmatization, stopword removal) |
| **Scikit-learn** | TF-IDF Vectorizer & Cosine Similarity |
| **Pandas** | Data handling and report generation |
| **Bootstrap** | Responsive front-end styling |
| **HTML/CSS** | Web UI |

---

## 📌 Key Features

- Upload multiple PDF resumes at once
- Paste a job description into the web form
- Automated resume ranking using similarity score
- CSV report download for HR use
- Clean and responsive UI for ease of use

---

## ⚙️ How It Works

1. **Upload Resumes:** Multiple resumes in `.pdf` format.
2. **Enter Job Description:** Paste job role, skills, qualifications, etc.
3. **Text Processing:**
   - Resumes and job description are preprocessed using SpaCy.
   - Stopwords and punctuations removed; text lemmatized.
4. **Vectorization & Scoring:**
   - Text is transformed into vectors using **TF-IDF**.
   - Similarity is computed using **cosine similarity**.
5. **Ranking:**
   - Resumes are scored based on similarity to job description.
   - Sorted results are displayed on the web page.
6. **Download:**
   - CSV report (`resume_ranking_report.csv`) can be downloaded.

---

## 🧪 Sample Output

| Resume File       | Match Score |
|-------------------|-------------|
| resume_amit.pdf   | 0.8532      |
| resume_sara.pdf   | 0.7911      |
| resume_vijay.pdf  | 0.6415      |

---

## 🖥️ UI Snapshot

- Simple upload and input form
- Ranked table view with scores
- Download button for CSV report

---

## 📁 Project Structure

