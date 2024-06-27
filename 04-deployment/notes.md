There are two types of deployment:

## 1. Batch (Offline):

It runs at a certain and regularly schedule (e.g. hourly, daily, monthly).

- Data is extracted from database (ingestion).
- Predictions are stored in database (inference).
- This kind of predictions are mainly used by internal teams (Marketing, Analytics, etc.)

#### Example:

If we work for UBER, we will need to identify the users that are more probable to be churn in the next week / month, so, we create a model that uses and process user history weekly (each monday) and send the information of the more likable churn users to the Marketing team.

## 2. Online:

### 2.1. Web Service (API):

Each prediction is triggered by an external interaction, it could be implemented to run serverless, if the response latency is not critical, otherwise it is better to have servers (with load balancer) waiting for requests.

- Data is received from the client-request (ingestion).
- Prediction are returned to the client, and optionally stored (inference).
- This kind of predictions are mainly used by users via web services (Waze, OpenAI, Spotify, etc.)

#### Example:

A user want to get the expected ride duration by setting up the pick up and drop off locations.

### 2.2. Streaming:

The backend (client) sends information that is consumed by various components, each component have a defined task.

- Data is received from the backend-request (ingestion).
- Prediction are returned to the backend by each component, and optionally stored (inference).
- This kind of predictions are mainly used by the web services (Waze, Spotify, etc.)

#### Example:

A user want to fetch a new ride by pressing a button in the app, in background the user information is send to different components:
- A component that draw the travel track on the app and computes an estimated road time.
- A component that estimates the road time with higher accuracy (so higher latency).
- A component that predicts the TIP.
- A component that predicts the CANCELATION RATE.
Some components should have lower latency to improve the interaction between the user and the app, while other components needs to have a higher accuracy, like the road time, because it will be used by the taxi drivers to pick or slide the offers. Other components could be run to improve the user immension in the APP.



