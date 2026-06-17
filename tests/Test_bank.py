
from main import bank_account


def test_deposit():
    account = bank_account()
    account.deposit(500)
    assert account.balance == 500 ##Deposit 500 Kronor

def test_withdraw():
    account = bank_account()
    account.withdraw(500)
    account.deposit(500)
    assert account.balance == 0 ##Withdraw 500 Kronor

def test_Check_Saldo():
    account = bank_account()
    account.deposit(500)
    account.deposit(500)
    assert account.check_saldo() == 1000##Visa saldo

def test_interest_result(): ## Kolla summan efter ränta, använde expected och assert för att bara tänka lite hur de ser ut enligt den metoden
    account = bank_account()
    account.deposit(1000)
    expected = account.balance
    expected += account.balance * account.interest / 12
    actual = account.check_interest()
    assert actual ==  expected ##Räkna ut ränta

def test_faktura_betalning():
    account = bank_account()
    account.deposit(500)
    assert account.faktura_betalning(100) == True ##Betala faktura True
    assert account.faktura_betalning(1000) == False ##Betala faktura False