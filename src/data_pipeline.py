import pandas as pd
import os

def load_and_validate_data(filepath='data/synthetic/production_cost_data.csv'):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    df = pd.read_csv(filepath)
    required_cols = [
        'batch_id', 'product_line', 'standard_material_cost', 'actual_material_cost',
        'standard_labor_hours', 'actual_labor_hours', 'coaching_support_ratio',
        'labor_rate_hourly', 'machine_hours', 'scrap_units', 'total_cost_variance'
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df

if __name__ == '__main__':
    df = load_and_validate_data()
    print(f"Data Pipeline loaded {len(df)} validated production records.")
