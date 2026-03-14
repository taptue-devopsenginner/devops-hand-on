FROM python:3.9-slim AS builder
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask

FROM python:3.9-slim AS runtime
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
