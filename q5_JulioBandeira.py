import uuid
from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

accounts = []

create_account = lambda name, password, balance: accounts.append({
    'id': str(uuid.uuid4()),
    'name': name,
    'password': hashlib.sha256(password.encode()).hexdigest(),
    'balance': balance
})

login_account = lambda: any(True for account in accounts if account['name'] == request.form.get('name') and account['password'] == hashlib.sha256(request.form.get('password').encode()).hexdigest())

TRANSFER_successful = lambda TRANSFER_amount, balance: (
    print("Requested Transfer amount: $%.2f" % TRANSFER_amount),
    print("Current balance: $%.2f" % (balance - TRANSFER_amount)),
    (
        (lambda recipient_account: print("Transfer of $%.2f successful! to account %s." % (TRANSFER_amount, recipient_account)))
        if (lambda confirm: confirm == 'Y')(input("Confirm transfer? (Y/N) ").upper())
        else print("Transfer of $%.2f cancelled." % TRANSFER_amount)
    )(input("Enter the account to transfer to: "))
)

withdrawal_successful = lambda withdrawal_amount, balance: (
    (lambda: (
        (lambda: print("Requested Withdrawal amount: $%.2f" % withdrawal_amount))(),
        (lambda: print("Current balance: $%.2f" % (balance - withdrawal_amount)))(),
        (lambda: (
            (lambda: print("Withdrawal of $%.2f successful!" % withdrawal_amount))
            if (lambda confirm: confirm == 'Y')(input("Confirm withdrawal? (Y/N) ").upper())
            else print("Withdrawal of $%.2f cancelled." % withdrawal_amount)
        ))(),
        (lambda: print("Payment receipt:"))(),
        (lambda: print("Name: John"))(),  # Replace "John" with the actual name variable
        (lambda: print("Withdrawal amount: $%.2f" % withdrawal_amount))()
    ))()
)

credit_successful = lambda: (
    (lambda: (
        (lambda: request_credit_account_details())(),
        (lambda: request_payment_from_bank(lambda: confirm_payment_approval_from_bank()))(),
        (lambda confirm: (
            (lambda: print("Credit transaction confirmed."))()
            if confirm == 'Y'
            else print("Credit transaction cancelled.")
        ))(input("Confirm credit transaction? (Y/N) ").upper())
    ))()
)

insufficient_balance = lambda balance: print("Insufficient balance. Your available balance is $%.2f." % balance)
transfer_successful = lambda: print("Transfer transaction successful!")
invalid_option = lambda: print("Invalid option.")

request_credit_account_details = lambda: (
    (lambda password: print("Credit account details requested."))
    if hashlib.sha256(request.form.get('password').encode()).hexdigest() == accounts[0]['password']
    else print("Invalid transaction password.")
)

request_payment_from_bank = lambda confirm_payment_fn: confirm_payment_fn()

confirm_payment_approval_from_bank = lambda: print("Payment approval confirmed.")

transaction = lambda balance: (
    (lambda TRANSFER_amount: TRANSFER_successful(TRANSFER_amount, balance) if TRANSFER_amount <= balance else insufficient_balance(balance))(float(input("Enter TRANSFER amount: ")))
    if (choice := input("Choose a transaction: Transfer (T), Credit (Credit), or Cash (Cash)? ").upper()) == 'T'
    else (
        credit_successful()
        if choice == 'CREDIT'
        else (
            withdrawal_successful(float(input("Enter withdrawal amount: ")), balance)
            if choice == 'CASH'
            else invalid_option()
        )
    )
)

@app.route('/login', methods=['POST'])
def login():
    print("Received request with the following data:")
    print("Name:", request.form.get('name'))
    print("Password:", request.form.get('password'))
    
    if login_account():
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'})

create_account("John", "password1", 1000.0)

if __name__ == '__main__':
    app.run()