#include <iostream>. 
#include <vector>
#include <string>

class Account {
private:
    std::string accountNumber;
    std::string accountHolderName;
    double balance;

public:
    Account(const std::string &accNum, const std::string &holderName, double initialBalance)
        : accountNumber(accNum), accountHolderName(holderName), balance(initialBalance) {}

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            std::cout << "Deposit successful. New balance: $" << balance << std::endl;
        } else {
            std::cout << "Invalid deposit amount." << std::endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            std::cout << "Withdrawal successful. New balance: $" << balance << std::endl;
        } else {
            std::cout << "Invalid withdrawal amount or insufficient funds." << std::endl;
        }
    }

    void display() const {
        std::cout << "Account Number: " << accountNumber << std::endl;
        std::cout << "Account Holder: " << accountHolderName << std::endl;
        std::cout << "Balance: $" << balance << std::endl;
    }
};

class Bank {
private:
    std::vector<Account> accounts;

public:
    void createAccount(const std::string &accNum, const std::string &holderName, double initialBalance) {
        accounts.emplace_back(accNum, holderName, initialBalance);
        std::cout << "Account created successfully." << std::endl;
    }

    Account* findAccount(const std::string &accNum) {
        for (auto &account : accounts) {
            if (account.getAccountNumber() == accNum) {
                return &account;
            }
        }
        return nullptr;
    }

    void deposit(const std::string &accNum, double amount) {
        Account* account = findAccount(accNum);
        if (account) {
            account->deposit(amount);
        } else {
            std::cout << "Account not found." << std::endl;
        }
    }

    void withdraw(const std::string &accNum, double amount) {
        Account* account = findAccount(accNum);
        if (account) {
            account->withdraw(amount);
        } else {
            std::cout << "Account not found." << std::endl;
        }
    }

    void displayAccountDetails(const std::string &accNum) {
        Account* account = findAccount(accNum);
        if (account) {
            account->display();
        } else {
            std::cout << "Account not found." << std::endl;
        }
    }
};

int main() {
    Bank bank;
    bank.createAccount("123456", "Alice", 1000.0);
    bank.createAccount("654321", "Bob", 500.0);

    bank.deposit("123456", 200.0);
    bank.withdraw("654321", 100.0);

    bank.displayAccountDetails("123456");
    bank.displayAccountDetails("654321");

    return 0;
}
