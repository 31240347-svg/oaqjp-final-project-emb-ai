"""Flask server for the Watson NLP Emotion Detection application."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text provided by the user."""
    text_to_analyse = request.args.get("textToAnalyze")

    if not text_to_analyse or not text_to_analyse.strip():
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
