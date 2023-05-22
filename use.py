import numpy as np

import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
stop_words = nltk.corpus.stopwords.words("english")
for word in ['what', 'how', 'where', 'who', 'which'] :
    stop_words.append(word)
from string import punctuation

import tensorflow_hub as hub


def preprocess(text) :

    file = open("./top_10_tags.txt", "r")
    top_10_tags = file.read()
    top_10_tags = list(top_10_tags.split('\n')[:-1])
    file.close()

    """" Nettoyage du texte :
    passage au minuscule
    passage des c# en csharp pour éviter des suppressions non souhaitées
    conservation des mots qui sont des tags
    suppression de la ponctuation, des chiffres,
    et des stopwords
    puis lemmatisation """
    
    text = text.lower()
    
    for i in range(1, len(text)) :
        if text[i-1] == 'c' and text[i] == '#' :
            text = text.replace(text[i], 'sharp')
    
    token_list = nltk.word_tokenize(text)
    
    new_text = []
    
    for token in token_list :
        if token in top_10_tags :
            new_text.append(token)
        elif token not in stop_words :
            for char in token :
                if char in punctuation or char.isdigit() :
                    token = token.replace(char, '')
            new_text.append(token)
    
    lem = nltk.stem.WordNetLemmatizer()
    
    for token in new_text :
        if nltk.pos_tag([token])[0][1].startswith('V') :
            index = new_text.index(token)
            token_lem = lem.lemmatize(token, pos = 'v')
            new_text[index] = new_text[index].replace(token, token_lem)
            
    new_text = ' '.join(new_text)

    return new_text


# Fonction de feature extraction pas USE

model_path = "https://tfhub.dev/google/universal-sentence-encoder/4"

embed = hub.load(model_path)

def feature_USE_fct(sentences, b_size = 10) :
    batch_size = b_size

    features = embed(sentences[0:batch_size]).numpy()

    return features


# Fonction de mise en forme du résultat

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