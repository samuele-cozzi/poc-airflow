# poc-airflow

## Install

Install apache airflow on k8s namespace "airflow"

``` bash

helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f ./override-values.yaml --debug

```

## Use Cases

### 1. k8s jobs

``` bash

kubectl create namespace airflow-jobs
kubectl apply -f ./k8s/job1.yaml --namespace airflow-jobs --create-namespace --debug

```
