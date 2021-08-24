# Etsy Scraper - Django Web Application w/ PostgreSQL
This is a django web application that can scrape **Product Name, Price, Image Link** from [Etsy](https://www.etsy.com) product links. The scraped data is then saved into a [**PostgreSQL**](https://www.postgresql.org/) database.

It has 3 pages: [index](#index), [product](#product-page), [products](#products-page). 

## Index
Index contains an input area where the link for a specific Etsy product can be submitted.

After the submission, the page will display the status (whether it was successfully uploaded to database or not).

If successful, the page will display an ID number, which can be used to specifically display products by ID numbers in [product page](#product-page)

## Product Page
Contains an input area for ID to retrieve related product information
The required ID will be displayed on the index page when an Etsy product link is submitted.

## Products Page
Displays all products that are currently stored in the database.
The products that are sold out will have a price of `-1.00`

---

## Setup

1. Preferrably, create a virtual environment

   ```powershell
   python -m venv venv
   venv/scripts/activate
   ```



If you receive a `scripts is disabled on this system` error, enable scripts on your system:

  - ```powershell
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```

    - This would allow running virtualenv in the *current PowerShell session*.

    

  - ```powershell
    Set-ExecutionPolicy Unrestricted -Force 
    ```

    - This would allow running scripts, thus virtualenv *for the whole system*. Which is a bit unsafe. To disable it:

    - ```powershell
      Set-ExecutionPolicy Restricted -Force
      ```

2. Install dependencies

   ```powershell
   pip install -r -requirements.txt
   ```

3. Run the web application

   ```powershell
   python EtsyScraper/manage.py runserver
   ```

You can access the database with `pgAdmin 4` 
- Or, through your preferred terminal by typing
```powershell
psql postgres postgres
```
- If prompted with `Password for user postgres:` just type `postgres`.


There is also `Dockerfile` and `docker-compose.yml` files available for Docker builds.

---

## Setup - Docker

<!-- **NOTE:** To directly download a pre-built Docker image of this application, head over to my Docker repository [link](https://hub.docker.com/r/yethranayeh/app) -->
**NOTE:** If using Docker, make sure to change database settings in `EtsyScraper/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',

        #####

        # USE CASE OPTIONS

        # For Docker:
        'HOST': 'db', # [MAKE SURE THAT THIS IS THE HOST WHEN USING DOCKER]

        # For local use:
        # 'HOST': '127.0.0.1',

        #####

        'PORT': 5432,
    }
}

```

- To build *without* `docker-compose.yml` the `Dockerfile` must be edited to *comment out* `/Docker-compose/` parts and enable `/Use without docker-compose/` parts

  1. `docker build --tag <ProjectName>`
  2. `docker run <ProjectName>`

- To build with `docker-compose`, run these commands in shell:

  1. `docker-compose build` - builds an image
  2. `docker-compose run --rm app` - Run this **ONLY FOR THE FIRST TIME** so that PostgreSQL database files can be created. After this, only repeat step `1` and `3` after making changes to the project.
  3. `docker-compose up` - runs the image in a container

### Accessing PostgreSQL through Docker CLI

1. Under `etsyscraper` container, click `postgres_db`'s CLI:
![Docker Desktop Image](https://i.imgur.com/TgqJlN0.jpg)

2. In CLI, write `psql postgres postgres` to access the database and run SQL commands.
