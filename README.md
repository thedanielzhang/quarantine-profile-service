# quarantine-profile-service

Steps to set up
1) Create GitHub Repository
2) Reference https://github.com/thedanielzhang/berkeley-pantry for set up of Flask/Flask-restful
3) Create DAO [commit master 4a39f8f]
    * DAO stands for Data Access Object, this is where the resources of the service is defined
    * Within repository, create a service_dao.py file (for instance, for this service, we'll create a profile_dao.py)
    * Define class and constructor to set parameters of the object 
    * n.b. All imports should be OK 
4) Set up db_manager [commit master 14ae906]
    * Create db_manager folder (all changes will be in this folder)
    * Create __init__.py (no code)
    * Create db_utils (should be able to simply copy code from other repositories). This provides functionality for SQL operations. Query is a SQL command, var is a parameter. TODO: Should probably rename methods to more informative names (sql_query is a get all, sql_query2 is a get with ONE parameter)
    * Create schema.sql (define the types of the DAO fields)
    * Create database.db (no code)
    * n.b. All imports should be OK
5) Create service.py (profile.py). This is the resource file, all methods to get a specific profile/profiles are defined here. [commit master 9c42791]
    * Import all necessary imports (reference repository for example, should include things from both flask_restful and flask, as well as dao and the db_manager.db_utils
    * Set up reqparse (lines 9 - 11). This helps parse any requests where the params are passed as arguments
    * Create Profile class - this is where we use db_utils to fetch from SQL db. For now, get, delete, and put is all we'll add, but more specific operations can be defined. 
6) Create api.py. This is where the service is run, set up, teardown, database set up, all other functionality basically [commit master f8ffdcf]
    * Import stuff!
    * DB methods can be copied directly, no code changes required (lines 13 - 31)
    * Set up test resource (lines 33 - 35). This is useful to test whether or not api is up and running.
    * Add resources (lines 37 - 38)
    * Copy last two lines!
7) To run everything, first: 
    * From cmd line, change working directory to ProfileService, and use command python api.py
    * After that, open python shell (just use command python). Then run the next few commands in the shell:
        >>> from api import init_db
        >>> init_db()
    This initalizes the database.
    * Use postman or curl to make requests

N.B.: Don't commit/push database.db or any of the pycache stuff
