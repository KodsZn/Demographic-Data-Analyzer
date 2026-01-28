import pandas as pd

# Load the data
df = pd.read_csv("adult.data.csv")

# Question 1: How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

# Question 4: What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_advanced_over_50k = round((advanced_education['salary'] == '>50K').sum() / len(advanced_education) * 100, 1)

# Question 5: What percentage of people without advanced education make more than 50K?
no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_no_advanced_over_50k = round((no_advanced_education['salary'] == '>50K').sum() / len(no_advanced_education) * 100, 1)

# Question 6: What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_workers = df[df['hours-per-week'] == min_hours_per_week]
percentage_min_hours_over_50k = round((min_hours_workers['salary'] == '>50K').sum() / len(min_hours_workers) * 100, 1)

# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
country_percentages = df.groupby('native-country').apply(
    lambda x: (x['salary'] == '>50K').sum() / len(x) * 100
)
highest_earning_country = country_percentages.idxmax()
highest_earning_country_percentage = round(country_percentages.max(), 1)

# Question 9: Identify the most popular occupation for those who earn >50K in India.
india_over_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india = india_over_50k['occupation'].value_counts().idxmax()

# Display results
if __name__ == '__main__':
    print("\n" + "="*60)
    print("DEMOGRAPHIC DATA ANALYSIS RESULTS")
    print("="*60)
    
    print("\n1. Race Distribution:")
    print(race_count)
    
    print("\n2. Average Age of Men:", average_age_men)
    
    print("\n3. Percentage with Bachelor's Degree:", percentage_bachelors, "%")
    
    print("\n4. Percentage with Advanced Education (Bachelors, Masters, Doctorate)")
    print("   earning >50K:", percentage_advanced_over_50k, "%")
    
    print("\n5. Percentage WITHOUT Advanced Education earning >50K:", percentage_no_advanced_over_50k, "%")
    
    print("\n6. Minimum Hours Per Week:", min_hours_per_week, "hours")
    
    print("\n7. Percentage of Minimum Hours Workers earning >50K:", percentage_min_hours_over_50k, "%")
    
    print("\n8. Country with Highest >50K Earning Percentage:")
    print("   Country:", highest_earning_country)
    print("   Percentage:", highest_earning_country_percentage, "%")
    
    print("\n9. Most Popular Occupation for >50K Earners in India:", most_popular_occupation_india)
    
    print("\n" + "="*60)
