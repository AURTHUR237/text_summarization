from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']

        summarizer = pipeline("summarization")
        abstractive_summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

        return render_template('index.html', text=text, abstractive_summary=abstractive_summary)

if __name__ == '__main__':
    app.run(debug=True)
