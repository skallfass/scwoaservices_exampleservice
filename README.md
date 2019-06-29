# create / update the development environment
Set the python version for the project:
```bash
pyenv local 3.7.3
```
Ensure to use the up to date dependency definition:
```bash
poetry update
```
Then activate the shell for the project and the projects environment:
```bash
poetry shell
```


# create the documentation for a service based on sanicbaseservice
Ensure to use the up to date dependency definition:
```bash
poetry update
```
Then activate the shell for the project and the projects environment:
```bash
poetry shell
```
Now you can create the documentation:
```bash
create_docu
```


# create package for this repo

## conda-workflow
Ensure to create the the version using git-tags, then run:
```bash
conda build . --python=3.7
```

## poetry-workflow
```bash
poetry build
```


# run the example-service

## poetry-worklow
Set the python version for the project:
```bash
pyenv local 3.7.3
```
Ensure to use the up to date dependency definition:
```bash
poetry update
```
Then activate it using
```bash
poetry shell
```
Now you can start the service with:
```bash
PYTHONPATH=. poetry run python exampleservice/service.py --port=50004
```

Then you can access the swagger-documentation at:
`http://0.0.0.0:50004/swagger`.

## conda-workflow
Create the conda environment (if it does not exist yet) using:
```bash
conda env create -f environment.yml
```
Or using `cenv`:
```bash
cenv -ay
```

Then activate the environment using:
```bash
conda activate <ENVIRONMENT_NAME>
```

Now you can start the service with:
```bash
PYTHONPATH=. python exampleservice/service.py --port=50004
```

Then you can access the swagger-documentation at:
`http://0.0.0.0:50004/swagger`.



## run the example-service inside docker
You can also run the service in a docker-container.

### conda-workflow
First create the base-conda docker-image using:
```bash
sudo docker build . --file Dockerfile_condabase -t base_conda
```
Then you can start the service using:
```bash
sudo docker-compose --file docker-compose_condaworkflow.yaml up
```
Then you can access the swagger-documentation at:
`http://0.0.0.0:50004/swagger`.

### poetry-workflow
Start the service using:
```bash
sudo docker-compose --file docker-compose_poetryworkflow.yaml up
```

Then you can access the swagger-documentation at:
`http://0.0.0.0:50004/swagger`.


# increase project-version

## poetry-workflow
First increase the version of the project inside the `pyproject.toml` using:
```bash
poetry version {major|minor|patch}
```
The version you choose depend on the changes you made. For bugfixes use
`patch`. If you added new functionality use `minor`. If
backwards-compatibility will not be ensured after your changes use `major`.
For details see: [semantic versioning](https://semver.org/).

After you updated the version to the `pyproject.toml`-file you need to create
a new `git tag`, too. The tag should be the same as resulted by the `poetry
version`-command.
Add the changed `pyproject.toml` file:
```bash
git add pyproject.toml
```
Then commit the changes:
```bash
git ci -m 'increased pyproject.toml version'
```
Now create the tag:
```bash
git tag -a <same version as new poetry-version> -m 'release message'
```

Now push the tag:
```bash
git push origin <VERSION>
```

## conda-workflow
The version you choose depend on the changes you made. For bugfixes use
`patch`. If you added new functionality use `minor`. If
backwards-compatibility will not be ensured after your changes use `major`.
For details see: [semantic versioning](https://semver.org/).

Create the new git-tag:
```bash
git tag -a <new version in semantic-versioning style> -m 'release message'
```

Now push the tag:
```bash
git push origin <VERSION>
```
