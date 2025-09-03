import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
df=sns.load_dataset('titanic')
print(df.head())

print(df.info())

print(df.isnull().sum())



df['age'].fillna(df['age'].median(),inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0],inplace=True)
df.drop('deck',axis=1,inplace=True)
df['embark_town'].fillna(df['embark_town'].mode()[0],inplace=True)
print(df.isnull().sum())

sns.countplot(x='survived',data=df)
plt.title('Survival Rates')
plt.xticks([0,1],['Non-Survivors','Survivors'])
plt.show()


sns.histplot(x='age',data=df,kde=True)
plt.title('Age Distribution Boxplot')
plt.show()

sns.scatterplot(x='age',y='fare',data=df,hue='survived')
plt.title('Age vs Fare by Survival Status')
plt.xlabel('Age')
plt.ylabel('Fare')

plt.show()

report_content = f"""
Exploratory Data Analysis Report - Titanic Dataset

1. Dataset Dimensions:
- The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.

2. Missing Values:
- All missing values in 'age', 'deck', and 'embarked_town' were successfully handled.
- Missing values in 'age' were filled with the median.
- Missing values in 'embarked_town' were filled with the most frequent value (mode).
- The 'deck' column was dropped due to a high number of missing values.

3. Key Findings from Visualizations:
- Survival Rates: A smaller number of passengers survived than did not survive.
- Age Distribution: The majority of passengers were in their 20s and 30s. There were some notable outliers, indicating very young and very old passengers.
- Age vs. Fare: There is no strong correlation between age and the fare paid. However, passengers who paid very high fares were more likely to survive.

This report summarizes the initial findings from the exploratory data analysis. The cleaned and prepared data is now ready for further machine learning model building.
"""


import os
os.makedirs('outputs', exist_ok=True)


with open('outputs/eda_report.txt', 'w') as file:
    file.write(report_content)

print("EDA report has been saved to the 'outputs' folder.")
