import streamlit as st

# Read the README.md file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Display the README.md content
st.markdown(readme_content)