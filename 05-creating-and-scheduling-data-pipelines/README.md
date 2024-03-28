## Get start
### 1. change directory to project 05-creating-and-scheduling-data-pipelines:
```sh
cd 05-creating-and-scheduling-data-pipelines/
```

### 2. prepare environment workspace 
(https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

```sh
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

docker-compose.yaml Input # (stop working code)
`line 56`
# AIRFLOW__CORE__EXECUTOR: CeleryExecutor 
`Add line 57`
AIRFLOW__CORE__EXECUTOR: LocalExecutor

`line 59-60`
# AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql://airflow:airflow@postgres/airflow
# AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0

`line 81-82`
# redis:
#   condition: service_healthy

`line 102-112`
# redis:
        ......
  #   restart: always

`line 146-182`
# airflow-worker:
        ......
#       condition: service_completed_successfully

`line 261-263`
# You can enable flower by adding "--profile flower" option e.g. docker-compose --profile flower up
# or by explicitly targeted on the command line e.g. docker-compose up flower.
# See: https://docs.docker.com/compose/profiles/


Running Docker
```sh
docker-compose up
```

### 3. Airflow
Airflow UI port 8080 (localhost:8080)
User & Password : airflow (by default line 241-242)

Show All DAGs (After Config code in files .py)
![DAGs]()

Show Graph
![Graph]()

Show Log detials
![Log]()

## data schedule
ให้เข้าที่ tab Dags แล้ว etl โดยเราสามารถตรวจสอบการทำงานได้ในหน้า Graph
![Graph]()




