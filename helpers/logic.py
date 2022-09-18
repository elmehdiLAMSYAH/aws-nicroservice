import wikipedia
from textblob import TextBlob


def wikiData(name="pablo escobar", length=1):
    return wikipedia.summary(name, length)


def wikiSearch(name="mohammed 6"):
    return wikipedia.search(name)


def sentencwblob(text):
    blob = TextBlob(text=text)
    return blob.tags
