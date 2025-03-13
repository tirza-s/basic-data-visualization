import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
brussels_temperature = [6, 7, 8, 11, 14, 14, 17]
lisbon_temperature = [9, 11, 10, 14, 12, 15, 21]
madrid_temperature = [8, 10, 11, 11, 13, 10, 8]

print(plt.style.available)
plt.style.use("ggplot")

plt.plot(days, brussels_temperature, label="Brussels", color="b", marker=".")
plt.plot(days, lisbon_temperature, label="Lisbon", color="g", marker=".")
plt.plot(days, madrid_temperature, label="Madrid", color="r", marker=".")

plt.grid(True)

plt.title("Weather forecast")
plt.legend(["Brussels", "Lisbon","Madrid"])
plt.xlabel("Days")
plt.ylabel("temperature (°C)")

plt.show()
