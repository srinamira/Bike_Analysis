from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Memuat dataset
day_data = pd.read_csv('day_clean.csv')
hour_data = pd.read_csv('hour_clean.csv')

# Convert date column
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Dashboard title
st.title("🚲 Bike Sharing Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [day_data['dteday'].min(), day_data['dteday'].max()]
)

# User type filter
user_type_options = ["Casual", "Registered"]
selected_user_type = st.sidebar.selectbox(
    "Select User Type", user_type_options, index=0
)

# Filter data based on user type
if selected_user_type == "Casual":
    user_column = 'casual'
elif selected_user_type == "Registered":
    user_column = 'registered'

# Apply filters
filtered_day_data = day_data[
    (day_data['dteday'].dt.date >= date_range[0]) &
    (day_data['dteday'].dt.date <= date_range[1])
]

filtered_hour_data = hour_data[
    (hour_data['dteday'].dt.date >= date_range[0]) &
    (hour_data['dteday'].dt.date <= date_range[1])
]

# Create layout with columns
col1, col2 = st.columns(2)

# Daily rentals by weekday
with col1:
    st.subheader(f"Daily Rentals ({selected_user_type}) by Weekday")
    daily_rentals = filtered_day_data.groupby('weekday').agg({
        user_column: 'sum'
    }).reset_index()

    fig_daily = go.Figure()
    fig_daily.add_bar(x=daily_rentals['weekday'], y=daily_rentals[user_column],
                      name=selected_user_type, marker_color='blue')
    fig_daily.update_layout(xaxis_title="Weekday",
                           yaxis_title="Total Rentals")
    st.plotly_chart(fig_daily, use_container_width=True)

# Monthly trends
with col2:
    st.subheader(f"Monthly Rental Trends ({selected_user_type})")
    monthly_rentals = filtered_day_data.groupby(
        filtered_day_data['dteday'].dt.strftime('%B')
    ).agg({
        user_column: 'sum'
    }).reset_index()

    fig_monthly = go.Figure()
    fig_monthly.add_scatter(x=monthly_rentals['dteday'], y=monthly_rentals[user_column],
                            name=selected_user_type, mode='lines+markers')
    fig_monthly.update_layout(xaxis_title="Month", yaxis_title="Total Rentals")
    st.plotly_chart(fig_monthly, use_container_width=True)

# Hourly distribution
st.subheader(f"Hourly Rental Distribution ({selected_user_type})")
hourly_rentals = filtered_hour_data.groupby('hr').agg({
    user_column: 'sum'
}).reset_index()

fig_hourly = go.Figure()
fig_hourly.add_bar(x=hourly_rentals['hr'], y=hourly_rentals[user_column],
                   name=selected_user_type, marker_color='blue')
fig_hourly.update_layout(barmode='stack', xaxis_title="Hour of Day",
                        yaxis_title="Total Rentals")
st.plotly_chart(fig_hourly, use_container_width=True)

# Key metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    total_rentals = filtered_day_data[user_column].sum()
    st.metric(f"Total Rentals ({selected_user_type})", f"{total_rentals:,}")

with col2:
    avg_daily_rentals = filtered_day_data[user_column].mean()
    st.metric(f"Average Daily Rentals ({selected_user_type})", f"{avg_daily_rentals:,.0f}")

with col3:
    hourly_peak = hourly_rentals[user_column].idxmax()
    st.metric("Peak Hour", f"{hourly_peak}:00")
