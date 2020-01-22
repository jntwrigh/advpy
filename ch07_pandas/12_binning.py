import pandas as pd

data = [('M', 33, 'California'), ('M', 55, 'Florida'), ('F', 44, 'Maine'),
        ('F', 43, 'Idaho'), ('F', 64, 'Alaska'), ('F', 49, 'Ohio'),
        ('F', 13, 'New York'), ('M', 37, 'California'), ('M', 61, 'Texas'),
        ('M', 27, 'Washington'), ('F', 22, 'Florida'), ('M', 55, 'New Jersey'),
        ('F', 18, 'Nevada'), ('M', 27, 'Oregon'), ('F', 26, 'Arizona'),
        ('M', 21, 'Utah'), ('F', 19, 'Oregon'), ('M', 67, 'Colorado')]


df = pd.DataFrame(data, columns = ['gender', 'age', 'state'])
bins = [0, 18, 25, 35, 45, 55, 150]
df['age_group'] = pd.cut(df['age'], bins=bins)
labels = ['kid', 'early adult', 'young adult', 'middle adult', 'older adult', 'senior']
df['age_name'] = pd.cut(df['age'], bins=bins, labels=labels)
print(df)
