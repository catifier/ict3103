FROM python:3.11.6-alpine3.18
RUN apk --update add bash nano
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
ENV FLASK_ENV=development
ENV FLASK_APP=main.py
COPY . .
CMD ["python", "main.py"]
