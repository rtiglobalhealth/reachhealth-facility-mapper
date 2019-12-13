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


 
