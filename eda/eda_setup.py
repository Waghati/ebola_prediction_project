# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the data from a CSV file
file_path = '/Users/admin/Desktop/projects/ebola_prediction_project/eda/ebola_sequences.csv'  # Adjust the path as necessary

# Set visual preferences for seaborn
sns.set(style="whitegrid")

# Function to load data
def load_data(file_path):
    """Load CSV data into pandas DataFrame"""
    return pd.read_csv(file_path)

# Function to set up basic plot appearance
def setup_plot():
    """
    Set up the default plot appearance
    You can basically customize how this looks like 
    In our case we are choosing to use the default."""
    plt.figure(figsize=(10, 6))

df = load_data(file_path)

# Basic Data Inspection
def basic_inspection(df):
    """Print basic info about the dataset."""
    print("Data Types and Missing Values:\n")
    print(df.info())  # Data types and missing values
    print("\nFirst few rows of the dataset:\n")
    print(df.head())  # Preview first few rows
    print("\nSummary statistics:\n")
    print(df.describe())  # Summary of numerical columns

# Run basic inspection
basic_inspection(df)

# Step 3: Handle missing values
def handle_missing_values(df):
    """Handle missing values by checking and filling or removing them."""
    # Check for missing data
    print("\nMissing Values Count:")
    print(df.isnull().sum())

    # Option 1: Drop rows with missing values (if small number)
    df_dropped = df.dropna()

    # Option 2: Fill missing values (if a larger number of missing values)
    df_filled = df.fillna({
        'Host': 'Unknown',  # Example: filling 'Host' with 'Unknown'
        'Country': 'Unknown'  # Example: filling 'Country' with 'Unknown'
    })

    # Return both modified DataFrames (for comparison)
    return df_dropped, df_filled

# Handle missing values
df_dropped, df_filled = handle_missing_values(df)

# Step 4: Basic visualizations
def plot_length_distribution(df):
    """Plot the distribution of sequence lengths."""
    setup_plot()
    sns.histplot(df['Length'], kde=True, color='blue', bins=20)
    plt.title('Distribution of Ebola Virus Sequence Lengths')
    plt.xlabel('Sequence Length')
    plt.ylabel('Frequency')
    plt.show()

def plot_country_distribution(df):
    """Plot the distribution of samples across different countries."""
    setup_plot()
    country_counts = df['Country'].value_counts()
    sns.barplot(x=country_counts.index, y=country_counts.values, palette='viridis')
    plt.title('Distribution of Ebola Virus Samples by Country')
    plt.xlabel('Country')
    plt.ylabel('Number of Samples')
    plt.xticks(rotation=90)  # Rotate country names for better visibility
    plt.show()

# Plot distributions
plot_length_distribution(df)
plot_country_distribution(df)

# Step 5: Check correlations and relationships
def plot_heatmap(df):
    """Plot a correlation heatmap for numerical features."""
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    corr = df[numeric_columns].corr()

    setup_plot()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Correlation Heatmap of Numerical Features')
    plt.show()

def plot_host_vs_country(df):
    """Plot a relationship between Host and Country."""
    setup_plot()
    host_country_count = df.groupby(['Host', 'Country']).size().reset_index(name='Count')
    sns.barplot(x='Host', y='Count', hue='Country', data=host_country_count, palette='Set2')
    plt.title('Host vs Country')
    plt.ylabel('Sample Count')
    plt.xticks(rotation=45)
    plt.show()

# Run correlation and relationship plots
plot_heatmap(df)
plot_host_vs_country(df)
