import pandas as pd
import requests

import streamlit as st


text = st.text_input(label = "Enter your question : ")
res = requests.get("http://127.0.0.1:5000/api/text=" + ''.join(text))
res = pd.read_json(res.content.decode('utf-8')).loc[0, 'tags']

st.write(res)