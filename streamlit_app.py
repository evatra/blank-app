import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LSTM Prediction Dashboard",
    page_icon="📈",
    layout="wide"
)

# Header section
st.title("🎈 Evan cahya Putra")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Main dashboard title
st.title("Prediction Dashboard")

# Sidebar configuration
with st.sidebar:
    st.title('📈 Dashboard-Prediction Use LSTM')