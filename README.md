# Rayka

This is an assignment from [Rayka](#) company.

## Environments
```
export AWS_ACCESS_KEY_ID=<yourAccessKey>
export AWS_SECRET_ACCESS_KEY=<yourSecretKey>
```

## Test and Coverage

To run tests, run command blow:
```
./manage.py test
```
To check test-coverage of project (it's 97%):
- first type command `coverage html` to generate `html` view of coverage
- then open `../htmlcov/index.html`

## Deployment

### Serverless
First you need to install serverless and related plugins:
```
npm install -g serverless serverless-python-requirements serverless-wsgi
```
Then create an *aws profile* with `rayka` name.
```
aws configure --profile rayka
```
Finally deploy:
```
sls deploy
```

### local
First run migrations:
```
./manage.py makemigrations
./manage.py migrate
```
Then run:
```
./manage.py runserver localhost:8000
```