# Content

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)

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
  2. .env file ?
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
