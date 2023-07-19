import numpy as np

import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
from string import punctuation




stop_words = nltk.corpus.stopwords.words("english")
for word in ['what', 'how', 'where', 'who', 'which'] :
    stop_words.append(word)


def preprocess(text) :

    file = open("./top20tags.txt", "r")
    top20tags = file.read()
    top20tags = list(top20tags.split('\n')[:-1])
    file.close()

    
    # text convert to lowercase
    text = text.lower()
    
    # remove punctuation in the string
    text = text.translate(text.maketrans('', '', punctuation))  
    
    # Tokenization
    token_list = nltk.word_tokenize(text)
    
    new_text = []
    
    for token in token_list :
        if token in top20tags :
            new_text.append(token)
        elif token not in stop_words :
            for char in token :
                if char.isdigit() :
                    token = token.replace(char, '')
            new_text.append(token)
    
    # Lemmatisation
    lem = nltk.stem.WordNetLemmatizer()
    
    # remove adjectives, adverbs, personal pronoun and preposition/subordinating conjunction
    tags=['JJ','RB','PRP','IN','VB']
    for token in new_text :
        for tag in tags:
            if nltk.pos_tag([token])[0][1].startswith(tag):
                new_text.remove(token)
    
    # remove duplicate words
    new_text=set(new_text)
    new_text =[word for word in new_text if word!='']
    print(new_text)
    new_text = ' '.join(new_text)
    
    # top20tags.txt follows the list in mlb.classes_
    file = open("./top20tags.txt", "r")
    top20tags = file.read()
    top20tags = top20tags.split()[:20]
    file.close()
    vector=[0 for i in top20tags]
    for word in new_text:
        if word in top20tags:
            vector[top20tags.index(word)]=1
    return new_text
    #return tf.reshape(embed([new_text]), [-1]).numpy()


def feature_USE_fct(sentences, b_size = 20) :
    
    batch_size = b_size

    features = sentences[0:batch_size].numpy()

    return features


def clean_output(result) :
    # top20tags.txt follows the list in mlb.classes_
    file = open("./top20tags.txt", "r")
    top20tags = file.read()
    top20tags = list(top20tags.split('\n')[:-1])
    file.close()

    output_tags_list = []

    for i in range(len(result[0])) :
        if result[0][i] == 1 :
          output_tags_list.append("#" + top20tags[i])

    if len(output_tags_list) == 0 :
        output_tags_list = ["no recommendation..."]

    return output_tags_list


