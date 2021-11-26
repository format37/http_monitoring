FROM python:3.9
WORKDIR /service
COPY requirements.txt /service
RUN pip3 install -r requirements.txt --no-cache-dir
COPY monitoring.py /service
ENTRYPOINT ["python3"]
CMD ["monitoring.py"]
