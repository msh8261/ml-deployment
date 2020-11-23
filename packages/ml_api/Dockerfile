FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD run.py /app
ADD wsgi.py /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]
