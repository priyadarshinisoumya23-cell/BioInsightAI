import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# ----------------------------
# Demo Training Data
# Replace this with your real
# labeled dataset later.
# ----------------------------
X = np.random.rand(100, 20)
y = np.random.randint(0, 2, 100)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/random_forest.pkl")

print("Model saved successfully!")