
News Classification App 

This project is a machine learning-based application that classifies news articles into categories such as Business, Sports, Crime, and Science based on the content of the news headline. The app is built using Python, Streamlit, and Scikit-learn.

Features
- Predicts the category of a news headline.
- User-friendly interface built with Streamlit.
- Real-time prediction and output.


📂 Project Structure
```
News_Classification/
├── app.py                            # Streamlit application script
├── news_category_model.pkl            # Pre-trained model file
├── requirements.txt                   # Dependencies
├── prediction_log.txt                 # Logs of predictions
├── News Category Classification.ipynb # Jupyter notebook with model training
└── README.md                          # Project documentation
```

🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Omeche/NLP.git
   cd NLP/News_Classification
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

💻 Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser:
   ```
   http://localhost:8501
   ```
3. Input a news headline and get the predicted category

📝 Example Usage
1. Enter a news headline, such as:
   ```
   "New scientific breakthrough in AI technology"
   ```
2. Click on the Predict button.
3. See the predicted category, e.g., Science.


🤔 How It Works
- Uses a CountVectorizer to transform text data into numerical features.
- Applies SMOTE to handle class imbalance.
- Utilizes a Multinomial Naive Bayes model for classification.
- The pipeline is created using imblearn's make_pipeline for seamless integration.


📝 Model Training
The model was trained using a dataset of news headlines with the following categories:
- Business
- Sports
- Crime
- Science

The Jupyter Notebook contains the data preprocessing and model training steps.


🛑 Known Issues
- Ensure that the `news_category_model.pkl` file is present in the root directory.
- Check compatibility of `scikit-learn` versions when loading the model.

You can view the deployed version of the app [here](https://omeche-nlp-news-classificationapp-lyoatt.streamlit.app/).

📬 Contact
Feel free to reach out to me at (mailto:omechetochi@gmail.com) for any questions or collaborations!


