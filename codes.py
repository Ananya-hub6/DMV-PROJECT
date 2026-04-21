import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv("company.csv")



# Convert review_count (remove 'k Reviews')
df['review_count'] = df['review_count'].str.replace('k Reviews', '').astype(float)

# Convert years
df['years'] = df['years'].str.replace(' years old', '').astype(int)

# Convert employees (rough conversion)
def convert_emp(x):
    if '1 Lakh+' in x:
        return 100000
    elif '50k-1 Lakh' in x:
        return 75000
    elif '10k-50k' in x:
        return 30000
    elif '1k-5k' in x:
        return 3000
    else:
        return 10000

df['employees'] = df['employees'].apply(convert_emp)


# 1. HEADQUARTERS

print("Company Headquarters:\n")
print(df[['name', 'hq']])


# 2. BAR CHART (Ratings)

plt.figure()
plt.bar(df['name'], df['ratings'])
plt.xticks(rotation=90)
plt.title("Company Ratings")
plt.xlabel("Companies")
plt.ylabel("Ratings")
plt.show()


# 3. FUNNEL CHART (Reviews)

fig = px.funnel(df, x='review_count', y='name', title="Company Reviews Funnel")
fig.show()


# 4. LINE CHART (Employees)

plt.figure()
plt.plot(df['name'], df['employees'])
plt.xticks(rotation=90)
plt.title("Employees Count")
plt.xlabel("Companies")
plt.ylabel("Employees")
plt.show()


# 5. PIE CHART (Top 5 Years)

top5 = df.head(5)

plt.figure()
plt.pie(top5['years'], labels=top5['name'], autopct='%1.1f%%')
plt.title("Top 5 Companies by Years")
plt.show()