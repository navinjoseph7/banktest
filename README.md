# My Banking Application

Welcome to My Banking Application! This is a simple Python application that allows users to manage their bank accounts by depositing and withdrawing funds and viewing transaction history.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create a bank account.
- Deposit funds into your account.
- Withdraw funds from your account.
- View transaction history in a specified format.

## Getting Started

Follow the instructions below to get started with this project.

## Softwares Used

- Python
- Pytest
- Python REPL


### Prerequisites

- Python (version 3.x) installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/my-banking-application.git

2. Change to the working directory
   cd banktest

3. Install Pytest
   pipenv install pytest --python 3.11

4. Setup Environment
   pipenv shell

5. Running tests
   pytest

### Usage

1.Run the Python REPL:
  python

2.Import the account class
  from lib.account import Account

3.Create an instance of the Account class:
  account = Account()

4.Use the following methods to interact with the account:
account.deposit(amount): Deposit funds into the account.
account.withdraw(amount): Withdraw funds from the account.
account.print_statement(): View the transaction history in the specified format.
Example usage:


account.deposit(1000)
account.withdraw(500)
account.print_statement()