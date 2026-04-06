import pandas as pd

# load dataset
df = pd.read_csv("ULTIMATE_HACKATHON_DATA.csv", low_memory=False)

# preview
print(df.head())

# clean column names
df.columns = df.columns.str.strip()

# print all columns
print("\nCOLUMNS:")
print(df.columns)

# find columns related to card/decline
card_cols = [c for c in df.columns if "card" in c.lower() or "decline" in c.lower()]

print("\nPossible card declined columns:")
print(card_cols)

# take first matching column
card_column = card_cols[0]

print(f"\nUsing column: {card_column}")

# Crosstab counts
print("\nCounts of card_declined vs churn:")
print(pd.crosstab(df[card_column], df["churn_status"]))

# Crosstab percentages
print("\nPercentages:")
print(pd.crosstab(df[card_column], df["churn_status"], normalize="index") * 100)