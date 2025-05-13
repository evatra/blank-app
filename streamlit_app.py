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

    # Threshold settings section
    st.subheader("🔒 Threshold Settings")
    enable_thresholds = st.checkbox("Enable Safety Thresholds", value=True)
    
    if enable_thresholds:
        col1, col2 = st.columns(2)
        with col1:
            threshold_percent_upper = st.number_input(
                "Upper Threshold (%)", 
                min_value=1, 
                max_value=100, 
                value=10,
                help="Maximum allowed deviation percentage"
            )
        with col2:
            threshold_percent_lower = st.number_input(
                "Lower Threshold (%)", 
                min_value=1, 
                max_value=100, 
                value=10,
                help="Minimum allowed deviation percentage"
            )
    
    st.divider()  # Adds a visual separator
    
    # Display options
    st.subheader("📊 Display Options")
    check_box = st.checkbox(
        label="Display Table of Prediction",
        help="Show/hide prediction results table"
    )