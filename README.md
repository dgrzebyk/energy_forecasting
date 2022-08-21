# energy_forecasting
This project aims to predict energy yield of a single wind turbine in Germany. Dataset contains more than 70 signals 
from a turbine, as well as its generated power with 10 min resolution over almost 3 years.

Interesting resources:
- https://www.kaggle.com/datasets/psycon/wind-turbine-energy-kw-generation-data
- https://www.kaggle.com/code/dimitriosroussis/electricity-price-forecasting-with-dnns-eda

The project is currently under development


## Workflow

1. Loading the data
2. Data Cleaning
- checking dtypes
- looking for duplicates
- looking for outliers
3. Exploratory Data Analysis
- calculating correlations & heatmap
- analysing when active power is negative
- analysing when grid is down (frequency far below 50 Hz)
4. Time Series Decomposition
- checking if power time series is stationary
    - plotting rolling mean and standard deviation
    - conducting Dickey-Fuller
5. Time Series Modeling
- Arima


Alternative approaches:
- using time lagged features with regular machine learning techniques such as Random Forest or Gradient Boosting