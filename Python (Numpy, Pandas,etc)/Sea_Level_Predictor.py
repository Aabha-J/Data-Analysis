import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", header = 0)

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")


    # Create first line of best fit
    res = linregress(x=df["Year"].values, y=df["CSIRO Adjusted Sea Level"].values)
    x_extended = np.arange(1880, 2051)
    plt.plot(x_extended, res.intercept + res.slope*x_extended, 'r', label='fitted line', color = "c")
    
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res = linregress(x=df_recent["Year"].values, y=df_recent["CSIRO Adjusted Sea Level"].values)
    x_extended = np.arange(2000, 2051)
    plt.plot(x_extended, res.intercept + res.slope*x_extended, 'r', label='fitted line 2', color = "r")

    # Add labels and title
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
