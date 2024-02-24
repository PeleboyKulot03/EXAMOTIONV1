from googletrans import Translator

translator = Translator()
translation = translator.translate("I am natatakot kanina", src='tl', dest='en')
print(translation.text)
