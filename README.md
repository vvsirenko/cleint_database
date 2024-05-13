## Simple client for connect a database

A client that connect with Postgres DB. 

### Getting started

The following parameters are required and can be set in the `.env file`:
| Parameter   | Description  |
| ----------- | ----------- | 
| `DB_USER`    |  Username for connect to database. The role should have a basic permissions are SELECT (read), INSERT (write)   |
| `PASSWORD`    | Pass for username    |
| `DATABASE`    |      Database's name      |

### Installing

Clone the repository and navigate to the project directory:

##
    git clone https://github.com/vvsirenko/client_database.git
    cd client_database

### From Source
1. Create a virtual environment:
##
    python -m venv venv
2. Activate the virtual environment:
##
    #For Linux or macOS:
    source venv/bin/activate
    
3. Install the dependencies using requirements.txt file:
##
    pip install -r requirements.txt
4. Use the following command to start:
##
    python3 main.py <table_name.json>
