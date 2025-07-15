import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset (update path if needed)
df = pd.read_csv("realistic_unique_job_roles_dataset.csv")  # or your custom CSV

# Features and labels
X = df["Skills"]
y = df["Job Role"]

# Convert text (skills) to numeric vectors using TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)


# 1. Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)
dt_acc = accuracy_score(y_test, dt_preds)

# 2. Random Forest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_preds)

#Print results
print("🔍 Model Accuracy Comparison:")
#print(f"Decision Tree:       {dt_acc:.4f}")   #96.45
#print(f"Random Forest:       {rf_acc:.4f}")   #100

#Optional: Classification report for one model
#print("\n📊 Classification Report (Decision Tree):")
#print(classification_report(y_test, dt_preds))


#print("\n📊 Classification Report (Random Forest):")
#print(classification_report(y_test, rf_preds))

joblib.dump(rf_model, "job_role_predictor.pkl")
joblib.dump(vectorizer, "skill_vectorizer.pkl")
