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
export DEBUG=True
./manage.py test
```
To check test-coverage of project (it's 93%):
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
double check production mode:
```
export DEBUG=False
```
Finally deploy:
```
sls deploy
```

### local
First make sure about AWS credentials, then:
```
./manage.py runserver localhost:8000
```