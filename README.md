# Content

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Application view](#application-view)

## General info
<details>
<summary>see <b>general info</b></summary>
  This project is a web app built with <b>Python (Django 4.1)</b> that allows logged users to save and share their recipes with others, with the possiblity to rank and comment them.
</details>

## Technologies
<details>
<summary>see <b>technologies</b></summary>
<ul>
  <li>Django</li>
  <li>Django REST Framework</li>
  <li>HTML/CSS</li>
  <li>javaScript</li>
  <li>Docker Compose</li>
  <li>PostgreSQL</li>
  <li>MongoDB</li>
  <li>Celery</li>
  <li>Redis</li>
</ul>
</details>

## Setup
<details>
<summary>see <b>setup</b></summary>

To run this project on your machine it is required to have installed previously Docker Compose on your computer. For further information, see [documentation](https://docs.docker.com/compose/install/ "Install docker").

  1. [Clone](https://help.github.com/articles/cloning-a-repository/) the repository on your machine.
  2. Create a .env file at the base of the project repository, in which you'll have to set the variables below.
       <details>
       <summary>see .env file variables</summary>
        SECRET_KEY<br>
        DEBUG<br>
        POSTGRES_DB<br>
        POSTGRES_USER<br>
        POSTGRES_PASSWORD<br>
        POSTGRES_HOST<br>
        MONGO_INITDB_DATABASE<br>
        MONGO_INITDB_ROOT_USERNAME<br>
        MONGO_INITDB_ROOT_PASSWORD<br>
        MONGODB_HOST<br>
        AWS_SECRET_ACCESS_KEY<br>
        AWS_ACCESS_KEY_ID<br>
        FROM_EMAIL<br>
        </details>
     Please note that mail sending functionality was built with AWS SES, you will have to register the mail address you wish to use on AWS platform. Otherwise, you can still adapt settings.py with the technology you wish to use.
  3. At the base of the project repository run the command: `docker compose -f docker-compose-dev.yml up --build -d`
  4. Open the link to the web app in your web browser: http://0.0.0.0:8000/
</details>

## More detailed information about modules
<details>
<summary>see <b>info about modules</b></summary>
  <ul>
    <li>The app allows logged users to rank and comment the recipes that are registered. API endpoints were created to permit those functionalities to work, the communication between the API and the app is done through AJAX.</li>
    <li>The users are able to download or share the recipe through mail, a PDF is generated from the chosen recipe.</li>
    <li>All registered users have the possibility to request a reset password if forgotten.</li>
  </ul>
</details>

## Application view
<details>
<summary>see <b>screenshots</b></summary>
    <img src="https://user-images.githubusercontent.com/42584510/212421569-73e2f7e1-352a-43f0-acb4-41509c906b01.png" width="50%" height="50%">
    <img src="https://user-images.githubusercontent.com/42584510/212421652-9e683ada-912a-4eb7-8f58-242001c75c42.png" width="50%" height="50%">
</details>
