# Disclaimer

The data in this package is provided as is, without warranty, and may contain mistakes. Nothing here is legal advice.

## About the data

- Only officially assigned codes are included. For example, `XK` is not an ISO 3166-1 code, so `country_name("XK")` returns `None`.
- Lookups for missing or unrecognised codes return `None` rather than a guess.
- The names are common English names written for this project, not the official ISO wording. This is not an official ISO product.
- Tables are written independently and are not copied from projects or standards licensed under terms other than MIT or Apache-2.0.
