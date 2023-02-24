FROM ubuntu

ARG APP_ENV=stock_products
ENV APP_ENV="${APP_ENV}"

WORKDIR /stocks_products

COPY ./stocks_products .

RUN apt-get update && apt-get install -y python3.10 && apt-get -y install python3-pip && pip install -r requirements.txt

EXPOSE 80 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]

