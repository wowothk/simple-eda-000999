import streamlit as st
import pandas as pd

# @st.cache(allow_output_mutation=True)
def load_dataset(dataset):
    df = pd.read_csv(dataset)

    return df
