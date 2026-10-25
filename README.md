# plainmaps

Small, dependency-free lookup tables for standard codes, released under the MIT license. Codes that are not officially assigned return `None`.

## Usage

```python
from plainmaps import country_name, currency_name

country_name("DE")    # "Germany"
country_name("US")    # "United States"
country_name("XK")    # None (not an ISO 3166-1 code)

currency_name("EUR")  # "Euro"
```

## Contributing

New tables are welcome. Please see [DISCLAIMER.md](DISCLAIMER.md) for what the data covers and where it may come from.

## License

MIT. See [LICENSE](LICENSE).
