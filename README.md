
# API for Spy Cats

Test task for DevelopsToday :)

## Link to Postman collection - https://www.postman.com/queryworld/1/collection/4b8ogfv/spycats-api?action=share&creator=36967078




## Deployment


### Clone the Repository

Clone the project repository to your local machine:
```bash
    git clone https://github.com/casual-user-asm/spyCats.git
    cd spyCats
```
### Set Up the Virtual Environment
Create and activate a Python virtual environment to isolate project dependencies:
#### On macOS/Linux: 
```bash
  python3 -m venv venv
  source venv/bin/activate
```
#### On Windows: 
```bash
  python -m venv venv
  .\venv\Scripts\activate
```
### Install Dependencies
Once your virtual environment is active, install the required dependencies:
```bash
pip install -r requirements.txt
```
### Set Up Environment Variables
Create a .env file in the root directory of the project to store sensitive information, such as API keys, database credentials, and other settings.

Here is an example .env file:
```bash
# Database settings
DB_HOST=localhost
DB_PORT=5432
DB_NAME=*****
DB_USER=*****
DB_PASSWORD=*****

# Secret keys for Django
DJANGO_SECRET_KEY=*****

# Other settings
DEBUG=*****
```
### Run Server
```bash
python manage.py runserver
```

