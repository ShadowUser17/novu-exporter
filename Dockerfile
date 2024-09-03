FROM python:3-alpine
WORKDIR /root
COPY ./main.py ./
COPY ./requirements.txt ./
RUN python3 -m venv env && ./env/bin/pip3 install --no-cache -r ./requirements.txt
EXPOSE 8080/tcp
ENTRYPOINT ["./env/bin/python3", "main.py"]
