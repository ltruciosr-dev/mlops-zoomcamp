import os
import pickle
import click

import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Set the tracking URI to point to your local server
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("random-forest-train")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    # Start a new MLflow run
    with mlflow.start_run():
        # Load Data
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

        # Train model
        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        params = rf.get_params()
        rmse = mean_squared_error(y_val, y_pred, squared=False)
        
        # Log parameters and metrics
        mlflow.log_params(params)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(rf, "rf_regressor_model")

if __name__ == '__main__':
    run_train()