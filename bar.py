import matplotlib.pyplot as plt

languages = ["French", "Spanish", "English", "Italian"]

counts = [80, 90, 100, 50]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

plt.pie(counts, labels=languages)

plt.xlabel('Languages')
plt.ylabel('Count')

plt.title('Spoken languages at EU Institutions')

plt.show()