import streamlit as st

from interface.data_management_interface import upload_dataset
from interface.auto_eda_interface import overview_interface, variables_overview_interface

def load_autoEDA(df):
    variables_name = df.columns.tolist()
    type_list = overview_interface(df)

    st.markdown(f"## Variables ")
    for i in range(len(variables_name)):
        st.markdown(f"### {variables_name[i]} ")
        variables_overview_interface(df[variables_name[i]], type_list[i])
    
    
        



def autoEDA_demo_interface():
    st.title("Automated EDA")

    df = upload_dataset()

    if df is not None:
        load_autoEDA(df)    


if __name__ == "__main__":
    autoEDA_demo_interface()