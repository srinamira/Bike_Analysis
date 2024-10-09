import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Sidebar for selecting dataset
dataset = st.sidebar.selectbox('Select Dataset', ('Day Data', 'Hour Data'))

# Show the selected dataset
st.title("Simple Streamlit Dashboard")
if dataset == 'Day Data':
    st.header('Day Data Overview')
    st.write(day_data.head())  # Display the first few rows of day_data
    
    # Visualize distribution of data
    st.subheader('Day Data Visualization')
    fig, ax = plt.subplots()
    day_data['cnt'].hist(ax=ax, bins=20, color='skyblue')
    ax.set_xlabel('Count')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Count in Day Data')
    st.pyplot(fig)

elif dataset == 'Hour Data':
    st.header('Hour Data Overview')
    st.write(hour_data.head())  # Display the first few rows of hour_data
    
    # Visualize relationship between temperature and count
    st.subheader('Hour Data Visualization')
    fig, ax = plt.subplots()
    ax.scatter(hour_data['temp'], hour_data['cnt'], alpha=0.5, color='orange')
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Count')
    ax.set_title('Count vs Temperature in Hour Data')
    st.pyplot(fig)
