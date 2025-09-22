# Load libraries
import pandas as pd

# Load dataset
df = pd.read_csv("metadata.csv")

# Inspect first rows
print(df.head())

# Data structure
print(df.shape)    # Rows & columns
print(df.info())   # Data types
print(df.isnull().sum())   # Missing values
print(df.describe())       # Basic statistics
