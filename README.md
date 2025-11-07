# Bank Account Simulator (Mini ATM Machine)

A Python-based simulation of an ATM machine that provides essential banking operations through a secure and user-friendly interface.

## Features

- **Secure PIN Authentication**: Access account with PIN verification
- **Balance Inquiry**: Check current account balance
- **Cash Deposits**: Make deposits with automatic balance updates
- **Cash Withdrawals**: Make withdrawals with safety checks
  - Maximum withdrawal limit: $1000 per transaction
  - Insufficient funds protection
- **PIN Management**: Secure PIN change functionality with validation
- **Transaction History**: View recent account transactions
  - Timestamps for all transactions
  - Detailed transaction logs

## Security Features

- Private attributes for sensitive data (balance, PIN)
- PIN validation for secure operations
- Transaction logging for all account activities
- Input validation for all operations

## Usage

Run the program using Python:

```bash
python mini_atm_machine.py
```

### Available Operations

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. View Transaction History
5. Change PIN
6. Exit

## Technical Details

- Written in Python
- Uses object-oriented programming principles
- Implements encapsulation for data security
- Includes input validation and error handling

## Requirements

- Python 3.x

## Implementation Details

The project implements a `BankAccount` class with the following features:

- Secure PIN storage and validation
- Balance management with safety checks
- Transaction history tracking with timestamps
- Input validation for all operations

## Error Handling

- Invalid PIN attempts
- Insufficient funds protection
- Invalid input validation
- Transaction limits enforcement