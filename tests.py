#!/usr/bin/env python3
import unittest
from flask import Flask
from flaskrestful import Api
from main import app, Account, BankApi

class BankApiTestCase(unittest.TestCase):
    def setUp(self):
        # Configura o Flask para testes
        self.app = app.testclient()
        self.app.testing = True
        self.account = Account('1234-5')

    def testgetbalance(self):
        # Testa o endpoint GET
        response = self.app.get('/1234-5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 0})

    def test_patch_deposit(self):
        # Testa o endpoint PATCH
        response = self.app.patch('/1234-5/10.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 10.0})

        response = self.app.patch('/1234-5/123.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'saldo': 133.5})

if __name == '__main':
    unittest.main()
