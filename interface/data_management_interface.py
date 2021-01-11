import streamlit as st

from model.data_management import load_dataset


def upload_dataset():
    st.markdown("## Upload Dataset")

    df = None
    dataset_file = st.file_uploader("Choose a dataset ", type="csv", accept_multiple_files=False)

    if dataset_file is not None:
        df = load_dataset(dataset_file)

    return df