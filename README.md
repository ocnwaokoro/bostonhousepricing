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