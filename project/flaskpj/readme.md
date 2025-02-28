> export FLASK_APP=flaskpj
>
> export FLASK_ENV= development

```cmd
venv➜  flaskpj git:(main) ✗ flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.
.venv➜  flaskpj git:(main) ✗ export FLASK_APP=flaskpj
.venv➜  flaskpj git:(main) ✗ export FLASK_ENV=development
.venv➜  flaskpj git:(main) ✗ flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not import 'flaskpj.flaskpj'.
.venv➜  flaskpj git:(main) ✗ echo $FLASK_APP
flaskpj
.venv➜  flaskpj git:(main) ✗ flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not import 'flaskpj.flaskpj'.
.venv➜  flaskpj git:(main) ✗ cd ..    
.venv➜  project git:(main) ✗ flask run
 * Serving Flask app 'flaskpj'
 * Debug mode: off
```

#### 問題１Error: Could not import 'flaskpj.flaskpj'.

> ディレクトリが間違っています。



https://www.hakuhodofoundation.or.jp/globalnetwork/