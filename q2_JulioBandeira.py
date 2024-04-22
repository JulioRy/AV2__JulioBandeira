from q1_JulioBandeira import transaction, insufficient_balance
import unittest

class TestTransaction(unittest.TestCase):
    def test_transfer_successful(self):
        # Test a successful transfer
        balance = 1000.0
        transfer_amount = 500.0
        expected_result = "Transfer transaction successful!"
        
        result = transaction(balance, transfer_amount)
        
        self.assertEqual(result, expected_result)
    
    def test_insufficient_balance(self):
        # Test a transfer with insufficient balance
        balance = 100.0
        transfer_amount = 500.0
        expected_result = "Insufficient balance. Your available balance is $100.00."
        
        result = transaction(balance, transfer_amount)
        
        self.assertEqual(result, expected_result)
    
    def test_credit_successful(self):
        # Test a successful credit transaction
        balance = 1000.0
        expected_result = "Credit transaction confirmed."
        
        result = transaction(balance, transaction_type="credit")
        
        self.assertEqual(result, expected_result)
    
    def test_stress_test(self):
        # Test a stress test with multiple transactions
        balance = 1000.0
        transfer_amount = 500.0
        expected_result = "Transfer transaction successful!"
        
        for _ in range(1000):
            result = transaction(balance, transfer_amount)
            self.assertEqual(result, expected_result)
            balance -= transfer_amount

if __name__ == '__main__':
    unittest.main()