from flask import Flask, jsonify
from joblib import load

from use import lemmatization, clean_output

app = Flask(__name__)


# route test hello world

@app.route("/")
def hello():
    return "Hello World!"


# route api pour requête get

pipe = load('trained_bow_logreg.joblib')

@app.route("/api/text=<text>")
def my_api(text) :

	text_clean = lemmatization([text])
	output = pipe.predict([text_clean])
	output_clean = clean_output(output)

	dictionnaire = {
		"text" : text,
		"tags" : output_clean
	}

	print(dictionnaire)

	return jsonify(dictionnaire)

if __name__ == "__main__" :
	app.run(debug = True)