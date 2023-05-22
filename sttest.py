import pandas as pd
import requests

import streamlit as st


text = st.text_input(label = "Enter your question : ")
res = requests.get("https://app-api-imlp5.herokuapp.com/api/text=" + ''.join(text))

#st.write(res.content.decode('utf-8'))

res = pd.read_json(res.content.decode('utf-8')).loc[0, 'tags']

st.write(res)