from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import genome_detection

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'iwillkillmyselfifthisdoesnotwork'

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(300))
    detected_items = db.Column(db.String(500))


def create_tables():
    with app.app_context():
        db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'lovepython':
            session['logged_in'] = True
            flash('You were successfully logged in', 'success')
            return redirect(url_for('upload_file'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were successfully logged out', 'success')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            filepath = './static/' + file.filename
            file.save(filepath)
            results, gender, disorder = genome_detection.detect(filepath)  # Assume this is a custom function for image processing

            results_str = ', '.join(f'{key}: {value}' for key, value in results.items())
            
            new_result = Result(image_name=file.filename, detected_items=results_str)
            db.session.add(new_result)
            db.session.commit()

            return render_template('display.html', results=results, image=file.filename, gender=gender, disorder=disorder)
    return render_template('index.html')


@app.route('/results')
def view_results():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    all_results = Result.query.all()
    return render_template('all_results.html', results=all_results)


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
