from transformers import pipeline
import random as rand

classifier = pipeline("text-classification", model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=False)

paragraph = "I am soprised"
prediction = classifier(paragraph, )

pred = prediction[0]["label"]
score = prediction[0]["score"]

sad = ['Bored', 'Neutral']

if pred == 'joy':
    pred = 'Excited'
if pred == 'sadness':
    pred = sad[rand.randint(0, 1)]
elif pred == 'anger':
    pred = 'Frustrated'
elif pred == 'surprise':
    pred = 'Surprised'
elif pred == 'fear':
    pred = 'Nervous'

if score < 0.60:
    pred = "No Emotion"

print(f"word: {paragraph}")
print(f"prediction: {pred}")
print(prediction)
