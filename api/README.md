# Getting started

In a terminal, navigate to the `api` directory and run the following

```
source bin/activate
```
Once the command has run successfully, in the same terminal, run:

```
pip install -r requirements.txt
```
This will install any necessary dependencies.


This is a template [flask app](https://flask.palletsprojects.com/en/3.0.x/), to run it, use the following command from the `api/src` directory

```
flask --app app run
```

This template app is designed with MySQL in mind and uses the [`mysql-connector`](https://www.w3schools.com/python/python_mysql_getstarted.asp) package.

If you are using a postgres database then [`psycopg2`](https://www.postgresqltutorial.com/postgresql-python/) will be more appropriate, it is already included as a dependency in the project. 

You will however need to replace the `mysql-connector` code to make it work

## Running the DB

The database is a MySQL database running on a docker instance. For this tep you will need to have docker installed.

From the `api` directory run:

```
docker build --file Dockerfile.db -t cooking-app-db .
```

This will create your DB docker image. To run the image, run:

```
docker run --name my-app-db -p 3306:3306 cooking-app-db
```

You should now be able to connect to the MySQL server hosted on the docker container, create your database and all the tables you need.

You can do this via the Docker GUI interactive terminal, here's an example of the type of commands you'll need to run in order:

```
mysql -p
```
Enter the password when prompted

```
CREATE DATABASE <your-db-name-goes-here>;
```

```
USE <your-db-name-goes-here>;
```

```
CREATE TABLE recipes(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NULL);
```

```
INSERT INTO recipes (name) VALUES ('Spaghetti');
```


You will need to create a `recipes` table for the template app to work correctly