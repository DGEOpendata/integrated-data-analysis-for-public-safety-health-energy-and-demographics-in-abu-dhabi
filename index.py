python
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
public_safety_data = pd.read_csv('public_safety_data.csv')
health_data = pd.read_csv('health_data.csv')
energy_data = pd.read_csv('energy_emissions_data.csv')
demographics_data = pd.read_csv('population_employment_data.csv')
air_water_quality_data = pd.read_csv('air_water_quality_data.csv')

# Example analysis: Correlation between energy consumption and greenhouse gas emissions
energy_consumption = energy_data[['Sector', 'Energy_Consumption']]
ghg_emissions = energy_data[['Sector', 'GHG_Emissions']]

# Merge data on Sector
energy_vs_emissions = pd.merge(energy_consumption, ghg_emissions, on='Sector')

# Visualize the correlation
plt.figure(figsize=(10, 6))
plt.scatter(energy_vs_emissions['Energy_Consumption'], energy_vs_emissions['GHG_Emissions'], alpha=0.5)
plt.title('Correlation between Energy Consumption and GHG Emissions')
plt.xlabel('Energy Consumption')
plt.ylabel('GHG Emissions')
plt.grid(True)
plt.show()

# Example analysis: COVID-19 vs vaccination rates
covid_cases = health_data[['Region', 'Date', 'COVID_Cases']]
vaccination_rates = health_data[['Region', 'Date', 'Vaccination_Rate']]

# Merge data on Region and Date
covid_vs_vaccination = pd.merge(covid_cases, vaccination_rates, on=['Region', 'Date'])

# Plot trends over time
plt.figure(figsize=(12, 6))
plt.plot(covid_vs_vaccination['Date'], covid_vs_vaccination['COVID_Cases'], label='COVID Cases')
plt.plot(covid_vs_vaccination['Date'], covid_vs_vaccination['Vaccination_Rate'], label='Vaccination Rate')
plt.title('COVID-19 Cases vs Vaccination Rates Over Time')
plt.xlabel('Date')
plt.ylabel('Counts / Percentage')
plt.legend()
plt.grid(True)
plt.show()
