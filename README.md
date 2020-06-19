# Energy Efficiency 

## Problem Statement and Scope
The goal of this challenge is to build a regression model for the dataset is available at https://archive.ics.uci.edu/ml/datasets/Energy+efficiency and deploy it with docker. You should be able to run the docker image and then curl the container by sending json containing the attributes of a new building and get a json response with the heating and cooling loads predicted by your trained model. 

## To run Jupyter Notebooks
Run 'Jupyter Notebook' inside of jupyter folder to initiate the following two notebooks:

### EDA and Regression
In this notebook we try to predict two numeric values heating_load and cooling_load using 8 features. The algorithms that will be used are:

* Decision tree 
* Random forest 
* Extras tree 

### Regression Pipeline
This notebook uses the best parameters found in Energy+efficiency dataset EDA and Regression.ipynb for the ExtraTreesRegressor when training our model. All steps are wrapped up as chain links in a pipeline. This pipeline takes the data, preprocess it and trains the model at the same time. Finally the model will be saved using joblib package, in order to use use it later, without the need to retrain it.


## To run flask-api 
Dockerfile script was optimized with base image that's already contain some of the required python library inside so it builds and pushes to docker hub faster because of the build result being smaller. You could push it to your own docker hub too using this file but for this time, I'm using my docker hub for deployment (sarakimmich/flask-api:latest). To deploy the service to your kubernetes cluster (in this case, minikube), execute the commands as needed below in the folder containing flask-api.yml.

1. sudo docker login
This will init docker with your credential. Enter your username and password for docker repo.

2. sudo docker build -t $DOCKERHUB_USER/flask-api:latest .
This will build the docker image for the api.

3. sudo docker push $DOCKERHUB_USER/flask-api:latest
This command will push the build result to the docker hub.

4. kubectl apply -f flask-api.yml
This will create flask-api deployment & service.

5. kubectl get nodes -o wide
This command will get the kubernetes nodes info. In this case, we're using it to get the node ip address.
For example: 172.17.0.4

6. kubectl get svc
This command will display the flask-api service info. In this case, we're using it to get the generated service port.
For example: 32499

7. kubectl get pods
This command is used to check the status of the pod. If the status is running, then the api is ready to be accessed.

To access the api, combine the node ip address with the port number.
In this case: http://172.17.0.4:32499
And access it according to the created route in the flask api
