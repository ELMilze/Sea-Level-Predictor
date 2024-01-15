import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load dataset
data = pd.read_csv('C:\\Users\\TOW Admin\\Downloads\\Test Documentation\\epa-sea-level.csv')

# Create scatter plot
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

# Create first line of best fit
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
x = list(range(1880, 2051))
y = [intercept + slope*year for year in x]
plt.plot(x, y, 'r', label='Line of Best Fit 1')

# Create second line of best fit
new_data = data[data['Year'] >= 2000]
slope, intercept, r_value, p_value, std_err = linregress(new_data['Year'], new_data['CSIRO Adjusted Sea Level'])
x = list(range(2000, 2051))
y = [intercept + slope*year for year in x]
plt.plot(x, y, 'green', label='Line of Best Fit 2')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.show()