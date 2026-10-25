"""Small lookup tables of commonly known facts.

Unknown codes return None. This package does not invent codes.
"""

from plainmaps.countries import country_name
from plainmaps.currencies import currency_name

__all__ = ["country_name", "currency_name"]
__version__ = "0.1.0"
