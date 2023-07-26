## Text Classification for StackOverflow Tags

The purpose of this project is to create an algorithm capable of taking textual data as input, specifically questions from the StackOverflow forum, and predicting the most relevant tag to automate and streamline question indexing on the site.

The algorithm used in this project consists of a pipeline with two main steps. It leverages the CountVectorizer for feature extraction and employs Logistic Regression based on the OneVsRestClassifier approach for multi-label classification. The pre-trained model is available in the file `trained_bow_logreg.joblib`.

The model is deployed on a web application using Flask, Streamlit, and Heroku.

This repository includes the following files:

* `flask_app.py`: Our API
* `preprocess.py`: Contains all functions to prepare the data
* `viz_app.py`: Contains information about the Streamlit web app's interface

To use the algorithm, follow these steps:

1. Download the code from this repository (either using `git clone` or direct download).
2. Open a command line interface and navigate to the downloaded folder.
3. Create a virtual environment using conda or venv (optional but recommended).
4. Run the command `pip install -r requirements.txt` to install all the necessary modules for the algorithm to work.
5. Run the command `python flask_app.py` and wait for the server to launch.
6. In a new terminal tab, still within the repository folder, run the command `streamlit run viz_app.py`. A window should open in your browser.

If everything works correctly, you should see an input bar prompting you to enter text. When you input a computer-related question, the algorithm will recommend relevant tags based on the topic you are addressing. If the algorithm is unsure of what to recommend, it will let you know.

Don't forget to deploy everything on Heroku!

Enjoy using the application!
