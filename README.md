# Links

Use nested directories (folders) with txt files that contain link (href)
with optional link names.

This script converts them to standard bookmarks import for chrome etc.

```
./script.py ./path > bookmarks.html
```

## Structure

You point this script to a (nested) directory with `.txt` files.

They may look like this:
```
example.com
blog.lent.ink option link text
https://lent.ink

https://msdn.microsoft.com/en-us/ie/aa753582(v=vs.94)
```
blank lines are allowed, but no commented lines.


## Optional views

besides importing into chrome, one could use:

- https://github.com/darekkay/static-marks
- https://github.com/go-shiori/shiori
- https://github.com/jarun/Buku

### optional addition

Retrieve the `<title>` of links without description.

This has not been implemented since frontends like shiori can do stuff like this,
it's just a simple parser for now,
but feel free to submit a PR.

```
curl --location --silent example.com \
  | grep "<title>" \
  | sed 's/<title>//g' \
  | sed 's/<.*//g'
```
