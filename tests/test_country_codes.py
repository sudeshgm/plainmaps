import json
from importlib.resources import files

import pytest

from plainmaps import alpha2_from_alpha3, alpha2_from_numeric, alpha3, country_name, numeric

DATA = json.loads(files("plainmaps").joinpath("data/country_codes.json").read_text())


@pytest.mark.parametrize("a2,a3,num", [
    ("RO", "ROU", "642"), ("CD", "COD", "180"), ("SS", "SSD", "728"), ("RS", "SRB", "688"),
    ("ME", "MNE", "499"), ("TL", "TLS", "626"), ("CW", "CUW", "531"), ("SX", "SXM", "534"),
    ("BQ", "BES", "535"), ("MF", "MAF", "663"), ("BL", "BLM", "652"), ("PS", "PSE", "275"),
    ("GB", "GBR", "826"), ("US", "USA", "840"), ("AF", "AFG", "004"),
])
def test_known_codes(a2: str, a3: str, num: str) -> None:
    assert alpha3(a2) == a3
    assert numeric(a2.lower()) == num
    assert alpha2_from_alpha3(a3.lower()) == a2
    assert alpha2_from_numeric(num) == a2


def test_round_trip_every_entry() -> None:
    for a2 in DATA:
        assert country_name(a2) is not None
        assert alpha2_from_alpha3(alpha3(a2)) == a2
        assert alpha2_from_numeric(numeric(a2)) == a2


@pytest.mark.parametrize("bad", [None, "", " ", "XK", "XKX", "XX", "ZZZ", "999", "1", "DEUX", "4", "04", "D1", 276])
def test_unknown_and_bad_input(bad) -> None:
    assert alpha3(bad) is None
    assert numeric(bad) is None
    assert alpha2_from_alpha3(bad) is None
    assert alpha2_from_numeric(bad) is None
