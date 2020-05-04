# Flask JWT Users

`python version 3.7`

## install dependencies using pipenv
`pipenv install`

## Configuration
In the file `/config.py` change the `SQLALCHEMY_DATABASE_URI` connection string and its SECRET_KEY 
In the `/ main.py` file set the desired environment
changing the do_ create_app parameter.
Example: `create_app ('dev')`

## Run
`
pipenv shell
`

`
python main.py
`
