import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dataset/netflix_titles.csv')

# Show first 5 rows
print(df.head())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')

# Convert date column safely
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Remove invalid dates
df.dropna(subset=['date_added'], inplace=True)

# Extract year
df['year_added'] = df['date_added'].dt.year

# Set style
sns.set_style('whitegrid')

# 1. Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title('Movies vs TV Shows on Netflix')
plt.show()

# 2. Top 10 Countries
plt.figure(figsize=(10,5))
df['country'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()

# 3. Ratings Distribution
plt.figure(figsize=(10,5))
sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)
plt.title('Ratings Distribution')
plt.show()

# 4. Content Added Over Years
plt.figure(figsize=(12,6))
df['year_added'].value_counts().sort_index().plot()
plt.title('Content Added Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

print("Project Completed Successfully!")
