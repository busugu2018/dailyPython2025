#A sales company is making a sales performance analysis to determine who are the Top-performing sales representatives
#on a specific team. Who are the top 3 salesmen out of the 20

# table_data = [
#         {"Name": "Alice", "Age": 30, "City": "New York", "salesRevenue": 5000},
#         {"Name": "Bob", "Age": 25, "City": "Los Angeles", "salesRevenue": },
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#         {"Name": "Charlie", "Age": 35, "City": "Chicago", "salesRevenue": }
#     ]




import random
import pandas as pd

# Sample names and cities
names = ["John Smith", "Jane Doe", "Michael Johnson", "Emily Davis", "Chris Brown", "Jessica Wilson", "David Martinez", "Ashley Anderson", "James Thomas", "Sarah White",
         "Brian Harris", "Olivia Martin", "Daniel Lewis", "Sophia Lee", "Matthew Walker", "Emma Hall", "Ethan Young", "Isabella King", "Alexander Scott", "Mia Adams"]

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
          "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis", "Fort Worth", "Charlotte", "Seattle", "Denver", "Washington"]

# Generate random sales revenue between 5000 and 25000
sales_revenue = [random.randint(5000, 25000) for _ in range(20)]

# Create a DataFrame
data = {
    "Name": names,
    "City": cities,
    "Sales Revenue": sales_revenue
}

df = pd.DataFrame(data)

# Display the table
print(df)
