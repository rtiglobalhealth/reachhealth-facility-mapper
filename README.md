![philippines](static/ph.png?raw=true "Title")

# Overview
This tool will look up the facility UIDs using the facility name. This can be used when creating the data import files for DHIS2.


### Getting started
 To start the server

 1. install python
 2. run pip install -r requirements.txt
 3. run gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon
 4. Go to the server and upload the csv file. See [this file](example.csv) for an example.
 5. Paste output in import file.


 ### Update/Create the sqlite db

    1. run FlattenOrgs.ipynb to create reach-orgs.csv from reach-orgs.json
 	2. sqlite3 orgs.sqlite
	3. .mode csv
	4. .import reach-orgs.csv orgs
    5. .quit



 
