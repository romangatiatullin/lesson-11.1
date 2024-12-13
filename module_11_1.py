import requests


response = requests.get('https://api.github.com/users/octocat')

if response.status_code == 200:
    user_data = response.json()
    print("Username:", user_data['login'])
    print("ID:", user_data['id'])
    print("Public Repos:", user_data['public_repos'])
else:
    print("Error:", response.status_code)


import pandas as pd


data = pd.read_csv('data.csv')
print(data.info())

average_value = data['column_name'].mean()
print("Average Value:", average_value)

category_counts = data['category_column'].value_counts()
print("Category Counts:\n", category_counts)


import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')

plt.title('Simple Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()