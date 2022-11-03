# MaintenanceApp

# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Tools](#tools)
* [Environment](#environment)
* [Setup](#setup)
* [API](#available-api-requests)


## General info
   MaintenanceApp is a django-based web application designed for manage and optimize maintenance processes in
a manufacturing environment. It allows production departments to report malfunctions and watch over upcoming planned
maintenances (a day-before e-mail notification). Maintenance department employees have concise view on pending malfunctions, planned maintenances and clean interface to
report performed actions. Manager profile offers compact view on current situation via dashboard and wide array of actions, such as
user and machines management, adding maintenance schemes and schedules etc. App also offers a simple REST API for managing machines, with a view to further development.


## Technologies
* Python 3.10
* Django 4.1
* Jinja
* Python Unittest
* Django rest framework 3.14
* PostgreSQL 12
* HTML5/CSS/JS
* Docker
* docker-compose


## Tools
* precommit
* plotly
* django-crontab
* factory_boy


## Environment
In order to build the application you need to define environment variables in the .env file. For a quick run just copy and paste text below:
`SECRET_KEY=8opxm+uzbo&rg7@6j)fzmznu&t2&41dwjk13zs=0bncq9ek+ne`\
`DB_NAME=maintenance_app`\
`DB_USER=postgres`\
`DB_PASSWORD=postgres`\
`DB_HOST=localhost`\
`DB_PORT=5432`

In order to activate SMTP service add the following lines to .env file: \
`EMAIL_HOST_USER=(your_email_username)`\
`EMAIL_HOST_PASSWORD=(your_email_password)`\
`EMAIL_HOST=(your_smtp_host)`\
`EMAIL_PORT=(your_smtp_port)`

## Setup
To run this project use the following commands in project directory: \
`$ docker-compose build` \
`$ docker-compose up`

App is available at **127.0.0.1:8080**

## Available API requests
`GET /api/machines/` Gets list of all machines \
`GET /api/machines/{id}/` Gets particular machine \
`POST /api/machines/` Adds new machine to database \
`PUT /api/machines/{id}/` Modify machine object with specified ID \
`PATCH /api/machines/` Modify particular field of machine object with specified ID \
`DELETE /api/machines/{id}/` Removes machine with specified ID from database


## Application view
![MaintenanceAppImg](https://user-images.githubusercontent.com/106873834/199683590-a488e512-7800-47c6-8bab-dac7a48b69e8.png)
