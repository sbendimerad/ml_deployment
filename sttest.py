import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

import streamlit as st

@st.cache_data
def load_data() :
	data = load_iris()
	df = pd.DataFrame(data = data.data, columns = data.feature_names)
	return df

data = load_data()
st.write(data)

fig = plt.figure(figsize=(10, 4))
sns.barplot(data = data, y = 'sepal length (cm)', x = 'sepal width (cm)')
plt.title("Dummy barplot")


st.pyplot(fig)