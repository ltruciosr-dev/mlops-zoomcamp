## 5.1 Intro to Monitoring

### What to monitor?

There are 3 main areas to check for monitoring; `service-health`, `model-health` and `data-health`:

1. **Service health**: It is about to measure metrics like `uptime`, `memory`, `latency`, it is a **must**.
2. **Model performance**: The particular set of metrics depends on the problem statement, for example for clasification we can metric the log-loss of the predicitions probs and also the f1-score to measure how well the model works for each category.
3. **Data quality and integrity**: There are many ways to check quality on data like counting missing values, the value range, etc.
4. **Data and concept drift**: As models interacts with real world environment data is enhanced to have variations and changes in distributions.

But we need to also take into account the comprehensive monitoring:

1. Performance by segment 
2. Model bias and fairness
3. Outliers
4. Explainability

### How to monitor?

About how to monitor the systems we have both:

1. **Service Health**: Frameworks like `Graphana`/`Prometheus` are used.

2. **Model Health**: Dashboard could be build for focused ML analytics on `Tableau`/`Looker`/`Graphana`, etc.

We can use `Evidently` to store the monitoring jobs outputs on a PostgreSQL db, that are feeded into dashboards.

## 5.3. Setup architecture and data

### What to use?

In this case we will use three next components:

1. **Grafana**: It will be used to show the monitoring plots and metrics.
2. **Postgres**: It will be used to store the monitoring logs of the model.
3. **Adminer**: It is optional and will be used to visualize the database tables in a simplified way.

Check the [docker-composer](docker-compose.yml) file where the connections between these three components are shown.

## 5.4 Evidently Metrics

