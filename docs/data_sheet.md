# Datasheet for Electric Ride-Hailing Demand Dataset

## Motivation
This dataset was created to help predict demand for an electric ride-hailing service. The primary objective is to forecast demand in specific time slots to optimize vehicle availability, minimize waiting times, and reduce operational downtime due to EV charging needs. This synthetic dataset simulates real-world patterns observed in the ride-hailing industry, helping to bridge the gap between demand and supply in a slot-based scheduling model.

## Composition
- **Attributes**:
  - `timestamp`: Date and time of the demand record.
  - `location`: The location where the ride request was made (categorical).
  - `time_slot`: The hour of the day when demand was recorded.
  - `hovered_slots`: Number of times users hovered over specific time slots without booking.
  - `last_served_location`: Location of the last successfully served ride.
  - `cancelled_rides`: Binary indicator of whether a ride was canceled (0 or 1).
  - `frequency_of_rides`: Number of rides taken by the user historically.
  - `demand`: Number of ride requests within the specified time slot, generated using a Poisson distribution to simulate realistic demand patterns.

- **Size**: 10,000 entries
- **Format**: CSV

## Collection Process
This synthetic dataset was generated based on assumptions about demand patterns in an electric ride-hailing business. Each record represents a ride request at a specific location and time. Data values were generated using random sampling for categorical variables and Poisson distribution for demand to simulate common patterns in the industry.

## Preprocessing / Cleaning / Labeling
Basic preprocessing steps were performed, including:
- Removing missing values
- Engineering new features, such as extracting `hour` from `time_slot` and creating a binary indicator for weekends
- Dropping irrelevant columns

## Uses
This dataset can be used to train and test machine learning models for demand forecasting in a slot-based scheduling system, helping improve operational efficiency and EV availability in an electric ride-hailing service.

## Distribution
The dataset is stored as a CSV file and is publicly available for educational and research purposes.

## License
This dataset is licensed under [Specify license if applicable, e.g., CC BY 4.0].
