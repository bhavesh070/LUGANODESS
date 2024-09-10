
FROM python:3.9-slim

WORKDIR /luganodes_task2

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Client.py .
COPY server.py .
COPY config.json .

CMD ["python", "Client.py"]
