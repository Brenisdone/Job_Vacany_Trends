import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Create Sample Dataset
# -------------------------------
data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "IT": [50000, 52000, 60000, 75000, 90000],
    "Healthcare": [40000, 45000, 50000, 65000, 70000],
    "Education": [30000, 28000, 32000, 35000, 38000],
    "Manufacturing": [45000, 42000, 48000, 55000, 60000],
    "Finance": [35000, 37000, 42000, 48000, 52000]
}

df = pd.DataFrame(data)

# -------------------------------
# 2. Display Data
# -------------------------------
print("Job Vacancy Data by Sector:\n")
print(df)

# -------------------------------
# 3. Line Plot – Trend Analysis
# -------------------------------
plt.figure()
plt.plot(df["Year"], df["IT"], marker='o', label="IT")
plt.plot(df["Year"], df["Healthcare"], marker='o', label="Healthcare")
plt.plot(df["Year"], df["Education"], marker='o', label="Education")
plt.plot(df["Year"], df["Manufacturing"], marker='o', label="Manufacturing")
plt.plot(df["Year"], df["Finance"], marker='o', label="Finance")

plt.xlabel("Year")
plt.ylabel("Number of Job Vacancies")
plt.title("Job Vacancy Trends by Sector")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# 4. Total Vacancies by Sector
# -------------------------------
sector_totals = df.drop("Year", axis=1).sum()

print("\nTotal Job Vacancies (2019–2023):\n")
print(sector_totals)

# -------------------------------
# 5. Bar Chart – Sector Comparison
# -------------------------------
plt.figure()
plt.bar(sector_totals.index, sector_totals.values)
plt.xlabel("Sector")
plt.ylabel("Total Vacancies")
plt.title("Total Job Vacancies by Sector (2019–2023)")
plt.show()
