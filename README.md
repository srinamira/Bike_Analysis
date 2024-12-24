# DATA ANALYSIS PROJECT : BIKE SHARING DATASET 🚴🏻‍♀️

## Dataset Information
[**Bike Sharing Dataset**](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset) contains the hourly and daily count of rental bikes between the years 2011 and 2012 in the Capital bike share system with the corresponding weather and seasonal information.

### About Dataset
- **instant**: Record index  
- **dteday**: Date  
- **season**: season (1: spring, 2: summer, 3: fall, 4: winter)  
- **yr**: Tahun (0: 2011, 1: 2012)  
- **mnth**: Bulan (1 to 12)  
- **hr**: Jam (0 to 23)  
- **holiday**: weather day is holiday or not
- **weekday**: day of the week
- **workingday**: if day is neither weekend nor holiday is 1, otherwise is 0
- **weathersit**:  
  1. Clear, Few clouds, Partly cloudy  
  2. Mist + Cloudy, Mist + Broken clouds  
  3. Light Snow, Light Rain + Thunderstorm + Scattered clouds  
  4. Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog  
- **temp**: Normalized temperature in Celsius
  - The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- **atemp**: Normalized feeling temperature in Celsius
  - The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- **hum**: Normalized humidity. The values are divided to 100 (max)
- **windspeed**: Normalized wind speed. The values are divided to 67 (max)
- **casual**: count of casual users
- **registered**: count of registered users 
- **cnt**: count of total rental bikes including both casual and registered


## 📝 Data Analysis With Python
You can check the data analysis on [**notebook**](https://github.com/srinamira/Bike_Analysis/blob/main/submission/notebook.ipynb)

### Instalation
Install all the necessary libraries by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

### Data Analysis includes
1. Import Packages/Library
2. Data Wrangling
3. Assessing Data
4. Exploratory Data Analysis (EDA)
5. Visualization & Explanatory Analysis
6. Analisis Lanjutan
7. Conclusion


## 📊 Dashboard with Streamlit
### How to Run the Dashboard
1.  Open the folder containing the dashboard
   ```bash
   cd dashboard
   ```
2. Run streamlit app
   ```bash
   streamlit run dashboard.py
   ```
### Dashboard View
![Halaman1](https://github.com/srinamira/Bike_Analysis/blob/main/submission/image/Halaman%201.jpeg)
![Halaman1](https://github.com/srinamira/Bike_Analysis/blob/main/submission/image/Halaman%201.jpeg)
