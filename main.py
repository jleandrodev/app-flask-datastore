from flask import Flask, request, render_template, redirect, url_for
from db import get_customer, show_all, add_person, delete, update_customer

app = Flask(__name__)

@app.route('/')
def index():
    contatos = show_all()
    return render_template('index.html', contatos = contatos)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        add_person(name, email, phone)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        update_customer(id, name, email, phone)

        return redirect(url_for('index'))
    customer = get_customer(id)    
    return render_template('edit.html', contato = customer)    

@app.route('/delete/<id>')
def exclude(id):
    delete(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


