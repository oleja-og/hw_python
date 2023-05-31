import pandas as pd

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

# Узнать какая максимальная households в зоне минимального значения population.

df = pd.read_csv('california_housing_train.csv')

task1 = df[(df['population']>0)&(df['population']<500)]['median_house_value'].mean()

task2 = df[df.population == df["population"].min()]['households'].max()

print(task1)

print(task2)