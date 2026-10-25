"""English country names for officially assigned ISO 3166-1 alpha-2 codes."""

from __future__ import annotations

import json
from importlib.resources import files

_NAMES: dict[str, str] = json.loads(
    files("plainmaps").joinpath("data/country_names_en.json").read_text(encoding="utf-8")
)


def country_name(alpha2: str | None) -> str | None:
    """Return the common English name, or None if the code is absent.

    User-assigned codes that are not in ISO 3166-1, such as XK, return None.
    """
    if alpha2 is None:
        return None
    code = alpha2.strip().upper()
    if len(code) != 2 or not code.isalpha():
        return None
    return _NAMES.get(code)
