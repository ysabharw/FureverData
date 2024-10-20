import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('pet_adoption_data.csv')

# Define features (X) and target (y)
X = df[['AgeMonths', 'WeightKg', 'Vaccinated', 'HealthCondition', 'AdoptionFee', 'PreviousOwner']]
y = df['AdoptionLikelihood']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Optional: Feature Importance
importances = model.feature_importances_
feature_names = X.columns
for feature, importance in zip(feature_names, importances):
    print(f'{feature}: {importance:.4f}')
