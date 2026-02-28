#!/usr/bin/env python3
"""Simple HTML generator script.

Usage:
  python generate_html.py
  python generate_html.py -o mypage.html --title "My Page" --body "<h1>Hello</h1>"
"""
import argparse
import sys


def build_html(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang=\"en\"> 
  <head>
    <meta charset=\"utf-8\"> 
    <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"> 
    <title>{title}</title>
  </head>
  <body>
    {body}
  </body>
</html>
"""


def main(argv=None):
    argv = argv or sys.argv[1:]
    p = argparse.ArgumentParser(description="Generate a simple HTML file")
    p.add_argument("-o", "--out", default="generated.html", help="output HTML filename")
    p.add_argument("--title", default="Generated Page", help="HTML title")
    p.add_argument("--body", default="<p>Hello, world!</p>", help="HTML body content (can include tags)")
    args = p.parse_args(argv)

    html = build_html(args.title, args.body)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
