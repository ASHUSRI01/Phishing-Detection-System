import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Example data: 20 rows, phishing = 1, legitimate = 0
data = pd.DataFrame({
    "input": [
        "http://paypal-login-update.click", "https://www.google.com",
        "support@apple.com", "noreply@amazon-update.xyz",
        "http://free-gift-prize.click", "admin@microsoft.com",
        "http://login.bankofamerica.verify.top", "support@trustedbank.com",
        "verify-account@apple-support.click", "helpdesk@realcompany.com",
        "http://login-reset.amazon-security.xyz", "support@google.com",
        "http://secure-update.account-login.com", "admin@bankofindia.co.in",
        "http://click-here-for-gift.com", "admin@officialsite.com",
        "noreply@scamlink.bank-alert.top", "support@flipkart.com",
        "http://signin.facebook.com.secure-login.click", "admin@mycompany.in"
    ],
    "label": [
        1, 0, 0, 1, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0
    ]
})

X_train, X_test, y_train, y_test = train_test_split(
    data["input"], data["label"], test_size=0.2, stratify=data["label"], random_state=42
)

# Train pipeline
model = Pipeline([
    ("vectorizer", TfidfVectorizer(lowercase=True, stop_words="english", max_features=1000)),
    ("classifier", RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42))
])

model.fit(X_train, y_train)

# Save to file
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("[✅] Model saved as phishing_model.pkl")
