"""ISO 3166-1 alpha-3 and numeric codes for officially assigned countries."""

from __future__ import annotations

import json
from importlib.resources import files

_CODES: dict[str, dict[str, str]] = json.loads(
    files("plainmaps").joinpath("data/country_codes.json").read_text(encoding="utf-8")
)
_FROM_ALPHA3 = {v["alpha3"]: k for k, v in _CODES.items()}
_FROM_NUMERIC = {v["numeric"]: k for k, v in _CODES.items()}


def _clean(code: str | None, length: int, digits: bool) -> str | None:
    if not isinstance(code, str):
        return None
    code = code.strip().upper()
    if len(code) != length:
        return None
    if digits and not code.isdigit():
        return None
    if not digits and not (code.isascii() and code.isalpha()):
        return None
    return code


def alpha3(alpha2: str | None) -> str | None:
    """Return the alpha-3 code for an alpha-2 code, or None."""
    code = _clean(alpha2, 2, False)
    return _CODES[code]["alpha3"] if code in _CODES else None


def numeric(alpha2: str | None) -> str | None:
    """Return the three-digit numeric code (zero-padded string), or None."""
    code = _clean(alpha2, 2, False)
    return _CODES[code]["numeric"] if code in _CODES else None


def alpha2_from_alpha3(code: str | None) -> str | None:
    """Return the alpha-2 code for an alpha-3 code, or None."""
    return _FROM_ALPHA3.get(_clean(code, 3, False) or "")


def alpha2_from_numeric(code: str | None) -> str | None:
    """Return the alpha-2 code for a three-digit numeric code, or None."""
    return _FROM_NUMERIC.get(_clean(code, 3, True) or "")
