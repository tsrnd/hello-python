import pytest
from wallet import Wallet, InsufficientAmount


@pytest.mark.parametrize(
    "earned,spent,expected", [(30, 10, 20), (20, 2, 18), (20, 5, 15)]
)
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


def test_transactions_error():
    my_wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        my_wallet.spend_cash(100)
