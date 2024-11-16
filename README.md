# Electric Ride-Hailing Demand Prediction

This project aims to predict demand for an electric ride-hailing service, with a focus on optimizing EV availability and minimizing downtime. The model leverages historical data to forecast demand patterns in specific time slots and locations, helping service providers allocate resources more efficiently.

## Project Structure
- `notebooks/`: Contains Jupyter notebooks for each stage of the project:
  - `EDA.ipynb`: For exploratory data analysis.
  - `Model_Training.ipynb`: For training the model.
  - `Hyperparameter_Tuning.ipynb`: For tuning hyperparameters.
  - `Evaluation.ipynb`: For evaluating model performance.
- `src/`: Holds Python scripts for loading data, engineering features, and training the model:
  - `data_loader.py`: Loads the dataset and handles preprocessing.
  - `feature_engineering.py`: Adds additional features to the dataset.
  - `model.py`: Contains the main model class and training functions.
- `data/`: Contains the sample dataset (`sample_ride_hailing_demand_data.csv`).
- `outputs/`: Stores trained models and performance metrics.
- `docs/`: Includes the model card and datasheet for documentation.

## Dataset
The dataset is a synthetic collection of ride request records, including attributes such as `timestamp`, `location`, `time_slot`, `hovered_slots`, `last_served_location`, `cancelled_rides`, `frequency_of_rides`, and `demand`. This data simulates real-world patterns in demand to help optimize ride-hailing services.

## Installation
1. Clone this repository: `git clone <repository-url>`
2. Install the required packages: `pip install -r requirements.txt`

## Usage
1. **Exploratory Data Analysis**: Run `EDA.ipynb` to explore the dataset and visualize trends.
2. **Model Training**: Use `Model_Training.ipynb` to train the initial model.
3. **Hyperparameter Tuning**: Tune the model parameters in `Hyperparameter_Tuning.ipynb` to improve performance.
4. **Evaluation**: Assess the model’s performance in `Evaluation.ipynb`.

## Results
The model achieved a Root Mean Squared Error (RMSE) of X on the test set, indicating its accuracy in predicting demand patterns across time slots and locations.

## License
This project is licensed under [Specify license if applicable, e.g., MIT License].
