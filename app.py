from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from flask.cli import with_appcontext
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask.cli import with_appcontext  # Import with_appcontext
from flask_migrate import Migrate

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///works.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_filename = db.Column(db.String(255))

# This decorator ensures that this function runs with the app's context
@with_appcontext
def create_tables():
    # Create the database tables
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

#route for static files
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/works')
def works():
    works_data = Work.query.all()  # Query all records from the Work table
    return render_template('works.html', works=works_data)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Handle image file upload
        if 'image' in request.files:
            image = request.files['image']
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                # Handle invalid file format or no file provided
                flash('Invalid file format. Allowed formats: png, jpg, jpeg, gif', 'error')
                return redirect(request.url)

        new_work = Work(title=title, description=description, image_filename=filename)
        db.session.add(new_work)
        db.session.commit()
        return redirect(url_for('add'))
    return render_template('add.html')





if __name__ == '__main__':
    app.run(debug=True)
