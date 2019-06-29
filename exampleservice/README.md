Exampleservice to demonstrate the usage of sanic, sanic-openapi and pydantic.

For the full documentation see: [exampleservice-documentation](http://127.0.0.1:8000)

## create / update the conda environment
```bash
cenv -ay
```


## build the conda-package
```bash
conda build . --python=3.7
```

## create the documentation
Run the following command with activated conda environment: `create_docu`


## run the example-service
create the environment using
`cenv -ay`.
Then activate it using
`conda activate baseservice_env`.
Now you can start the service with:
`PYTHONPATH=. python example/service.py --port=50004`

Then you can access the swagger-documentation at:
`http://0.0.0.0:50004/swagger`.
