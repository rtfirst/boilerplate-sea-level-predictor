import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    data = pd.read_csv('epa-sea-level.csv')

    # Calculate line of best fit for all years
    slope_A, intercept_A, *_ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_values = np.arange(data['Year'].min(), 2051, 1)
    y_values_A = slope_A * x_values + intercept_A

    # Calculate line of best fit for years >= 2000 directly
    slope_B, intercept_B, *_ = linregress(data.loc[data['Year'] >= 2000, 'Year'], data.loc[data['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    y_values_B = slope_B * x_values[x_values >= 2000] + intercept_B

    # Create the plot efficiently
    plt.figure(figsize=(8, 6))  # Adjust figure size for better visibility
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.plot(x_values, y_values_A, label='Line of Best Fit')
    plt.plot(x_values[x_values >= 2000], y_values_B, label='Line of Best Fit (2000-2021)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
