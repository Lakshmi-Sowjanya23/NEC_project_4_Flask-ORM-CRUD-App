from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Model
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Person {self.name}>'


# Create database tables
with app.app_context():
    db.create_all()


# Routes
@app.route('/')
def index():
    """Display all records and Add form"""
    people = Person.query.all()
    return render_template('index.html', people=people)


@app.route('/add', methods=['POST'])
def add():
    """Add a new record"""
    name = request.form.get('name')
    age = request.form.get('age')
    
    if name and age:
        try:
            age = int(age)
            new_person = Person(name=name, age=age)
            db.session.add(new_person)
            db.session.commit()
        except ValueError:
            pass
    
    return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
    """Edit page for a specific record"""
    person = Person.query.get_or_404(id)
    return render_template('edit.html', person=person)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    """Update a record"""
    person = Person.query.get_or_404(id)
    
    name = request.form.get('name')
    age = request.form.get('age')
    
    if name and age:
        try:
            person.name = name
            person.age = int(age)
            db.session.commit()
        except ValueError:
            pass
    
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    """Delete a record"""
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
