FROM python:3.7

COPY ./src/ /src/
COPY ./requirements.txt /src/

WORKDIR /src/
RUN ls
# RUN mkdir logs
RUN pip install -r requirements.txt
# EXPOSE 8000
CMD ["python", "app.py"]