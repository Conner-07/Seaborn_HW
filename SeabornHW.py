import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


exercise_data = pd.read_csv('/Users/connerstarkey/Downloads/Exercise_Data.csv')


print(exercise_data.head())


plt.figure(figsize=(10, 6))
pulse_pivot = exercise_data.pivot_table(values='1 min', index='diet', columns='kind')
sns.heatmap(pulse_pivot, annot=True, cmap='coolwarm')
plt.title('Heatmap of Pulse at 1 Minute by Diet and Exercise Type')
plt.xlabel('Exercise Type')
plt.ylabel('Diet')
plt.show()


sns.catplot(data=exercise_data, x='diet', y='1 min', hue='kind', kind='box', height=6, aspect=1.5)
plt.title('Pulse at 1 Minute by Diet and Exercise Type')
plt.xlabel('Diet')
plt.ylabel('Pulse at 1 Minute')
plt.show()




planets = sns.load_dataset('planets')


plt.figure(figsize=(10, 6))
sns.scatterplot(data=planets, x='distance', y='orbital_period', hue='method')
plt.title('Orbital Period vs Distance')
plt.xlabel('Distance')
plt.ylabel('Orbital Period')
plt.legend(title='Discovery Method')
plt.show()


plt.figure(figsize=(10, 6))
sns.lineplot(data=planets, x='year', y='distance', hue='method', ci=None)
plt.title('Discovery Year vs Distance')
plt.xlabel('Year')
plt.ylabel('Distance')
plt.legend(title='Discovery Method')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(data=planets, x='orbital_period', kde=True)
plt.title('Distribution of Orbital Periods')
plt.xlabel('Orbital Period')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=planets, y='distance')
plt.title('Distribution of Distances')
plt.xlabel('Distance')
plt.show()



plt.figure(figsize=(10, 6))
sns.countplot(data=planets, x='method')
plt.title('Count of Planets by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
sns.violinplot(data=planets, x='method', y='orbital_period')
plt.title('Orbital Period by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Orbital Period')
plt.xticks(rotation=45)
plt.show()

