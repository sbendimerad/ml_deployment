from flask import Flask, jsonify
from joblib import load
from preprocess import lemmatization, clean_output

app = Flask(__name__)

pipe = load('trained_bow_logreg.joblib')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/text=<text>")
def my_api(text) :

	text_clean = lemmatization([text])
	output = pipe.predict([text_clean])
	output_clean = clean_output(output)

	dictionnaire = {
		"text" : text,
		"tags" : output_clean
	}

	return jsonify(dictionnaire)

if __name__ == "__main__" :
	app.run(debug = True)