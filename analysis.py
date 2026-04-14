import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("dataset.csv")

print("First 5 rows:\n", df.head())

# -----------------------------
# 2. Missing Values
# -----------------------------
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# -----------------------------
# 3. Outlier Detection (IQR Method)
# -----------------------------
numeric_cols = df.select_dtypes(include='number')

for col in numeric_cols.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"\nOutliers in {col}:\n", outliers)

# -----------------------------
# 4. Bar Chart (Math Marks)
# -----------------------------
plt.figure()
plt.bar(df['Student'], df['Math'])
plt.xlabel("Students")
plt.ylabel("Math Marks")
plt.title("Math Marks of Students")
plt.xticks(rotation=90)
plt.show()

# -----------------------------
# 5. Pie Chart (Top 5 Students Math Marks)
# -----------------------------
plt.figure()
top5 = df.head(5)

plt.pie(top5['Math'], labels=top5['Student'], autopct='%1.1f%%')
plt.title("Top 5 Students - Math Distribution")
plt.show()

# -----------------------------
# 6. Stair Chart (Science Marks)
# -----------------------------
plt.figure()
plt.step(df['Student'], df['Science'])
plt.xlabel("Students")
plt.ylabel("Science Marks")
plt.title("Science Marks (Stair Chart)")
plt.xticks(rotation=90)
plt.show()