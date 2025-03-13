import matplotlib.pyplot as plt

hours_studied = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
breaks_taken = [0, 2, 1, 3, 0, 1, 2, 0, 3, 0, 2, 1, 3, 0, 2] 
exam_scores = [52, 54, 57, 59, 63, 67, 72, 76, 78, 82, 85, 88, 90, 93, 95]

print(plt.style.available)
plt.style.use("ggplot")

#scatter plot for hours studied
plt.scatter(hours_studied, exam_scores, label="hours studied", color="#667BC6",s=50, alpha=0.75)

#scatter plot for breaks taken
plt.scatter(breaks_taken, exam_scores, label="break taken in hours", color="#597445",s=50, alpha=0.50)

plt.grid(True)

plt.title("Exam scores vs hours studied")
plt.legend(["hours studied", "Breaks taken in hours"])
plt.xlabel("Hours studied")
plt.ylabel("Exam scores in %")

plt.show()
