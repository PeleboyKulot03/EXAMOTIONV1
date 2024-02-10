from transformers import pipeline

classifier = pipeline("text-classification", model='bhadresh-savani/bert-base-uncased-emotion', return_all_scores=False)

paragraph = "I'm really scared. The test was so hard, and I'm worried I didn't do well at all.y"
prediction = classifier(paragraph, )


pred = prediction[0]["label"]

if pred == 'joy':
    pred = 'excited'
if pred == 'sad':
    pred = 'bored'
elif pred == 'anger':
    pred = 'frustrated'

print(f"word: {paragraph}")
print(f"prediction: {pred}")
print(prediction)


paragraph = "Wow, that exam was way different than I thought it would be. I'm genuinely surprised by the questions. It's Maam Ruth's fault."
prediction = classifier(paragraph, )


pred = prediction[0]["label"]

if pred == 'joy':
    pred = 'excited'
if pred == 'sad':
    pred = 'bored'
elif pred == 'anger':
    pred = 'frustrated'

print(f"word: {paragraph}")
print(f"prediction: {pred}")
print(prediction)

