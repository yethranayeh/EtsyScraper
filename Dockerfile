FROM python:3.8

WORKDIR /scraper

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# CMD [ "cd", "EtsyScraper", ";", "python3", "EtsyScraper/manage.py", "runserver", "0.0.0.0:8000" ]
CMD cd EtsyScraper ; python3 manage.py runserver 0.0.0.0:8000
