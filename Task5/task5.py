# -*- coding: utf-8 -*-
"""TASK5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ug0X9Pazk0DpIroQzHcQRkoZjTVOyNGH
"""

#Task 5
#Engineer new features and select relevant features for model training.
# 1.Generate meaningful features from existing data.
# 2.Use techniques like PCA or feature importance to select the most important features.
# 3.Optimize feature sets for improved model performance.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score

#Load data
data = pd.read_csv('/content/heart.csv')
data.head()

# Separate features and target variable
X = data.drop('target', axis=1)
y = data['target']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature Selection using PCA
pca = PCA(n_components=0.95)  # Retain 95% of the variance
X_pca = pca.fit_transform(X_scaled)

# Feature Selection using Feature Importance from RandomForest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Get feature importances and select the most important ones
selector = SelectFromModel(clf, threshold='median', prefit=True)
X_important = selector.transform(X_scaled)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_important, y, test_size=0.2, random_state=42)

# Train a model with the selected features
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy with selected features: {accuracy:.2f}")

