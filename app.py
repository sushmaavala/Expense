from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('view_expense.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        new_expense = Expense(name=name, amount=amount)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

if __name__ == '__main__':
    app.run(debug=True)
