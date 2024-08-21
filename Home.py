import streamlit as st

st.set_page_config(
    page_title="Stellar Minesite",
    page_icon="💫",
)

st.title("💫 Stellar Minesite")

st.sidebar.success("Select a model from above")
st.markdown(
    """
    Stellar Minesite is a Machine Learning driven web 
    platform for exploring analyzing data on mining sites,
    and generating recommendations based on user input. 
    Machine Learning and Data Science projects.

    **👈 Select a model from the sidebar** to see it in action!
    ### 🚀 The Prediction Model
    - brief description line
    - brief description line
    - brief description line
    - brief description line

    ### ✨ The Recommendation Model
    - The recommendation model evaluates space mining sites 
    based on user-defined feature weights and a trained 
    machine learning model.
    - It normalizes input data, predicts suitability scores, and adjusts for user preferences.
    - Finally, it ranks sites to provide the top recommendations.
    - Users interactively adjust feature weight/priority and the model recommends best minesites available.
"""
)
