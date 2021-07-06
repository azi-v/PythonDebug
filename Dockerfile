FROM python:3

ENV HTTP_PORT 8888

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

COPY . .

# CMD [ "python", "./app.py" ]
CMD python -m debugpy --listen 0.0.0.0:5678 --wait-for-client ./app.py

EXPOSE ${HTTP_PORT}
EXPOSE 5678