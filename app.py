from flask import Flask, jsonify
from joblib import load

from use import preprocess, clean_output

app = Flask(__name__)


# route test hello world

@app.route("/")
def hello():
    return "Hello World!"


# route api pour requête get

pipe = load('trained_use_logreg.joblib')

@app.route("/api/text=<text>")
def my_api(text) :

	text_clean = preprocess(text)
	output = pipe.predict([text_clean])
	output_clean = clean_output(output)

	dictionnaire = {
		"text" : text,
		"tags" : output_clean
	}

	return jsonify(dictionnaire)

if __name__ == "__main__" :
	app.run(debug = True)