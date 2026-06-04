from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h2>Emotion Detector</h2>
    <form action="/emotionDetector">
        <input type="text" name="textToAnalyze">
        <input type="submit" value="Analyze Emotion">
    </form>
    '''

@app.route("/emotionDetector")
def sent_analyzer():
    text = request.args.get("textToAnalyze", "")

    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"Dominant Emotion: {result['dominant_emotion']}"

if __name__ == "__main__":
    app.run(port=5001, debug=True)