FROM python:3.11.4-alpine

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r ./requirements.txt
CMD ["python", "/app/src/main.py"]
