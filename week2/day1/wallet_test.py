import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(20)


@pytest.mark.parametrize("balance,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_cash(balance, spent, expected):
    wallet = Wallet()
    wallet.add_cash(balance)
    wallet.spend_cash(spent)
    assert wallet.balance == expected
    assert wallet.info() == "Your wallet has {}".format(expected)


def test_spend_cash_raise_exception(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(20)
