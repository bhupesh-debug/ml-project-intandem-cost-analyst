import os
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from data_pipeline import load_and_validate_data
from feature_engineering import build_cost_features

def train_cost_model(data_path='data/synthetic/production_cost_data.csv', model_out='models/best_model.pkl'):
    df = load_and_validate_data(data_path)
    X, y = build_cost_features(df)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"Random Forest Regressor -> R²: {r2:.4f}, RMSE: ${rmse:.2f}")
    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    with open(model_out, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model serialized to {model_out}")
    return model, r2, rmse

if __name__ == '__main__':
    train_cost_model()
