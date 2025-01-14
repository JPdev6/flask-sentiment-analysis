from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')  # Get the user input from the form

    # Check if input is empty
    if not text.strip():
        result = "Please enter some text!"
        color_class = "alert-warning"  # Yellow background for warnings
        return render_template('index.html', result=result, color_class=color_class, text=text)

    # Use TextBlob for sentiment analysis
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity  # Returns a value between -1.0 and 1.0

    # Determine the sentiment based on polarity score
    if sentiment_score > 0:
        result = "Positive Sentiment"
        color_class = "alert-success"  # Light green background
    elif sentiment_score < 0:
        result = "Negative Sentiment"
        color_class = "alert-danger"  # Light red background
    else:
        result = "Neutral Sentiment"
        color_class = "alert-secondary"  # Light gray background

    return render_template('index.html', result=result, color_class=color_class, text=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
