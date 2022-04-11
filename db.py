from urllib import response
from flask import jsonify
from google.cloud import datastore

client = datastore.Client()


def show_all():
    query = client.query(kind="customers")
    results = list(query.fetch())
    return results

def add_person(name, email, phone):
    
    with client.transaction():
        incomplete_key = client.key("customers")

        contato = datastore.Entity(key=incomplete_key)

        contato.update(
            {
                "name": name,
                "email": email,
                "phone": phone
            }
        )

    client.put(contato)


def update_customer(id, name, email, phone):

    key = client.key("customers", int(id))
    customer = client.get(key)

    customer["name"] = name
    customer["email"] = email
    customer["phone"] = phone

    client.put(customer)
    return "Ok"

def delete(id):
    key = client.key("customers", int(id))
    client.delete(key)    
    return 'Deleted!'

def get_customer(id):

    key = client.key("customers", int(id))
    customer = client.get(key)
    
    return customer
