# poc-airflow

## Install

Install apache airflow on k8s namespace "airflow"

``` bash

helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f ./override-values.yaml --debug

```

## Docker

``` bash

docker build -t samuelecozzi/job-sample:0.0.1 .
docker push samuelecozzi/job-sample:0.0.1

```

## Use Cases

### 1. k8s jobs

``` bash

kubectl create namespace airflow-jobs
kubectl apply -f ./k8s/job1.yaml --namespace airflow-jobs

```


## References

- [dotnet job](https://benbrougher.tech/posts/kubernetes-cron-job/)