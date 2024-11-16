from src.data_loader import load_data
from src.feature_engineering import add_features
from src.model import train_model, evaluate_model


def main():
    # Load the data
    print("Loading data...")
    data = load_data('data/sample_ride_hailing_demand_data.csv')

    # Perform feature engineering
    print("Adding features...")
    data = add_features(data)

    # Train the model
    print("Training model...")
    model, X_test, y_test = train_model(data)

    # Evaluate the model
    print("Evaluating model...")
    metrics = evaluate_model(model, X_test, y_test)
    print("Evaluation metrics:", metrics)


if __name__ == "__main__":
    main()
