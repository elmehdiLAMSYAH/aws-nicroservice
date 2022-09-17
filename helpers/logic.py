import wikipedia


def wikiData(name="pablo escobar", length=1):
    return wikipedia.summary(name, length)


def wikiSearch(name="mohammed 6"):
    return wikipedia.search(name)
