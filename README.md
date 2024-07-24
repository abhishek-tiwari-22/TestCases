# install the requirements

pip install -r requirements.txt

# migrate db

python manage.py makemigrations
python manage.py migrate

# run the django server

python manage.py runserver


Goto http://127.0.0.1:8000/admin/ make sure all db entries are present there and in the testcases (db name) add/delete/update the data. Also data (api) can be seen at http://127.0.0.1:8000/testcases/
