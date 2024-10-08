"""
This module defines a Flask web application for detecting emotions in text.

It provides an endpoint `/emotionDetector` that takes a text string as input and returns
the detected emotions along with the dominant emotion. The application uses a custom 
emotion detection model for analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to analyze the emotion of a given text.

    Retrieves the text from the request arguments, processes it through the
    emotion detector, and returns the detected emotions along with the dominant emotion.
    """
    # Retrieve the text to detect from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector and store the response
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return "Invalid input! Try again."

    # Format the output string
    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
