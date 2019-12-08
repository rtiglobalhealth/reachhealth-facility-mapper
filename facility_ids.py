import os
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['csv'])
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'orgs.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

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
            uids=[]
            uids.append("hello")
            uids.append("there")
            adam = "hello htere"
            #flash('File successfully uploaded')
			#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("results.html", message=adam, uids = uids);
        else:
            flash('The only allowed file types is csv')
            return redirect(request.url)
        

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    app.run(host='0.0.0.0')
