import os
import pickle
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from data_pipeline import load_and_validate_data
from feature_engineering import build_cost_features

def evaluate_model(model_path='models/best_model.pkl', data_path='data/synthetic/production_cost_data.csv'):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    df = load_and_validate_data(data_path)
    X, y = build_cost_features(df)
    
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("=" * 45)
    print("  INTANDEM-COSTAI MODEL EVALUATION REPORT")
    print("=" * 45)
    print(f"  R² Score (Explained Variance): {r2:.4f}")
    print(f"  Mean Absolute Error (MAE):     ${mae:.2f}")
    print(f"  Root Mean Squared Error (RMSE): ${rmse:.2f}")
    print("=" * 45)

if __name__ == '__main__':
    evaluate_model()
