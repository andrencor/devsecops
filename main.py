# curl http://localhost:3001/1234-5
# curl -X PATCH http://localhost:3001/1234-5/10.0
# curl -X PATCH http://localhost:3001/1234-5/123.5

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class BankApi(Resource):
    def get(self):
        return {'saldo': account.balance}

    def patch(self, amount):
        return {'saldo': account.deposit(amount)}

account =  Account('1234-5')

api.add_resource(BankApi, "/1234-5", "/1234-5/<float:amount>")

if __name__ == '__main__':
    app.run(port=3001, debug=True)
