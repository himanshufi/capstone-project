import pandas as pd

def add_features(data):
    """Add new features to the dataset based on time and user interaction patterns."""
    # Extract hour from time slot (assuming time_slot is in 'HH:MM' format)
    data['hour'] = data['time_slot'].apply(lambda x: int(x.split(':')[0]))
    
    # Feature to indicate if the timestamp is during the weekend
    data['is_weekend'] = pd.to_datetime(data['timestamp']).dt.dayofweek >= 5
    
    # Previous demand as a lagged feature
    data['previous_demand'] = data['demand'].shift(1).fillna(0)
    
    return data
