import wikipedia


def wiki_summary(val):
    return wikipedia.summary(val,sentences=2)