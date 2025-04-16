# Import data libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset and show first 5 rows
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

#print the number of columns
print(len(diabetes_data.columns))

# Print the number of rows
print(len(diabetes_data))

# find whether columns contain null values
print(diabetes_data.isnull().sum())

# Perform summary statistics
print(diabetes_data.describe())

# replace instances of 0 in the dataset with NaN
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 
'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

# find whether columns contain values after replacements are made
print(diabetes_data.isnull().sum())

# print rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# print data types using .info() method
print(diabetes_data.info())

# Print unique values of Outcome column
print(diabetes_data.Outcome.unique())

# Describe all data types using .describe() method
print(diabetes_data.describe(include='all'))

# Replace instances of'O' with '0' in the Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)
print (diabetes_data.Outcome.unique())

# Ensure the Outcome column is an integer type
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)
print(diabetes_data.dtypes)

# Calculate the diabetes_diagnosis rate from the Outcome column
diabetes_diagnosis_rate = diabetes_data['Outcome'].value_counts()
print(diabetes_diagnosis_rate)

# Create a Bar Chart to show the Outcome of diabetes diagnosis rate
sns.countplot(x= 'Outcome', data=diabetes_data)
plt.show()
plt.close()