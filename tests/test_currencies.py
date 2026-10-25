from plainmaps import currency_name


def test_known_codes() -> None:
    assert currency_name("usd") == "US Dollar"
    assert currency_name("EUR") == "Euro"


def test_unknown_codes_are_absent() -> None:
    assert currency_name("") is None
    assert currency_name(None) is None
    assert currency_name("XXX") is None
