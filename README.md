# Etsy Scraper - Django Web Application
This image contains a django web application that has 3 pages: [index](#index), [product](#products-page), [products](#products-page)

## Index
Index contains an input area where the link for a specific Etsy product can be submitted.

After the submission, the page will display the status (whether it was successfully uploaded to database or not).

If successful, the page will display an ID number, which can be used to specifically display products by ID numbers in [product page](#product page)

## Product Page
Contains an input area for ID to retrieve related product information

## Products Page
Displays all products that are currently stored in the database.



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

2. Run the web application

   ```powershell
   python EtsyScraper/manage.py runserver
   ```



## Setup - Docker

**NOTE:** To directly download a pre-built Docker image of this application, head over to my Docker repository [link](https://hub.docker.com/r/yethranayeh/app)

There is also `Dockerfile` and `docker-compose.yml` files available for Docker builds.

- To build without `docker-compose.yml` the `Dockerfile` must be edited to *comment out* Docker-compose parts and enable `/Use without docker-compose/` parts
- To build with `docker-compose`, run these commands in shell:

  1. `docker-compose build` - builds an image
  2. `docker-compose up` - runs the image in a container
