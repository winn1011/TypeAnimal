FROM python:3.11.4

WORKDIR /work

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

COPY ./requirements.txt /work/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /work/requirements.txt

COPY ./app /work/app
COPY ./model /work/model

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
