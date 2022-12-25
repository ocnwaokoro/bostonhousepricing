### Boston House Pricing Prediction

### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

```
conda create -p venv python==3.7 -y
conda activate ./venv 
```

```
pip install -r requirements.txt
```
```
git clone "git-clone-url"
```

```
git config --global user.name ""
git config --global user.email ""
git add .
git status
git commit -m ""
git push origin main

```

Code app.py and then do
```
python app.py
```

Test app w/ Postman.
Go to Postman & Create a Sample request in JSON.
Check if json is valid w/ jsonlint.com.
Check if the desired output is given.
```
POST http://127.0.0.1:5000/predict_api

{
    "data": {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0.0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.0900,
        "RAD": 1.0,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.90,
        "LSTAT": 4.98
    }
}

```

To leave app
```
cntrl-Z
cntrl-C
```

Create frontend version of web app for upload into cloud.
Create Procfile that tells Heroku what commands the app must execute as soon as it starts.
Use g unicorn to create python https server for wsgi applications. It allows you to run python application concurrently by running multiple processes. gunicorn allows for loadbalancing & sends the requests of many users to many diff instances. app:app specifies the app name as app.
```
web: gunicorn app:app
```

Go to Heroku & create an app. Connect via Github connect button & find the repo. Enable Automatic Deploys to change app when github upload changes. Check logs to see if the build succeeds or not. Predict frontend & predict_api backend should both work.

Docker container can hold all dependencies & base configs.
* FROM selects base images from DockerHub (i.e python:3.7 takes base image of python w/ Linux server on top)
* COPY copy info from current location into an app
* WORKDIR establish the app folder as the working directory
* RUN dictate what command should be run
* EXPOSE expose some port to enable access to url; doing $PORT allows cloud server to automatically decide that port
* CMD (gunicorn allows you to run the python app w/i Heroku cloud) (--workers divides tasks among a set number of instances ) (--bind give some local addr. in Heroku cloud) (app:app first app goes into app.py & second app runs the app variable w/i which is the Flask app)

Configure CI/CD workflow using github actions.
1. create folder called .github
2. create workflows folder w/i that
3. create main.yaml file w/i which tells what must be done to create the container