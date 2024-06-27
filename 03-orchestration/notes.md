## 3.0.1 ML Pipelines

Sequence of steps to train, evaluate and deploy a model but in this case we will centralize the learning on the __training__ pipelines. The sequence is as follows:

1. Data Ingestion :: extract information from source.
2. Data Preparation :: filter, clean and feature engineering.
3. Hyperparameter Tuning :: get the best hyperparameters.
4. Model Training :: train the model in all the data.

On step 4, we need to store the model on some registry (e.g. MLFlow) where te model will live.

## 3.0.2 Running Mage

We could build and run mage mlops platform locally or using codespaces (github), follow the steps listed here:

https://github.com/mage-ai/mlops

(*) Remember that we only have 60 free hours per month to use codespaces (using 2 core CPU)