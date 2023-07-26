import spacy
import numpy as np

def lemmatization(text, allowed_postags=["NOUN", "VERB", "ADJ", "ADV"]):
    """
    Lemmatize the input text using spaCy.

    Parameters:
        text (str): The input text to be lemmatized.
        allowed_postags (list): List of allowed part-of-speech tags for lemmatization.

    Returns:
        str: The lemmatized text.
    """
    top_10_tags = []
    with open("./top_10_tags.txt", "r") as file:
        top_10_tags = [tag.strip() for tag in file]

    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    doc = nlp(text)
    new_text = []
    for token in doc:
        if token.orth_ in top_10_tags:
            new_text.append(token.orth_)
        else:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
    final = " ".join(new_text)
    return final

def clean_output(result):
    """
    Clean the output result obtained from model predictions.

    Parameters:
        result (numpy.array): The binary array obtained from model predictions.

    Returns:
        list: A list of cleaned output tags.
    """
    top_10_tags = []
    with open("./top_10_tags.txt", "r") as file:
        top_10_tags = [tag.strip() for tag in file]

    output_tags_list = ["#" + top_10_tags[i] for i, val in enumerate(result[0]) if val == 1]

    if not output_tags_list:
        output_tags_list = ["no recommendation..."]

    return output_tags_list
