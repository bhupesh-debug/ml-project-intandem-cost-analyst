import pandas as pd
import numpy as np

def build_cost_features(df):
    df_feat = df.copy()
    df_feat['labor_efficiency_ratio'] = df_feat['actual_labor_hours'] / np.maximum(df_feat['standard_labor_hours'], 1.0)
    df_feat['coaching_intensity_factor'] = df_feat['coaching_support_ratio'] * df_feat['labor_efficiency_ratio']
    df_feat['mat_price_variance_pct'] = (df_feat['actual_material_cost'] - df_feat['standard_material_cost']) / np.maximum(df_feat['standard_material_cost'], 1.0)
    df_feat['scrap_rate_per_machine_hr'] = df_feat['scrap_units'] / np.maximum(df_feat['machine_hours'], 0.1)
    
    feature_cols = [
        'standard_material_cost', 'actual_material_cost', 'standard_labor_hours',
        'actual_labor_hours', 'coaching_support_ratio', 'labor_rate_hourly',
        'machine_hours', 'scrap_units', 'labor_efficiency_ratio',
        'coaching_intensity_factor', 'mat_price_variance_pct', 'scrap_rate_per_machine_hr'
    ]
    return df_feat[feature_cols], df_feat['total_cost_variance']

if __name__ == '__main__':
    from data_pipeline import load_and_validate_data
    df = load_and_validate_data()
    X, y = build_cost_features(df)
    print(f"Feature Engineering complete: Matrix shape {X.shape}, Target shape {y.shape}")
