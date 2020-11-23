FROM python:3.7-alpine

WORKDIR /app

#ADD ./packages/ml_api /app/
ADD ./requirements.txt /app/requirements.txt
ADD ./wsgi.py /app/wsgi.py

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt


EXPOSE 5000
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]