FROM python:3.7

RUN mkdir /watchapp

WORKDIR /watchapp

ADD . /watchapp/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "/watchapp/app.py"]