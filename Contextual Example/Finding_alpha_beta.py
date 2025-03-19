
# Finding alpha and beta values

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Machine learning
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


books = pd.read_csv("Books_Data_Clean.csv")

# Select cols

select_cols = ["Publishing Year", "Author_Rating", "Book_average_rating", "sale price", "Publisher ", "units sold"]
books = books[select_cols]

# _____________________________________________________________________________

# Use RandomForest to find highest contributing factors

# Select numerical features (excluding target)
X = books.drop(columns=["units sold"])  
y = books["units sold"]

# Convert categorical data (if any) using one-hot encoding
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Get feature importance
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance = feature_importance.sort_values(ascending=False)

# Display top features
print(feature_importance.head(10))

# _____________________________________________________________________________

# Plot sales price against units sold
select_cols = ["Book_average_rating", "units sold"]
df = books[select_cols]

plt.figure(figsize=(8, 5))

plt.scatter(df["Book_average_rating"], df["units sold"], color='blue', alpha=0.6)

plt.xlabel("Book Average Rating")
plt.ylabel("Units Sold")
plt.title("Sale Price vs Units Sold")
plt.grid(True)

plt.show()

