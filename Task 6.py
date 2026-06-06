"""Task  14 Feb """
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Math': [80, 90, 70, 85],
    'Science': [75, 95, 65, 80],
    'English': [85, 88, 72, 78],
    'Department': ['CS', 'IT', 'CS', 'IT']
}

df = pd.DataFrame(data)
print(df)