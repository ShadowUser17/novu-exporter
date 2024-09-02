### Novu Prometheus Exporter

#### Configure environment:
```bash
python3 -m venv --upgrade-deps env && \
./env/bin/pip3 install -r requirements_dev.txt
```

#### Scan project dependencies:
```bash
./env/bin/pip-audit -f json | python3 -m json.tool
```

#### Validate project files:
```bash
./env/bin/flake8 --ignore="E501" *.py
```

#### Build docker image:
```bash
docker build -t "shadowuser17/novu-exporter:testing" .
```
```bash
docker build -t "shadowuser17/novu-exporter:latest" .
```

#### Scan docker image:
```bash
dockle "shadowuser17/novu-exporter:testing"
```
```bash
trivy image "shadowuser17/novu-exporter:testing"
```

#### Publish docker image:
```bash
docker login -u "${DOCKERHUB_LOGIN}" -p "${DOCKERHUB_TOKEN}"
```
```bash
docker push "shadowuser17/novu-exporter:testing"
```
```bash
docker push "shadowuser17/novu-exporter:latest"
```

#### Publish docker image to AWS/ECR:
```bash
export IMAGE_NAME=""
export IMAGE_TAG=""
export AWS_ECR_NAME=""
export AWS_DEFAULT_REGION=""
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
```
```bash
./env/bin/python3 push_aws_ecr.py
```
```bash
docker logout "${AWS_ECR_NAME}"
```

#### Dependencies:
- [PyMongo](https://github.com/mongodb/mongo-python-driver)
- [prometheus-client](https://github.com/prometheus/client_python)
