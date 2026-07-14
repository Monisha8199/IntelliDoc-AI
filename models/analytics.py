import math

def analyze_document(text):

    words = len(text.split())

    characters = len(text)

    paragraphs = len([p for p in text.split("\n") if p.strip()])

    reading_time = math.ceil(words / 200)

    return {
        "Words": words,
        "Characters": characters,
        "Paragraphs": paragraphs,
        "Reading Time": f"{reading_time} min"
    }
    