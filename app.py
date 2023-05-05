from flask import Flask, jsonify
from joblib import load

from use import preprocess, clean_output

app = Flask(__name__)


# route test hello world

@app.route("/")
def hello():
    return "Hello World!"

pipe = load('trained_use_logreg.joblib')


# route api pour requête get

@app.route("/api")
def my_api(text = input("entrez du texte : ")) :

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