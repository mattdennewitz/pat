# pat

Test XPath and CSS queries against HTML at the CLI.

This was banged out on a bumpy flight with shoddy internet access.
More docs forthcoming.

## Usage

XPath query via STDIN? Sure!

```bash
$ cat /path/to/file.html | pat -x '//an/xpath/query' -
```

Or perhaps you want to specify the file directly
and use a CSS selector? Why not!

```bash
$ pat -c 'table tr:first-of-type td.row:first-of-type' /path/to/file.html
```

## Testing

Install pip reqs via `requirements-dev.txt`, then run `py.test`.
Off to the races!

## Contributing

Excellent! PRs accepted.

