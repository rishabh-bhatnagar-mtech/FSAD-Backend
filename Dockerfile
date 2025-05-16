FROM python:3.11-slim

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 5000
ENTRYPOINT ["python3", "run.py"]
