from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

#from sqlalchemy.testing import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique= True, nullable= False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/customers')
def get_customers():
    customers = Customer.query.all()
    output = []
    for customer in customers:
        customer_data = {'name': customer.name, 'description': customer.description}
        output.append(customer_data)

    return {"customers": output}

@app.route('/customers/<id>')
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return {"name": customer.name, "description": customer.description}




if __name__ == "__main__":
    app.run()