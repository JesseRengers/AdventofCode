import pandas as pd

# Create a DF from our input text
df = pd.read_csv('inputs/input-1.txt', sep='   ', names=['left','right'])

sorted_left = sorted(df['left'].values)
sorted_right = sorted(df['right'].values)

df['left'] = sorted_left
df['right'] = sorted_right

total_distance = 0
for _, row in df.iterrows():
    total_distance += abs(row['left'] - row['right'])

print(total_distance)