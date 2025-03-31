import streamlit as st
import joblib
import datetime

# Load the saved model
model = joblib.load('news_category_model.pkl')

# Define the categories
category_mapping = {0: 'BUSINESS', 1: 'SPORTS', 2: 'CRIME', 3: 'SCIENCE'}

# Function to log predictions
def log_prediction(headline, category):
    with open("prediction_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {headline} -> {category}\n")

# Streamlit app setup
st.title("News Category Prediction")
st.markdown("Welcome to the News Category Prediction App! ")
st.markdown("""
This app uses a Machine Learning model to predict the category of a news headline.
The possible categories are:
- Business
- Sports
- Crime
- Science

Just enter a news headline, and the app will predict its category
""")

# Input from user
text_input = st.text_input("Enter a news headline")

# Predict button
if st.button("Predict"):
    if text_input:
        try:
            with st.spinner("Predicting... Please wait..."):
                # Make prediction
                prediction = model.predict([text_input])[0]
                prediction = int(prediction)

                # Get the category from mapping
                category = category_mapping.get(prediction, "Unknown Category")
                st.success(f"Predicted Category: {category}")

                # Log the prediction
                log_prediction(text_input, category)

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please enter a news headline.")

# Additional information
st.markdown("About the Model")
st.markdown("""
- Model Type: Multinomial Naive Bayes
- Vectorizer: Bag of n_grams (Bigram)
- Imbalance Handling: SMOTE
- Accuracy: Approximately 85% 
""")
