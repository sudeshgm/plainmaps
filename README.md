# plainmaps

Small MIT lookup tables. A code that is not officially assigned returns `None`.

```python
from plainmaps import country_name

country_name("DE")  # "Germany"
country_name("US")  # "United States"
country_name("XK")  # None. Not an official ISO 3166-1 code.
```

Read [DISCLAIMER.md](DISCLAIMER.md) before adding a table. Do not copy data from a non-permissive project and relicense it.

Not published to PyPI yet. Publishing needs a PyPI token from the repo owner.
