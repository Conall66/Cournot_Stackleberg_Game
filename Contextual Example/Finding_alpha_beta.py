
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
books = books[books["Publisher "] != "Amazon Digital Services,  Inc."]

# _____________________________________________________________________________

# Use RandomForest to find highest contributing factors

# Select numerical features (excluding target)
X = books.drop(columns=["sale price"])  
y = books["sale price"]

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

# From above, the most important features are the publishing year, book average rating, sale price, publisher and a high author rating
# Filter the dataset

books = books[books["Book_average_rating"] >= 4.2] # We know the book will do well
books = books[books["sale price"] >= 10]

# Plot sales price against units sold
select_cols = ["units sold", "sale price"]
df = books[select_cols]

slope, intercept = np.polyfit(df["units sold"], df["sale price"], 1)  # 1 for linear
line_of_best_fit = slope * df["units sold"] + intercept

plt.figure(figsize=(8, 5))

plt.scatter(df["units sold"], df["sale price"], color='blue', alpha=0.6)
plt.plot(df["units sold"], line_of_best_fit, color='red', label='Line of Best Fit')

plt.xlabel("Units sold")
plt.ylabel("Sale Price (£)")
plt.title("Units Sold vs Sale Price")
plt.grid(True)
plt.legend()

plt.show()

# _________________________________________________________________________________

# Find alpha and beta values from slope

print("alpha: ", intercept, ", beta: ", slope)
