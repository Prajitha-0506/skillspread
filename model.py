import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("realistic_unique_job_roles_dataset.csv")

# Features and labels
X = df["Skills"]
y = df["Job Role"]

# Fit the vectorizer
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)  # ✅ FITTING done here

# Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Evaluate
print("✅ Accuracy:", accuracy_score(y_test, rf_model.predict(X_test)))

# ✅ Save the fitted model and vectorizer
joblib.dump(rf_model, "job_role_predictor.pkl")
joblib.dump(vectorizer, "skill_vectorizer.pkl")
