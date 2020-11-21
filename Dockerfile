FROM python:3.7.0


WORKDIR /app/ml_api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run.py

# Install requirements, including from Gemfury
ADD ./packages/ml_api /app/ml_api
RUN pip install --upgrade pip
RUN pip install -r /app/ml_api/requirements.txt

RUN chmod +x /app/ml_api/run.cmd
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000

CMD ["cmd", "./run.cmd"]