
from flask import Flask, jsonify
from joblib import load
from preprocess import lemmatization, clean_output

app = Flask(__name__)
pipe = load('trained_bow_logreg.joblib')


@app.route("/")
def hello():
    """
    Default route to display "Hello World!" message just to test you are good with flask :).
    """
    return "Hello World!"


@app.route("/api/text=<text>")
def my_api(text):
    """
    API route to process the input text and return the tags.

    Parameters:
        text (str): The input text from the user.

    Returns:
        JSON: A JSON object containing the input text and the predicted tags.
    """
    text_clean = lemmatization([text])
    output = pipe.predict([text_clean])
    output_clean = clean_output(output)

    data = {
        "text": text,
        "tags": output_clean
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
