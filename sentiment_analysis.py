from textblob import TextBlob

sentence = input("Enter a sentence: ")

snt = TextBlob(sentence)

print("The sentiment of your sentence btw (-1,1) is {}".format(str(snt.sentiment.polarity)))
