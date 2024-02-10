from deepface import DeepFace
from transformers import pipeline


class Models:
    def __init__(self):
        self.classifier = pipeline("text-classification", model='bhadresh-savani/bert-base-uncased-emotion',
                                   return_all_scores=False)
        self.model = DeepFace.build_model('Emotion')

    def get_emotion_model(self):
        return self.model

    def get_classifier(self):
        return self.classifier
