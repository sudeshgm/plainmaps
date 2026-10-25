from plainmaps import country_name


def test_known_codes() -> None:
    assert country_name("de") == "Germany"
    assert country_name("US") == "United States"
    assert country_name("GB") == "United Kingdom"
    assert country_name("jp") == "Japan"


def test_unofficial_code_is_absent() -> None:
    assert country_name("XK") is None
    assert country_name("XX") is None
    assert country_name("") is None
    assert country_name(None) is None
    assert country_name("DEU") is None
