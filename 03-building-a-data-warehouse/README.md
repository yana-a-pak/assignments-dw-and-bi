# Building a Data Warehouse with BigQuery (GCP)

## Started
### Getting Started
```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Running ETL Script
```sh
python etl.py
```

### Set def main(dataset_id, table_id, file_path)
```sh
main(dataset_id="github", table_id="events", file_path="github_events.csv")
```

![def main]()


### Set Project ID
```sh
project_ID = ""YOUR_GCP_PROJECT""
```


### Set Keyfile Path
```sh
project_ID = ""YOUR_GCP_PROJECT""
```

### Keyfile Path from GCP
```sh
IAM & Admin --> Service Accounts
Create Service Accounts : 
    Service accounts details: Service account name
    Grant account access to project: Role
    Grant user access to service account: Done
    Create private key type: JSON
```

### Load data to BigQuery
```sh
python etl.py
```
![BigQuery]()


### Add Actor in etl and show in bigquery
```sh
Delete events
python etl.py
Create new events
```
![Actor in etl0]()
![Actor in etl1]()
![Actor in BigQuery]()

### Query Data

![Query Data]()