import nltk
from string import punctuation
import tensorflow_hub as hub

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

stop_words = nltk.corpus.stopwords.words("english")
stop_words.extend(['what', 'how', 'where', 'who', 'which'])

# Feature extraction using USE
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


def preprocess(text):
    # Load top 10 tags from file
    with open("./top_10_tags.txt", "r") as file:
        top_10_tags = file.read().split('\n')[:-1]

    text = text.lower()

    # Replace 'c#' with 'csharp'
    for i in range(1, len(text)):
        if text[i - 1] == 'c' and text[i] == '#':
            text = text.replace(text[i], 'sharp')

    token_list = nltk.word_tokenize(text)

    new_text = []

    for token in token_list:
        # Keep tokens that are top 10 tags
        if token in top_10_tags:
            new_text.append(token)
        # Remove stopwords and punctuation
        elif token not in stop_words:
            token = ''.join(char for char in token if char not in punctuation and not char.isdigit())
            new_text.append(token)

    lem = nltk.stem.WordNetLemmatizer()
"""
    for token in new_text:
        # Lemmatize verbs
        if nltk.pos_tag([token])[0][1].startswith('V'):
            index = new_text.index(token)
            token_lem = lem.lemmatize(token, pos='v')
            new_text[index] = new_text[index].replace(token, token_lem)"""

    new_text = ' '.join(new_text)

    return new_text

def feature_USE_fct(sentences, b_size = 10) :
    
    batch_size = b_size

    features = embed(sentences[0:batch_size]).numpy()

    return features

def clean_output(result):
    # Load top 10 tags from file
    with open("./top_10_tags.txt", "r") as file:
        top_10_tags = file.read().split('\n')[:-1]

    output_tags_list = ['#' + top_10_tags[i] for i, tag in enumerate(result[0]) if tag == 1]

    if len(output_tags_list) == 0:
        output_tags_list = ["no recommendation..."]

    return output_tags_list
