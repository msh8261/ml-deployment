FROM python:3.7-alpine

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /app

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP wsgi.py

ADD ./packages/ml_api /app/
#ADD ./packages/ml_api/requirements.txt /app/requirements.txt
#ADD ./packages/ml_api/run.py /app/run.py
#ADD ./packages/ml_api/wsgi.py /app/wsgi.py

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

RUN chmod +x /app/wsgi.py
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]