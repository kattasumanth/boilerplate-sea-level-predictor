import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    df.plot(kind = 'scatter', x = 'Year', y = 'CSIRO Adjusted Sea Level')


    # Create first line of best fit
    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x1 = range(1880, 2051)
    y1 = (lineA.slope * x1) + lineA.intercept 

    plt.plot(x1, y1)

    # Create second line of best fit
    df_new = df[df['Year'] >= 2000]

    lineB = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])

    x2 = range(2000, 2051)
    y2 = lineB.intercept + (lineB.slope * x2)

    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()