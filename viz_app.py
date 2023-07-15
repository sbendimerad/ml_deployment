import pandas as pd
import requests

import streamlit as st

st.title("My Streamlit Application")

try:
    user_input = st.text_input(label="Enter your question:")

    if not user_input:
        raise ValueError("Text cannot be empty")

    api_url = "http://127.0.0.1:5000/api/text=" + user_input

    response = requests.get(api_url)

    if response.ok:
	    data = response.json()
	    tags = data["tags"]
	    tag_names = [tag.strip("#") for tag in tags]
	    st.write("Tags:", ", ".join(tag_names))
    else:
        raise ValueError("API request failed")

except ValueError as e:
    st.error(str(e))
