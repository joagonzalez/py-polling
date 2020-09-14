FROM python:3.7

COPY ./ /src/
COPY requirements.txt /src/

WORKDIR /src/
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]