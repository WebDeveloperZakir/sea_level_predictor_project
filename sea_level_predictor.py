import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the data with encoding fix
    df = pd.read_csv("epa-sea-level.csv", encoding='utf-8-sig')
    
    # Clean column names: remove leading/trailing spaces and fix BOM issues
    df.columns = df.columns.str.strip()
    if '\ufeffYear' in df.columns:
        df.rename(columns={'\ufeffYear': 'Year'}, inplace=True)

    # Debug: Print the columns to verify
    # print("DEBUG: Columns:", df.columns.tolist())

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", alpha=0.6)

    # First line of best fit (1880 - 2050)
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    line1 = res1.intercept + res1.slope * years_extended
    plt.plot(years_extended, line1, 'r', label='Best fit: 1880–2050')

    # Second line of best fit (2000 - 2050)
    df_recent = df[df["Year"] >= 2000]
    res2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    line2 = res2.intercept + res2.slope * years_recent
    plt.plot(years_recent, line2, 'green', label='Best fit: 2000–2050')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and return plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
