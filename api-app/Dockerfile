FROM python:slim
RUN mkdir /app
RUN useradd -ms /bin/bash pyuser
COPY ./src/requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./src/ /app/
USER pyuser
WORKDIR /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]