import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/alex/sura-poc-analisis-de-sueno-297379928d09.json"

def analyze(movie_review_filename):
    client = language.LanguageServiceClient()
    with open(movie_review_filename, 'r') as review_file:
        content = review_file.read()
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT,
        language="es-CL")
    annotations = client.analyze_sentiment(document=document)
    print_result(annotations)


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


analyze('/home/alex/Imágenes/frases_WA0032.txt')