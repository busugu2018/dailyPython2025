import pandas as pd

#createing a dataframe from a dictionary
data = {'Name': ['Jo', 'Job', 'Jane', 'Bob']}, 
'Age': [25, 45, 49, 32], 
'City': ['Mumbai', 'Libreville', 'Chicago', 'Dallas']}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

#Accessing columns
print("\nAccessing columns:")
print("Names column:")
print(df['Name'])

#Adding a new column
df['Salary'] = [50000, 60000, 75000, 48000]
print ("\nDataFrame with Salary column:")
print (df)

#Descriptive statistics 
print ("\Descriptive Statistics:")
print(df.describel())

#Filtering data
print ("\Filtering Data:")
filtered_df = df[df['Age'] > 30]
print("People older 30:")
print(filtered_df)