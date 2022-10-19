# frontend

### Adding router for the first time
```
vue add router --> For handling navigation.
npm install axios --> For handling client/server-side requests.
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# BACKEND
pip3 install Flask -> NEEDED
    Flask is a micro web framework written in Python. 
    It is classified as a microframework because it does not require particular
    tools or libraries. It has no database abstraction layer, form validation,
    or any other components where pre-existing third-party libraries provide 
    common functions. 

pip install Flask-Cors
pip install mysql-connector-python

virtual environment python (how do you set up??)
source virt/bin/activate

Links --> THIS WAS VERY HELPFUL
- https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

# DATABASE
---------------------------->
SQLITE
----------------------------
add extension sql tools
1) first run `python3 database_start.py` to create your database table
2) second run `python3 database_insert.py` to insert some data into your database
optional... if you need more data
Run the insert into numbers... sql statement
 extra information --> https://www.sqlitetutorial.net/sqlite-python/insert/


---------------------------->
MYSQL
----------------------------
 login for mysql database
    host="localhost",
    user="root",
    password="Password!"





EXTRA INFO
Your variable sql_insert_query is a tuple consisting of the query string and a tuple of parameters. That raises an AttributeError in the connection when attempting to encode what is expected to be a string. From the handling of that error, the OperationalError raises. Very misleading, I admit. cursor.execute(*sql_insert_query) should fix that. Note the unpack operator (*)