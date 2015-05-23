import unittest
from BankAccount import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.test_account = BankAccount("Rado", 0, "$")

    def test_create_new_bank_class(self):
        self.assertTrue(isinstance(self.test_account, BankAccount))

    def test_is_name_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount(1000, 10, "$")

    def test_is_balance_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Rado", "balance", "$")

    def test_is_currency_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Rado", 10, 100)

    def test_value_error_raises_from_negative_amount(self):
        with self.assertRaises(ValueError):
            self.test_account.balance = BankAccount("Rado", -10, "$")

    def test_is_withdraw_possible_with_negative_number(self):
        self.assertFalse(self.account.withdraw(-10))

    def test_int_dunder_for_account(self):
        self.assertEqual(self.test_account.balance, 0)

    def test_str_dunder_for_account(self):
        self.assertEqual(str(self.test_account), "Bank account for Rado with balance of 0$")

if __name__ == '__main__':
    unittest.main()
