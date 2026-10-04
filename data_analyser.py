import pandas as pd

print("===== CSV DATA ANALYZER =====")

# Make sure 'students.csv' is in your working directory
df = pd.read_csv("students.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\n--- Student Data ---")
print(df)

print("\n--- Basic Information ---")
print("Number of students:", len(df))
print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())

top_student = df.loc[df["Marks"].idxmax(), "Name"]
print("Top student:", top_student)
