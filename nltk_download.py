import nltk

try:
    nltk.download()
    print("nltk downloaded")
except:
    print("ntlk download fail")