"""English currency names for officially assigned ISO 4217 alphabetic codes."""

from __future__ import annotations

import json
from importlib.resources import files

_NAMES: dict[str, str] = json.loads(
    files("plainmaps").joinpath("data/currency_names_en.json").read_text(encoding="utf-8")
)


def currency_name(code: str | None) -> str | None:
    """Return the common English name, or None if the code is absent.

    Unknown codes return None. XXX is not mapped.
    """
    if code is None:
        return None
    normalized = code.strip().upper()
    if len(normalized) != 3 or not normalized.isalpha():
        return None
    return _NAMES.get(normalized)
