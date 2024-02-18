FROM python:3.12-slim

WORKDIR /usr/app/src
COPY src ./
COPY requirements.txt ../
RUN pip install -r ../requirements.txt

CMD ["python", "-u", "./crawl_controller.py"]