import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
lstrobot = list()
lsthuman = list()
for i in lst:
    if i == "robot":
        lstrobot.append('1')
        lsthuman.append('0')
    else:
        lstrobot.append('0')
        lsthuman.append('1')

df = pd.DataFrame({'robot':lstrobot, 'human': lsthuman})

print(data.head())
print(df.head())