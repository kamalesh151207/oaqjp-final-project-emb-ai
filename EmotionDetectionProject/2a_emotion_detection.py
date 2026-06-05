from EmotionDetection.emotion_detection import emotion_detector

if __name__ == "__main__":
    text = "I am very happy today!"
    result = emotion_detector(text)
    print(result)