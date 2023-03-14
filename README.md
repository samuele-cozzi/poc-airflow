# poc-airflow

## Install

Install apache airflow on k8s namespace "airflow"

``` bash

helm repo add apache-airflow https://airflow.apache.org
kubectl create namespace airflow
helm upgrade --install airflow apache-airflow/airflow --namespace airflow -f ./override-values.yaml --debug

```

## Docker

``` bash

docker build -t samuelecozzi/job-sample:0.0.1 .
docker push samuelecozzi/job-sample:0.0.1

```

## Gitpod

``` bash
brew install okteto helm
okteto ctx use https://cloud.okteto.com --token=JaHB56XBwi32txCcUB5KccD46jGPLLdjpFMGklcdwWbOXMNV
okteto deploy
``` 

## Use Cases

### 1. k8s jobs

Kubernetes Operator

``` bash

kubectl create namespace airflow-jobs
kubectl apply -f ./k8s/job1.yaml --namespace airflow-jobs
kubectl apply -f ./k8s/job2.yaml --namespace airflow-jobs
kubectl apply -f ./k8s/job3.yaml --namespace airflow-jobs

```

## Run Airflow

``` bash
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow

```

## References

- [dotnet job](https://benbrougher.tech/posts/kubernetes-cron-job/)
- [kubernates executor vs operator](https://stackoverflow.com/questions/59952465/airflow-when-to-use-kubernetesexecutor-vs-kubernetespodoperator)
- [gitpod + okteto](https://www.okteto.com/blog/modern-development-environments-for-cloud-native-applications-using-gitpod-and-okteto/)