
import streamlit as st
import joblib
import re
from pathlib import Path

# Configure the web page
st.set_page_config(
    page_title="Researchly Research Abstract Classifier",
    layout="centered"
)

# Load the saved model
@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "research_classifier.joblib"
    return joblib.load(model_path)

# Apply the same text cleaning used during training
def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Display the title and description
st.title("Researchly Research Abstract Classifier")

st.write(
    "This app classifies research abstracts as either "
    "AI-related or classical research."
)

# Text input field
abstract = st.text_area(
    "Enter research abstract:",
    height=180,
    placeholder="Paste your research abstract here..."
)

# Classification button
if st.button("Classify Abstract"):

    cleaned_abstract = clean_text(abstract)

    if cleaned_abstract == "":
        st.warning("Please enter a research abstract.")

    else:
        # Predict the research category
        model = load_model()
        prediction = model.predict([cleaned_abstract])[0]

        st.subheader("Prediction")

        if prediction == "ai":
            st.success(
                "The abstract is classified as: artificial intelligence"
            )
        else:
            st.success(
                "The abstract is classified as: classical research"
            )
