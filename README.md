##  Project Overview
This project builds a machine learning model that detects whether an email is *Spam* or *Not Spam* using features such as:
- num_links
- num_words
- has_offer
- sender_score
- all_caps

Why these models were chosen?

Logistic Regression is a simple linear model commonly used for binary classification problems like spam vs. not spam. It provides fast training and gives interpretable results.
Random Forest is an ensemble model that combines multiple decision trees. It handles nonlinear relationships, detects feature interactions, and usually gives higher accuracy for tabular data. That’s why both were tested to compare performance.

Feature impact on prediction :

num_links - More links usually increases chance of spam
num_words - Very small messages can indicate spam
has_offer - Presence of "special offer" keywords increases spam probability
sender_score - Lower sender reputation increases spam probability
all_caps - Messages in ALL CAPS often indicate spam

Possible improvements:

Add more features 
Use XGBoost or LightGBM
Do hyperparameter tuning
Handle class imbalance

##  Technologies Used
- Python
- Scikit-Learn
- Flask (API)
- NumPy & Pandas

##  Machine Learning Models
Two ML models were trained:
- Logistic Regression
- Random Forest

*Evaluation Metrics used:*
- Accuracy
- Precision
- Recall
- F1 Score

Random Forest performed better and was chosen as the final model.

## Features Impact
- num_links and has_offer strongly indicate spam.
- sender_score helps detect trusted emails.
- all_caps indicates spam behavior.

##  API Deployment (Flask)
To run API:

```bash
python app.py

Send a POST request to:
Copy code
http://127.0.0.1:5000/predict
Example JSON:
Copy code
Json
{
  "num_links": 2,
  "num_words": 150,
  "has_offer": 1,
  "sender_score": 0.45,
  "all_caps": 0
}
Response:
Copy code
Json
{
  "spam": 1,
  "message": "Spam"
}
