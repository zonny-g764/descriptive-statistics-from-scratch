import pandas as pd

df = pd.read_csv("bike_count.csv")
col = df.iloc[: , 0].tolist()

#print(sum(col) / len(col))

def mean(df, i): 
    col= df.iloc[: , i].tolist()
    return sum(col) / len(col)
  
def median(df, i):
    col = sorted(df.iloc[: , i].tolist())
    n = len(col)
    mid = n // 2
    if n % 2 == 0:
        return (col[mid - 1] + col[mid]) / 2.0
    else:
            return col[mid]

def mode(df, i):
    col = df.iloc[: , i].tolist()
    freq = {}
    for val in col:
        freq[val] = freq.get(val, 0) + 1

    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if  v == max_freq]
    return modes[0] if len(modes) == 1 else modes

def sd(df, i):
    col =df.iloc[: , i].tolist()
    n = len(col)
    mu = sum(col) / n
    var = sum((x - mu)**2 for x in  col) / n
    return var **0.5

def quantile(df, i, q):
    col = sorted(df.iloc[: , i].tolist())

    n = len(col)
    pos = q * (n + 1)
    pos = n * q
    if pos == int(pos):
        idx = int(pos)
        return(col[idx - 1] + col[idx]) / 2.0

    else:
        idx = int(pos) + 1
        return col[idx - 1]


def scm(df, i, k):
    col= df.iloc[: , i].tolist()
    n = len(col)
    mu = sum(col) / n
    var = sum((x - mu)**2 for x in col) / n
    sigma = var**0.5
    mu_k = sum((x - mu)**k for x in col) / n
    return mu_k / sigma**k



print("First 5 rowa:")
print(df.head())

print("\nStatistical Results:")
print("Mean:", mean(df, 0))
print("Median:", median(df, 0))
print("Mode:", mode(df, 0))
print("Standard Deviation:", sd(df, 0))
print("Quantile (0.5):", quantile(df, 0, 0.5))
print("Standardized Central Moment (k=3):", scm(df, 0, 3))
