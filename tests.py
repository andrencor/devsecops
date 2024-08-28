#!/usr/bin/env python3

import unittest
from flask import Flask
from flask_restful import Api
from main import app, Account, BankApi

class BankApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.account = Account('1234-5')

    def test_get_balance(self):
        response = self.app.get('/1234-5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 0})

    def test_patch_deposit(self):
        response = self.app.patch('/1234-5/10.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 10.0})

        response = self.app.patch('/1234-5/123.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 133.5})

if __name__ == '__main__':
    unittest.main()
