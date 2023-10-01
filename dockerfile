FROM python:3-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirement.txt
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=80"]