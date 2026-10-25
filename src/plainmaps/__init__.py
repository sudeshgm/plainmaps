"""Small lookup tables of commonly known facts.

Unknown codes return None. This package does not invent codes.
"""

from plainmaps.countries import country_name
from plainmaps.country_codes import (
    alpha2_from_alpha3,
    alpha2_from_numeric,
    alpha3,
    numeric,
)
from plainmaps.currencies import currency_name

__all__ = [
    "alpha2_from_alpha3",
    "alpha2_from_numeric",
    "alpha3",
    "country_name",
    "currency_name",
    "numeric",
]
__version__ = "0.1.0"
