from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_car = db.Column(db.String(50), nullable=False)
    model_of_car = db.Column(db.String(50), nullable=False)
    engine_type = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    transition_type = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    colour = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@app.route('/add_car', methods=['POST'])
def add_car():
    try:
        new_car = Car(
            name_of_car=request.form['name_of_car'],
            model_of_car=request.form['model_of_car'],
            engine_type=request.form['engine_type'],
            fuel_type=request.form['fuel_type'],
            transition_type=request.form['transition_type'],
            condition=request.form['condition'],
            colour=request.form['colour'],
            year=int(request.form['year']),
            price=float(request.form['price']),
        )
        db.session.add(new_car)
        db.session.commit()
        flash("✅ Car added successfully!")
    except Exception as e:
        flash(f"❌ Error adding car: {str(e)}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
with app.app_context():
    db.create_all()
    print("✅ Tables created!")
