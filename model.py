import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Assuming you have a dataset
df = pd.read_csv('space_mining_dataset.csv')

# Define features and target
features = df[['iron', 'nickel', 'water_ice', 'other_minerals', 'sustainability_index', 'efficiency_index', 'distance_from_earth']]

# Create a composite score if not already present
weights = {
    'iron': 0.3,
    'nickel': 0.2,
    'water_ice': 0.2,
    'other_minerals': 0.1,
    'sustainability_index': 0.1,
    'efficiency_index': 0.1,
    'distance_from_earth': -0.1
}

df['composite_score'] = (
    weights['iron'] * df['iron'] +
    weights['nickel'] * df['nickel'] +
    weights['water_ice'] * df['water_ice'] +
    weights['other_minerals'] * df['other_minerals'] +
    weights['efficiency_index'] * df['efficiency_index'] +
    weights['sustainability_index'] * df['sustainability_index'] +
    weights['distance_from_earth'] * df['distance_from_earth']
)

target = df['composite_score']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the trained model as a pickle file
with open('space_mining_model.pkl', 'wb') as file:
    pickle.dump(model, file)
