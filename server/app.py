#!/usr/bin/env python3

from flask import Flask, Response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
@app.route('/contract/<int:id>')
def get_contract(id):

    for contract in contracts:
        if contract["id"] == id:
            return Response(contract["contract_information"], status=200)

    return Response("Contract not found", status=404)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):

    if customer_name in customers:
        return Response("", status=204)

    return Response("Customer not found", status=404)