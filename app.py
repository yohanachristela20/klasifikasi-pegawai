import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Memuat data
file_path = "Employee.csv"
df = load_data(file_path)

def plot_age_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Age'])
    plt.title('Age Distribution', fontsize=15)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    st.pyplot()

# Panggil fungsi plot_age_distribution dengan data df
plot_age_distribution(df)

def plot_confusion_matrix(cm):
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='PuBu', linewidths=0.4, square=True, cbar=True,
        xticklabels=["0", "1"],
        yticklabels=["0", "1"]
    )
    plt.xlabel('Predicted', fontsize=14, fontweight='bold')
    plt.ylabel('Actual', fontsize=14, fontweight='bold')
    plt.title('Confusion Matrix', fontsize=16, fontweight='bold')
    plt.yticks(rotation=360)
    st.pyplot()

# Memplot confusion matrix
plot_confusion_matrix(cm)
