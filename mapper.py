import os
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, request, redirect, render_template, g
from werkzeug.utils import secure_filename
import io
import csv
import sqlite3
from flask_csv import send_csv


app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['csv'])
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'orgs.sqlite'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
    for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def query_db2(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream, delimiter='\t')
            
            uids=[]

            for row in csv_input:
                facility = query_db('SELECT id, "name(en)" from orgs where "name(en)" = ?',
                [row[0]], one=True)
                
                print(row[0])

                if facility is None:
                    uids.append({"uid": '', "facility name": ''})
                    print('No such Facility')
                else:
                    uids.append({"uid": facility['id'],"facility name": facility['name(en)']})
                    #print(the_facility + 'has the id' + )
            return send_csv(uids,
                    "uids.csv", ["uid","facility name"])

            #return render_template("results.html", uids = uids);
        else:
            flash('The only allowed file types is csv')
            return redirect(request.url)
        

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0')
