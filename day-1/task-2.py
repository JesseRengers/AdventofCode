import pandas as pd

# Create a DF from our input text
df = pd.read_csv('inputs/input.txt', sep='   ', names=['left','right'])

#create a hashmap from column 'right'
hashmap = dict()

for _, row in df.iterrows():
    # convert to standard int
    right = int(row['right'])

    if right in hashmap:
        hashmap[right] += 1
    else:
        hashmap[right] = 1

# Calculate total similarity score
similarity_score = 0
for _, row in df.iterrows():
    if row['left'] in hashmap:
        similarity_score += row['left'] * hashmap[int(row['left'])]

print(similarity_score)