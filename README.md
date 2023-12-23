# CAN I BORROW ONE?

As they say, sharing is caring, and we wanted to create a pool of books where we would like to share the books we have in our libraries at home with people in our community. We hope that this attitude will expand in our community with many more people adding their books to the Can I Borrow 1 REST API database by simple CRUD operations. Please note that locating the books requested by users and arranging pick up or delivery is not the scope of this mini project.

THE AIM OF OUR REST API:

The aim of our REST API is to create a platform, a pool of books, where we can borrow or lend books from different literatures and languages.

Let's start with a little introduction to our application's architecture.


<img width="883" alt="Screenshot 2023-12-23 at 18 18 31" src="https://github.com/alexanderhovan/jobsearch/assets/148468625/c58945da-a8d2-444f-aceb-5eed67416e02">

Here we have our front end which is combined from multiple apps and HTML templates for these apps, where via CRUD operations they connect to the database for login - this is also how the user rights are being applied - and then we pass to the next page, where we again use the CRUD operations to both connect to our API and the database.

Now, let's start with the set-up.

First, you need to create the directory for the project. 

```
mkdir caniborrow
cd caniborrow

```
After the directory has been created and we got into it, we need to create the Python environment and intialise the upload of all the required packages that are contained the requirements.txt file.

There we need:

* Flask: we need this for web application creation.
* requests: which we need for HTTP requests, and we also need it to interact with APIs.
* Flask-SQLAlchemy: is needed for our SQL database. It is also an Object-Relational Mapping (ORM) library for Python.




