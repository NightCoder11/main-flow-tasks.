# -*- coding: utf-8 -*-
"""TASK4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q0IufTL_WfOMq45lE-y8T_dVY-Dsej0Z
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('/content/USvideos.csv')

df.head()

# Basic statistics of the dataset
df.describe()

# Check for missing values
missing_values = df.isnull().sum()
print(f'Missing values:\n{missing_values}')

# Visualize the distribution of numerical variables
num_columns = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Identify outliers using boxplots
for col in num_columns:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Select only numeric columns for correlation matrix calculation
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Correlation matrix
corr_matrix = df[numeric_columns].corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Pairplot to check relationships between variables
sns.pairplot(df[num_columns])
plt.show()

