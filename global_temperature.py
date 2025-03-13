import matplotlib.pyplot as plt

# Create two subplots, sharing the x-axis
fig, (ax1,ax2) = plt.subplots(2,1, sharex=True, figsize=(10, 6))

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

#plot global temperature anomalies
ax1.plot(years, temp_anomalies, label="Temp. Anomalies", color="#4D55CC" ,marker=".", markersize=15)
ax1.set_xlabel("Years")
ax1.set_ylabel("Temperature Anomalies (°C)")
ax1.set_title("Global Termperature Anomalies")

# Set x-ticks (year) to display as integers
ax1.set_xticks(years)
ax1.grid(True)

#second plot for CO2 emissions
ax2.bar(years, co2_emissions, label="CO2 Emissions", color="#FFA500", alpha=0.75)
ax2.set_title("Global CO2 Emissions")
ax2.set_xlabel("Years")
ax2.set_ylabel("CO2 Emissions (in billions of metric tons)")
ax2.grid(True)

#show the plot
fig.tight_layout()
plt.show()