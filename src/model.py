import os

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import json


def train_model(data):
    """Train an XGBoost regressor on the prepared dataset."""
    # Define features and target
    X = data[['hour', 'is_weekend', 'previous_demand']]
    y = data['demand']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = XGBRegressor()
    model.fit(X_train, y_train)
    # Save the model and evaluate
    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """Evaluate the model and save metrics to a JSON file."""
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5

    # Save metrics to file
    metrics = {'mean_squared_error': mse, 'root_mean_squared_error': rmse}

    # Path to the directory and file
    output_dir = "outputs"
    output_file = os.path.join(output_dir, "performance_metrics.json")

    if not os.path.exists(output_file):
        # Ensure the directory exists
        os.makedirs(output_dir, exist_ok=True)

    with open('outputs/performance_metrics.json', 'w') as f:
        json.dump(metrics, f)

    return metrics
