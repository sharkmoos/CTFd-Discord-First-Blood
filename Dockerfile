FROM python:3.10-slim

RUN apt update && apt install -qy nano curl

WORKDIR /home/api/

COPY requirements.txt src /home/api/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]