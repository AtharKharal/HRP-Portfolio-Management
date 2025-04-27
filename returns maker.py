# File: generate_returns_csv.py

import numpy as np
import pandas as pd

# Settings
np.random.seed(42)
num_assets = 10
num_days = 252  # One trading year
asset_names = [f"Asset_{i+1}" for i in range(num_assets)]

# Simulate random walk returns with slight positive drift
returns = np.random.normal(loc=0.0005, scale=0.02, size=(num_days, num_assets))

# Create DataFrame
dates = pd.date_range(start="2023-01-01", periods=num_days, freq='B')
returns_df = pd.DataFrame(data=returns, index=dates, columns=asset_names)

# Save to CSV
returns_df.to_csv("returns.csv")

print("returns.csv generated successfully.")
