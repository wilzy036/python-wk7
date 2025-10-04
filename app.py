import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Sidebar filter
year_range = st.slider("Select year range", 2015, 2023, (2020, 2021))
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications per year
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top Journals
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_title("Top Journals")
st.pyplot(fig)

# Word Cloud
text = " ".join(df_filtered['title'].dropna())
if text:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.write(df_filtered.head())
