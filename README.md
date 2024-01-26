# Experiment Hub
Welcome to the Experiment Hub!
This is a personal project by Momodou B Jallow, student of FH Dortmund pursuing a Master's in Digital Transformation. As part of the compact course on programming with Python, this web application serves as a platform to showcase various scientific experiments and findings.

- Student Details
- Name: Momodou B Jallow
- Student ID: 7216697
- School: FH Dortmund
- Major: Masters in Digital Transformation
- Course: Compact Course on Programming with Python
- Project Github link: https://github.com/mbjallow6/ccp-hw06


## About the Site
The Experiment Hub is a Django-based web application that offers a glimpse into the world of scientific exploration. You can find a collection of experiments, each with its details and status. It's a space where learning meets functionality, and data meets design.

You can check out the site locally at: http://127.0.0.1:8000/experiments/

## Features
- Home Page: A table listing all the experiments with essential details like date, title, and short description, along with a link to view more.
- About Page: Redirects to my personal page where you can learn more about my academic journey and interests.
- Submit New Entry Page: An interactive form that allows the contribution of new experimental data to the platform.
- Detail Page: Provides an in-depth look at each experiment, including a comprehensive description and its current status.

## Administrative Capabilities
As an admin, you have the power to add, modify, and manage users and entries, keeping the Experiment Hub up-to-date and accurate.

## Setup and Requirements
- For details on setting up the project and the list of requirements, refer to the requirements.txt file which outlines all necessary dependencies.


## New updates for homework 07
- We created a new file `mongo_db_connection` to handle the connection to our mongo db database
- We added a new view in the `experiments/views.py` to handle the search and filter view.
- Now we are no longer using the Django models so we interface direct with MongoBD 

