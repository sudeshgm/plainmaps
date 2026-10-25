# What this bot adds

Create an MIT module only when all four are true:

1. No single MIT or Apache-2.0 package on PyPI already offers the whole collection. plainmaps aims to be one complete permissive alternative to pycountry, so a table is still worth adding when a separate MIT or Apache package covers just that one piece.
2. The code people use today is missing, or it is under a license that is not MIT or Apache-2.0. pycountry is LGPL. An ISO publication is not MIT.
3. The contents can be written from common knowledge. A short lookup or a small function. Do not download or copy the other project.
4. Every code is officially assigned. Do not invent a country, a currency, or a language. `XK` stays out. An unknown code returns `None`.

One module per run. Add a test. Push to this repository. Do not publish to PyPI.

If the only way to build it is to copy the non-MIT source, skip it. A disclaimer does not make that copy legal.

Country names qualify. Currency names qualify. A table that needs the official ISO wording copied does not.
