import pandas as pd
from narrationMap import narration_map

# Read the Excel file
file_path = 'june.xls'  # Replace with your file path
df = pd.read_excel(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y', errors='coerce')
grouped = df.groupby('Date')


# Loop through each group
for date, group in grouped:
    print(f"Date: {date}")
    for narration, amount in zip(group['Narration'], group['Withdrawal Amt.']):
        description = narration
        for key in narration_map:
            if key in narration:
                description = narration_map[key]
        print(f"{description}: {amount}")
    print("")
