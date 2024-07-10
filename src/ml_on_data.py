from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

class RentPredictor:

    def prepare_data(self, df):
        #df['rent_per_room'] = df['rent'] / df['no_of_rooms']

        X = df[["postcode", "no_of_rooms"]]  # Double brackets for column selection
        y = df["rent"]

        # Split the data into training and test sets with 80% training and 20% testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        # Initlaizing KNN neighbouyrrs regressor
        model = KNeighborsRegressor(n_neighbors=5)
        # fit model on training data
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        predictions = model.predict(X_test)

        mse = mean_squared_error(y_test, predictions)
                
        # Print the Mean Squared Error
        print(f"Mean Squared Error: {mse}")
        
        # Return the predictions
        return predictions


    def predict_rent(self, model, new_data):
        X_new = new_data.values  # Extract the values from DataFrame

        predictions = model.predict(X_new)

        return predictions
