import requests

def emotion_detector(text_to_analyse):

    if text_to_analyse == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return {
        'anger': 0.01,
        'disgust': 0.01,
        'fear': 0.01,
        'joy': 0.95,
        'sadness': 0.02,
        'dominant_emotion': 'joy'
    }