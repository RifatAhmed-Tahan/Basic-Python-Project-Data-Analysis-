# Student Performance Data Analysis

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dataset
data = {
    "Name": ["Bodrul", "Abdul", "Obaydul", "Nazrul", "Sadrul", "Nahidur", "Asha", "Samiha"],
    "Math": [80, 75, 92, 78, 71, 95, 85, 67],
    "Science": [88, 62, 89, 77, 83, 94, 72, 67],
    "English": [33, 74, 80, 68, 76, 83, 85, 68],
    "Sports": [60, 85, 76, 55, 99, 88, 76, 62]
}

df = pd.DataFrame(data)

#Line Plot
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Math"], marker="o", linestyle="-", color="b", label="Math Scores")
plt.title("Line Plot - Math Scores of Students")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.legend()
plt.show()

#Bar Plot
avg_scores = df[["Math","Science","English","Sports"]].mean()
plt.figure(figsize=(8,5))
sns.barplot(x=avg_scores.index, y=avg_scores.values, palette="viridis")
plt.title("Bar Plot - Average Scores per Subject")
plt.ylabel("Average Score")
plt.show()

#Pie Chart
plt.figure(figsize=(6,6))
plt.pie(df["Sports"], labels=df["Name"], autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart - Sports Scores Distribution")
plt.show()

#Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(data=df[["Math","Science","English","Sports"]], palette="Set2")
plt.title("Box Plot - Score Distribution by Subject")
plt.ylabel("Scores")
plt.show()

#Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English","Sports"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap - Correlation between Subjects")
plt.show()