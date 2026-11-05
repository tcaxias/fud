# fud

Fetch the top 5 Urban Dictionary definitions for a term.

## Why a rewrite?

The original (2015) scraped `http://www.urbandictionary.com/define.php` with a
fragile `grep` over a `<meta>` tag. That breaks today because:

- Urban Dictionary requires **HTTPS** (the old `http://` URL fails).
- HTML markup changes, so the `grep` pattern no longer matches.
- Only spaces were URL-encoded (`&`, `?`, `#`, `+` break the request).
- No `User-Agent`, timeouts, or error handling.
- HTML entities (`&amp;`, `&#39;`, …) were printed raw.

## Usage

Python standard library only — no extra dependencies:

```sh
chmod +x fud.py fud
./fud.py fud
./fud "hello world"
```

Returns the top 5 definitions by default.

## License

ISC — see `LICENSE`.
