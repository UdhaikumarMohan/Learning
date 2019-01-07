#Test condition for counting digits:
import countinteger


def test_canassertTrue():
    assert True


def test_countintegerofgivennumber():
    actual=countinteger.countdigits(12345)
    expected=5
    assert actual==expected