import numpy as np
import spacy
spacy.load('en_core_web_sm')


def lemmatization(text, allowed_postags = ["NOUN", "VERB", "ADJ", "ADV"]) :

    file = open("./top_10_tags.txt", "r")
    top_10_tags = file.read()
    top_10_tags = list(top_10_tags.split('\n')[:-1])
    file.close()


    nlp = spacy.load("en_core_web_sm", disable = ["parser", "ner"])
    doc = nlp(str(text))
    new_text = []
    for token in doc :
        if token.orth_ in top_10_tags :
            new_text.append(token.orth_)
        else :
            if token.pos_ in allowed_postags :
                new_text.append(token.lemma_)
    final = " ".join(new_text)
    return final

def clean_output(result) :

    file = open("./top_10_tags.txt", "r")
    top_10_tags = file.read()
    top_10_tags = list(top_10_tags.split('\n')[:-1])
    file.close()

    output_tags_list = []

    for i in range(len(result[0])) :
        if result[0][i] == 1 :
          output_tags_list.append("#" + top_10_tags[i])

    if len(output_tags_list) == 0 :
        output_tags_list = ["no recommendation..."]

    return output_tags_list
